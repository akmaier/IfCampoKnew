"""HTTP client for Campo (www.campo.fau.de).

Responsibilities:
  * Bootstrap a fresh session by visiting the HISinOne start page — stale
    sessions cause silent POST rejection (see docs/campo-public-surface.md §7a.1).
  * Apply a minimum interval between requests (polite scraping).
  * Retry 5xx responses with exponential backoff.

This module is intentionally dependency-light: only ``requests``.
"""
from __future__ import annotations

import logging
import time
from typing import Optional

import requests

log = logging.getLogger("campo.client")

BASE = "https://www.campo.fau.de"
START_PAGE = f"{BASE}/qisserver/pages/cs/sys/portal/hisinoneStartPage.faces"
CATALOG_FLOW = (
    f"{BASE}/qisserver/pages/cm/exa/coursecatalog/showCourseCatalog.xhtml"
    "?_flowId=showCourseCatalog-flow"
)

DEFAULT_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)


class CampoClient:
    """Session-aware, rate-limited client for Campo."""

    def __init__(
        self,
        min_interval: float = 1.0,
        user_agent: str = DEFAULT_UA,
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        self.min_interval = min_interval
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": user_agent,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "de,en;q=0.9",
            }
        )
        self._last_ts: float = 0.0
        self._started: bool = False

    def start_session(self) -> None:
        if self._started:
            return
        self._rate_limit()
        r = self.session.get(START_PAGE, timeout=self.timeout)
        r.raise_for_status()
        self._started = True
        js = self.session.cookies.get("JSESSIONID", "")
        log.info("session started, JSESSIONID=%s…", js[:16])

    def get(self, url: str, *, referer: Optional[str] = None) -> requests.Response:
        """Rate-limited, retried GET. Auto-starts the session on first call."""
        if not self._started:
            self.start_session()
        headers = {"Referer": referer} if referer else None

        last_exc: Optional[BaseException] = None
        for attempt in range(1, self.max_retries + 1):
            self._rate_limit()
            try:
                r = self.session.get(url, timeout=self.timeout, headers=headers)
                if 500 <= r.status_code < 600:
                    raise RuntimeError(f"server error {r.status_code}")
                return r
            except (requests.RequestException, RuntimeError) as e:
                last_exc = e
                if attempt == self.max_retries:
                    break
                backoff = 2**attempt
                log.warning(
                    "GET %s failed (attempt %d/%d): %s — backoff %ds",
                    url,
                    attempt,
                    self.max_retries,
                    e,
                    backoff,
                )
                time.sleep(backoff)
        raise RuntimeError(f"GET {url} failed after {self.max_retries} attempts: {last_exc}")

    def catalog_url(self, period_id: int, path: Optional[list[str]] = None) -> str:
        """Build a catalogue deep-link URL.

        ``path`` is a list of *segment strings* like ``["title:17593",
        "exam:14867623"]``. Pass an empty list or ``None`` for the root.
        """
        url = f"{CATALOG_FLOW}&periodId={period_id}"
        if path:
            url += "&path=" + "|".join(path)
        return url

    def _rate_limit(self) -> None:
        dt = time.monotonic() - self._last_ts
        if dt < self.min_interval:
            time.sleep(self.min_interval - dt)
        self._last_ts = time.monotonic()
