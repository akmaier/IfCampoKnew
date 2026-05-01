---
kind: "fau-faudir-professoren-index"
total_persons: 4897
chunks: 21
source: "https://faudir.fau.de/publicDir/persons"
scraped_at: 2026-05-01T19:22:19+00:00
rank_distribution:
  W1: 11
  W3: 103
  W?: 4731
  Junior: 65
  other: 6
---

# FAUdir — Professor:innen (Übersicht)

Diese Datei ist die Einstiegsseite für den FAUdir-Personen-Korpus. Insgesamt **4897** Personen mit professorartiger Funktion wurden aus FAUdir gepullt; sie liegen in alphabetisch geordneten Teil-Dateien (à ~26 k Tokens) im selben Verzeichnis. (21 Chunks)

## Vorbehalte

* FAUdir wird als Self-Service betrieben (Banner auf der Seite: *„currently still in the test phase, the quality and completeness of data may vary“*) — Vollständigkeit nicht garantiert.
* **W-Rang-Heuristik:** wir parsen explizite Strings *„W1-Professur“*, *„W2-Professur“*, *„W3-Professur“* aus dem Organisationsnamen. Wenn der Name *„Lehrstuhl für …“* lautet (ohne W-Nummer), markieren wir mit `W?` — solche Lehrstuhlprofessuren sind in Deutschland *meistens* W3, aber der RAG-Agent prüft das bei Bedarf bitte selbst.
* `apl.` = außerplanmäßige Professur, `Hon.` = Honorarprofessur, `Junior` = Juniorprofessur (W1).

## Rang-Verteilung

- **W1**: 11
- **W3**: 103
- **W?**: 4731
- **Junior**: 65
- **other**: 6

## Chunks

- [`faudir-Aad_Bec.md`](faudir-Aad_Bec.md): 241 Personen — *Aadil, Aadil* … *Becker, Julia*
- [`faudir-Bec_Buc.md`](faudir-Bec_Buc.md): 227 Personen — *Becker, Maik* … *Buchner, Andrea*
- [`faudir-Buc_Deu.md`](faudir-Buc_Deu.md): 243 Personen — *Buchner, Silvia* … *Deuerlein, Nadja*
- [`faudir-Deu_Eve.md`](faudir-Deu_Eve.md): 233 Personen — *Deutel, Mark* … *Evert, Stephanie*
- [`faudir-Eyb_Gai.md`](faudir-Eyb_Gai.md): 238 Personen — *Eyb, Alexander* … *Gaillard, Aixala*
- [`faudir-Gal_Gut.md`](faudir-Gal_Gut.md): 234 Personen — *Galanakis, Stathis* … *Guthmann, Florian*
- [`faudir-Gut_Hel.md`](faudir-Gut_Hel.md): 225 Personen — *Gutjahr, Lene* … *Helmer, Alexandra*
- [`faudir-Hel_Isr.md`](faudir-Hel_Isr.md): 247 Personen — *Helmer, Madeleine* … *Israel, Dominic*
- [`faudir-Itz_Kle.md`](faudir-Itz_Kle.md): 234 Personen — *Itzenhäuser, Tatjana* … *Kleinöder, Jürgen*
- [`faudir-Kle_Küc.md`](faudir-Kle_Küc.md): 233 Personen — *Klek, Konrad* … *Kücükkaya, Selim*
- [`faudir-Küf_Mac.md`](faudir-Küf_Mac.md): 236 Personen — *Küffner, Christoph* … *Mackensen, Andreas*
- [`faudir-Mad_Mon.md`](faudir-Mad_Mon.md): 229 Personen — *Mader, Benedikt* … *Monajem, Mehrpad*
- [`faudir-Mon_Oni.md`](faudir-Mon_Oni.md): 231 Personen — *Moninger, Marco* … *Onishchukov, Georgy*
- [`faudir-Opd_Rac.md`](faudir-Opd_Rac.md): 236 Personen — *Opdenhövel, René* … *Rachuj, Sebastian*
- [`faudir-Rad_Rze.md`](faudir-Rad_Rze.md): 239 Personen — *Rademacher, Jasmin* … *Rzepka, Lisa*
- [`faudir-Räd_Sch.md`](faudir-Räd_Sch.md): 224 Personen — *Rädle, Karin* … *Schneider, Judith*
- [`faudir-Sch_Sip.md`](faudir-Sch_Sip.md): 240 Personen — *Schneider, Klaus* … *Sippel, Felix*
- [`faudir-Sir_Teg.md`](faudir-Sir_Teg.md): 229 Personen — *Sirbu, Horia* … *Teget-Welz, Manuel*
- [`faudir-Tei_Waf.md`](faudir-Tei_Waf.md): 231 Personen — *Teich, Jürgen* … *Waffler, Marleen*
- [`faudir-Wag_Wit.md`](faudir-Wag_Wit.md): 228 Personen — *Wagner, Anja* … *Witte, Lukas*
- [`faudir-Wit_Üna.md`](faudir-Wit_Üna.md): 219 Personen — *Wittek, Marvin* … *Ünalan, Irem*
