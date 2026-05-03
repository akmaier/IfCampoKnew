"""Probe Campo's rate limits empirically — gentle by default.

Two-axis probe:

* Sequential: one session at progressively faster intervals (default
  1.0 → 0.5 → 0.3 → 0.2 s). Looks for the inflection where p95 latency
  creeps up or 429/503 appears.

* Parallel: at the safe single-session interval, fan out across a small
  set of session counts (default 1, 2, 4). Reveals whether Campo
  throttles per-session or globally.

Each cell does N requests (default 20) against a small pool of stable
unit_ids, cycled to avoid hot-cache skew. **Cells abort on the FIRST
429/503**, the descent stops, and the probe never overruns the limit.

The defaults stay well under what a routine scrape (`fetch_courses.py
--interval 0.5`) already produces. To probe more aggressively, pass
explicit `--intervals` and `--parallel` lists.

Usage::

    python scraper/probe_rate.py --period 589 -v
"""
from __future__ import annotations

import argparse
import logging
import statistics
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

import requests

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from campo_client import CampoClient  # noqa: E402

log = logging.getLogger("campo.probe_rate")

DETAIL_URL_TPL = (
    "https://www.campo.fau.de/qisserver/pages/startFlow.xhtml"
    "?_flowId=detailView-flow&unitId={unit_id}&periodId={period_id}"
)


@dataclass
class CellResult:
    interval: float
    parallel: int
    n_planned: int
    n_done: int = 0
    latencies: list[float] = field(default_factory=list)
    statuses: dict[int, int] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    elapsed: float = 0.0
    aborted: bool = False
    abort_reason: str | None = None

    def add_status(self, status: int) -> None:
        self.statuses[status] = self.statuses.get(status, 0) + 1

    @property
    def ok_count(self) -> int:
        return sum(c for s, c in self.statuses.items() if 200 <= s < 300)

    @property
    def hard_limit_count(self) -> int:
        return sum(c for s, c in self.statuses.items() if s in (429, 503))

    @property
    def server_error_count(self) -> int:
        return sum(c for s, c in self.statuses.items() if 500 <= s < 600)

    @property
    def drift_ms(self) -> float:
        if len(self.latencies) < 4:
            return 0.0
        h = self.latencies[: len(self.latencies) // 2]
        t = self.latencies[len(self.latencies) // 2 :]
        return 1000 * (statistics.median(t) - statistics.median(h))

    def fmt(self) -> str:
        if not self.latencies:
            return f"  interval={self.interval:.2f}s parallel={self.parallel}: NO DATA"
        med_ms = 1000 * statistics.median(self.latencies)
        if len(self.latencies) >= 20:
            p95_ms = 1000 * statistics.quantiles(self.latencies, n=20)[18]
        else:
            p95_ms = 1000 * max(self.latencies)
        rate = self.n_done / self.elapsed if self.elapsed else 0
        target = self.parallel / self.interval if self.interval > 0 else float("inf")
        statuses = ", ".join(f"{s}:{c}" for s, c in sorted(self.statuses.items()))
        flags = []
        if self.aborted:
            flags.append(f"ABORTED ({self.abort_reason})")
        elif self.hard_limit_count:
            flags.append(f"HARD-LIMIT×{self.hard_limit_count}")
        elif self.server_error_count:
            flags.append(f"5xx×{self.server_error_count}")
        if self.errors:
            flags.append(f"{len(self.errors)} client-errors")
        if abs(self.drift_ms) > 200:
            flags.append(f"DRIFT{self.drift_ms:+.0f}ms")
        flag_s = "  ⚠ " + " ".join(flags) if flags else ""
        return (
            f"  interval={self.interval:.2f}s parallel={self.parallel} "
            f"target={target:.1f}r/s actual={rate:.2f}r/s "
            f"n={self.n_done}/{self.n_planned} statuses={{{statuses}}} "
            f"med={med_ms:.0f}ms p95={p95_ms:.0f}ms drift={self.drift_ms:+.0f}ms"
            f"{flag_s}"
        )


def _do_request(
    session: requests.Session,
    url: str,
    timeout: float,
    referer: str | None = None,
) -> tuple[float, int | None, str | None]:
    """Single timed request. Returns (latency_s, status_or_None, err_or_None)."""
    headers = {"Referer": referer} if referer else None
    t0 = time.monotonic()
    try:
        r = session.get(url, timeout=timeout, headers=headers)
        return time.monotonic() - t0, r.status_code, None
    except requests.RequestException as e:
        return time.monotonic() - t0, None, type(e).__name__


def probe_cell_sequential(
    client: CampoClient,
    unit_ids: list[int],
    period_id: int,
    *,
    interval: float,
    n: int,
    abort_on_hard_limit: int = 1,
) -> CellResult:
    """Sequential probe: one client, paced at `interval` between requests."""
    res = CellResult(interval=interval, parallel=1, n_planned=n)
    if not client._started:
        client.start_session()
    referer = (
        f"https://www.campo.fau.de/qisserver/pages/startFlow.xhtml"
        f"?_flowId=showCourseCatalog-flow&periodId={period_id}"
    )
    t_start = time.monotonic()
    next_t = t_start
    for i in range(n):
        sleep = next_t - time.monotonic()
        if sleep > 0:
            time.sleep(sleep)
        uid = unit_ids[i % len(unit_ids)]
        url = DETAIL_URL_TPL.format(unit_id=uid, period_id=period_id)
        lat, status, err = _do_request(client.session, url, timeout=client.timeout, referer=referer)
        res.latencies.append(lat)
        res.n_done += 1
        if status is not None:
            res.add_status(status)
        if err:
            res.errors.append(err)
        if res.hard_limit_count >= abort_on_hard_limit:
            res.aborted = True
            res.abort_reason = f"{res.hard_limit_count}× 429/503"
            break
        next_t += interval
    res.elapsed = time.monotonic() - t_start
    return res


def probe_cell_parallel(
    clients: list[CampoClient],
    unit_ids: list[int],
    period_id: int,
    *,
    interval: float,
    n_total: int,
    abort_on_hard_limit: int = 1,
) -> CellResult:
    """Parallel probe: N clients, each paced at `interval` independently."""
    parallel = len(clients)
    n_per_thread = max(1, n_total // parallel)
    res = CellResult(interval=interval, parallel=parallel, n_planned=n_per_thread * parallel)
    referer = (
        f"https://www.campo.fau.de/qisserver/pages/startFlow.xhtml"
        f"?_flowId=showCourseCatalog-flow&periodId={period_id}"
    )

    # Warm sessions before the clock starts (so JSESSIONID bootstrap doesn't
    # skew the first cell's latency measurements).
    for c in clients:
        if not c._started:
            c.start_session()

    abort_event = threading.Event()
    lock = threading.Lock()

    def worker(client: CampoClient, thread_idx: int) -> None:
        next_t = time.monotonic()
        for i in range(n_per_thread):
            if abort_event.is_set():
                return
            sleep = next_t - time.monotonic()
            if sleep > 0:
                time.sleep(sleep)
            uid = unit_ids[(thread_idx + i * parallel) % len(unit_ids)]
            url = DETAIL_URL_TPL.format(unit_id=uid, period_id=period_id)
            lat, status, err = _do_request(
                client.session, url, timeout=client.timeout, referer=referer,
            )
            with lock:
                res.latencies.append(lat)
                res.n_done += 1
                if status is not None:
                    res.add_status(status)
                if err:
                    res.errors.append(err)
                if res.hard_limit_count >= abort_on_hard_limit:
                    res.aborted = True
                    res.abort_reason = f"{res.hard_limit_count}× 429/503"
                    abort_event.set()
            next_t += interval

    t_start = time.monotonic()
    with ThreadPoolExecutor(max_workers=parallel) as ex:
        futs = [ex.submit(worker, clients[i], i) for i in range(parallel)]
        for f in futs:
            f.result()
    res.elapsed = time.monotonic() - t_start
    return res


def run_probe(
    period_id: int,
    unit_ids: list[int],
    *,
    sequential_intervals: list[float],
    parallel_factors: list[int],
    n_per_cell: int,
) -> tuple[list[CellResult], list[CellResult]]:
    seq_results: list[CellResult] = []
    log.info("=" * 60)
    log.info("Sequential probe (single session)")
    log.info("=" * 60)

    client = CampoClient(min_interval=0.0)

    safe_interval: float | None = None
    for iv in sequential_intervals:
        log.info("running cell: interval=%.2fs", iv)
        cell = probe_cell_sequential(
            client, unit_ids, period_id, interval=iv, n=n_per_cell,
        )
        seq_results.append(cell)
        log.info(cell.fmt())
        if cell.aborted:
            log.warning("aborting sequential descent at interval=%.2fs", iv)
            break
        # Mark interval as safe if no hard limits, no 5xx, drift < 200ms.
        if (
            cell.hard_limit_count == 0
            and cell.server_error_count == 0
            and cell.drift_ms < 200
        ):
            safe_interval = iv
        elif cell.server_error_count or cell.drift_ms >= 200:
            log.warning(
                "interval=%.2fs shows soft trouble (5xx=%d, drift=%+.0fms) — keeping descent",
                iv, cell.server_error_count, cell.drift_ms,
            )

    par_results: list[CellResult] = []
    if safe_interval is None:
        log.warning("no safe interval found — skipping parallel probe")
        return seq_results, par_results

    log.info("=" * 60)
    log.info("Parallel probe (interval=%.2fs, varying sessions)", safe_interval)
    log.info("=" * 60)

    for p in parallel_factors:
        log.info("running cell: parallel=%d", p)
        clients = [CampoClient(min_interval=0.0) for _ in range(p)]
        cell = probe_cell_parallel(
            clients, unit_ids, period_id,
            interval=safe_interval, n_total=n_per_cell,
        )
        par_results.append(cell)
        log.info(cell.fmt())
        if cell.aborted:
            log.warning("aborting parallel ascent at parallel=%d", p)
            break

    return seq_results, par_results


def _print_summary(seq: list[CellResult], par: list[CellResult]) -> None:
    print("\n=== SEQUENTIAL ===")
    for c in seq:
        print(c.fmt())
    print("\n=== PARALLEL ===")
    for c in par:
        print(c.fmt())

    print("\n=== RECOMMENDATION ===")
    safe_seq = [
        c for c in seq
        if not c.aborted and c.hard_limit_count == 0 and c.server_error_count == 0
    ]
    if safe_seq:
        best = min(safe_seq, key=lambda c: c.interval)
        print(
            f"Single-session safe interval: {best.interval:.2f}s "
            f"({1/best.interval:.1f} req/s, p95="
            f"{1000 * (statistics.quantiles(best.latencies, n=20)[18] if len(best.latencies) >= 20 else max(best.latencies)):.0f}ms)"
        )
    else:
        print("No safe single-session interval found — keep current 1.0s default.")

    safe_par = [
        c for c in par
        if not c.aborted and c.hard_limit_count == 0 and c.server_error_count == 0
    ]
    if safe_par:
        best_p = max(safe_par, key=lambda c: c.parallel)
        agg = best_p.parallel / best_p.interval
        print(
            f"Parallel safe ceiling: {best_p.parallel} sessions × "
            f"{best_p.interval:.2f}s = {agg:.1f} req/s aggregate"
        )
    else:
        print("No parallel ceiling found.")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--period", type=int, default=589, help="periodId (default 589 = SoSe 2026)")
    p.add_argument(
        "--unit-ids", type=int, nargs="+",
        default=[88134, 86230, 92294, 91021, 94895],
        help="unit IDs to cycle through (avoid hot-cache skew)",
    )
    p.add_argument(
        "--n-per-cell", type=int, default=20,
        help="requests per cell (default 20; total <= ~5 min at 4 cells)",
    )
    p.add_argument(
        "--intervals", type=float, nargs="+",
        default=[1.0, 0.5, 0.3, 0.2],
        help=(
            "sequential probe intervals in seconds (descending). "
            "Default 1.0/0.5/0.3/0.2 stays under the existing scraper's load."
        ),
    )
    p.add_argument(
        "--parallel", type=int, nargs="+", default=[1, 2, 4],
        help="parallel probe session counts (default 1, 2, 4)",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    args = p.parse_args(argv)

    level = logging.WARNING - 10 * args.verbose
    logging.basicConfig(
        level=max(level, logging.DEBUG),
        format="%(levelname)s %(name)s: %(message)s",
    )
    log.info(
        "period=%d unit_ids=%d n_per_cell=%d",
        args.period, len(args.unit_ids), args.n_per_cell,
    )
    seq, par = run_probe(
        args.period, args.unit_ids,
        sequential_intervals=sorted(args.intervals, reverse=True),
        parallel_factors=sorted(args.parallel),
        n_per_cell=args.n_per_cell,
    )
    _print_summary(seq, par)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
