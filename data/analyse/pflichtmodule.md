---
kind: "campo-pflichtmodule-aus-po"
po_files_with_pflicht_modules: 694
total_pflicht_modules: 6317
scraped_at: 2026-08-17T13:08:06+00:00
---

# Pflichtmodule — direkt aus PO-Anlagen extrahiert

Diese Datei sammelt strukturierte Pflichtmodul-Listen, die wir aus den *Studienverlaufsplan*- und *Curricular-Übersicht*-Tabellen der FAU-Prüfungsordnungen gelesen haben (Markdown-Tables, vom PyMuPDF4LLM-Konverter aus den PDF-Anlagen erzeugt). Pro PO wird die Sektion verfolgt — Module aus Sektionen *Grundlagen*, *Pflichtbereich*, *Basismodule*, *Kernbereich*, *Bachelorarbeit*, *Masterarbeit* gelten als Pflicht. *Wahlpflicht*, *Wahlbereich*, *Aufbaumodule*, *Vertiefungsmodule*, *Schwerpunkte* und *Schlüsselqualifikationen* werden ausgenommen.

## Vorbehalte

* **Vollständigkeit:** ~74 % der PO-Markdown-Dateien enthalten   überhaupt erkennbare Tabellen; davon haben wieder nur ~30 %   klare Pflicht-Section-Marker. Etwa die Hälfte aller POs liefert   hier deshalb noch kein Ergebnis — bei vielen ist die Anlage als   **Bild** im PDF eingebettet (typisches Beispiel: *Curricular-  Übersicht* als Diagramm) und entzieht sich der Text-Extraktion.
* **Modul-Name vs. Veranstaltungs-Titel:** ein Pflichtmodul   *Analysis I* erscheint in Campo als *Vorlesung Analysis I* +   *Übung Analysis I* + *Tafelübung Analysis I*. Hier wird nur das   Modul gelistet; das Cross-Mapping zu Campo-Veranstaltungen   übernimmt die Heuristik in `pflichtveranstaltungen.md` bzw.   ein RAG-Agent zur Anfragezeit.
* **Modul-Reihenfolge:** Module erscheinen in der Reihenfolge des   Studienverlaufsplans (typisch nach Fachsemester sortiert).

**Statistik:** 694 POs lieferten zusammen 6317 eindeutige Pflichtmodul-Einträge.

## Pro PO

### 13. Mai 2014

PO-Quelle: [`pruefungsordnungen/lehramt/6aes-lapo-allgemein.md`](../pruefungsordnungen/lehramt/6aes-lapo-allgemein.md)

**Pflichtmodule (1):**
- im Rahmen der Didaktiken einer Fächerg oduls 3 ECTS aus dem Modul „Arbeit un

### 30. September 2015

PO-Quelle: [`pruefungsordnungen/lehramt/7aes-lapo-allgemein.md`](../pruefungsordnungen/lehramt/7aes-lapo-allgemein.md)

**Pflichtmodule (5):**
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungs- kompetenzen in der Mittel- schule
- Basismodul Berufsorientierung<sup>1</sup>
- Masterarbeit

### 9. September 2010

PO-Quelle: [`pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/1aes-20ba-ma-20berufspaedagogik-20la-20berufl-20schulen.md`](../pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/1aes-20ba-ma-20berufspaedagogik-20la-20berufl-20schulen.md)

**Pflichtmodule (28):**
- Grundlagen der Produktentwicklung B 5
- Konstruktionsübung
- B 6 Konstruktive Projektarbeit(Teamwork,Präsentationstechnik)
- Informatik und Mathematik
- (GOP)
- B 10 Grundlagen der Informatik
- Produktion,Optik und Messtechnik
- B 12 Optik und optische Technologien
- B 13 Grundlagen der Messtechnik
- Elektrotechnik,Thermodynamik und Werkstoffkunde
- B 15 Grundlagen der Elektrotechnik
- B 16 Technische Thermodynamik
- Werkstoffkunde
- Berufspädagogik
- B 19 Grundlagen der Berufspädagogik
- B 20 Präsentations- und Moderationstechnik
- B 21 Berufliche Weiterbildung
- B 22 Betriebspädagogisches Seminar
- B 23 Schulpraktische Studien
- B 24 Berufspädagogische Vertiefung
- Zweitfach
- B 25 Unterrichtsfach(Zweitfach)inkl. Fachdidaktik
- A bschlussarbeit
- B 26 Bachelorarbeit incl. Vortrag
- (GOP) Bestandteil der Grundlagen- und Orientierungsprüfung
- uSL unbenotete Studienleistung
- bSL benotete Studienleistung
- *) gemäß den Vorgaben des Zweitfaches

### BMPO BP-T 20230928 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/bmpo-bp-t-20230928-aes.md`](../pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/bmpo-bp-t-20230928-aes.md)

**Pflichtmodule (2):**
- vgl.§ 4 FPO WiWi
- FSP vgl.§ 4 FPO WiWi

### PO ZS Geow im LA 20250320 .pdf

PO-Quelle: [`pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/po-zs-geow-im-la-20250320.md`](../pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/po-zs-geow-im-la-20250320.md)

**Pflichtmodule (4):**
- Grundlagen der Geowissenschaften I
- Rohstoffe und Nachhaltigkeit
- Dynamik des Systems Erde
- Kompetenzseminar zum Klimawandel

### pdf vom 19.02.2009

PO-Quelle: [`pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/sto-po-berufspaedagogik-eei.md`](../pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/sto-po-berufspaedagogik-eei.md)

**Pflichtmodule (33):**
- (30) Grundlagen der Elektrotechnik, Energie und Antriebstechnik
- Grundlagen der Elektrotechnik I (GOP)
- Grundlagen der Elektrotechnik II (GOP)
- Grundlagen der Elektrotechnik III
- Praktikum Grundlagen der Elektrotechnik
- Grundlagen der Elektrischen Antriebstechnik
- Grundlagen der Elektrischen Energieversorgung
- (30) Informatik und Mathematik
- Mathematik A1 oder B1 (GOP)
- Mathematik A2 oder B2 (GOP)
- Mathematik A3 oder B3
- Grundlagen der Informatik (GOP)
- (10) Hochfrequenztechnik
- Hochfrequenztechnik I
- Passive Bauelemente und deren HF-Verhalten
- Kommunikationselektronik und Schaltungstechnik
- Digitaltechnik
- Halbleiterbauelemente
- Schaltungstechnik
- Praktikum Schaltungstechnik
- Kommunikationselektronik
- (10) Systeme und Regelungen
- Regelungstechnik A (Grundlagen)
- Einführung in die Systemtheorie
- (5) Seminar und Laborpraktikum aus der Elektro- und Informationstech- nik
- Grundlagen der Berufspädagogik
- Präsentations- und Moderationstechnik
- Berufliche Weiterbildung
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Berufspädagogische Vertiefung
- Unterrichtsfach (Zweitfach) inkl. Fachdidaktik
- _Bachelorarbeit incl. Vortrag_

### pdf vom 23.02.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lapo-20-20ausgefertigt.md`](../pruefungsordnungen/lehramt/lapo-20-20ausgefertigt.md)

**Pflichtmodule (2):**
- Basismodul Lernprozesse gestal- ten:
- Theor.undmethod.Grundlagen

### pdf vom 23.02.2009 i.d.F. 28.03.2011

PO-Quelle: [`pruefungsordnungen/lehramt/lapo-lehramt-maerz2011.md`](../pruefungsordnungen/lehramt/lapo-lehramt-maerz2011.md)

**Pflichtmodule (2):**
- Basismodul Lernprozesse gestalten:
- Theor. und method. Grundlagen

### pdf vom 23.02.2009 i.d.F. 14.03.2012

PO-Quelle: [`pruefungsordnungen/lehramt/lapo-lehramt-maerz2012.md`](../pruefungsordnungen/lehramt/lapo-lehramt-maerz2012.md)

**Pflichtmodule (2):**
- Basismodul Lernprozesse gestalten:
- Theor. und method. Grundlagen

### pdf vom 23.02.2009 i.d.F. 13.05.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lapo-lehramt-mai2014.md`](../pruefungsordnungen/lehramt/lapo-lehramt-mai2014.md)

**Pflichtmodule (1):**
- Masterarbeit

### pdf vom 23.02.2009 i.d.F. 22.11.2013

PO-Quelle: [`pruefungsordnungen/lehramt/lapo-lehramt-nov2013.md`](../pruefungsordnungen/lehramt/lapo-lehramt-nov2013.md)

**Pflichtmodule (2):**
- Basismodul Lernprozesse gestalten:
- Theor. und method. Grundlagen

### pdf vom 23.02.2009 i.d.F. 15.09.2011

PO-Quelle: [`pruefungsordnungen/lehramt/lapo-lehramt-sept2011.md`](../pruefungsordnungen/lehramt/lapo-lehramt-sept2011.md)

**Pflichtmodule (2):**
- Basismodul Lernprozesse gestalten:
- Theor. und method. Grundlagen

### pdf vom 23.02.2009 i.d.F. 30.09.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lapo-lehramt-sept2015.md`](../pruefungsordnungen/lehramt/lapo-lehramt-sept2015.md)

**Pflichtmodule (1):**
- Masterarbeit

### pdf vom 23.02.2009 i.d.F. 01.12.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lapo-lehramt.md`](../pruefungsordnungen/lehramt/lapo-lehramt.md)

**Pflichtmodule (2):**
- (2) Basismodul Lernprozesse gestal- ten:
- Theor. und method. Grundlagen

### 24. September 2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-franzoesisch-abws2010-2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-franzoesisch-abws2010-2011.md)

**Pflichtmodule (14):**
- Abschlussmodul
- Schriftliche Hausarbeit
- Abschlussmodul Schriftliche Hausarbeit
- BereichFachdidaktiksind im Fach lschulen folgende Module abzulegen Modulbezeichnung
- Fachdidaktisches Modul 1: Einführung in die Didaktik des Französischen
- Übung: Einführung in die Fachdidaktik desFranzösischen
- Proseminar / Übung
- Fachdidaktisches Modul 2: Didaktik des Französischen (Lehramt Realschulen)
- Mittelseminar: Französische Sprach-, Literatur-undKulturvermittlung
- Angeleitete Lektüre
- Vertiefungsmodul Freier Bereich
- Optionsmodul Sprachwissenschaft
- Optionsmodul Literaturwissenschaft
- Optionsmodul Sprachpraxis

### 24. September 2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-franzoesisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-franzoesisch.md)

**Pflichtmodule (14):**
- Abschlussmodul
- Schriftliche Hausarbeit
- Abschlussmodul Schriftliche Hausarbeit
- BereichFachdidaktiksind im Fach lschulen folgende Module abzulegen Modulbezeichnung
- Fachdidaktisches Modul 1: Einführung in die Didaktik des Französischen
- Übung: Einführung in die Fachdidaktik desFranzösischen
- Proseminar / Übung
- Fachdidaktisches Modul 2: Didaktik des Französischen (Lehramt Realschulen)
- Mittelseminar: Französische Sprach-, Literatur-undKulturvermittlung
- Angeleitete Lektüre
- Vertiefungsmodul Freier Bereich
- Optionsmodul Sprachwissenschaft
- Optionsmodul Literaturwissenschaft
- Optionsmodul Sprachpraxis

### 24. September 2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-italienisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-italienisch.md)

**Pflichtmodule (2):**
- Abschlussmodul Schriftliche Hausarbeit
- Schriftlichen Hausarbeit

### 24. September 2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-spanisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-spanisch.md)

**Pflichtmodule (6):**
- Abschlussmodul Schriftliche Hausarbeit
- Schriftliche Hausarbeit
- Spanische Sprachpraxis 5
- Producción oral y escrita – registros y tipología de textos
- Traducción español-alemán
- Gramática y estilística II

### 14. September 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aes-la-arbeitslehre.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aes-la-arbeitslehre.md)

**Pflichtmodule (6):**
- Grundlagen der Fachdidaktik (GFD)
- Grundlagen der Fachwissenschaft (GFW)
- Medien und
- Methoden I (MuM I)
- Methoden II (MuM II)<sup>2</sup>
- Arbeit und Beruf

### 21. Oktober 2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-20la-mathematik.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-20la-mathematik.md)

**Pflichtmodule (41):**
- Analysis (Ana)
- AnalysisI
- Übungen zur AnalysisI
- AnalysisII
- Übungen zur AnalysisII
- Lineare Algebra (LA)
- LineareAlgebraI
- Übungen zur Linearen AlgebraI
- LineareAlgebraII
- Übungen zur Linearen Algebra II
- Orientierungsseminar (OrSe)<sup>~~1,2~~</sup>
- Teil 1
- Teil 2
- Mehrdimensionale Integration(MInt)
- Übungen
- Elemente der Linearen Algebra (ELA)
- Elemente der Linearen AlgebraI
- Übungen Linearen AlgebraI
- Elemente der Linearen AlgebraII
- Übungen Linearen AlgebraII
- Elemente der Analysis (EAna)
- Elemente der AnalysisI
- Übungen AnalysisI
- Elemente der AnalysisII
- Übungen AnalysisII
- Analytische Geometrie (AGeo)
- Vorlesung/Übung
- Aufbaumodul Analysis (AmAn)<sup>~~1~~</sup>
- Elemente der Analysis III
- Elementare Stochastik (EStoch)
- Mathematisches Seminar in elementarer Stochastik (SemEStoch)
- Geometrie für das Lehramt (GeoL)
- Mathematisches Seminar in Geometrie für das Lehramt (SemGeoL)
- Elementare Zahlentheorie (EZth)
- Mathematisches Seminar in elementarer Zahlentheorie (SemEZth)
- Fachdidaktik A Mathematik (FDAR)
- Didaktik der Arithmetik und Bruchrechnung
- Didaktikder Algebra
- Fachdidaktik B Mathematik (FDBR)
- DidaktikderGeometrie
- DidaktikderStochastik

### 9. Oktober 2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-chemie.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-chemie.md)

**Pflichtmodule (5):**
- Grundlagen der anorga-
- nisch-chemischen Labor-
- praxis
- Prüfungsvorbereitung
- Grundlagen der anorga- nisch-chemischen Labor-

### 29. September 2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-franzoesisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-franzoesisch.md)

**Pflichtmodule (14):**
- Basismodul Didaktik der Einführungsseminar in die Didaktik der romanischen Sprachen<sup>1)</sup> 2 5 (3) (3) (3)
- romanischen Sprachen Proseminar Fachdidaktik Französisch 2 (2) (2) (2)
- Mittelseminar Fachdidaktik Französisch 2 (4) (4)
- Basismodul Französische Sprachpraxis 1
- Communication orale
- Vocabulaire,idiomatique et civilisation II
- Basismodul Französische Sprachpraxis 2
- Phonétique pratique, orthophonie et intonation
- Basisseminar französische Sprachwissenschaft
- Basismodul Einführung in die Frankoromanistik
- Phonetik und Phonologie des Französischen
- Basismodul Didaktik der
- romanischen Sprachen
- Mittelseminar Fachdidaktik Französisch

### 29. September 2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-italienisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-italienisch.md)

**Pflichtmodule (2):**
- Basismodul Didaktik der romanischen Sprachen 2 (3) (3) (3)
- romanischen Sprachen 5 Proseminar Fachdidaktik Italienisch 2 (2) (2) (2)

### 29. September 2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-spanisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-spanisch.md)

**Pflichtmodule (9):**
- Basismodul Spanische Sprachpraxis 1
- Español intermedio II
- Basismodul Spanische Sprachpraxis 2
- Basisseminar Spanische Sprachwissenschaft
- Basismodul Einführung in die Iberoromanistik
- Phonetik und Phonologie des Spanischen
- Basismodul Didaktik d ih
- er romanscen Sprachen
- Mittelseminar Fachdidaktik Spanisch

### 27. Februar 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-wirtschaftswiss.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-wirtschaftswiss.md)

**Pflichtmodule (6):**
- Grundlagen der Fachdidaktik Wirtschaftswissenschaft en(Gymnasium)
- Praxisfelder der
- Fachdidaktik
- Grundlagen der Fachdidaktik
- Wirtschaftswissenschaft en(Realschule)
- Fachdidaktik Wirtschaftswissenschaft en

### 18. September 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/3aes-la-chemie.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/3aes-la-chemie.md)

**Pflichtmodule (5):**
- Grundlagen der anorga-
- nisch-chemischen Labor-
- praxis
- Prüfungsvorbereitung
- Grundlagen der anorga- nisch-chemischen Labor-

### 22. März 2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/3aes-la-sport.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/3aes-la-sport.md)

**Pflichtmodule (27):**
- (1V) Grundlagen der Sportdidaktik (FD)*
- (1V) Grundlagen der Sportpädagogik
- (3) Sportpädagogische /-didaktische Kompetenz II
- (2S) Normative und empirische Sportpädagogik /-didaktik (FD)*
- (4) Sportpädagogische /-didaktische Kompetenz III
- (2S) Psychologische Aspekte des (Schul-)Sports
- Lehrübungen für den Sportunterricht (FD)*
- (5) Lehrkompetenz Rückschlagspiele
- Tennis o. Tischtennis o. Badminton I
- Tennis o Tischtennis o Badminton II inkl
- . . . Bewegungslernen und –beobachtung
- (4) Kompetenz in Bewegung und Gesundheit II
- Stärkung Gesundheitsressourcen 1
- StärkungGesundheitsressourcen 2
- (6) Kompetenz in Bewegung und Gesundheit III
- (3S) Interventionskonzepte und QM
- (3S) Projekt „Entwicklung und Umsetzung von Interventionen zur Gesundheitsförderung“
- Grundlagen der Sportpädagogik I (FD) Ausgewählte Aspekte des Schulsports (FD)
- (3) Sportpädagogische / -didaktische Kompetenz II
- (2S) Normative und empirische Sportpädagogik /- didaktik (FD)*
- (1V) Normative und empirische Sportpädagogik /- didaktik(FD)*
- (4) Sportpädagogische / -didaktische Kompetenz III
- Klettern o. Wassersport o. MTB o. Inlineskaten o. Triathlon o. Zirkus- o. Kampfkünste o.entsprechendeAngebote
- (1S) PsychologischeAspekte des (Schul-) Sports
- (2S) „Stärkung Gesundheitsressourcen 1“
- „Stärkung Gesundheitsressourcen 2“
- (3) Projekt „Entwicklung und Umsetzung zur Gf“

### 8. August 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-franzoesisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-franzoesisch.md)

**Pflichtmodule (14):**
- Basismodul Französische Srachraxis 1
- Communication orale
- Introduction à la civilisation
- Basismodul Französische Sprachpraxis 2
- Phonétiquepratique,orthophonie et intonation
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Basismodul Didaktik der
- romanischen Sprachen
- Phonétique pratique, orthophonie et intonation
- Afbdl 1 Föih Shihf 1
- uaumou : ranzssce pracwssenscat
- Proseminar Sprachwissenschaft
- Mittelseminar Fachdidaktik Französisch

### 8. August 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-italienisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-italienisch.md)

**Pflichtmodule (9):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I
- Corso di italiano intermedio II
- Basismodul Italienische Sprachpraxis 2
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft
- Basismodul Didaktik der
- romanischen Sprachen

### 8. August 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-spanisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-spanisch.md)

**Pflichtmodule (4):**
- Basismodul Spanische Sprachpraxis 1
- Basismodul Spanische Sprachpraxis 2
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft

### 25. Oktober 2016

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/4aesa-la-sozialkunde.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/4aesa-la-sozialkunde.md)

**Pflichtmodule (9):**
- Grundlagen der politi- schen Bildun
- PolitischesLernen
- Methodik und Wertorien-
- tierung im Politikunterricht
- Grundlagen der politischen Bildung
- Wertorientierte Politische Bildung
- Methodik, Praxis und Wertorientierung
- im Politikunterricht
- im PU (FG GS)

### 14. Dezember 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/5aesa-la-ev-religion.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/5aesa-la-ev-religion.md)

**Pflichtmodule (20):**
- Basismodul: Theologie und wissenschaftliches Arbeiten
- RU in der Sek 1 (FD)
- Biblisches Grundwissen
- (Lehramt GS/MS/RS)
- Grundlagen der Theologie
- und Religionspädagogik
- Biblische Theologie 1 (AT)
- NT – Einführung in den Umgang mit dem NT
- Biblische Theologie 2 (NT)
- AT - Themen alttestamentlicher Theologie
- Biblische Theologie 3
- Systematische Theologie 1:
- Dogmatik (GMRS)
- Systematische Theologie 2:
- Ethik (GMRS)
- Epochen der Kirchengeschichte 1 - GS/MS/RS
- Kirchengeschichte 1
- Epochen der Kirchengeschichte 2 - GS/MS/RS
- Kirchengeschichte 2
- WPM-RS 1

### 16. Januar 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/6aes-la-deutsch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/6aes-la-deutsch.md)

**Pflichtmodule (18):**
- Grundlagen der Germanistischen Linguistik (Ling1)
- Grundlagen der Germanistischen Mediävistik (Med 1)
- Grundlagen der Neueren deutschen Literatur
- (NdL 1)
- Basismodul Grundlagen der Fachdidaktik Deutsch
- (BM FDD)
- Grundlagen der Fachdidaktik Deutsch
- prac- un eena
- Afbdl
- uaumoue Historische Sprachwissenschaft
- (Ling 2)
- Grammatik der deutschen
- Gegenwartssprache (Ling 3)
- Literaturgeschichte I: Mittelalterliche und frühneuzeitliche deutsche Literatur (LitG 1-GSHS)
- Literaturgeschichte II:
- Neuere deutsche Literatur (LitG 2)
- Sprach- und Mediendidaktik
- Vorlesung<sup>2</sup> 2

### 27. September 2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/7aes-la-englisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/7aes-la-englisch.md)

**Pflichtmodule (22):**
- Basismodul I
- Language
- Grundseminar 2
- Basismodul II Linuistics
- Basisvorlesung 1
- Basismodul III
- Literature
- Landeskunde USA/GB 2
- Basismodul IV Culture/Landeskunde
- Proseminar 2
- Zwischenmodul L‐GYM Linguistics
- Zwischenmodul L‐GYM Literature
- Writing in Academic Contexts 2
- Zwischenmodul
- L‐GYM Language
- Conversation Practice
- Einführungsseminar TEFL
- Englischdidaktik
- Afbdl
- uaumou Englischdidaktik
- Grundseminar
- itende fachd SWS

### 10. November 2016

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/8aes-la-dt-didaz.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/8aes-la-dt-didaz.md)

**Pflichtmodule (19):**
- Grundlagen der Germanistischen
- Analyseseminar 1
- Analyseseminar 2
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1 (Med BM 1)
- Grundlagen der Germanistischen Mdiäitik 2 Md BM
- eraur- un uurwssensca
- Grundlagen der Germanistischen Linguistik 1
- Grundlagen der Germanistischen Linguistik 2
- Grundlagen der Germanistischen Mediävistik
- Literatur- und Kulturwissenschaft
- Basismodul DiDaZ (LA GS)
- Tutorium
- Tutorium oder<sup>5</sup>Kolloquium
- Vorlesung 2
- Seminar aus dem Bereich „Theorie und Praxis des Zweitspracherwerbs / der Mehrsprachigkeit“
- Basismodul DiDaZ (LA MS)
- Tutorium oder<sup>3</sup>Kolloquium

### FPO LA DaZ 20200203 i.d.F. 20201123.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-daz-20200203-idf-20201123.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-daz-20200203-idf-20201123.md)

**Pflichtmodule (4):**
- Seminar<sup>2</sup>
- assmou a
- Tutorium
- Tutorium oder Kolloquium

### FPO LA DiDaZ 20200203.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-didaz-20200203.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-didaz-20200203.md)

**Pflichtmodule (18):**
- Bidl DiDZ LA GS
- assmou a
- Tutorium
- Tutorium oder Kolloquium
- Grundlagen des
- Deutschen als Zweit- sprache
- Sprache im Fachunterricht
- Linguistische Grundlagen
- Sprachsystem und Zweitsracherwerb
- Sprachdiagnostik
- Vermittlung von Text- und Diskurskompetenz
- Medien im DaZ-Kontext
- eren un ernen n der zweiten Sprache
- Sprachvergleich unter didak- tischen Aspekten
- Sprachmodul 1
- Sprachmodul 2
- Begleitveranstaltung
- Praktikumsmodul

### FPO LA Mathe 20151111 i.d.F. 20191010.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20191010.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20191010.md)

**Pflichtmodule (22):**
- Vorlesung Analysis I
- Analysis I<sup>1)</sup>
- Tafelübung Analysis I
- Vorlesung Lineare Algebra I
- Lineare Algebra I<sup>1)</sup>
- ien)
- Vorlesung Analysis II
- Gym Analysis II<sup>1)</sup>
- Tafelübung Analysis II
- Vorlesung Lineare Algebra II
- Lehr Lineare Algebra II<sup>1)</sup>
- ule (
- Vorlesung Algebra
- chtm Algebra<sup>2)</sup>
- Pfli
- Köhi<sup>2)</sup>
- rperteore
- Vorlesung Analysis für Lehramt
- Analysis für Lehramt
- Tafelübung Analysis für Lehramt
- (2) Funktionentheorie<sup>2)</sup> Vorlesung Funktionentheorie I
- (2) Übung Funktionentheorie I

### FPO LA Mathe 20151111 i.d.F. 20201029.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20201029.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20201029.md)

**Pflichtmodule (3):**
- Funktionentheorie<sup>2)</sup>
- Übung Funktionentheorie I
- ule (Lehramt an Gymnasien)

### FPO LA Mathe 20151111 i.d.F. 20230426.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20230426.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20230426.md)

**Pflichtmodule (2):**
- Übung Funktionentheorie I
- ule (Lehramt an Gymnasien)

### FPO LA PuG 20090330 i.d.F. 20201026.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-pug-20090330-idf-20201026.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-pug-20090330-idf-20201026.md)

**Pflichtmodule (3):**
- Grundlagen der Fachdidaktik Politik und Gesellschaft
- PuGDid 2:
- Weiterführung der Fachdidaktik Politik und Gesellschaft (RS-GS-MS)

### FPO LA PuG 20240904.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-pug-20240904.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-pug-20240904.md)

**Pflichtmodule (6):**
- Grundlagen der Fachdidaktik Politik und Gesellschaft
- PuGDid 2: Weiterführung der Fachdidaktik Po- litik und Gesellschaft
- PuGDid 2: Weiterführung der Fachdidaktik
- Politik und Gesellschaft (RS-GS-MS)
- PuGDid 2: Weiterführung der Fachdidak- tik Politik und Gesellschaft
- (FG GS)

### FPO LA Sozial 20201026 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-sozial-20201026-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-sozial-20201026-aes.md)

**Pflichtmodule (17):**
- Grundlagen der Fachdidaktik Politik und Gesellschaft
- PuGDid 2:
- Weiterführung der Fachdidaktik Politik und Gesellschaft (RS-GS-MS)
- PuGDid 2: Witfüh d Fhdidktik
- eerrung er aca Politik und Gesellschaft (RS- GS-MS)
- PuGDid 2: Weiterführung der Fachdidaktik
- Politik und Gesellschaft (FG GS)
- Gesellschaftsunterricht
- PuGDid 2: Weiterführung der Fachdidaktik Politikund Gesellschaft
- g handelt es sich um eine Empfeh kreten Lehrveranstaltung durch d hält die Tabelle folgend
- Fachwissenschaft
- ExamenskolloquiumSoziologie
- Fachdidaktik
- PuGDid 4:
- Vertiefung der Fachdidaktik Politi und Gesellschaft
- PuGDid 5: Prüfungsvorbereitung
- PuGDid 6: PraxisbezogeneEinführung

### LA Arbeitslehre FPO LA ArbL 20090727 i.d.F. 20190913.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-arbeitslehre-fpo-la-arbl-20090727-idf-20190913.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-arbeitslehre-fpo-la-arbl-20090727-idf-20190913.md)

**Pflichtmodule (8):**
- Grundlagen der Fach-
- didaktik (GFD)
- wissenschaft (GFW)
- Medien und Methoden I
- (MuM I)
- Medien und Methoden II
- (MuM II)<sup>2</sup>
- ret un eru (u)

### LA Beruf und Wirtschaft FPO LA BuW 20090727 i.d.F. 20210301.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-beruf-und-wirtschaft-fpo-la-buw-20090727-idf-20210301.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-beruf-und-wirtschaft-fpo-la-buw-20090727-idf-20210301.md)

**Pflichtmodule (8):**
- Grundlagen der Fach-
- wissenschaft (GFW)
- didaktik (GFD)
- Medien und Methoden I
- (MuM I)
- Medien und Methoden II
- (MuM II)<sup>2</sup>
- re un eru (u)

### LA Deutsch FPO LA Deutsch 20090226 i.d.F. 20200203.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20200203.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20200203.md)

**Pflichtmodule (27):**
- Basismodul Fachdidaktik Deutsch
- (BM FDD)
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
- Grundlagen der Neueren deutschen Literatur- wissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literatur- wissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik (Med-BM-LANV) Afl
- ubaumodue Linguistik (LingAM)für Lehramt RS/MS/GS<sup>2</sup>
- Literaturgeschichte (LitG AM)
- Lektüreseminar<sup>4</sup>
- Basismodul Fachdidaktik
- Deutsch (BM FDD)
- Grundlagen der Germanistischen Linguistik 1 (LingBM 1)
- Grundlagen der Germanistischen Linguistik 2 (LingBM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen MdiäitikMdBM LANV
- evs (e ) Aufbaumodule
- Linguistik (LingAM)für Lehramt RS/MS/GS<sup>2</sup>
- Literaturgeschichte
- (LitG AM MS/GS) Vertiefungsmodule
- Hauptseminar aus den Bereichen SprachwandelundVariation
- Sprachwandel und Variation (Ling VM 1)
- Gegenwartssprache/DaF (Ling VM 2)
- Kolleg aus den Bereichen Gegenwarts- sprache oder DeutschalsFremdsprache
- Neuere deutsche Literatur
- (NdL VM)

### LA Deutsch FPO LA Deutsch 20090226 i.d.F. 20200923.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20200923.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20200923.md)

**Pflichtmodule (24):**
- Basismodul Fachdidaktik Deutsch
- (BM FDD)
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
- Grundlagen der Neueren deutschen Literatur- wissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literatur- wissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik (Med-BM-LANV)
- Grundlagen der Germanistischen Linguistik 1 (LingBM 1)
- Grundlagen der Germanistischen Linguistik 2 (LingBM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik(MedBM LANV)
- Afbdl
- uaumoue Linguistik (LingAM)für Lehramt RS/MS/GS<sup>2</sup>
- Literaturgeschichte
- (LitG AM MS/GS) Vertiefungsmodule
- Sprachwandel und Variation
- Kolleg aus den Bereichen Sprachwandel undVariation
- Gegenwartssprache/DaF
- Kolleg aus den Bereichen Gegenwarts- sprache oder DeutschalsFremdsprache
- Neuere deutsche Literatur
- (NdL VM)
- Basismodul Fachdidaktik
- Deutsch (BM FDD)

### LA Deutsch FPO LA Deutsch 20090226 i.d.F. 20220914.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20220914.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20220914.md)

**Pflichtmodule (20):**
- Ling BM-1<sup>2</sup> Grundlagen der germanistischen Linguistik
- Lit BM<sup>4</sup> Grundlagen des wissenschaftli- chen Arbeitens in der Literatur- wissenschaft
- NdL BM-1<sup>5</sup> Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- Ling BM-2<sup>2</sup>
- Grundlagen der historischen Linguistik
- Basismodul Fachdidaktik Deutsch (BM FDD)
- Ling BM-1<sup>2</sup> Grundlagen der germanisti- schen Linguistik
- NdL BM-1<sup>4</sup> Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- Ling BM-2<sup>2</sup> Gdl d hitih
- runagen er sorscen Linguistik
- NdL BM-2<sup>4</sup> Grundlagen der Neueren deut- schen Literaturwissenschaft 2
- Med BM nv<sup>4</sup> Grundlagen der Germanisti- schen Mediävistik – nicht ver-
- tieftes LA
- Ling BM-2<sup>2</sup> Grundlaen der historischen
- g Linguistik
- Med BM nv<sup>4</sup> Grundlagen der Germanisti- schen Mediävistik – nicht ver- tieftes LA
- Basismodul Basismodul Fachdidaktik
- Deutsch (BM FDD)
- Basismodul Fachdidaktik Deutsc
- (BM FDD)

### LA Deutsch FPO LA Deutsch 20200203 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20200203-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20200203-aes.md)

**Pflichtmodule (4):**
- Basismodul Fachdidaktik Deutsch
- (BM FDD)
- Basismodul Fachdidaktik
- Deutsch (BM FDD)

### LA Deutsch FPO LA Deutsch 20220914 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20220914-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20220914-aes.md)

**Pflichtmodule (13):**
- Ling BM-1<sup>2</sup> Grundlagen der germanistischen Linguistik
- Lit BM<sup>4</sup> Grundlagen des wissenschaftli- chen Arbeitens in der Literatur- wissenschaft
- NdL BM-1<sup>5</sup> Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- Ling BM-2<sup>2</sup>
- Grundlagen der historischen Linguistik
- Med BM<sup>6</sup> Grundlagen der Germanisti- schen Mediävistik
- NdL BM-2<sup>5</sup> Grundlagen der Neueren deut- schen Literaturwissenschaft 2
- Ling BM-1<sup>2</sup> Grundlagen der germanisti- schen Linguistik
- NdL BM-1<sup>4</sup> Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- Ling BM-2<sup>2</sup> Gdl d hitih
- runagen er sorscen Linguistik
- NdL BM-2<sup>4</sup> Grundlagen der Neueren deut- schen Literaturwissenschaft 2
- Med BM nv<sup>4</sup> Grundlagen der Germanisti- schen Mediävistik – nicht ver- tieftes LA

### LA Englisch 20090226 i.d.F. 20200124.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20090226-idf-20200124.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20090226-idf-20200124.md)

**Pflichtmodule (30):**
- Basismodul I
- Language
- Basismodul II Linguistics (A)
- Basismodul III
- Linguistics (B)
- Basismodul IV Literature(A)
- Basismodul V Literature(B)
- Basismodul VI Culture
- Basismodul VII
- Landeskunde
- Zwischenmodul
- L-GYM Linguistics
- Mittelseminar
- Zwischenmodul L-GYM Literature
- Descriptive Phonetics
- Zwischenmodul L-GYM Language
- Practical Phonetics
- Basismodul Englischdidaktik
- GLC I
- Elementarmodul L-UF Linguistics I
- Elementarmodul L-UF Linguistics II
- Elementarmodul L-UF Literature I
- Elementarmodul L-UF Literature II
- LK US/UK
- Elementarmodul L-UF Landeskunde
- Presentation Skills<sup>3</sup>
- Zwischenmodul L-UF Language
- Afbmdl L-UF
- uauou Language
- Hauptmodul L-UF

### LA Englisch 20200124 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20200124-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20200124-aes.md)

**Pflichtmodule (31):**
- Basismodul I
- Language
- Basismodul II Linguistics (A)
- Basismodul III
- Linguistics (B)
- Basismodul IV Literature(A)
- Basismodul V Literature(B)
- Basismodul VI Culture
- Basismodul VII
- Landeskunde
- Zwischenmodul
- L-GYM Linguistics
- Mittelseminar
- Zwischenmodul L-GYM Literature
- Descriptive Phonetics
- Zwischenmodul L-GYM Language
- Practical Phonetics
- Basismodul Englischdidaktik
- GLC I
- Elementarmodul L-UF Linguistics I
- Elementarmodul L-UF Linguistics II
- Elementarmodul L-UF Literature I
- Elementarmodul L-UF Literature II
- LK US/UK
- Elementarmodul L-UF Landeskunde
- Presentation Skills<sup>3</sup>
- ihdl
- Zwscenmou L-UF Language
- Afbmdl L-UF
- uauou Language
- Hauptmodul L-UF

### LA Erweiterungsfach Chinesisch FPO LA Chin. 20161111 i.d.F. 20190828.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20161111-idf-20190828.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20161111-idf-20190828.md)

**Pflichtmodule (2):**
- Basismodul Chine-
- sischdidaktik

### LA Erweiterungsfach Chinesisch FPO LA Chin. 20230822 i.d.F. 20260331.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822-idf-20260331.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822-idf-20260331.md)

**Pflichtmodule (2):**
- Basismodul Chinesischdidak- tik
- didaktik I

### LA Erweiterungsfach Chinesisch FPO LA Chin. 20230822.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822.md)

**Pflichtmodule (2):**
- Basismodul Chinesischdi-
- daktik

### LA Französisch 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-20210624-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-20210624-aes.md)

**Pflichtmodule (3):**
- Basismodul Didaktik der
- romanischen Sprachen
- Mittelseminar Fachdidaktik Französisch

### LA Französisch FPO LA Französisch 20090309 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-fpo-la-franzoesisch-20090309-idf-20210624.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-fpo-la-franzoesisch-20090309-idf-20210624.md)

**Pflichtmodule (3):**
- Basismodul Didaktik der
- romanischen Sprachen
- Mittelseminar Fachdidaktik Französisch

### LA Geographie FPO LA Geo 20090310 i.d.F. 20221011.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-geographie-fpo-la-geo-20090310-idf-20221011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-geographie-fpo-la-geo-20090310-idf-20221011.md)

**Pflichtmodule (4):**
- Einführung in die Planung und Analyse von Geographieunterricht
- Aktuelle Fragestellungen der Geographiedidaktik
- GeoDid 2: Geographiedidaktik – Vertiefung
- Ausgewählte Fragestellungen der Geographiedidaktik II

### LA Geographie FPO LA Geo 20230928.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-geographie-fpo-la-geo-20230928.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-geographie-fpo-la-geo-20230928.md)

**Pflichtmodule (4):**
- Einführung in die Planung und Analyse von Geographieunterricht
- Aktuelle Fragestellungen der Geographiedidaktik
- GeoDid 2: Geographiedidaktik – Vertiefung
- Ausgewählte Fragestellungen der Geographiedidaktik II

### LA Geschichte FPO LA Geschichte 20090310 i.d.F. 20180911.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20090310-idf-20180911.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20090310-idf-20180911.md)

**Pflichtmodule (18):**
- Basismodul I
- Basismodul II
- Basismodul III
- Basismodul IV
- Methodische und Theoretische
- Methodische Grundlagen
- Theoretische Grundlagen
- undMethodik
- Landesgeschichte Schwerpunkt Historische For- schungspraxis Landesgeschichte
- Basismodul I<sup>2</sup>
- Basismodul II<sup>3</sup>
- Landesgeschichte
- Schwerunkt Historisches
- p Fachwissen Landesge- schichte
- Basismodul III<sup>4</sup>
- Basismodul Didaktik der Geschichte
- Einführung in die Planung und Analy- se des Geschichts- unterrichts
- Einführung in die Pla- nung und Analyse des Geschichts-unterrichts

### LA Geschichte FPO LA Geschichte 20180911 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20180911-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20180911-aes.md)

**Pflichtmodule (5):**
- Basismodul I<sup>2</sup>
- Basismodul II<sup>3</sup>
- Landesgeschichte
- Basismodul Didaktik der Geschichte
- Einführung in die Planung und Analyse des Geschichts- unterrichts

### LA Griechisch FPO LA Griechisch 20090310 i.d.F. 20200806.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-griechisch-fpo-la-griechisch-20090310-idf-20200806.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-griechisch-fpo-la-griechisch-20090310-idf-20200806.md)

**Pflichtmodule (10):**
- Prosa
- Lektüre
- Srachübnen I
- Sprache Ib
- Poesie 2
- oese
- Prosa 2
- rosa
- Srhübnn II
- pacuge

### LA Informatik FPO LA INF 20220421.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20220421.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20220421.md)

**Pflichtmodule (9):**
- Grundlagen der Programmierung
- Sichere Systeme
- Einführung in die Algorithmik
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende
- Parallele und funktionale Programmierung
- Softwareentwicklung in Großprojekten*
- Konzeptionelle Modellierung und Grundlagen von Datenbanken
- Grundlagen der Systemprogrammie- rung
- Grundlagen des Maschinellen Lernens und der Künstlichen Intelligenz

### LA Informatik FPO LA INF 20240904.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20240904.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20240904.md)

**Pflichtmodule (27):**
- Grundlagen der Systemprogrammierung
- Grundlagen des Maschinellen Lernens und der Künstlichen Intelligenz
- Grundlagen der Programmierung
- Sichere Systeme
- Einführung in das Software Engineering
- Einführung in die Algorithmik
- Einführung in Datenbanken
- Parallele und funktionale Programmierung
- Praktikum Informatik
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende
- Praktikum Maschinen- programmierung
- Grundlagen der Informatik(GdI-Kompakt)
- Einführung in die Fachdidaktik Informatik VÜ 2
- Didaktik der Informatik 1
- Praktikum zur Anwendung von Informatiksystemen aus fachdidaktischerSicht
- nkte 9
- Grundlagen der Programmierung V 2
- Programmierung
- Einführung in das Software
- Engineering
- nrung n e Algorithmik
- Eifüh i Dbk
- nrung n atenanen
- nkte 11
- Grundlagen des
- Maschinellen Lernens und der Künstlichen Intelligenz
- unkte

### LA Italienisch 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-20210624-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-20210624-aes.md)

**Pflichtmodule (2):**
- Basismodul Didaktik
- der romanischen Sprachen

### LA Italienisch FPO LA Italienisch 20090325 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-fpo-la-italienisch-20090325-idf-20210624.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-fpo-la-italienisch-20090325-idf-20210624.md)

**Pflichtmodule (2):**
- Basismodul Didaktik
- der romanischen Sprachen

### LA Katholische Religionslehre 20210415 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-20210415-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-20210415-aes.md)

**Pflichtmodule (2):**
- Basismodul Grundlaen
- g der Fachdidaktik

### LA Katholische Religionslehre FPO LA KathRel 20090727 i.d.F. 20210415.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20090727-idf-20210415.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20090727-idf-20210415.md)

**Pflichtmodule (2):**
- Basismodul Grundlaen
- g der Fachdidaktik

### LA Katholische Religionslehre FPO LA KathRel 20240118.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20240118.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20240118.md)

**Pflichtmodule (2):**
- Basismodul Grundlagen
- der Fachdidaktik

### LA Mathematik  FPO LA Mathe 20191010 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-fpo-la-mathe-20191010-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-fpo-la-mathe-20191010-aes.md)

**Pflichtmodule (22):**
- Vorlesung Analysis I
- Analysis I<sup>1)</sup>
- Tafelübung Analysis I
- Vorlesung Lineare Algebra I
- Lineare Algebra I<sup>1)</sup>
- ien)
- Vorlesung Analysis II
- Gym Analysis II<sup>1)</sup>
- Tafelübung Analysis II
- Vorlesung Lineare Algebra II
- Lehr Lineare Algebra II<sup>1)</sup>
- ule (
- Vorlesung Algebra
- chtm Algebra<sup>2)</sup>
- Pfli
- Köhi<sup>2)</sup>
- rperteore
- Vorlesung Analysis für Lehramt
- Analysis für Lehramt
- Tafelübung Analysis für Lehramt
- Funktionentheorie<sup>2)</sup> Vorlesung Funktionentheorie I
- (2) Übung Funktionentheorie I

### LA Musik 20220601 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-musik-20220601-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-musik-20220601-aes.md)

**Pflichtmodule (8):**
- Grundlagen fachbezogenen Leh-
- rens und Lernens
- MS1 2
- Fachdidaktisches Lernen, Lehren und Beurteilen
- mme SWS und ECTS-Punkte: 10
- Grundlagen des Musikunterrichts
- Fachbezogenes Lehren und Lernen: Praxis des Musikunterrichts
- und ECTS-Punkte:

### LA Musik FPO LA Musik 20090326 i.d.F. 20220601.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-musik-fpo-la-musik-20090326-idf-20220601.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-musik-fpo-la-musik-20090326-idf-20220601.md)

**Pflichtmodule (7):**
- Grundlagen fachbezogenen
- Lehrens und Lernens
- Fachdidaktisches Lernen, Lehren und Beurteilen
- umme SWS und ECTS-Punkte:
- MS1 2
- umme SWS und ECTS-Punkte: 10
- Grundlagen des Musikunterrichts

### LA Musik FPO LA Musik 20240904.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-musik-fpo-la-musik-20240904.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-musik-fpo-la-musik-20240904.md)

**Pflichtmodule (3):**
- Grundlagen<sup>1</sup>
- me SWS und ECTS-Punkte:
- (2) Grundlagen musikpäda- gogischer Forschung

### LA Spanisch 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-spanisch-20210624-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-spanisch-20210624-aes.md)

**Pflichtmodule (2):**
- Basismodul Didaktik der romanischen Spra-
- chen

### LA Spanisch FPO LA Spanisch 20090401 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-spanisch-fpo-la-spanisch-20090401-idf-20210624.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-spanisch-fpo-la-spanisch-20090401-idf-20210624.md)

**Pflichtmodule (5):**
- Basismodul Spanische Sprachwissenschaft<sup>5</sup>
- Basismodul Spanische Literatur- wissenschaft<sup>6</sup>
- Sanische Srachraxis 3<sup>1, 3</sup>
- Basismodul Didaktik der romanischen Srachen
- Proseminar Fachdidaktik Spanisch

### LA Sport FPO LA Sport 20230822.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-sport-fpo-la-sport-20230822.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-sport-fpo-la-sport-20230822.md)

**Pflichtmodule (1):**
- <sup>1</sup>

### LA Wirtschaftswissenschaften FPO LA WiWi 20090401 i.d.F. 20190916.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-wirtschaftswissenschaften-fpo-la-wiwi-20090401-idf-20190916.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-wirtschaftswissenschaften-fpo-la-wiwi-20090401-idf-20190916.md)

**Pflichtmodule (6):**
- Grundlagen der Fachdidaktik Wirtschaftswissenschaften (Gymnasium)
- Seminar Medien im Wirtschaftsunterricht
- Praxisfelder der Fachdidaktik
- Grundlagen der Fachdidaktik Wirtschaftswissenschaften (Realschule)
- Medien im Wirtschaftsunterricht
- Praxisfelder der Fachdidaktik Wirtschaftswissenschaften

### LA Wirtschaftswissenschaften FPO LA WiWi 20090401 i.d.F. 20200923.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-wirtschaftswissenschaften-fpo-la-wiwi-20090401-idf-20200923.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-wirtschaftswissenschaften-fpo-la-wiwi-20090401-idf-20200923.md)

**Pflichtmodule (6):**
- Grundlagen der Fachdidaktik Wirtschaftswissenschaften (Gymnasium)
- Seminar Medien im Wirtschaftsunterricht
- Praxisfelder der Fachdidaktik
- Grundlagen der Fachdidaktik Wirtschaftswissenschaften (Realschule)
- Medien im Wirtschaftsunterricht
- Praxisfelder der Fachdidaktik Wirtschaftswissenschaften

### LA Wirtschaftswissenschaften FPO LA WiWi 20090401 i.d.F. 20210225.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-wirtschaftswissenschaften-fpo-la-wiwi-20090401-idf-20210225.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-wirtschaftswissenschaften-fpo-la-wiwi-20090401-idf-20210225.md)

**Pflichtmodule (8):**
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Wirtschaftsprivatrecht
- Grundlagen der Fachdidaktik Wirtschaftswissenschaften (Gymnasium)
- Seminar Medien im Wirtschaftsunterricht
- Praxisfelder der Fachdidaktik
- Grundlagen der Fachdidaktik Wirtschaftswissenschaften (Realschule)
- Medien im Wirtschaftsunterricht
- Praxisfelder der Fachdidaktik Wirtschaftswissenschaften

### pdf vom 26.02.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20deutsch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20deutsch.md)

**Pflichtmodule (22):**
- Basismodul: Grundlagen der Germanistischen Linguistik
- Einführungskurs: Einführung in die GermanistischeLinguistik
- Basismodul: Grundlagen der Germanistischen Mediävistik
- Einführungskurs: Einführung in die GermanistischeMediävistik
- Basismodul: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die Neuere deutsche Literatur- wissenschaft
- Abschlussmodul Schriftliche Hausarbeit
- Kolloquium zur Besprechung der Schriftlichen Hausarbeit
- SchriftlicheHausarbeit
- Basismodul: Grundlagen der Fachdidaktik Deutsch
- Vorlesung mit Übung: Fachdidak- tik Deutsch: Geschichte – Grund- fragen –Grundlagen
- Proseminar: Einführung in die Literatur-, Sprach- und Mediendi- daktik Deutsch
- Einführungskurs<sup>~~1~~</sup>: Einführung in die Neuere deutsche Literatur- wissenschaft
- Kolloquium zur Besprechung der SchriftlicheHausarbeit
- Examensvorbereitung
- ExamenskursNDL
- Examenskurs Sprachwissenschaft
- Grundkurs: Einführung in die GermanistischeLinguistik
- Einführungskurs<sup>~~2~~</sup>: Einführung in die Neuere deutsche Literatur- wissenschaft
- Basismodul: Grundlagen der
- Fachdidaktik Deutsch
- VorlesungmitÜbung: Fachdidak-

### pdf vom 26.02.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20ev-20religion.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20ev-20religion.md)

**Pflichtmodule (1):**
- (4) Pflichtmodul Praktikum

### pdf vom 09.03.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20franzoesisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20franzoesisch.md)

**Pflichtmodule (13):**
- Vertiefungsmodul Französische Sprachwissenschaft 2
- Mittelseminar
- Vertiefungsmodul Französische Literatur- und Kulturwissenschaft 2
- Abschlussmodul Schriftliche Hausarbeit
- Kolloquium zur Besprechung der Schriftlichen Hausarbeit
- SchriftlicheHausarbeit
- Fachdidaktisches Modul 1: Einführung in die Didaktik des Französischen
- Übung: Einführung in die Fachdidaktik desFranzösischen
- Proseminar / Übung
- Fachdidaktisches Modul 2: Didaktik des Französischen (Lehramt Realschulen)
- Übung zur Didaktik der französischen Sprache an RS
- Mittelseminar: Französische Sprach- und Kulturvermittlung an RS
- Angeleitete Lektüre

### pdf vom 25.03.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20italienisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20italienisch.md)

**Pflichtmodule (3):**
- Abschlussmodul Schriftliche Hausarbeit
- Kolloquium zur Besprechung der Schriftlichen Hausarbeit
- SchriftlicheHausarbeit

### pdf vom 26.03.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20latein.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20latein.md)

**Pflichtmodule (17):**
- Basismodul: Lateinische Lite- raturwissenschaft I (LIT 1)
- Übung: Einführung in die Lateini- sche Philologie
- <sup>Vorlesung: Lateinische Literatur</sup> (Prosa)
- Proseminar: Lateinische Literatur (Prosa)
- Basismodul: Lateinische Sprachwissenschaft und Sprachpraxis (SPR 1)
- Übung: Deutsch-lateinische Ü- bersetzung (Grundlagen 1)
- Übung: Deutsch-lateinische Ü- bersetzung (Grundlagen 2)
- Übung: Lateinisch-deutsche Ü- bersetzung (Grundlagen)
- Basismodul: Altertumswissen- schaft für Latinisten (AWS 1)
- Vorlesung / Übung Alte Ge- schichte
- Vorlesung / Übung Klassische Archäologie
- Exkursion mit Vorbereitungskurs
- on aus Alter Geschichte und Archäologie zus
- Examensvorbereitung
- <sup>Examenskurs zur Klausurvorbe-</sup> reitung
- Übung Interpretation
- Übung Texterstellung

### pdf vom 26.03.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20mathematik.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20mathematik.md)

**Pflichtmodule (35):**
- Analysis (Ana)
- AnalysisI
- Übungen zur AnalysisI
- AnalysisII
- Übungen zur AnalysisII
- Lineare Algebra (LA)
- LineareAlgebraI
- Übungen zur Lin. AlgebraI
- LineareAlgebraII
- Übungen zur Lin. AlgebraII
- Orientierungsseminar<sup>~~2~~</sup>(OrSe)
- Teil 1
- Teil 2
- Algebra(Alg)
- Übungen
- Stochastische Modellbildung (StMo)
- Mehrdimensionale Integration (MInt)
- Vorlesung/Übung
- Angewandte Mathematik<sup>1</sup>(AMLA)
- Elemente der Zahlentheorie (EZth)
- Gew. Differentialgleichungen (GDgl)
- Geometrie für das Lehramt (GeoLA)
- Funktionentheorie (Futh)
- Geometrie (Geom)
- Elemente der Linearen Algebra (ELA)
- Elemente der Lin. AlgebraI
- Übungen Lin. AlgebraI
- Elemente der Lin. AlgebraII
- Übungen Lin. AlgebraII
- Elemente der Analysis (EAna)
- Elemente der AnalysisI
- Übungen AnalysisI
- Elemente der AnalysisII
- Übungen AnalysisII
- Analytische Geometrie (AGeo)

### pdf vom 26.03.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20musik.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20musik.md)

**Pflichtmodule (9):**
- (4) Grundlagen fachbezogenen Lehrens undLernens
- (5) Fachdidaktisches Lernen, Lehren und Beurteilen
- Grundlagen u. musikalische Praxis
- (2) Musikalische Praxis 1
- (2) Musikalische Praxis 2
- (2) _2. Fachdidaktik/Musikpädagogik_
- (2) Fachbezogenes Lehren und Lernen
- (4) Modellemusikalischer Praxis
- (3) GrundlagendesMusikunterrichts

### pdf vom 01.04.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20spanisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20spanisch.md)

**Pflichtmodule (3):**
- Abschlussmodul Schriftliche Hausar- beit
- Kolloquium zur Besprechung der Schriftli- chen Hausarbeit
- SchriftlicheHausarbeit

### pdf vom 09.03.2009 i.d.F. 14.04.2016

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-chemie-april2016.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-chemie-april2016.md)

**Pflichtmodule (2):**
- Grundlagen der anorganisch- chemischen Laborpraxis
- Prüfungsvorbereitung

### pdf vom 09.03.2009 i.d.F. 18.09.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-chemie-oktober-2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-chemie-oktober-2015.md)

**Pflichtmodule (2):**
- Grundlagen der anorganisch- chemischen Laborpraxis
- Prüfungsvorbereitung

### pdf vom 26.02.2009 i.d.F. 16.01.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-feb2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-feb2015.md)

**Pflichtmodule (10):**
- Grundlagen der Fachdidaktik Deutsch
- (BM FDD)
- Sprach-undMediendidaktik
- Grundlagen der Neueren deut- schen Literatur
- deutsche Literaturwissenschat
- (NdL 1)
- prac- un eena
- Grundlagen der Germanisti-
- schen Linguistik (Ling1)
- Vorlesung<sup>2</sup> 2

### pdf vom 26.02.2009 i.d.F. 28.03.2011

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-maerz2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-maerz2011.md)

**Pflichtmodule (20):**
- Basismodul: Grundlagen der Germanistischen Linguistik
- Einführungskurs: Einführung in die GermanistischeLinguistik
- Basismodul: Grundlagen der Germanistischen Mediävistik
- Einführungskurs: Einführung in die GermanistischeMediävistik
- Basismodul: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die Neuere deutsche Literatur- wissenschaft
- Examensvorbereitung
- ExamenskursNDL
- Examenskurs Sprachwissenschaft oder Mediävistik
- Basismodul: Grundlagen der Fach- didaktik Deutsch
- Vorlesung mit Übung: Fachdidaktik Deutsch: Geschichte – Grundfragen – Grundlagen
- Proseminar: Einführung in die Literatur-, Sprach-undMediendidaktik Deutsch
- Einführungskurs: Einführung in die Germanistische Linguistik
- Einführungskurs<sup>~~1~~</sup>: Einführung in die Neuere deutsche Literatur- wissenschaft
- Basismodul: Grundlagen der Fachdi- daktik Deutsch
- Basismodul: Grundlagen der Germa- nistischen Linguistik
- Grundkurs: Einführung in die Germanis- tischeLinguistik
- Basismodul: Grundlagen der Neue- ren deutschen Literatur
- Einführungskurs<sup>~~2~~</sup>: Einführung in die Neuere deutsche Literaturwissenschaft
- Proseminar: Einführung in die Litera- tur-, Sprach- und Mediendidaktik Deutsch

### pdf vom 26.02.2009 i.d.F. 25.05.2012

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-mai2012.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-mai2012.md)

**Pflichtmodule (19):**
- Basismodul: Grundlagen der Germanistischen Linguistik
- Einführungskurs: Einführung in die Germanistische Linguistik
- Basismodul: Grundlagen der Germanistischen Mediävistik
- Einführungskurs: Einführung in die GermanistischeMediävistik
- Basismodul: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die Neuere deutsche Literatur- wissenschaft
- Examensvorbereitung
- ExamenskursNDL
- Examenskurs Sprachwissenschaft oder Mediävistik
- Basismodul: Grundlagen der Fach- didaktik Deutsch
- Vorlesung mit Übung: Fachdidaktik Deutsch: Geschichte – Grundfragen – Grundlagen
- Proseminar: Einführung in die Literatur-, Sprach-undMediendidaktik Deutsch
- Einführungskurs<sup>~~1~~</sup>: Einführung in die Neuere deutsche Literatur- wissenschaft
- Basismodul: Grundlagen der Fachdi- daktik Deutsch
- Basismodul: Grundlagen der Germa- nistischen Linguistik
- Grundkurs: Einführung in die Germanis- tischeLinguistik
- Basismodul: Grundlagen der Neue- ren deutschen Literatur
- Einführungskurs<sup>~~2~~</sup>: Einführung in die Neuere deutsche Literaturwissenschaft
- Proseminar: Einführung in die Litera- tur-, Sprach- und Mediendidaktik Deutsch

### pdf vom 26.02.2009 i.d.F. 10.11.2016

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-nov2016.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-nov2016.md)

**Pflichtmodule (40):**
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Analyseseminar 1
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
- Analyseseminar 2
- Grundlagen der Neueren deut- schen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deut- schen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1(Med BM 1)
- Grundlagen der Germanistischen Mediävistik 2(Med BM 2)
- Grundlagen der Fachdidaktik Deutsch (BM FDD)
- Proseminar: Einführung in die Literatur- Sprach- und Mediendidaktik
- Grundlagen der Neueren deutschen Literatur- wissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literatur- wissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 2(MedBM 2)
- Grundlagen der Germanistischen Lingu- istik 1 (Ling BM 1)
- Grundlagen der Germanistischen Lingu- istik 2 (Ling BM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Medi- ävistik 2(Med BM 2)
- Proseminar: Einführung in die Literatur- Sprach-undMediendidaktik
- Basismodul DiDaZ (LA GS)
- Seminar2
- Tutorium
- Tutorium oder5Kolloquium
- Basismodul DiDaZ (LA MS)
- Seminar aus dem Bereich „Theorie und Praxis des Zweitspracherwerbs / der Mehrsprachigkeit“
- Seminar aus dem Bereich „Methoden, Verfahren,Arbeitsformen und Medien“
- Tutorium oder3Kolloquium
- Grundlagen des Deutschen als Zweitsprache
- Theorie und Praxis der Sprachvermittlung
- Sprache im Fachunterricht
- Sprachsystem und Zweitspracherwerb
- Zweitspracherwerb
- Sprachdiagnostik
- Lehren und Lernen in der zweiten Sprache
- Medien im DaZ-Kontext
- Sprachgebrauch und Sprachvermittlung
- Sprachvergleich unter di- daktischen Aspekten
- Sprachmodul 1
- Sprachmodul 2
- Praktikumsmodul

### pdf vom 26.02.2009 i.d.F. 29.11.2011

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-november2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-november2011.md)

**Pflichtmodule (19):**
- Basismodul: Grundlagen der Germanistischen Linguistik
- Einführungskurs: Einführung in die Germanistische Linguistik
- Basismodul: Grundlagen der Germanistischen Mediävistik
- Einführungskurs: Einführung in die GermanistischeMediävistik
- Basismodul: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die Neuere deutsche Literatur- wissenschaft
- Examensvorbereitung
- ExamenskursNDL
- Examenskurs Sprachwissenschaft oder Mediävistik
- Basismodul: Grundlagen der Fach- didaktik Deutsch
- Vorlesung mit Übung: Fachdidaktik Deutsch: Geschichte – Grundfragen – Grundlagen
- Proseminar: Einführung in die Literatur-, Sprach-undMediendidaktik Deutsch
- Einführungskurs<sup>~~1~~</sup>: Einführung in die Neuere deutsche Literatur- wissenschaft
- Basismodul: Grundlagen der Fachdi- daktik Deutsch
- Basismodul: Grundlagen der Germa- nistischen Linguistik
- Grundkurs: Einführung in die Germanis- tischeLinguistik
- Basismodul: Grundlagen der Neue- ren deutschen Literatur
- Einführungskurs<sup>~~2~~</sup>: Einführung in die Neuere deutsche Literaturwissenschaft
- Proseminar: Einführung in die Litera- tur-, Sprach- und Mediendidaktik Deutsch

### pdf vom 26.02.2009 i.d.F. 24.09.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-sept2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-sept2015.md)

**Pflichtmodule (35):**
- Grundlagen der Fachdidaktik Deutsch
- (BM FDD)
- Sprach-undMediendidaktik
- Grundlagen der Germanisti- schen Linguistik (Ling1)
- Grundlagen der Neueren deut- schen Literatur
- (NdL 1)
- Sprach- und Mediendidaktik
- Vertiefnsmodle
- ugu Fachdidaktik Deutsch (Litera-
- turdidaktik) (VM (a) FDD)
- Fachdidaktik Deutsch (Sprach-
- didaktik) (VM (b) FDD)
- Fachdidaktik Deutsch (Medien-
- didaktik) (VM (c) FDD)
- Examensmodul
- (EVK FDD) Studienbegleitendesfachdidaktisc
- Studienbegleitendes fachdidak-
- tisches Praktikum Deutsch
- Grundlagen der Germanisti-
- schen Linguistik (Ling1)
- Vorlesung<sup>2</sup> 2
- Grundlagen des
- Deutschen als Zweitsprache
- Sprache im Fachunterricht
- Sht d
- pracsysem un Zweitsracherwerb
- Sprachdiagnostik
- Vermittlung von Text- und Diskurskompetenz
- Lehren und Lernen
- in der zweiten Sprache
- Sprachvergleich unter di- daktischen Aspekten
- Sprachmodul 1
- Sprachmodul 2
- Begleitveranstaltung
- Praktikumsmodul

### pdf vom 26.02.2009 i.d.F. 31.03.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu.md)

**Pflichtmodule (25):**
- Basismodul: Grundlagen der Germanistischen Linguistik
- Einführungskurs: Einführung in ie GermanistischeLinguistik d
- Basismodul: Grundlagen der Germanistischen Mediävistik
- Einführungskurs: Einführung in die GermanistischeMediävistik
- Basismodul: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die Neuere deutsche Literatur- issenschaft w
- Examensvorbereitung
- ExamenskursNDL
- Examenskurs Sprachwissenschaft oder Mediävistik
- Basismodul: Grundlagen der Fachdidaktik Deutsch
- Vorlesung mit Übung: Fachdidak- tik Deutsch: Geschichte – Grund- fragen –Grundlagen
- Proseminar: Einführung in die Literatur-, Sprach- und Mediendi- daktik Deutsch
- Einführungskurs: Einführung in die GermanistischeLinguistik
- Einführungskurs<sup>~~1~~</sup>: Einführung in die Neuere deutsche Literatur- wissenschaft
- Abschlussmodul Schriftliche Hausarbeit
- Kolloquium zur Besprechung der SchriftlicheHausarbeit
- SchriftlicheHausarbeit
- Examenskurs Sprachwissenschaft
- Basismodul: Grundlagen der Fachdi- daktik Deutsch
- Vorlesung mit Übung: Fachdidaktik Deutsch: Geschichte – Grundfragen – Grundlagen
- Proseminar: Einführung in die Literatur-, Sprach-undMediendidaktik Deutsch
- Basismodul: Grundlagen der Germa- nistischen Linguistik
- Grundkurs: Einführung in die Germanis- tischeLinguistik
- Basismodul: Grundlagen der Neue- ren deutschen Literatur
- Einführungskurs<sup>~~2~~</sup>: Einführung in die Neuere deutscheLiteraturwissenschaft

### pdf vom 26.02.2009 i.d.F. 28.03.2011

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-englisch-maerz2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-englisch-maerz2011.md)

**Pflichtmodule (4):**
- Basismodul I Language
- Elementarmodul L-UF Linguistics
- Elementarmodul L-UF Literature
- Elementarmodul L-UF Landeskunde

### pdf vom 26.02.2009 i.d.F. 26.03.2012

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-englisch-maerz2012.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-englisch-maerz2012.md)

**Pflichtmodule (4):**
- Basismodul I Language
- Elementarmodul L-UF Linguistics
- Elementarmodul L-UF Literature
- Elementarmodul L-UF Landeskunde

### pdf vom 26.02.2009 i.d.F. 27.09.2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-englisch-sept2013.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-englisch-sept2013.md)

**Pflichtmodule (26):**
- Basismodul I
- Language
- Grundseminar
- Basismodul II Linuistics
- Basisvorlesung 1
- Basismodul III
- Literature
- Landeskunde USA/GB
- Basismodul IV Culture/Landeskunde
- Proseminar
- Zwischenmodul L‐GYM Linguistics
- Zwischenmodul L‐GYM Literature
- Writing in Academic Contexts
- Zwischenmodul
- L‐GYM Language
- Conversation Practice
- Basismodul Einführungsseminar TEFL
- Englischdidaktik Proseminar
- Mittelseminar
- Elementarmodul L‐UF
- Linguistics
- Elementarmodul L‐UF Landeskunde
- Seminar Landeskunde
- ÜbersetzungE‐D
- Writingin Academic Contexts
- Basismodul Englischdidaktik

### pdf vom 26.02.2009 i.d.F. 09.06.2011

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-juni2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-juni2011.md)

**Pflichtmodule (6):**
- Grundlagen und Fragen christlicher Ethik
- Religionswissenschaft
- (2Ü) Das Judentum(in seinem Verhältnis zum Christentum)
- Der Islam (in seinem Verhältnis zum Christentum)
- Grundfragen der Religionswissenschaft
- (4) Pflichtmodul Praktikum

### pdf vom 26.02.2009 i.d.F. 01.12.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-neu.md)

**Pflichtmodule (1):**
- (4) Pflichtmodul Praktikum

### pdf vom 26.02.2009 i.d.F. 15.09.2011

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-sept2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-sept2011.md)

**Pflichtmodule (6):**
- Grundlagen und Fragen christlicher Ethik
- Religionswissenschaft
- (2Ü) Das Judentum(in seinem Verhältnis zum Christentum)
- Der Islam (in seinem Verhältnis zum Christentum)
- Grundfragen der Religionswissenschaft
- (4) Pflichtmodul Praktikum

### (pdf vom 26.02.2009 i.d.F. 14.12.2017)

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-religion-dez2017.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-religion-dez2017.md)

**Pflichtmodule (18):**
- Basismodul: Theologie und wissenschaftliches Arbeiten
- RU in der Grundschule bzw. Mittelschule (FD)
- Biblisches Grundwissen
- (Lehramt GS/MS/RS)
- Grundlagen der Theologie
- und Religionspädagogik
- Biblische Theologie 1 (AT)
- AT – Geschichte Israels
- Biblische Theoloie 2 (NT)
- NT - Synoptische Evangelien/Jesus
- Biblische Theologie 3
- NT – Themen neutestamentl. Theologie: Paulus
- Systematische Theologie 1:
- Dogmatik (GMRS)
- Systematische Theologie 2:
- Ethik (GMRS)
- Epochen der Kirchengeschichte 1 - GS/MS/RS
- Kirchengeschichte 1

### pdf vom 26.02.2009 i.d.F. 01.10.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-religion-okt2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-religion-okt2015.md)

**Pflichtmodule (6):**
- Grundlagen und Fragen christlicher Ethik
- Religionswissenschaft
- (2Ü) Das Judentum(in seinem Verhältnis zum Christentum)
- Der Islam (in seinem Verhältnis zum Christentum)
- Grundfragen der Religionswissenschaft
- (4) Pflichtmodul Praktikum

### pdf vom 09.03.2009 i.d.F. 08.08.2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-aug2017.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-aug2017.md)

**Pflichtmodule (11):**
- Basismodul Französische Sprachpraxis 1
- Communication orale
- Introduction à la civilisation
- Basismodul Französische Srachraxis 2
- Phonétique pratique, orthophonie et intonation
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Basismodul Didaktik der
- romanischen Sprachen
- Mittelseminar Fachdidaktik Französisch
- Aubaumodu Didati der romanischen Sprachen

### pdf vom 09.03.2009 i.d.F. 24.09.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-neu-ws2010-2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-neu-ws2010-2011.md)

**Pflichtmodule (13):**
- Abschlussmodul Schriftliche Hausarbeit
- Schriftliche Hausarbeit
- ereichFachdidaktiksind im Fach Fra schulen folgende Module abzulegen: Modulbezeichnung
- Fachdidaktisches Modul 1: Einführung in die Didaktik des Französi- schen
- Übung: Einführung in die Fachdidaktik des Französischen
- Proseminar / Übung
- Fachdidaktisches Modul 2: Didaktik des Französischen (Lehramt Re- alschulen)
- Mittelseminar: Französische Sprach-, Litera- tur-und Kulturvermittlung
- Angeleitete Lektüre
- Vertiefungsmodul Freier Bereich
- Optionsmodul Sprachwissen- schaft
- Optionsmodul Literaturwis- senschaft
- Optionsmodul Sprachpraxis

### pdf vom 09.03.2009 i.d.F. 24.09.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-neu.md)

**Pflichtmodule (10):**
- Abschlussmodul Schriftliche Hausarbeit
- Kolloquium zur Besprechung der schriftlichen Hausarbeit
- Schriftliche Hausarbeit
- Fachdidaktisches Modul 1: Einführung in die Didaktik des Französi- schen
- Übung: Einführung in die Fachdidaktik des Französischen
- Proseminar / Übung
- Fachdidaktisches Modul 2: Didaktik des Französischen (Lehramt Re- alschulen)
- Übung zur Didaktik der französischen Spra- che an RS
- Mittelseminar: Französische Sprach- und Kulturvermittlung
- Angeleitete Lektüre

### pdf vom 09.03.2009 i.d.F. 29.09.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-sept2014.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-sept2014.md)

**Pflichtmodule (15):**
- Basismodul Didaktik der roma-
- nischen Sprachen
- Mittelseminar Fachdidaktik Franzö- sisch
- Basismodul Französische Sprachpraxis 1
- Communication orale
- Vocabulaire,idiomatique et civilisation II
- Basismodul Französische Sprachpraxis 2
- Phonétique pratique, orthophonie et intona- tion
- Basisseminar französische Sprachwissenschaft
- Basismodul Einführung in die Frankoromanistik
- Afbdl 1 Föih Shihf 1
- uaumou : ranzssce pracwssenscat
- Basismodul Didaktik der romani-
- schen Sprachen
- Mittelseminar Fachdidaktik Französisch

### pdf vom 10.03.2009 i.d.F. 28.10.2016

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-geographie-okt2016.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-geographie-okt2016.md)

**Pflichtmodule (4):**
- Einführung in die Planung und Analyse von Geographieunterricht
- Aktuelle Fragestellungen der Geographiedidaktik
- GeoDid 2: Geographiedidaktik – Vertiefung - FGGS
- Exkursion

### pdf vom 10.03.2009 i.d.F. 02.04.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-april2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-april2015.md)

**Pflichtmodule (9):**
- Prosa
- Lektüre
- Sprache Ia
- Sprachübungen I
- Poesie 2
- Poesie
- Prosa 2
- Sprache IIa
- Sprachübungen II

### pdf vom 25.03.2009 i.d.F. 08.08.2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-aug2017.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-aug2017.md)

**Pflichtmodule (10):**
- Basismodul Italienische
- Sprachpraxis 1
- Basismodl Italienische
- Foneticapratica
- pracpraxs
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft
- Basismodul Didaktik der
- romanischen Sprachen
- Mittelseminar Fachdidaktik Italienisch 2

### pdf vom 25.03.2009 i.d.F. 24.09.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-neu-ws2010-2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-neu-ws2010-2011.md)

**Pflichtmodule (2):**
- Abschlussmodul Schriftliche Hausarbeit
- SchriftlicheHausarbeit

### pdf vom 25.03.2009 i.d.F. 24.09.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-neu.md)

**Pflichtmodule (3):**
- Abschlussmodul Schriftliche Hausarbeit
- Kolloquium zur Besprechung der Schriftli- chen Hausarbeit
- SchriftlicheHausarbeit

### pdf vom 25.03.2009 i.d.F. 29.09.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-sept2014.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-sept2014.md)

**Pflichtmodule (10):**
- Basismodul Italienische Sprachpraxis 1
- Corso di italiano intermedio II
- Basismodul Italienische Sprachpraxis 2
- Tecniche di lettura
- Basismodul Einführung in die
- Italoromanistik
- Phonetik und Phonologie des Italienischen
- Basismodul Didaktik der
- romanischen Sprachen
- Mittelseminar Fachdidaktik Italienisch

### pdf vom 26.03.2009 i.d.F. 26.03.2012

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-latein-maerz2012.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-latein-maerz2012.md)

**Pflichtmodule (23):**
- Basismodul: Lateinische Literaturwissen- schaft I (LIT 1)
- Übung: Einführung in die Lateinische Philologie
- Vorlesung: Lateinische Literatur (Prosa)
- Proseminar: Lateinische Literatur (Prosa)
- Basismodul: Lateinische Sprachwissen- schaft und Sprachpraxis (SPR 1)
- Übung: Deutsch-lateinische Übersetzung (Grundlagen 1)
- Übung: Deutsch-lateinische Übersetzung (Grundlagen 2)
- Übung: Lateinisch-deutsche Übersetzung (Grundlagen)
- Basismodul: Altertumswissenschaft für Latinisten (AWS 1)
- Vorlesung / Übung Alte Geschichte
- Vorlesung / Übung Klassische Archäologie
- Exkursion mit Vorbereitungskurs
- Davon aus Alter Geschichte und Archäologie zusamme dabei mindestens 2 aus Archäologie
- Examensvorbereitung
- Examenskurs zur Klausurvorbereitung
- Übung Interpretation
- Übung Texterstellung
- Basismodul: Lateinische Fachdidaktik I(FD 1)
- Proseminar: Lateinische Fachdidaktik I
- Selbststudium (Lektürekanon Fachdidaktik I mit Konsultationen)
- Vertiefungsmodul: Lateinische Fachdidaktik II (FD 2)
- Proseminar: LateinischeFachdidaktik II
- Selbststudium (Lektürekanon Fachdidaktik II mit Konsultationen)

### pdf vom 26.03.2009 i.d.F. 21.10.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-latein-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-latein-neu.md)

**Pflichtmodule (16):**
- Basismodul: Lateinische Lite- raturwissenschaft I (LIT 1)
- Übung: Einführung in die Lateini- sche Philologie
- <sup>Vorlesung: Lateinische Literatur</sup> (Prosa)
- Proseminar: Lateinische Literatur (Prosa)
- Basismodul: Lateinische Sprachwissenschaft und Sprachpraxis (SPR 1)
- Übung: Deutsch-lateinische Übersetzung (Grundlagen 1)
- Übung: Deutsch-lateinische Übersetzung (Grundlagen 2)
- Übung: Lateinisch-deutsche Übersetzung (Grundlagen)
- Basismodul: Altertumswissen- schaft für Latinisten (AWS 1)
- Vorlesung / Übung Alte Ge- schichte
- Vorlesung / Übung Klassische Archäologie
- Exkursion mit Vorbereitungskurs
- Examensvorbereitung
- <sup>Examenskurs zur Klausurvorbe-</sup> reitung
- Übung Interpretation
- Übung Texterstellung

### pdf vom 26.03.2009 i.d.F. 14.03.2012

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-maerz2012.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-maerz2012.md)

**Pflichtmodule (50):**
- Analysis (Ana)
- AnalysisI
- Übungen zur AnalysisI
- AnalysisII
- Übungen zur Analysis II
- Lineare Algebra (LA)
- Lineare Algebra I
- Übungen zur Linearen Algebra I
- LineareAlgebraII
- Übungen zur Linearen AlgebraII
- Orientierungsseminar (OrSe)<sup>1,2</sup>
- Teil 1
- Teil 2
- Mehrdimensionale Integration (MInt)
- Übungen
- Stochastische Modellbildung (StMo)
- Algebra (Alg)
- Vertiefungsmodul Körpertheorie (VKT)
- Angewandte Mathematik(AMLA)<sup>~~1~~</sup>
- Geometrie (Geom)<sup>~~2~~</sup>
- Funktionentheorie (Futh)
- Gewöhnliche Differentialgleichungen (GDgl)
- ECTS-Punkte gesamt
- Elemente der Linearen Algebra (ELA)
- Elemente der Linearen AlgebraI
- Übungen Linearen AlgebraI
- Elemente der Linearen AlgebraII
- Übungen Linearen AlgebraII
- Elemente der Analysis (EAna)
- Elemente der AnalysisI
- Übungen AnalysisI
- Elemente der AnalysisII
- Übungen AnalysisII
- Analytische Geometrie (AGeo)
- Vorlesung/Übung
- Aufbaumodul Analysis (AmAn)<sup>~~1~~</sup>
- Elemente der Analysis III
- Elementare Stochastik (EStoch)
- Mathematisches Seminar in elemen- tarer Stochastik (SemEStoch)
- Geometrie für das Lehramt (GeoL)
- Mathematisches Seminar in Geomet- rie für das Lehramt (SemGeoL)
- Elementare Zahlentheorie (EZth)
- Mathematisches Seminar in elemen- tarer Zahlentheorie (SemEZth)
- Fachdidaktik A Mathematik (FDAR)
- Didaktik der Arithmetik und Bruchrech- nung
- Didaktikder Algebra
- Fachdidaktik B Mathematik (FDBR)
- DidaktikderGeometrie
- DidaktikderStochastik
- Didaktikder Zahlen-und Größenbereiche

### pdf vom 26.03.2009 i.d.F. 30.05.2011

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-mai2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-mai2011.md)

**Pflichtmodule (43):**
- Analysis (Ana)
- Analysis I
- Übungen zur Analysis I
- Analysis II
- Übungen zur Analysis II
- Lineare Algebra (LA)
- Lineare Algebra I
- Übungen zur Linearen Algebra I
- Lineare Algebra II
- Übungen zur Linearen AlgebraII
- Orientierungsseminar (OrSe)<sup>1,2</sup>
- Teil 1
- Teil 2
- Mehrdimensionale Integration (MInt)
- Übungen
- Stochastische Modellbildung (StMo)
- Algebra (Alg)
- Vertiefungsmodul Körpertheorie (VKT)
- Angewandte Mathematik(AMLA)<sup>~~1~~</sup>
- Geometrie (Geom)<sup>~~2~~</sup>
- Funktionentheorie (Futh)
- Gewöhnliche Differentialgleichungen (GDgl)
- ECTS-Punkte gesamt
- Elemente der Linearen Algebra (ELA)
- Elemente der Linearen AlgebraI
- Übungen Linearen AlgebraI
- Elemente der Linearen AlgebraII
- Übungen Linearen AlgebraII
- Elemente der Analysis (EAna)
- Elemente der AnalysisI
- Übungen AnalysisI
- Elemente der AnalysisII
- Übungen AnalysisII
- Analytische Geometrie (AGeo)
- Vorlesung/Übung
- Aufbaumodul Analysis (AmAn)<sup>~~1~~</sup>
- Elemente der Analysis III
- Elementare Stochastik (EStoch)
- Mathematisches Seminar in elemen- tarer Stochastik (SemEStoch)
- Geometrie für das Lehramt (GeoL)
- Mathematisches Seminar in Geomet- rie für das Lehramt (SemGeoL)
- Elementare Zahlentheorie (EZth)
- Mathematisches Seminar in elemen- tarer Zahlentheorie (SemEZth)

### pdf vom 26.03.2009 i.d.F. 07.05.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-neu.md)

**Pflichtmodule (39):**
- Analysis (Ana)
- AnalysisI
- Übungen zur AnalysisI
- AnalysisII
- Übungen zur AnalysisII
- Lineare Algebra (LA)
- LineareAlgebraI
- Übungen zur Lin. AlgebraI
- LineareAlgebraII
- Übungen zur Lin. AlgebraII
- Orientierungsseminar<sup>~~2~~</sup>(OrSe)
- Teil 1
- Teil 2
- Algebra(Alg)
- Übungen
- Stochastische Modellbildung (StMo)
- Mehrdimensionale Integration (MInt)
- Vorlesung/Übung
- Angewandte Mathematik<sup>1</sup>(AMLA)
- Elemente der Zahlentheorie (EZth)
- Gew. Differentialgleichungen (GDgl)
- Geometrie für das Lehramt (GeoLA)
- Funktionentheorie (Futh)
- Geometrie (Geom)
- ECTS-Punkte gesamt
- Elemente der Linearen Algebra (ELA)
- Elemente der Lin. AlgebraI
- Übungen Lin. AlgebraI
- Elemente der Lin. AlgebraII
- Übungen Lin. Algebra II
- Elemente der Analysis (EAna)
- Elemente der AnalysisI
- Übungen AnalysisI
- Elemente der AnalysisII
- Übungen AnalysisII
- Analytische Geometrie (AGeo)
- Aufbaumodul Analysis<sup>~~1~~</sup>(AmAn)
- Elemente der Analysis III
- Mathematisches Seminar (MSnv) (nicht vertieft)<sup>2</sup>

### pdf vom 26.03.2009 i.d.F. 30.10.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-oktober2014.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-oktober2014.md)

**Pflichtmodule (43):**
- Analysis(Ana)
- Analysis I
- Übungen zur Analysis I
- Analysis II
- Übungen zur AnalysisII
- Lineare Algebra(LA)
- Lineare Algebra I
- Übungen zur Linearen Algebra I
- Lineare Algebra II
- Übungen zur Linearen Algebra II
- Orientierungsseminar(OrSe)<sup>1,2</sup>
- Teil 1
- Teil 2
- Mehrdimensionale Integration(MInt)
- Übungen
- Stochastische Modellbildung (StMo)
- Algebra(Alg)
- Vertiefungsmodul Körpertheorie(VKT)
- Angewandte Mathematik(AMLA)<sup>~~1~~</sup>
- Geometrie(Geom)<sup>~~2~~</sup>
- Funktionentheorie(Futh)
- Gewöhnliche Differentialgleichungen(GDgl)
- ECTS-Punktegesamt
- Elemente der Linearen Algebra(ELA)
- Elemente der Linearen AlgebraI
- Übungen Linearen AlgebraI
- Elemente der Linearen AlgebraII
- Übungen Linearen AlgebraII
- Elemente der Analysis(EAna)
- Elemente der AnalysisI
- Übungen AnalysisI
- Elemente der AnalysisII
- Übungen AnalysisII
- Analytische Geometrie(AGeo)
- Vorlesung/Übung
- Aufbaumodul Analysis (AmAn)<sup>~~1~~</sup>
- Elemente der Analysis III
- Elementare Stochastik(EStoch)
- Mathematisches Seminar in elemen- tarer Stochastik(SemEStoch)
- Geometrie für das Lehramt(GeoL)
- Mathematisches Seminar in Geomet- rie für das Lehramt(SemGeoL)
- Elementare Zahlentheorie(EZth)
- Mathematisches Seminar in elemen- tarer Zahlentheorie (SemEZth)

### pdf vom 26.03.2009 i.d.F. 21.10.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-ws2010-2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-ws2010-2011.md)

**Pflichtmodule (52):**
- Analysis (Ana)
- Analysis I
- Übungen zur Analysis I
- Analysis II
- Übungen zur Analysis II
- Lineare Algebra (LA)
- Lineare Algebra I
- Übungen zur Linearen Algebra I
- Lineare Algebra II
- Übungen zur Linearen AlgebraII
- Orientierungsseminar (OrSe)<sup>1,2</sup>
- Teil 1
- Teil 2
- Mehrdimensionale Integration (MInt)
- Übungen
- Stochastische Modellbildung (StMo)
- Algebra (Alg)
- Vertiefungsmodul Körpertheorie (VKT)
- Angewandte Mathematik(AMLA)<sup>~~1~~</sup>
- Vorlesung/Übung oderSeminar
- Gewöhnliche Differentialgleichungen (GDgl)
- Geometrie (Geom)<sup>~~2~~</sup>
- Funktionentheorie (Futh)
- Mathematik(MathVa)
- ECTS-Punkte gesamt
- Elemente der Linearen Algebra (ELA)
- Elemente der Linearen AlgebraI
- Übungen Linearen AlgebraI
- Elemente der Linearen AlgebraII
- Übungen Linearen AlgebraII
- Elemente der Analysis (EAna)
- Elemente der AnalysisI
- Übungen AnalysisI
- Elemente der AnalysisII
- Übungen AnalysisII
- Analytische Geometrie (AGeo)
- Vorlesung/Übung
- Aufbaumodul Analysis (AmAn)<sup>~~1~~</sup>
- Elemente der Analysis III
- Elementare Stochastik (EStoch)
- Mathematisches Seminar in elemen- tarer Stochastik (SemEStoch)
- Geometrie für das Lehramt (GeoL)
- Mathematisches Seminar in Geomet- rie für das Lehramt (SemGeoL)
- Elementare Zahlentheorie (EZth)
- Mathematisches Seminar in elemen- tarer Zahlentheorie (SemEZth)
- Fachdidaktik A Mathematik (FDAR)
- Didaktik der Arithmetik und Bruchrech- nung
- Didaktikder Algebra
- Fachdidaktik B Mathematik (FDBR)
- DidaktikderGeometrie
- DidaktikderStochastik
- Didaktikder Zahlen-und Größenbereiche

### pdf vom 26.03.2009 i.d.F. 31.03.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-musik-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-musik-neu.md)

**Pflichtmodule (9):**
- (4) Grundlagen fachbezogenen Lehrens undLernens
- (5) Fachdidaktisches Lernen, Lehren und Beurteilen
- Grundlagen u. musikalische Praxis
- (2) Musikalische Praxis 1
- (2) Musikalische Praxis 2
- (2) _2. Fachdidaktik/Musikpädagogik_
- (2) Fachbezogenes Lehren und Lernen
- (4) Modellemusikalischer Praxis
- (3) GrundlagendesMusikunterrichts

### pdf vom 30.03.2009 i.d.F. 25.10.2016

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-sozialkunde-okt2016.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-sozialkunde-okt2016.md)

**Pflichtmodule (9):**
- Grundlagen der politi- schen Bildun
- PolitischesLernen
- Methodik und Wertorien-
- tierung im Politikunterricht
- Grundlagen der politischen Bildung
- Wertorientierte Politische Bildung
- Methodik, Praxis und Wertorientierung
- im Politikunterricht
- im PU (FG GS)

### pdf vom 01.04.2009 i.d.F. 08.08.2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-aug2017.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-aug2017.md)

**Pflichtmodule (7):**
- Basismodul Spanische
- Sprachpraxis 1
- Sprachpraxis 2
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Basismodul Didaktik der romanischen Srachen
- Proseminar Fachdidaktik Spanisch

### pdf vom 01.04.2009 i.d.F. 24.09.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-neu-ws2010-2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-neu-ws2010-2011.md)

**Pflichtmodule (2):**
- Abschlussmodul Schriftliche Hausarbeit
- Schriftliche Hausarbeit

### pdf vom 01.04.2009 i.d.F. 24.09.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-neu.md)

**Pflichtmodule (3):**
- Abschlussmodul Schriftliche Hausarbeit
- Kolloquium zur Besprechung der Schriftlichen Hausarbeit
- SchriftlicheHausarbeit

### pdf vom 01.04.2009 i.d.F. 29.09.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-sept2014.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-sept2014.md)

**Pflichtmodule (7):**
- Basismodul Sanische Srachraxis 1
- Cultura y comunicación oral 2
- Español intermedio II 6
- Basismodul Spanische Sprachpraxis 2
- Basisseminar Spanische Sprachwissen- schaft 2
- Basismodul Einführung in die Iberoromanistik
- Phonetik und Phonologie des Spanischen 1

### pdf vom 01.04.2009 i.d.F. 22.03.2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-sport-maerz2013.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-sport-maerz2013.md)

**Pflichtmodule (18):**
- (1V) Grundlagen der Sportpädagogik
- (3) Sportpädagogische /-didaktische Kompetenz II
- Normative und empirische Sportpädagogik /-didaktik
- (1V) Normative und empirische Sportpädagogik /-didaktik (FD)*
- (4) Sportpädagogische /-didaktische Kompetenz III
- Grundlagen der Sportdidaktik (FD)*
- Grundlagen der Sportpädagogik I(FD)*
- Ausgewählte Aspekte des Schulsports (FD)*
- (5) Sportdidaktische/-pädagogische Kompetenz II
- Normative und empirische Sportpädagogik / -didaktik (FD)*
- Klettern o. Wassersport o. MTB o. Inlineskaten o. Triathlon o. Zirkus- o. Kampfkünste o. entsprechendeAngebote
- (2S) Lehrübungen für den Sportunterricht (FD)*
- (5) Kompetenz in Bewegung und Gesundheit II
- „Stärkung Gesundheitsressourcen 1“ Elementare
- Bewegungs- und Spielerziehung musisch-ästhetische + kompensatorischeBewegungsformen
- Interventionskonzepte und QM
- (4) Kompetenz in Bewegung und Gesundheit III
- (4) Projekt „Entwicklung und Umsetzung zur Gf“

### pdf vom 01.04.2009 i.d.F. 27.02.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-wiwi-februar2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-wiwi-februar2015.md)

**Pflichtmodule (7):**
- Grundlagen der Fachdidaktik Wirtschaftswissenschaft en(Gymnasium)
- Prifldr dr
- axsee e Fachdidaktik
- Grundlagen der Fachdidaktik
- Wirtschaftswissenschaft en(Realschule)
- Praxisfelder der
- Fachdidaktik Wirtschaftswissenschaft en

### pdf vom 27.07.2009 i.d.F. 14.09.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lehramt-arbeitslehre-sept2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lehramt-arbeitslehre-sept2015.md)

**Pflichtmodule (7):**
- Grundlagen der Fachdi- daktik (GFD)
- Grundlagen der Fach- wissenschaft (GFW)
- Medien und Methoden I
- (MuM I)
- Seminar mit Medien- schwerpunkt
- Medien und Methoden II (MuM II)<sup>2</sup>
- Arbeit und Beruf (AuB)

### PO ZS Geow im LA 20250320 .pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/po-zs-geow-im-la-20250320.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/po-zs-geow-im-la-20250320.md)

**Pflichtmodule (4):**
- Grundlagen der Geowissenschaften I
- Rohstoffe und Nachhaltigkeit
- Dynamik des Systems Erde
- Kompetenzseminar zum Klimawandel

### StuPO LAPO 20090223 i.d.F. 20180629.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/stupo-lapo-20090223-idf-20180629.md`](../pruefungsordnungen/lehramt/stupo-lapo-20090223-idf-20180629.md)

**Pflichtmodule (6):**
- Vorlesung Seminar
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungs- kompetenzen in der Mittel- schule
- Basismodul Berufsorientierung<sup>1</sup>
- Masterarbeit

### StuPO LAPO 20090223 i.d.F. 20200513.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/stupo-lapo-20090223-idf-20200513.md`](../pruefungsordnungen/lehramt/stupo-lapo-20090223-idf-20200513.md)

**Pflichtmodule (6):**
- Vorlesung Seminar
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungs- kompetenzen in der Mittel- schule
- Basismodul Berufsorientierung<sup>1</sup>
- Masterarbeit

### StuPO LAPO 20090223 i.d.F. 20220808.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/stupo-lapo-20090223-idf-20220808.md`](../pruefungsordnungen/lehramt/stupo-lapo-20090223-idf-20220808.md)

**Pflichtmodule (10):**
- Grundlagen der Grundschul- pädagogik
- Einführungsmodul GSD:
- Grundlagen der Grundschul-
- didaktik (Sachunterricht und Shifhb
- crtspracerwer)
- Vorlesung Seminar
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungskom- petenzen in der Mittelschule
- Basismodul Berufsorientierung<sup>1</sup>

### StuPO LAPO 20220808 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/stupo-lapo-20220808-aes.md`](../pruefungsordnungen/lehramt/stupo-lapo-20220808-aes.md)

**Pflichtmodule (5):**
- Vorlesungoder Seminar
- Grundlagen der Grundschul- pädagogik
- Einführungsmodul GSD:
- Grundlagen der Grundschuldi-
- daktik (Sachunterricht und Schriftspracherwerb)

### StuPO LAPO 20240918 i.d.F. 20250806.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/stupo-lapo-20240918-idf-20250806.md`](../pruefungsordnungen/lehramt/stupo-lapo-20240918-idf-20250806.md)

**Pflichtmodule (6):**
- Vorlesung Seminar
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungskompetenzen in der Mittelschule
- Basismodul Berufsorientierung<sup>1</sup>
- Masterarbeit

### StuPO LAPO 20240918.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/stupo-lapo-20240918.md`](../pruefungsordnungen/lehramt/stupo-lapo-20240918.md)

**Pflichtmodule (10):**
- Grundlagen der Grundschul- pädagogik
- Einführungsmodul GSD:
- Grundlaen der Grundschul-
- g didaktik (Sachunterricht und Schriftspracherwerb)
- Vorlesung Seminar
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungskompetenzen in der Mittelschule
- Basismodul Berufsorientierung<sup>1</sup>
- Masterarbeit

### 29. September 2010

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/2aes-20ba-ma-20molekmed.md`](../pruefungsordnungen/medizinische-fakultaet/2aes-20ba-ma-20molekmed.md)

**Pflichtmodule (2):**
- Vorlesung Seminar Physiologie, Vorlesung Bioinformatik
- Vorlesung, Seminar, Praktikum Vorlesung, Seminar, Praktikum

### 18. Februar 2016

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/5aes-ba-ma-molekulare-medizin.md`](../pruefungsordnungen/medizinische-fakultaet/5aes-ba-ma-molekulare-medizin.md)

**Pflichtmodule (1):**
- unkte)

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20070928 i.d.F. 20210113.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210113.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210113.md)

**Pflichtmodule (15):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch- chemisches Praktikum<sup>2)</sup>
- Biochemie und Grundzüge der Mlkl Mdii
- oeuaren ezn
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie
- und Embryologie
- Spezielle Histologie
- und Organogenese
- Allg. Physiologie
- Physiologie des Menschen und Grundlagen der
- Bioinformatik
- Organische Chemie
- Vegetative Physiologie

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20070928 i.d.F. 20210429.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210429.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210429.md)

**Pflichtmodule (13):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch- chemisches Praktikum<sup>2)</sup>
- Biochemie und Grundzüge der Molekularen Medizin
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie
- und Embryologie
- Spezielle Histologie
- und Organogenese
- Allg. Physiologie
- Physiologie des Menschen und Grundlagen der Bioinformatik
- Organische Chemie
- Bachelorarbeit

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20210113 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20210113-aes.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20210113-aes.md)

**Pflichtmodule (21):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch- chemisches Praktikum<sup>2)</sup>
- Biochemie und Grundzüge der Molekularen Medizin
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Allg. Physiologie
- Physiologie des Menschen und Grundlagen der Bioinformatik
- Organische Chemie
- Bachelorarbeit
- Pflichtbereich (35 EC
- Advanced Lectures in
- Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of
- Biopolymers
- Research Design
- Lecture Animal Care
- Laboratory Animal Science and Biological Safety
- Lecture Biological Safety

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20230822 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822-idf-20240926.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822-idf-20240926.md)

**Pflichtmodule (14):**
- Bachelorarbeit
- WS und ECTS-Punkte:
- Pflichtbereich (35 ECTS
- vance ectures n Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of
- Biopolymers
- Research Design
- Lecture Animal Care
- Laboratory Animal Science and Biological Safety
- Lecture Biological Safety
- Masterarbeit mit
- Masterkolloquium
- Summ

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20230822.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822.md)

**Pflichtmodule (14):**
- Bachelorarbeit
- WS und ECTS-Punkte:
- Pflichtbereich (35 ECTS
- vance ectures n Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of
- Biopolymers
- Research Design
- Lecture Animal Care
- Laboratory Animal Science and Biological Safety
- Lecture Biological Safety
- Masterarbeit mit
- Masterkolloquium
- Summ

### MSc Medical Process Management MPM 20240807.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/msc-medical-process-management-mpm-20240807.md`](../pruefungsordnungen/medizinische-fakultaet/msc-medical-process-management-mpm-20240807.md)

**Pflichtmodule (1):**
- Vier Wochen Praktikum

### PDF vom 28.09.2007 i.d.F. 18.02.2016

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-feb2016.md`](../pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-feb2016.md)

**Pflichtmodule (15):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch-chemisches Praktikum
- Propädeutikvorlesung
- Biochemie und Grundzüge der
- Molekularen Medizin
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Grundlagen der Physiologie des
- Menschen und Grundlagen der Bioinformatik
- Organische Chemie
- Masterarbeit (30 EC
- Master’s Thesis
- Master’s Colloquium

### PDF vom 28.09.2007 i.d.F. 22.07.2014

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-juli2014.md`](../pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-juli2014.md)

**Pflichtmodule (12):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch-chemisches Prakti- kum
- Propädeutikvorlesung 1
- Biochemie und Grundzüge der
- Molekularen Medizin
- Funktionelle Anatomie des Men- schen
- Vorlesung 3
- Allgemeine Histologie und Emb- ryologie
- Spezielle Histologie und Orga- nogenese
- Grundlagen der Physiologie des
- Menschen und Grundlagen der Bioinformatik

### Weiterbildungsstudiengang Zahnerhaltung StuPO ZahnE 20250131.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/weiterbildungsstudiengang-zahnerhaltung-stupo-zahne-20250131.md`](../pruefungsordnungen/medizinische-fakultaet/weiterbildungsstudiengang-zahnerhaltung-stupo-zahne-20250131.md)

**Pflichtmodule (2):**
- Masterarbeit
- nd ECTS-Punkte:

### 15. August 2011

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/2aes-20ba-20bio-20-20ma-20zellmolek-1.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/2aes-20ba-20bio-20-20ma-20zellmolek-1.md)

**Pflichtmodule (2):**
- Kernmodul I (Pflicht)
- Kernmodul II (Pflicht)

### FPO BAMA Bio 20191028.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bama-bio-20191028.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bama-bio-20191028.md)

**Pflichtmodule (13):**
- Grundlagenvorlesung I
- Grundlagenvorlesung II
- Orientierungsmodul 1
- Orientierungsmodul 2
- Orientierungsmodul 3
- Orientierungsmodul 4
- Übung mit Hauptseminar
- Wahlmodul Externes Praktikum<sup>1)</sup>
- Wahlmodul Internes Praktikum<sup>1) 3)</sup>
- Wahlmodul UNIcert ® III<sup>1)</sup>
- Scientific Presentations
- schriftliche Masterarbeit
- Masterarbeit

### PDF vom 22.07.2015 i.d.F. 05.08.2016

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bio-zellmolekbio-neu-aug2016.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bio-zellmolekbio-neu-aug2016.md)

**Pflichtmodule (14):**
- Basismodul Englisch
- Fachmodul A (Teil 1)
- Fachmodul B (Teil 1)
- Fachmodul A (Teil 2)
- Fachmodul B (Teil 2)
- Fachmodul C (nur Teil 2)
- Fachmodul D (nur Teil 2)
- Digitale Werkzeuge für Biologen
- Kernmodul I
- Kernmodul II
- Mastermodul 1
- Mastermodul 2
- Mastermodul 3
- Mastermodul 4

### (PDF vom 22.07.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bio-zellmolekbio-neu.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bio-zellmolekbio-neu.md)

**Pflichtmodule (6):**
- Kernmodul I
- Kernmodul II
- Mastermodul 1
- Mastermodul 2
- Mastermodul 3
- Mastermodul 4

### FPO BSc-MSc ILS FPO BAMA ILS 20230822.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20230822.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20230822.md)

**Pflichtmodule (8):**
- Grundlagen der Experimentalphysik 1
- Grundlagen der Experimentalphysik 2
- ILS-P2: Grundlagen der Experimentalphsik 2
- Praktikum Grundlagen der Experimen- talphysik
- ILS-P4:
- Strukturphysik
- ILS-P5:
- Physik der Biologischen Materie

### PDF vom 05.08.2008 i.d.F. 15.08.2011

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-august2011.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-august2011.md)

**Pflichtmodule (2):**
- Kernmodul I (Pflicht)
- Kernmodul II (Pflicht)

### PDF vom 05.08.2008 i.d.F. 15.02.2013

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-feb2013.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-feb2013.md)

**Pflichtmodule (2):**
- Kernmodul I (Pflicht)
- Kernmodul II (Pflicht)

### PDF vom 05.08.2008 i.d.F. 06.10.2014

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-okt2014.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-okt2014.md)

**Pflichtmodule (2):**
- Kernmodul I (Pflicht)
- Kernmodul II (Pflicht)

### PDF vom 29.02.2016 i.d.F. 02.03.2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-maerz2017.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-maerz2017.md)

**Pflichtmodule (17):**
- Grundlagen der Geowissenschaften I
- Minerale und Gesteine
- Mathematik für Naturwissen- schaftler
- Mathematik
- Biologie
- Allgemeine und Anorganische Chemie
- le Chemie
- modu Geowissenschaftliche Arbeitsmethoden I
- flicht
- P Grundlagen der Geowissenschaften II
- Dynamik des Systems Erde
- Spezielle Minerale
- Mineralogie I
- Experimentalphysik für Nebenfächler
- Physik
- Allgemeine Paläontologie
- Paläobiologie I

### PDF vom 29.02.2016 i.d.F. 30.09.2016

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-sept2016.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-sept2016.md)

**Pflichtmodule (19):**
- Grundlagen der Geowissenschaften I
- Minerale und Gesteine
- Mathematik für Naturwissen- schaftler
- Mathematik
- Biologie
- Allgemeine und Anorganische Chemie
- le Chemie
- modu Geowissenschaftliche Arbeitsmethoden I
- flicht
- P Grundlagen der Geowissenschaften II
- Dynamik des Systems Erde
- Spezielle Minerale
- Mineralogie I
- Experimentalphysik für Nebenfächler
- Physik
- Allgemeine Paläontologie
- Paläobiologie I
- Masterarbeit
- Schriftliche Masterarbeit

### PDF vom 29.02.2016

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften.md)

**Pflichtmodule (18):**
- Grundlagen der Geowissenschaften I
- Minerale und Gesteine
- Mathematik für Naturwissen- schaftler
- Mathematik
- Biologie
- Allgemeine und Anorganische Chemie
- le Chemie
- modu Geowissenschaftliche Arbeitsmethoden I
- flicht
- P Grundlagen der Geowissenschaften II
- Dynamik des Systems Erde
- Spezielle Minerale
- Mineralogie I
- Experimentalphysik für Nebenfächler
- Physik
- Allgemeine Paläontologie
- Paläobiologie I
- Masterarbeit

### FPO Kulturgeo 20221011 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-kulturgeo-20221011-aes.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-kulturgeo-20221011-aes.md)

**Pflichtmodule (15):**
- Kulturgeographie 1
- KG 2: Grundlagen der
- Kulturgeographie 2
- KG 3: Grundlagen der Physischen
- Geographie 1
- KG 4: Grundlagen der Physischen
- Geographie 2
- KG 5: Einführung in die Geographie<sup>3)</sup>
- KG 6: GIS und Gilii<sup>3)</sup>
- eovsuaserung
- KG 7: Qualitative und
- Quantitative
- Methoden<sup>3)</sup>
- Geländepraktikum
- Kleines Geländeseminar/

### FPOGeoT-GeoEn 20170620 i.d.F. 20190930.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpogeot-geoen-20170620-idf-20190930.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpogeot-geoen-20170620-idf-20190930.md)

**Pflichtmodule (1):**
- Sum Gesa

### PO ZS Geow im LA 20250320 .pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/po-zs-geow-im-la-20250320.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/po-zs-geow-im-la-20250320.md)

**Pflichtmodule (4):**
- Grundlagen der Geowissenschaften I
- Rohstoffe und Nachhaltigkeit
- Dynamik des Systems Erde
- Kompetenzseminar zum Klimawandel

### PDF vom 11.03.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-mathematik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-mathematik.md)

**Pflichtmodule (3):**
- Masterarbeit
- Master Masterkolloquium
- asterkolloquium

### PDF vom 11.03.2015 i.d.F. 27.02.2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik-feb2017.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik-feb2017.md)

**Pflichtmodule (45):**
- Lineare und Kombinatorische
- Optimierung
- Vorlesung Stochastische Modellbil- dung
- Stochastische Modellbildung
- Tafelübung Stochastische Modellbil- dung
- Vorlesung Numerische Mathematik
- Numerische Mathematik
- Rechnerübung Numerische Mathematik
- Diskretisierung und numerische
- Numerik partieller Differential-
- gleichungen
- Mathematische Modellierung
- Theorie
- Nihtli Otii
- cneare pmerung
- chungen
- Funktionalanalsis
- Übung Funktionalanalysis
- Partielle Differenzialgleichungen
- Übung Partielle Differenzialgleichun- gen I
- e Mathematik, Modelle und Optimie-
- Grundlagen der Elektrotechnik I
- Übung GET I
- Vorlesung GET II
- Grunagen er Eetrotecni II
- EEI Grundlaen der Elektrotechnik III
- TWF) g
- hlfach ( Signale und Systeme I
- Übung Signale und Systeme I
- chnisch Sinale nd Ssteme II
- Übung Signale und Systeme II
- Vorlesung Nachrichten- technische Systeme
- Nachrichtentechnische Systeme
- Vorlesung Digitale Signalver- arbeitung
- Digitale Signalverarbeitung
- Vorlesung Grundlagen der Elektrotechnik II
- Grundlagen der Elektrotechnik II
- Gdl d Mthik
- runagen er essecn
- Informationssysteme im Ge- sundheitswesen 1
- Elektromagnetische Felder I
- Übung Elektromagnetische Felder I
- minar, eit (BA) Bachelorseminar
- chelorse helorarb Bachelorarbeit
- Ba Bac Summe Bachelorseminar, Ba

### PDF vom 11.03.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik.md)

**Pflichtmodule (45):**
- Lineare und Kombinatorische
- Optimierung
- Vorlesung Stochastische Modellbil- dung
- Stochastische Modellbildung
- Tafelübung Stochastische Modellbil- dung
- Vorlesung Numerische Mathematik
- Numerische Mathematik
- Rechnerübung Numerische Mathematik
- Diskretisierung und numerische
- Numerik partieller Differential-
- gleichungen
- Mathematische Modellierung
- Theorie
- Nihtli Otii
- cneare pmerung
- Gewöhnliche Differentialglei-
- chungen
- Funktionalanalsis
- Übung Funktionalanalysis
- Partielle Differenzialgleichungen
- Übung Partielle Differenzialgleichun- gen I
- e Mathematik, Modelle und Optimie-
- Grundlagen der Elektrotechnik I
- Übung GET I
- Gdl d Elktthik II
- runagen er eroecn
- EEI Grundlaen der Elektrotechnik III
- TWF) g
- hlfach ( Signale und Systeme I
- Übung Signale und Systeme I
- chnisch Signale und Systeme II
- Übung Signale und Systeme II
- Vorlesung Nachrichten- technische Systeme
- Nachrichtentechnische Systeme
- Vorlesung Digitale Signalver- arbeitung
- Digitale Signalverarbeitung
- Vorlesung Grundlagen der Elektrotechnik II
- Grundlagen der Elektrotechnik II
- Gdl d Mthik
- runagen er essecn
- Informationssysteme im Ge- sundheitswesen 1
- Elektromagnetische Felder I
- Übung Elektromagnetische Felder I
- chelorse helorarb Bachelorarbeit
- Ba Bac Summe Bachelorseminar, Ba

### PDF vom 11.03.2015 i.d.F. 13.03.2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik-maerz2017.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik-maerz2017.md)

**Pflichtmodule (10):**
- Lineare und Kombinatorische
- Optimierung<sup>1</sup>
- imierung (PSO) Projektseminar Optimierung<sup>2</sup>
- nd Opt
- astik u Stochastische Modellbildung<sup>1</sup>
- e Stoch
- tmodul
- Pflich Introduction to Statistics and Statistical Programming<sup>2</sup>
- Rechnerübung Introduction to Statistics and Statistical Program- ming
- k und Optimierung (PSO)

### PDF vom 11.03.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik.md)

**Pflichtmodule (10):**
- Lineare und Kombinatorische
- Optimierung<sup>1</sup>
- imierung (PSO) Projektseminar Optimierung<sup>2</sup>
- nd Opt
- astik u Stochastische Modellbildung<sup>1</sup>
- e Stoch
- tmodul
- Pflich Introduction to Statistics and Statistical Programming<sup>2</sup>
- Rechnerübung Introduction to Statistics and Statistical Program- ming
- k und Optimierung (PSO)

### FPODataScience 20200820 i.d.F. 20210311.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210311.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210311.md)

**Pflichtmodule (3):**
- (9) Masterkol- loquium
- rarbeit
- (mind.) und nkte

### FPODataScience 20200820 i.d.F. 20210805.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210805.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210805.md)

**Pflichtmodule (4):**
- Masterar- beit
- Masterkol- loquium
- beit
- mind.) und kte

### FPODataScience 20200820.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820.md)

**Pflichtmodule (3):**
- (9) Masterkol- loquium
- rarbeit
- (mind.) und nkte

### Modulstudien Naturale POM-SN 20170626 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/modul-und-zusatzstudien/modulstudien-naturale-pom-sn-20170626-idf-20180730.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/modul-und-zusatzstudien/modulstudien-naturale-pom-sn-20170626-idf-20180730.md)

**Pflichtmodule (5):**
- Grundlagen der Zellbiologie und Genetik
- Molekularbiologie
- werb Einführung in die Chemie
- Zertifikatser Experimentalphysik
- bereich für Physik 1

### PDF vom 26.06.2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/modul-und-zusatzstudien/po-modulstudien-naturale.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/modul-und-zusatzstudien/po-modulstudien-naturale.md)

**Pflichtmodule (14):**
- Grundlagen der Zellbiologie und Genetik (ILS-B1)
- Molekularbiologie
- (ILS-B2)
- werb Einführung in die Chemie
- tser (ILS-C1)
- rtifika Experimentalphysik
- für Ze (ExpPhys CBI, LSE, CEN)
- eich Physik
- chtber (PhNF)
- lpfli
- Wah Mathematik
- Übungsprogramm Mathematik für Naturwissenschaftler
- Das System Erde für
- Naturwissenschaftler

### PDF vom 25.09.1980 i.d.F. 28.12.2004

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/modul-und-zusatzstudien/zwischenpruefungso.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/modul-und-zusatzstudien/zwischenpruefungso.md)

**Pflichtmodule (13):**
- Basismodul 1: Sprachwissen- schaft
- Basismodul 2: Literaturwissen- schaft
- Basismodul 3: Sprachpraktische Grundlagen
- Basismodul 4:
- Sprachproduktion
- Basismodul 5: Landeskunde
- Basismodul 1 _Linguistik_
- Basismodul 2 _Literatur- und_
- _Kulturwissenschaft_
- Literaturwiss.
- oder
- Kulturwissenschaft
- Dauer der schriftlichen Prüfung

### 29. September 2010

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/physik/1aes-ba-ma-physik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/physik/1aes-ba-ma-physik.md)

**Pflichtmodule (1):**
- seme

### 17. Oktober 2014

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/physik/3aes-ba-ma-physik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/physik/3aes-ba-ma-physik.md)

**Pflichtmodule (1):**
- seme

### PDF vom 07.09.2007 i.d.F. 29.09.2010

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/physik/po-bachelor-ma-physik-ws-2010-2011.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/physik/po-bachelor-ma-physik-ws-2010-2011.md)

**Pflichtmodule (1):**
- chse

### PDF vom 07.09.2007 i.d.F. 02.10.2013

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/physik/po-bachelor-ma-physik-ws-okt2013.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/physik/po-bachelor-ma-physik-ws-okt2013.md)

**Pflichtmodule (1):**
- chsem

### PDF vom 07.09.2007

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/physik/po-bachelor-ma-physik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/physik/po-bachelor-ma-physik.md)

**Pflichtmodule (1):**
- ster

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1aesa-ba-1fach-ba-literatur-buch.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1aesa-ba-1fach-ba-literatur-buch.md)

**Pflichtmodule (13):**
- Basismodul Französische Sprachpraxis 1
- Grundlagen der Neueren deutschen Literatur- wissenschaft(NdL BM 1)
- Grundlagen der Buchwissenschaft
- Einführung in das wissenschaftliche Arbeiten
- Basismodul Französische Sprachpraxis 2
- Basismodul Französische Literaturwissenschaft
- Grundlagen der Neueren deutschen Literatur- wissenschaft 2(NdL BM 2)
- Lesen und Lese(r)geschichte im Überblick
- Lehrveranstaltungen an der Partneruniversität<sup>~~2~~</sup>
- Grundlagen des Electronic Publishing und Electronic Commerce
- Typografische Grundlagen
- Literatur und Buch D – F
- Bachelorarbeit

### PDF vom 03.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1fachba-literatur-und-buch.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1fachba-literatur-und-buch.md)

**Pflichtmodule (27):**
- Basismodul Französische Sprach-
- praxis 1
- Grundlagen der Neueren deut- schen Literatur(NdL 1)
- Grundlagen der Buchwissenschaft
- Übungbegleitend zur Vorlesung
- Einführung in das wissenschaftli-
- che Arbeiten Buchwissenschaft
- Vocabulaire,idiomatique et civilisation II
- Grammaire cours élémentaire II
- Basismodul Französische Sprach- praxis 2
- Einführung französische Literatur- wissenschaft
- Systematische Aspekte der Litera- tihft LitS
- urwssensca ()
- Überblicksvorlesung
- Lesen und Lese(r)geschichte im Überblick
- Proseminar Schwerpunktthema B (Gegenwart),
- alternativ zuSchwerpunktthemaA
- Lehrveranstaltungen an der Part- neruniversität<sup>*</sup>
- Lehrveranstaltungen an der Part-
- neruniversität*
- Grundlagen E-Publishing/E- Commerce
- Hauptseminar Schwerpunktthema B (E-Commerce), alternativ zu Schwerpunktthema A
- Typographie Grundlagen
- Angewandte Typographie
- Literatur und Buch D – F
- Buchwirtschaftliches Praktikum
- Bachelorarbeit

### PDF vom 18.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1fachba-soziologie.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1fachba-soziologie.md)

**Pflichtmodule (11):**
- Grundlagen der soziologischen Analyse
- (SozG)
- PS „Wissenschaftstheorie“
- Qualifikationsrofil I
- p (SozQ-I)
- Statistische Analseverfahren I
- y (SozS-I)
- Statistische
- Analyseverfahren II (SozS-II)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Vertiefung Soziologische Metho- denlehre (SozM-V)

### 22. Juli 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/2aes-1fachba-islamischreligioesestudien.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/2aes-1fachba-islamischreligioesestudien.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### berufsbegl BA Sportwissenschaft BPOSport 20160509 i.d.F. 20190115.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/berufsbegl-ba-sportwissenschaft-bposport-20160509-idf-20190115.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/berufsbegl-ba-sportwissenschaft-bposport-20160509-idf-20190115.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### berufsbegl BA Sportwissenschaft BPOSport 20160509 i.d.F. 20190503.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/berufsbegl-ba-sportwissenschaft-bposport-20160509-idf-20190503.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/berufsbegl-ba-sportwissenschaft-bposport-20160509-idf-20190503.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### berufsbegl BA Sportwissenschaft BPOSport 20190115 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/berufsbegl-ba-sportwissenschaft-bposport-20190115-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/berufsbegl-ba-sportwissenschaft-bposport-20190115-aes.md)

**Pflichtmodule (3):**
- Bachelorarbeit
- Kompetenzreflexion Shlüllifikti
- (cssequaaon)

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20241219.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer:
- VorlesungMultivariateVerfahren
- M1 Multivariate Statistik
- Vorlesung Evaluationsforschung
- M2 Forschungsmethoden
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20071009 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20180730.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20180730.md)

**Pflichtmodule (3):**
- Bachelorarbeit und –prüfung
- Oberseminar
- Bachelorarbeit

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20071009 i.d.F. 20190220.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20190220.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20190220.md)

**Pflichtmodule (3):**
- Bachelorarbeit und -prüfung
- Oberseminar
- Bachelorarbeit

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20180730 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20180730-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20180730-aes.md)

**Pflichtmodule (3):**
- Bachelorarbeit und -prüfung
- Bhlbit
- aceorare

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20190220 ÄS zu 5ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20190220-aes-zu-5aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20190220-aes-zu-5aes.md)

**Pflichtmodule (19):**
- Basismodule: Kulturentwicklun Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie:
- Ältere Urgeschichte I B
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Jüngere Urgeschichte I B
- Klassische Archäologie
- Klassische Archäologie: Griechische Archäologie I A
- Klassische Archäologie:
- Griechische Archäologie I B
- Klassische Archäologie: Römische Archäologie I A
- Römische Archäologie I B
- Christliche Archäologie
- Christliche Archäologie: Kulturgeschichte I A
- Christliche Archäologie:
- Übung zur Kulturgeschichte des Christentums vom 3. bis ins 8. Jh.
- Bachelorarbeit und -prüfung
- Oberseminar
- Bachelorarbeit

### Ein-Fach-BA  Islamisch Religiöse Studien BA IRS Ein-Fach 20121109 i.d.F. 20180709.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20121109-idf-20180709.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20121109-idf-20180709.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- Begleitkurs

### Ein-Fach-BA  Islamisch Religiöse Studien BA IRS Ein-Fach 20121109 i.d.F. 20200909.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20121109-idf-20200909.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20121109-idf-20200909.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- WS und ECTS-Punkte:

### Ein-Fach-BA  Islamisch Religiöse Studien BA IRS Ein-Fach 20180709 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20180709-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20180709-aes.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- Begleitkurs

### Ein-Fach-BA Islamisch-Religiöse Studien BA IRS Ein-Fach 20210318 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20210318-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20210318-aes.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- WS und ECTS-Punkte:

### Ein-Fach-BA  Islamisch Religiöse Studien FPO BA IRS Ein-Fach 20121109 i.d.F. 20210318.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-fpo-ba-irs-ein-fach-20121109-idf-20210318.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-fpo-ba-irs-ein-fach-20121109-idf-20210318.md)

**Pflichtmodule (5):**
- Bachelorarbeit
- Begleitkurs
- WS und ECTS-Punkte:
- Bhlbi
- aceoraret

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20140718 i.d.F. 20190806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20190806.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20190806.md)

**Pflichtmodule (15):**
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I
- (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische
- Methodenlehre (SozM-E)
- Vertiefung Soziologische Metho- denlehre(SozM-V)
- Einführung Soziologische Theo- rien(SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Qualifikationsprofil II
- (SozQ-II), vgl. § 5
- Bachelorarbeit
- mfang) und ECTS 12 32

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20140718 i.d.F. 20200818.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20200818.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20200818.md)

**Pflichtmodule (14):**
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I
- (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I
- (SozS-I)
- Statistische Analyseverfahren II
- (SozS-II)
- Einführung in die soziologische
- Methodenlehre (SozM-E)
- Vertiefung Soziologische Methodenlehre (SozM-V)
- Einführung Soziologische Theorien(SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Bachelorarbeit

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20190806 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20190806-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20190806-aes.md)

**Pflichtmodule (11):**
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I
- (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische
- Methodenlehre (SozM-E)
- Vertiefung Soziologische Methoden- lehre(SozM-V)
- Bachelorarbeit
- mfang) und ECTS

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20200818 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20200818-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20200818-aes.md)

**Pflichtmodule (19):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I
- (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I
- (SozS-I)
- Statistische Analyseverfahren II
- (SozS-II)
- Einführung in die soziologische
- Methodenlehre (SozM-E)
- Vertiefung Soziologische Methodenlehre (SozM-V)
- Einführung Soziologische Theorien(SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Bachelorarbeit
- (SozQ-I) vgl. § 5
- Einführung Soziologische Theorien (SozT-E)
- mfang) und ECTS 12 32

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20230822.md)

**Pflichtmodule (16):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Grundlagen der soziologischen Analyse I(SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I
- (SozS-I)
- Statistische Analyseverfahren II
- (SozS-II)
- Einführung in die soziologische Methodenlehre(SozM-E)
- Vertiefung Soziologische Methodenlehre (SozM-V)
- Einführung Soziologische Theorien(SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Bachelorarbeit
- und ECTS
- mfang) und ECTS

### PDF vom 03.08.2015 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fachba-literatur-und-buch-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fachba-literatur-und-buch-aug2017.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 09.10.2007 i.d.F. 06.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fachstuopro-archaeolwiss-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fachstuopro-archaeolwiss-aug2015.md)

**Pflichtmodule (2):**
- Bachelorarbeit und -prüfung
- Bachelorarbeit

### PDF vom 09.10.2007 i.d.F. 08.03.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fachstuopro-archaeolwiss-maerz2011.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fachstuopro-archaeolwiss-maerz2011.md)

**Pflichtmodule (7):**
- Studienleistung (Klausur)
- Referat mit Hausarbeit
- Studienleistungen (Kurz- referate, kleine Hausar- beiten)
- Studienleistung (Regel- mäßige Teilnahme)
- Arbeits- und Ergebnispro- tokoll
- Anforderungen der jewei- ligen Fächer
- Schriftliche Abschlussar- beit

### FPOLitBuch 20190906 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fpolitbuch-20190906-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fpolitbuch-20190906-aes.md)

**Pflichtmodule (10):**
- Basismodul Französische Sprachpraxis 1
- Grundlagen der Neueren deutschen Literaturwissenschaft (NdL BM 1)
- Einführung
- Methoden
- Basismodul Französische Sprachpraxis 2
- Basismodul Französische Literaturwissen- schaft
- Grundlagen der Neueren deutschen Literatur- wissenschaft2(NdL BM 2)
- RezeptionundNutzung
- Lehrveranstaltungen an der Partneruniversität<sup>2</sup>
- Bachelorarbeit

### PDF vom 28.09.2007 i.d.F. 11.08.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psycho.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psycho.md)

**Pflichtmodule (9):**
- VL EinführungindieDiagnostik
- psychologischen
- Diagnostik
- Sem Leistungstests
- Diagnostische
- eraren
- VL KlinischePsychologie1
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 04.06.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psychojuni2010.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psychojuni2010.md)

**Pflichtmodule (9):**
- VL EinführungindieDiagnostik
- psychologischen
- Diagnostik
- Sem. Leistungstests
- Diagnostische
- eraren
- VL KlinischePsychologie1
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 31.07.2012

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-ba-ma-psycho-juli2012.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-ba-ma-psycho-juli2012.md)

**Pflichtmodule (11):**
- VL EinführungindieDiagnostik
- psychologischen
- Diagnostik
- Sem. Leistungstests
- Diagnostische Verfahren
- VL KlinischePsychologie1
- Klinische Psychologie
- S Htf d Phth
- Hauptformen der
- Psychotherapie
- Sem. Vertiefung II

### PDF vom 09.11.2012 i.d.F. 22.07.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/stuopro-ba-1fach-islam-relig-studien-juli2015.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/stuopro-ba-1fach-islam-relig-studien-juli2015.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- Begleitkurs

### 29. August 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/1aes-european-ma-lexicography.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/1aes-european-ma-lexicography.md)

**Pflichtmodule (15):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-1<sup>3</sup>
- Basismodul B3-2<sup>3</sup>
- Basismodul B3-3<sup>3</sup>
- Basismodul B3-4<sup>3</sup>
- Basismodul B3-5<sup>3</sup>
- Basismodul B3-6<sup>3</sup>
- Basismodul B3-7<sup>3</sup>
- Basismodul B3-8<sup>3</sup>
- Basismodul B3-9<sup>3</sup>
- aumodule
- Masterarbeit
- Begleitseminar

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20241219.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer:
- VorlesungMultivariateVerfahren
- M1 Multivariate Statistik
- Vorlesung Evaluationsforschung
- M2 Forschungsmethoden
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20190308.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190308.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190308.md)

**Pflichtmodule (14):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-1<sup>3</sup>
- Basismodul B3-2<sup>3</sup>
- Basismodul B3-3<sup>3</sup>
- Basismodul B3-4<sup>3</sup>
- Basismodul B3-5<sup>3</sup>
- Basismodul B3-6<sup>3</sup>
- Basismodul B3-7<sup>3</sup>
- Basismodul B3-8<sup>3</sup>
- Basismodul B3-9<sup>3</sup>
- Masterarbeit
- Begleitseminar

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20190723.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190723.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190723.md)

**Pflichtmodule (15):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-1<sup>3</sup>
- Basismodul B3-2<sup>3</sup>
- Basismodul B3-3<sup>3</sup>
- Basismodul B3-4<sup>3</sup>
- Basismodul B3-5<sup>3</sup>
- Basismodul B3-6<sup>3</sup>
- Basismodul B3-7<sup>3</sup>
- Basismodul B3-8<sup>3</sup>
- Basismodul B3-9<sup>3</sup>
- baumodule
- Masterarbeit
- Begleitseminar

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20230223.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230223.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230223.md)

**Pflichtmodule (14):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-1<sup>3</sup>
- Basismodul B3-2<sup>3</sup>
- Basismodul B3-3<sup>3</sup>
- Basismodul B3-4<sup>3</sup>
- Basismodul B3-5<sup>3</sup>
- Basismodul B3-6<sup>3</sup>
- Basismodul B3-7<sup>3</sup>
- Basismodul B3-8<sup>3</sup>
- Masterarbeit
- Begleitseminar
- S-Punkte

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230731.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230731.md)

**Pflichtmodule (16):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-1<sup>3</sup>
- Basismodul B3-2<sup>3</sup>
- Basismodul B3-3<sup>3</sup>
- Basismodul B3-4<sup>3</sup>
- Basismodul B3-5<sup>3</sup>
- Basismodul B3-6<sup>3</sup>
- Basismodul B3-7<sup>3</sup>
- Basismodul B3-8<sup>3</sup>
- Im ersten Fachsemeste fortgesetzt wird.
- aumodule
- Masterarbeit
- Begleitseminar
- S-Punkte

### European MA Lexicography  MPOEMLex 20190723 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20190723-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20190723-aes.md)

**Pflichtmodule (15):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-1<sup>3</sup>
- Basismodul B3-2<sup>3</sup>
- Basismodul B3-3<sup>3</sup>
- Basismodul B3-4<sup>3</sup>
- Basismodul B3-5<sup>3</sup>
- Basismodul B3-6<sup>3</sup>
- Basismodul B3-7<sup>3</sup>
- Basismodul B3-8<sup>3</sup>
- Basismodul B3-9<sup>3</sup>
- baumodule
- Masterarbeit
- Begleitseminar

### European MA Lexicography  MPOEMLex 20230223 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20230223-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20230223-aes.md)

**Pflichtmodule (6):**
- E-Learning
- vgl. APO/SprZ<sup>4</sup>
- Consortium Agreement
- Masterarbeit
- Begleitseminar
- -Punkte

### PDF vom 28.09.2007 i.d.F. 11.08.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-20ba-ma-psycho.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-20ba-ma-psycho.md)

**Pflichtmodule (9):**
- VL EinführungindieDiagnostik
- psychologischen
- Diagnostik
- Sem Leistungstests
- Diagnostische
- eraren
- VL KlinischePsychologie1
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 04.06.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-20ba-ma-psychojuni2010.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-20ba-ma-psychojuni2010.md)

**Pflichtmodule (9):**
- VL EinführungindieDiagnostik
- psychologischen
- Diagnostik
- Sem. Leistungstests
- Diagnostische
- eraren
- VL KlinischePsychologie1
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 31.07.2012

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-ba-ma-psycho-juli2012.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-ba-ma-psycho-juli2012.md)

**Pflichtmodule (11):**
- VL EinführungindieDiagnostik
- psychologischen
- Diagnostik
- Sem. Leistungstests
- Diagnostische Verfahren
- VL KlinischePsychologie1
- Klinische Psychologie
- S Htf d Phth
- Hauptformen der
- Psychotherapie
- Sem. Vertiefung II

### PDF vom 04.09.2009

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/stuopro-20ma-lexicography.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/stuopro-20ma-lexicography.md)

**Pflichtmodule (5):**
- Basismodul B1
- Basismodul B2 (Heimmodul)
- Basismodul B3
- (Softskill, Import aus dem Sprachenzentrum oder der Informatik)
- Masterarbeit

### PDF vom 04.09.2009 i.d.F. 29.08.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/stuopro-ma-lexicography-aug2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/stuopro-ma-lexicography-aug2016.md)

**Pflichtmodule (14):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-1<sup>3</sup>
- Basismodul B3-2<sup>3</sup>
- Basismodul B3-3<sup>3</sup>
- Basismodul B3-4<sup>3</sup>
- Basismodul B3-5<sup>3</sup>
- Basismodul B3-6<sup>3</sup>
- Basismodul B3-7<sup>3</sup>
- Basismodul B3-8<sup>3</sup>
- Basismodul B3-9<sup>3</sup>
- Masterarbeit
- Begleitseminar

### 9. März 2011

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-20ma-komparatroman.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-20ma-komparatroman.md)

**Pflichtmodule (3):**
- (8) Basismodul Sprachpraxis
- (4) Elementarkurs 1
- (4) Elementarkurs 2

### 28. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-ma-nahoststudien.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-ma-nahoststudien.md)

**Pflichtmodule (11):**
- Einführung in die raumtheoretischen Diskussionen
- Raum und Region
- Transregionale Themen und Methoden I
- Transregionale Themen und Methoden II
- Forschunskollouium
- gq Schwerpunkt Sprache und Lit
- Arabische Sprachwissen- schaft
- Zweite semitische Sprache
- Klassische arabische
- Literatur
- Moderne arabische Litera-

### 13. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-ma-philosophie.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-ma-philosophie.md)

**Pflichtmodule (2):**
- Masterarbeit Praktische Philo- sophie
- Masterarbeit Theoretische Philosophie

### 6. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-fpo-ma-archaeologwiss.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-fpo-ma-archaeologwiss.md)

**Pflichtmodule (2):**
- Masterarbeit (ca. 60 Seiten, 80%) und Master-Kolloquium (mündliche Prüfung, ca. 60 Min.,20%)
- . lhandbuch.

### 23. Februar 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-ma-geschichte.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-ma-geschichte.md)

**Pflichtmodule (2):**
- Prüfungsmodul
- Masterarbeit(gem.§ 3A

### 2. März 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-ma-mittelalterfrueheneuzeit.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-ma-mittelalterfrueheneuzeit.md)

**Pflichtmodule (10):**
- Grundlagen der Germanistischen Mediävistik (Med 1)<sup>2</sup>
- Interdisziplinäres Kolloquium
- Masterfach
- Fachmodul I<sup>~~3~~</sup> Masterfach
- Fachmodul II<sup>~~3~~</sup> Masterfach
- Fachmodul III<sup>~~3~~</sup> Masterfach
- Oberseminar <sup>4</sup>
- Profilfach
- Fachmodul I<sup>~~3~~</sup> Profilfach
- Fachmodul II<sup>~~3~~</sup> Profilfach

### 28. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-developeconominternstudies.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-developeconominternstudies.md)

**Pflichtmodule (2):**
- den.
- fangvon 10 ECTS-

### 13. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-komparatromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-komparatromanistik.md)

**Pflichtmodule (20):**
- Basismodul Französische
- Sprachpraxis 1
- Communication orale
- Vocabulaire, idiomatique et civilisation II
- Bidl
- assmou Französische
- Sprachpraxis 2
- q pq, p intonation
- Expression écrite I
- Basismodul Italienische
- Tecniche di lettura
- Grammatica e stilistica
- Basismodul Spanische
- Basismodul Sanische
- Fonética práctica 2
- Comprensión oral 2
- (4) Basismodul Srachraxis Elementarkurs 1
- (2) Otidl Sprachkurs 1
- (2) ponsmou Shi Sprachkurs 2
- (2) pracpraxs Sprachkurs 3

### 26. Januar 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-theaterpaedagogik.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-theaterpaedagogik.md)

**Pflichtmodule (28):**
- Grundlagen und Rahmen
- der Theaterpädagogik
- Theaterwissenschaft I:
- Dimensionen des Theatralen und Performativen
- Kulturpädagogik II:
- Handlungsfelder und Hand- lungsformen
- Anndt thträd
- gewae eaepa- gogische Forschung
- Theaterwissenschaft II:
- Kulturen, Funktionen und Wahrnehmungsformen der theatralen Praktiken
- Theaterpädagogische Pra- xisreflexion
- Theaterpädagogische For- schungspraxis
- Masterarbeit
- Begleitseminar
- Grundlagen und Rahmen der
- Theaterpädagogik
- Theaterwissenschaft I: Dii d Thtl d
- mensonen es earaen un
- Performativen
- Kulturpädagogik II: Handlunsfelder und Handluns-
- Angewandte theaterpädagogische
- Forschung
- Theaterwissenschaft II: Kulturen Funktionen und Wahr-
- , nehmungsformen der theatralen Praktiken
- Theaterpädagogische Praxisrefle-
- xion
- Theaterpädagogische For-
- schungspraxis

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aesa-ma-fposino.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aesa-ma-fposino.md)

**Pflichtmodule (8):**
- Basismodul Praktische Philosophie
- Basismodul Theoretische Philosophie
- Praktische Philosophie I<sup>2</sup>
- Praktische Philosophie II<sup>2</sup>
- Praktische Philosophie III<sup>2</sup>
- Theoretische Philosophie I<sup>2</sup>
- Theoretische Philosophie II<sup>2</sup>
- Theoretische Philosophie III<sup>2</sup>

### 17. Januar 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aesa-ma-soziologie.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aesa-ma-soziologie.md)

**Pflichtmodule (1):**
- Masterarbeit

### 3. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aes-ma-mittelneulatein.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aes-ma-mittelneulatein.md)

**Pflichtmodule (1):**
- Masterarbeit

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aesa-ma-fpoansk.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aesa-ma-fpoansk.md)

**Pflichtmodule (1):**
- Masterarbeit

### 8. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/5aesa-fpo-ma-kunstgeschichte.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/5aesa-fpo-ma-kunstgeschichte.md)

**Pflichtmodule (1):**
- Ohne Wahlpflicht- module, je nach Schwerpunkt 30-34 SWS

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/6aesa-ma-fpo-englstudies.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/6aesa-ma-fpo-englstudies.md)

**Pflichtmodule (18):**
- Basismodul Aktuelle Interkulturalitäts- und Intermedialitätstheorien
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität
- Tätigkeit als studentische Hilfskraft oder Tutor/Tutorin im Umfang von
- ca. 3 SWS
- ess oue: uure an Literature
- Masterarbeit
- MA Thesis Module: Linguistics and Applied Linguistics
- Basismodul Aktuelle Inter- kulturalitäts- und Inter- medialitätstheorien
- A WP 2/7 Angewandte und deskriptive Linguistik der romanischen Sprachen
- Tätigkeit als studentische Hilfskraft oder Tutor/Tutorin
- im Umfang von ca. 3 SWS
- Masterarbeit:Es ist eines der bei Masterarbeit im Schwerpunkt C
- MA Thi Mdl Clt
- ess oue: uure
- and Literature Masterarbeit im Schwerpunkt Li
- MA Thesis Module:
- Linguistics and Applied
- Linguistics

### PDF vom 08.06.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuo-pro-20ma-20archaeolwissensch.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuo-pro-20ma-20archaeolwissensch.md)

**Pflichtmodule (1):**
- jeweils als Studienschwerpunkt entweder UFG/KA/CA

### PDF vom 08.06.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuo-pro-20ma-20kunstgesch.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuo-pro-20ma-20kunstgesch.md)

**Pflichtmodule (6):**
- (4) Teilnahme an mind. 5 Exkursionstagen, mdl. Vortrag (ca. 30 Minuten),Exposé
- (4) Modulimport: Nach Maßgabe des An- bieters
- (2) Mdl. Vortrag (ca. 30 Minuten), Rezensi- on, Vortrags- oder Kongreßbericht
- Schriftliche Hausar- beit (ca. 80 Seiten)
- (2) Mdl. Vortrag (ca. 30 Minu- ten), Rezen- sion, Vor- trags- oder Kongreßbe- richt
- Schriftliche Hausarbeit (ca. 80 Sei- ten)

### PDF vom 08.06.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuo-pro-20ma-20mittelaltrenaissance.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuo-pro-20ma-20mittelaltrenaissance.md)

**Pflichtmodule (2):**
- Masterarbeit
- Mündl. Prüfung

### PDF vom 08.06.2010 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-antikesprachenkulturen-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-antikesprachenkulturen-aug2017.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 27.02.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-antikesprachenkulturen-feb2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-antikesprachenkulturen-feb2017.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 05.11.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-antikesprachenkulturen.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-antikesprachenkulturen.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 06.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-archaeologischewiss-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-archaeologischewiss-aug2015.md)

**Pflichtmodule (4):**
- Masterarbeit
- mmen SWS / ECTS
- Masterarbeit Summ
- ummenSWS /ECTS

### PDF vom 08.06.2010 i.d.F. 26.01.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-archaeologischewiss-feb2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-archaeologischewiss-feb2016.md)

**Pflichtmodule (3):**
- Masterarbeit
- SummenSWS /ECTS
- ummenSWS /ECTS

### PDF vom 08.06.2010 i.d.F. 05.11.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-archaeologischewiss.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-archaeologischewiss.md)

**Pflichtmodule (1):**
- jeweils als Studienschwerpunkt entweder UFG/KA/CA

### PDF vom 08.06.2010 i.d.F. 28.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-developmenteconomicsinternstudies-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-developmenteconomicsinternstudies-juli2014.md)

**Pflichtmodule (14):**
- Pflichtbereich – es müssen alle Modu
- Development Economics I
- Development Economics II
- International Economics I
- International Economics II
- Research Methods I
- Research Methods II
- International Business Ethics I
- International Business Ethics II
- Regionale Vertiefung– es müssen M
- Regional Module I
- Regional Module II
- Regional Module III
- Regional Module IV

### PDF 2nd of August 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2016-en.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2016-en.md)

**Pflichtmodule (2):**
- chosen.
- ecialisation Ling

### PDF vom 08.06.2010 i.d.F. 02.08.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2016.md)

**Pflichtmodule (14):**
- Basismodul Aktuelle Inter- kulturalitäts- und Interme- dialitätstheorien
- Interdisziplinäres Basis- modul zur konkreten Analyse von Medialität und Kulturalität
- Praktikum (intern oder extern)
- Tätigkeit als studentische Hilfskraft oder Tutor/Tutorin
- im Umfang von ca. 3 SWS
- MA Thesis Module
- Summ
- Masterarbeit
- MA Thesis
- Masterarbeit (60-80 Seiten) Summe 18 37
- Basismodul Aktuelle Inter- kulturalitäts- und Inter- medialitätstheorien
- im Umfan von ca 3 SWS
- g . Masterarbeit:Es ist eines der bei Masterarbeit im Schwerpunkt C
- Masterarbeit im Schwerpunkt Li

### PDF vom 08.06.2010 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2017.md)

**Pflichtmodule (20):**
- Basismodul Aktuelle Interkul- turalitäts- und Intermediali- tätstheorien
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität
- Tätigkeit als studentische Hilfs- kraft oder Tutor/Tutorin im Um- fang von ca. 3 SWS
- Masterarbeit
- MA Thesis Module: Linguis-
- tics and Applied Linguistics
- Basismodul Aktuelle Inter- kulturalitäts- und Inter- medialitätstheorien
- Interdisziplinäres Basis- modul zur konkreten Analyse von Medialität und Kulturalität
- A WP 2/7 Angewandte und deskriptive Linguistik der romanischen Sprachen
- Tätigkeit als studentische Hilfskraft oder Tutor/Tutorin
- im Umfang von ca. 3 SWS
- Masterarbeit:Es ist eines der bei Masterarbeit im Schwerpunkt C MA Thi Mdl Clt
- ess oue: uure
- and Literature Masterarbeit im Schwerpunkt Li
- Interdisziplinäres Basis- modul zur konkreten Ana- lyse von Medialität und Kulturalität
- Tätigkeit als studentische Hilfskraft oder Tutor/Tutorin im Umfang von ca. 3 SWS
- Masterarbeit:Es ist eines der be Masterarbeit im Schwerpunkt C MA Thi Mdl Clt
- and Literature
- Masterarbeit im Schwerpunkt L
- MA Thesis Module: Linguis- tics and Applied Linguistics

### PDF vom 08.06.2010 i.d.F. 07.03.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-maerz2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-maerz2017.md)

**Pflichtmodule (14):**
- Basismodul Aktuelle Inter- kulturalitäts- und Interme- dialitätstheorien
- Interdisziplinäres Basis- modul zur konkreten Analyse von Medialität und Kulturalität
- Praktikum (intern oder extern)
- Tätigkeit als studentische Hilfskraft oder Tutor/Tutorin
- im Umfang von ca. 3 SWS
- MA Thesis Module
- Summ
- Masterarbeit
- MA Thesis
- Masterarbeit (60-80 Seiten) Summe 18 37
- Basismodul Aktuelle Inter- kulturalitäts- und Inter- medialitätstheorien
- im Umfan von ca 3 SWS
- g . Masterarbeit:Es ist eines der bei Masterarbeit im Schwerpunkt C
- Masterarbeit im Schwerpunkt Li

### PDF vom 08.06.2010 i.d.F. 23.02.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-geschichte-feb2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-geschichte-feb2017.md)

**Pflichtmodule (2):**
- Prüfungsmodul
- bs. 6)

### PDF vom 08.06.2010 i.d.F. 13.06.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2014.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2014.md)

**Pflichtmodule (19):**
- Basismodul Französi-
- sche Sprachpraxis 1
- Communication orale
- Vocabulaire, idiomatique et civilisation II
- Grammaire cours élémentaire II (groupe
- Basismodul Französi- sche Sprachpraxis 2
- Phonétique pratique, orthophonie et into- nation
- Expression écrite I
- Basismodul Italienische
- Sprachpraxis 1
- Sprachpraxis 2
- Tecniche di lettura
- Grammatica e stilistica
- Basismodul Spanische
- Comprensión oral
- (4) Basismodul Sprachpraxis Elementarkurs 1
- (4) Elementarkurs 2
- (2) Optionsmodul Sprach- Sprachkurs 1
- (2) raxis Sprachkurs 2

### PDF vom 08.06.2010 i.d.F. 11.06.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2015.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2015.md)

**Pflichtmodule (19):**
- Basismodul Französi-
- sche Sprachpraxis 1
- Communication orale
- Vocabulaire, idiomatique et civilisation II
- Basismodul Französi- sche Sprachpraxis 2
- Phonétique pratique, orthophonie et into- nation
- Expression écrite I
- Basismodul Italienische
- Sprachpraxis 1
- Sprachpraxis 2
- Tecniche di lettura
- Grammatica e stilistica
- Basismodul Spanische
- Comprensión oral 2
- Basismodul Sprachpraxis
- Elementarkurs 2
- Otionsmodul Srach-
- Sprachkurs 2
- Sprachkurs 3

### PDF vom 08.06.2010 i.d.F. 09.03.2011

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-maerz2011.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-maerz2011.md)

**Pflichtmodule (8):**
- (8) Basismodul Sprachpraxis
- (4) Elementarkurs 1
- (4) Elementarkurs 2
- _2e: Wahlpflichtmodul: Optionsmodul Sprachpraxis (Italie_
- (6) Optionsmodul Sprachpraxis
- (2) Sprachkurs 1
- (2) Sprachkurs 2
- (2) Sprachkurs 3

### PDF vom 08.06.2010 i.d.F. 08.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-aug2017.md)

**Pflichtmodule (5):**
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul
- Oberseminar
- Summ

### (PDF vom 08.06.2010 i.d.F: 05.08.2011

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-august2011.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-august2011.md)

**Pflichtmodule (7):**
- (4) Mündl. Vortrag (ca. 30 Minuten), Stundenprotokol- le, schriftl. Hausarbeit
- Präsentation, Essay, Protokoll
- (4) Mündl. Vortrag (ca. 30 Minuten), Stundenprotokol- le, schriftl. Hausarbeit (10- 20 Seiten)
- Modulimport: Nach Maß- gabe des Anbieters
- (4) Teilnahme an mind. 5 Exkursionstagen, mdl. Vortrag (ca. 30 Minuten), Exposé
- (2) Mdl. Vortrag (ca. 30 Minu- ten), Rezension, Vortrags- oder Kongressbericht
- Schriftliche Hausarbeit (ca. 80 Seiten)

### PDF vom 08.06.2010 i.d.F. 05.11.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch.md)

**Pflichtmodule (4):**
- (4) Teilnahme an mind. 5 Exkursionstagen, mdl. Vortrag (ca. 30 Minuten),Exposé
- (4) Modulimport: Nach Maßgabe des An- bieters
- (2) Mdl. Vortrag (ca. 30 Minuten), Rezensi- on, Vortrags- oder Kongressbericht
- Schriftliche Hausar- beit(ca. 80 Seiten)

### PDF vom 08.06.2010 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-aug2017.md)

**Pflichtmodule (10):**
- Grundlagen der Germanistischen Mediävistik (Med 1)<sup>2</sup>
- Interdisziplinäres Kolloquium
- Masterfach
- Fachmodul I<sup>3</sup> Masterfach
- Fachmodul II<sup>3</sup> Masterfach
- Fachmodul III<sup>3</sup> Masterfach
- Oberseminar <sup>4</sup>
- Profilfach
- Fachmodul I<sup>3</sup> Profilfach
- Fachmodul II<sup>3</sup>

### PDF vom 08.06.2010 i.d.F. 02.03.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-maerz2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-maerz2017.md)

**Pflichtmodule (13):**
- Grundlagen der Germanistischen Mediävistik (Med 1)<sup>2</sup>
- Interdisziplinäres Kolloquium
- Masterfach
- Fachmodul I<sup>~~3~~</sup> Masterfach
- Fachmodul II<sup>~~3~~</sup> Masterfach
- Fachmodul III<sup>~~3~~</sup> Masterfach
- Oberseminar <sup>4</sup>
- Profilfach Fhdl I<sup>~~3~~</sup>
- acmou Profilfach
- Fachmodul II<sup>~~3~~</sup>
- Profilfach
- Masterarbeit Mdl
- astermou

### PDF vom 08.06.2010 i.d.F. 03.08.3015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelneulatein-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelneulatein-aug2015.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 28.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-nahoststudien-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-nahoststudien-juli2014.md)

**Pflichtmodule (6):**
- Raum und Region
- Einführung in das Studi- um des Nahen Ostens
- Transregionale Themen und Methoden I
- Transregionale Themen und Methoden II
- Forschungskolloquium
- quium

### PDF vom 08.06.2010 i.d.F. 08.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-northamerstud-fponoamstudaug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-northamerstud-fponoamstudaug2017.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 24.03.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-northamerstud-maerz2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-northamerstud-maerz2016.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 06.07.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-politikwiss-juli2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-politikwiss-juli2016.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-romanistik-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-romanistik-aug2017.md)

**Pflichtmodule (6):**
- Basismodul Aktuelle Interkulturalitäts- und Intermedialitätstheorien
- América Latina: Cultura y literatura
- Modul 4: Sprachpraxis Sprache A: Es ist ein Modul
- Französisch als Sprache A Abschlussmodul Französische Sprach- praxis 5
- Italienisch als Sprache A Abschlussmodul Italienische Sprach- praxis 5
- Spanisch als Sprache A Abschlussmodul Spanische Sprach- praxis 6

### PDF vom 08.06.2010 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-sinologie-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-sinologie-aug2017.md)

**Pflichtmodule (8):**
- Basismodul Praktische Philosophie
- Basismodul Theoretische Philosophie
- Praktische Philosophie I<sup>2</sup>
- Praktische Philosophie II<sup>2</sup>
- Praktische Philosophie III<sup>2</sup>
- Theoretische Philosophie I<sup>2</sup>
- Theoretische Philosophie II<sup>2</sup>
- Theoretische Philosophie III<sup>2</sup>

### PDF vom 08.06.2010 i.d.F. 17.01.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-soziologie-jan2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-soziologie-jan2017.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 12.02.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-theamericas-absose2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-theamericas-absose2016.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 12.02.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-theamericas-feb2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-theamericas-feb2016.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 26.01.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-theaterpaedjan2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-theaterpaedjan2016.md)

**Pflichtmodule (28):**
- Grundlagen und Rahmen
- der Theaterpädagogik
- Theaterwissenschaft I:
- Dimensionen des Theatralen und Performativen
- Kulturpädagogik II:
- Handlungsfelder und Hand- lungsformen
- Anewandte theateräda-
- g p gogische Forschung
- Theaterwissenschaft II:
- Kulturen, Funktionen und Wahrnehmungsformen der theatralen Praktiken
- Theaterpädagogische Pra- xisreflexion
- Theaterpädagogische For- schungspraxis
- Masterarbeit
- Begleitseminar
- Grundlagen und Rahmen der
- Theaterpädagogik
- Theaterwissenschaft I: Dii d Thtl d
- mensonen es earaen un
- Performativen
- Kulturpädagogik II: Handlunsfelder und Handluns-
- Angewandte theaterpädagogische
- Forschung
- Theaterwissenschaft II: Kulturen Funktionen und Wahr-
- , nehmungsformen der theatralen Praktiken
- Theaterpädagogische Praxis-
- reflexion
- Theaterpädagogische
- Forschungspraxis

### PDF vom 15.05.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-arabistik-islamwiss-semitistik.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-arabistik-islamwiss-semitistik.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPO MA DH 20190328.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-dh-20190328.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-dh-20190328.md)

**Pflichtmodule (4):**
- Masterarbeit
- Kolloquium
- SWS und ECTS-Punkte
- nd ECTS-Punkte

### PDF vom 14.06.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-imperientranskontraeume.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-imperientranskontraeume.md)

**Pflichtmodule (18):**
- Basismodul Nordamerika
- Modul 2
- Basismodul Ostasien
- Modul 3
- Basismodul Europa
- Modul 4 Lektüremodul 1 - Grundlagen der Area Studies
- Modul 5 Lektüremodul 2 - Themenfel- der der Area Studies
- Wissenschaftliches Präsentieren
- Modul 6 Basismodul Forschungspraxis
- Workshop/Sommerakademie/Exkursion
- Modul 7 Projekt- und Mobilitätsmodul
- Modul 8 Profilierungsmodul 1: Transat-
- lantik
- Modul 9
- Profilierungsmodul 2: Transat- lantik
- Modul 14a<sup>2</sup> Wahlpflichtmodul Staat und Gesellschaft
- cher
- ischer

### PDF vom 15.05.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-islamisch-relig-studien.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-islamisch-relig-studien.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPO MA L.D. 20230223.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-l-d-20230223.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-l-d-20230223.md)

**Pflichtmodule (12):**
- Wissenschaftliches Basismodul
- Mediendidaktik
- Educational Techno- l
- Einführung Educational Techno- logy
- Praxis Digital Educa-
- tion
- Lernumebunen
- Produktion Lernmedien
- E-Assessment
- Qualitätssicherung
- Masterarbeit
- Masterabschluss-

### (PDF vom 30.07.2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-populaermedienkult-japans.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-populaermedienkult-japans.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Antike Sprachen und Kulturen FPOAnSK 20100608 i.d.F. 20190326.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20190326.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20190326.md)

**Pflichtmodule (12):**
- Pflichtmodul für alle Studienrichtungen
- (2) Motive und Formen Proseminar Orient und Okzident
- (2) Pi i blid Eidi<sup>1</sup>
- rosemnar mt egetenemgenstuum Indogermanistik und Indoiranistik Basisbereich Indogermanistik und Indoiranistik<sup>2</sup>
- (2) Fragestellungen und Geschichte Vorlesung Die frühe Indogermanistik
- (2) der Indogermanistik Hauptseminar Fragestellungen der Indo- germanistik
- (2) Mykenisch und die griechischen Hauptseminar Einführung in das Mykenische und Überblicküberdie griechischen Dialekte
- (2) Dialekte<sup>4</sup> Hauptseminar Die Kunstsprache Homers
- (2) Indoiranisch Hauptseminar Avesta- oder Vedalektüre
- (2) Übung Altpersisch
- Historische Linguistik und Sprachwandel (II LING 2) gem. FPO M.A. Germ
- Masterarbeit

### MA Antike Sprachen und Kulturen FPOAnSK 20100608 i.d.F. 20210222.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20210222.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20210222.md)

**Pflichtmodule (12):**
- Pflichtmodul für alle Studienrichtungen
- (2) Motive und Formen Proseminar Orient und Okzident
- (2) Pi i blid Eidi<sup>1</sup>
- rosemnar mt egetenemgenstuum Indogermanistik und Indoiranistik Basisbereich Indogermanistik und Indoiranistik<sup>2</sup>
- (2) Fragestellungen und Geschichte Vorlesung Die frühe Indogermanistik
- (2) der Indogermanistik Hauptseminar Fragestellungen der Indo- germanistik
- (2) Mykenisch und die griechischen Hauptseminar Einführung in das Mykenische und Überblicküberdie griechischen Dialekte
- (2) Dialekte<sup>4</sup> Hauptseminar Die Kunstsprache Homers
- (2) Indoiranisch Hauptseminar Avesta- oder Vedalektüre
- Übung Altpersisch
- Historische Linguistik und Sprachwandel (II LING 2) gem. FPO M.A. Germa
- Masterarbeit

### MA Antike Sprachen und Kulturen FPOAnSK 20190326 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20190326-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20190326-aes.md)

**Pflichtmodule (10):**
- (2) Pflichtmodul für alle Studienrichtungen Proseminar Orient und Okzident
- (2) Motive und Formen Pi i blid Eidi<sup>1</sup>
- rosemnar mt egetenemgenstuum Indogermanistik und Indoiranistik Basisbereich Indogermanistik und Indoiranistik<sup>2</sup>
- (2) Fragestellungen und Geschichte Vorlesung Die frühe Indogermanistik
- (2) der Indogermanistik Hauptseminar Fragestellungen der Indo- germanistik
- (2) Mykenisch und die griechischen Hauptseminar Einführung in das Mykenische und Überblicküberdie griechischen Dialekte
- (2) Dialekte<sup>4</sup> Hauptseminar Die Kunstsprache Homers
- (2) Indoiranisch Hauptseminar Avesta- oder Vedalektüre
- Übung Altpersisch
- Historische Linguistik und Sprachwandel (II LING 2) gem. FPO M.A. Germa

### MA Antike Sprachen und Kulturen FPOAnSk 20250131.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20250131.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20250131.md)

**Pflichtmodule (14):**
- Pflichtmodul für alle Studienrichtunge
- Proseminar Orient und Okzident
- Motive und Formen
- dium<sup>1</sup>
- Indogermanistik und Indoiranistik Basisbereich Indogermanistik und Ind
- Vorlesung Die frühe Indogermanistik
- Fragestellungen und Geschichte der Indogermanistik
- Mykenisch und die griechischen Dialekte<sup>4</sup>
- Hauptseminar Die Kunstsprache Ho- mers
- Hauptseminar Avesta- oder Vedalektüre
- Indoiranisch
- Historische Linguistik und Sprach-
- wandel
- Masterarbeit

### MA Arabistik Islamwissenschaft Semitistik FPOAIS 20150515 i.d.F. 20200813.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-arabistik-islamwissenschaft-semitistik-fpoais-20150515-idf-20200813.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-arabistik-islamwissenschaft-semitistik-fpoais-20150515-idf-20200813.md)

**Pflichtmodule (4):**
- Masterarbeit
- Forschungskolloquium
- Mtbit
- aserare

### MA Archäologische Wissenschaften FPOArWi 20100608 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-archaeologische-wissenschaften-fpoarwi-20100608-idf-20180730.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-archaeologische-wissenschaften-fpoarwi-20100608-idf-20180730.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Archäologische Wissenschaften FPOArWi 20100608 i.d.F. 20200214.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-archaeologische-wissenschaften-fpoarwi-20100608-idf-20200214.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-archaeologische-wissenschaften-fpoarwi-20100608-idf-20200214.md)

**Pflichtmodule (2):**
- Masterarbeit
- SummenSWS /ECTS

### MA Archäologische Wissenschaften FPOArWi 20180730 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-archaeologische-wissenschaften-fpoarwi-20180730-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-archaeologische-wissenschaften-fpoarwi-20180730-aes.md)

**Pflichtmodule (2):**
- Masterarbeit
- SummenSWS /ECTS

### MA Bildungsforschung 20121109 i.d.F. 20180213.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-bildungsforschung-20121109-idf-20180213.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-bildungsforschung-20121109-idf-20180213.md)

**Pflichtmodule (23):**
- Mentorat
- Modul 2: Eihihftlih
- rzeungswssenscace Vertiefung
- Modul 3:
- Methoden der Empirischen Bildungsforschung – Grund-
- lagen
- Modul 4: Methoden der Empirischen
- Bildungsforschung – Vertie- fung
- Modul 5: Ergebnisse der Empirischen
- Bildungsforschung in schuli-
- schen und außerschulischen
- Feldern
- Modul 6:
- Pfildl Whlflih<sup>2)</sup>
- rogrunagen (apct)
- Modul 7:
- Profilvertiefung (Wahlpflicht)<sup>2)</sup>
- Seminar 1
- Modul 8: Pktdl
- rojegrunagen
- Modul 9:
- Projektdurchführung
- Modul 10: Masterarbeit

### MA Buchwissenschaft FPO M.A. BuWi 20100608 i.d.F. 20190611.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpo-m-a-buwi-20100608-idf-20190611.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpo-m-a-buwi-20100608-idf-20190611.md)

**Pflichtmodule (14):**
- Wissenschaftstheorie
- Transformationsprozesse
- Kernmodul 1:
- Medienkommunikation
- Kernmodul 2:
- Medienwirtschaft
- Projekt
- Pktbit
- rojeare
- Forschungsperspektiven
- Masterarbeit
- .)und ECTS-Punkte
- Pkbi
- rojetaret

### MA Buchwissenschaft FPOBuWi 20190611 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpobuwi-20190611-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpobuwi-20190611-aes.md)

**Pflichtmodule (14):**
- Wissenschaftstheorie
- Transformationsprozesse
- Kernmodul 1:
- Medienkommunikation
- Kernmodul 2:
- Medienwirtschaft
- Projekt
- Hauptseminar
- rojetarbet
- Forschungsperspektiven
- Masterarbeit
- mind.) undECTS-Punkte
- Projektarbeit
- mme SWS und ECTS

### MA Buchwissenschaft FPOBuWi 20230223 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpobuwi-20230223-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpobuwi-20230223-aes.md)

**Pflichtmodule (10):**
- Kernmodul 1: Rahmenbedingungen
- Hauptseminar II
- Kernmodul 2: Praktiken
- Projekt
- Projektarbeit
- Masterarbeit
- ind.) und ECTS-Punkte
- Mtbit
- aserare
- (mind.) und ECTS-Punkte

### MA DEIS FPODEIS 20100608 i.d.F. 20180221.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20180221.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20180221.md)

**Pflichtmodule (11):**
- Development Economics I
- Development Economics II
- International Economics I
- International Economics II
- Research Methods I
- Research Methods II
- International Business Ethics I
- International Business Ethics II
- CTS)
- Regional Module I
- Regional Module II

### MA DEIS FPODEIS 20100608 i.d.F. 20190731.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20190731.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20190731.md)

**Pflichtmodule (11):**
- Development Economics I
- Development Economics II
- International Economics I
- International Economics II
- Research Methods I
- Research Methods II
- International Business Ethics I
- International Business Ethics II
- oder Hauptseminar
- Regional Module I
- Regional Module II

### MA DEIS FPODEIS 20100608 i.d.F. 20200408.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20200408.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20200408.md)

**Pflichtmodule (11):**
- Development Economics I
- Development Economics II
- International Economics I
- International Economics II
- Research Methods I
- Research Methods II
- International Business Ethics I
- International Business Ethics II
- oder Hauptseminar
- Regional Module I
- Regional Module II

### MA DEIS FPODEIS 20100608 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20230731.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20230731.md)

**Pflichtmodule (13):**
- Development Economics I
- Development Economics II
- International Economics I
- International Economics II
- Research Methods I
- Research Methods II
- International Business Ethics I
- International Business Ethics II
- Regional Module I
- Regional Module II
- Masterarbeit
- Master Thesis
- umme SWS und ECTS 8-16

### MA DEIS FPODEIS 20180221 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20180221-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20180221-aes.md)

**Pflichtmodule (13):**
- Development Economics I
- Development Economics II
- International Economics I
- International Economics II
- Research Methods I
- Research Methods II
- International Business Ethics I
- International Business Ethics II
- CTS)
- Regional Module I
- Regional Module II
- Masterarbeit
- Master Thesis

### MA DEIS FPODEIS 20240807.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20240807.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20240807.md)

**Pflichtmodule (2):**
- Masterarbeit
- Master Thesis

### MA Digitale Japanstudien FPO M.A DIJAS 20210429 i.d.F. 20230426.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-digitale-japanstudien-fpo-m-a-dijas-20210429-idf-20230426.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-digitale-japanstudien-fpo-m-a-dijas-20210429-idf-20230426.md)

**Pflichtmodule (19):**
- Grundlagen der Computerlinguistik I
- Grundlagen der Computerlinguistik II
- Grundlagen der Computerlinguistik III
- Programmierung & Infrastrukturen I
- Programmierung &Infrastrukturen II
- B.A. Politikwissenschaft
- Politische Systeme I
- Außereuropäische Regionen I
- Außereuropäische Regionen II
- InternationaleBeziehungen I
- B.A. Sozialökonomik
- Grundzüge der Kommunikationswissenschaft
- Einführung in das Mediensystem
- M.A. Buchwissenschaft
- Transformationsprozesse
- Kernmodul 1: Medienkommunikation
- Kernmodul 2: Medienwirtschaft
- M.A. Medienwissenschaft
- Modul I: Dimensionen des Medialen und Visuellen

### MA Digitale Japanstudien FPO M.A DIJAS 20210429.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-digitale-japanstudien-fpo-m-a-dijas-20210429.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-digitale-japanstudien-fpo-m-a-dijas-20210429.md)

**Pflichtmodule (25):**
- MABM1 Pliik llhf
- MA-BM2 Medien in Japan
- MABM3 Diitl Mthd
- - gae eoen
- Masterarbeit
- MA-MA1 Masterarbeit
- Grundlagen der Computerlinguistik I
- Grundlagen der Computerlinguistik II
- Programmierung I
- B.A. Politikwissenschaft
- Politische SystemeI
- Außereuropäische Regionen I
- Außereuropäische Regionen II
- Internationale Beziehungen I
- B.A. Sozialökonomik
- Grundzüge der Kommunikationswissenschaft
- Einführung in das Mediensystem
- M.A. Buchwissenschaft
- Transformationsprozesse
- Kernmodul 1: Medienkommunikation
- Kernmodul 2: Medienwirtschaft
- M.A. Medienwissenschaft
- Modul I: Dimensionen des Medialen und Visuellen
- Modul III: Komparatistische Analyse- verfahren
- Modul IV: Bildanalyse

### PDF 24th of August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-20100608-idf-20170824-en.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-20100608-idf-20170824-en.md)

**Pflichtmodule (3):**
- osen.
- t be obtained from the following modu
- from the followin

### MA English Studies FPOEnStud 20100608 i.d.F. 202108012 en.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20100608-idf-202108012-en.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20100608-idf-202108012-en.md)

**Pflichtmodule (3):**
- hosen.
- be obtained from the following mo
- credits must be obtaine

### MA English Studies FPOEnStud 20100608 i.d.F. 20210812.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20100608-idf-20210812.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20100608-idf-20210812.md)

**Pflichtmodule (16):**
- Basismodul Aktuelle Interkulturalitäts- und Intermedialitätstheorien<sup>7</sup>
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität<sup>7</sup>
- A WP 2/7 Angewandte und deskriptive Linguistik der romanischen Sprachen<sup>7</sup>
- Tätigkeit als studentische Hilfskraft oder Tutor/Tutorin im Umfang von ca. 3 SWS
- Masterarbeit:Es ist eines der b
- Masterarbeit im Schwerpunkt
- MA Thesis Module: Culture and Literature
- MA Thesis Module: Linguistics and Applied Linguistics
- Basismodul Aktuelle Interkulturalitäts- und Intermedialitätstheorien
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität
- Masterarbeit
- Basismodul Aktuelle Inter- kulturalitäts- und Inter- medialitätstheorien<sup>7</sup>
- Masterarbeit:Es ist eines der be Masterarbeit im Schwerpunkt C
- MA Thesis Module: Culture
- and Literature
- Masterarbeit im Schwerpunkt L

### MA English Studies FPOEnStud 20210812 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20210812-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20210812-aes.md)

**Pflichtmodule (15):**
- Basismodul Aktuelle Interkulturalitäts- und Intermedialitätstheorien
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität
- Basismodul Aktuelle Interkulturalitäts- und Intermedialitätstheorien<sup>7</sup>
- Masterarbeit im Schwerpunkt C
- MA Thesis Module: Culture
- siehe Anlage 1
- and Literature
- Masterarbeit im Schwerpunkt Li
- MA Thesis Module: Linguistics and Applied
- Linguistics
- Tätigkeit als studentische Hilfskraft oder Tutor/Tutorin im Umfang von ca. 3 SWS
- Basismodul Aktuelle Inter- kulturalitäts- und Inter- medialitätstheorien<sup>7</sup>
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität<sup>7</sup>
- Masterarbeit:Es ist eines der bei Masterarbeit im Schwerpunkt C
- an terature Masterarbeit im Schwerpunkt Li

### MA Germanistik 20100608 i.d.F. 20180213.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20180213.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20180213.md)

**Pflichtmodule (4):**
- Masterarbeit NDL (IV NDL 1)
- Abschlussprüfung NDL (IV NDL 2)
- Masterarbeit ÄDL (IV MED 1)
- Abschlussprüfung ÄDL (IV MED 2)

### MA Germanistik 20100608 i.d.F. 20200610.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20200610.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20200610.md)

**Pflichtmodule (22):**
- Fachmodulegemäß§ 5
- Fachmodul I<sup>2)</sup>
- Übung/Kolleg
- Fachmodul II<sup>2)</sup>
- Fachmodul III
- Profilbereich (gem. FPO § 3 Abs. 2
- Profilmodul Germanistische
- Linguistik<sup>3)</sup>
- Profilmodul Neuere deutsche
- Literaturwissenschaft<sup>3)</sup>
- Mediävistik<sup>3)</sup>
- Oberseminar/Kolloquium
- Interdisziplinäre undpraktische M
- Workshop
- Projektmodul
- ratum
- Extradisziplinäres Modul I
- Abschlussmodul
- Masterarbeit
- Abschlussprüfung
- Freier Bereich (Es sind Module i
- Fachmodul IV<sup>4)</sup>

### MA Germanistik 20100608 i.d.F. 20210113.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20210113.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20210113.md)

**Pflichtmodule (34):**
- Pflichtbereich Fachmodulegemäß § 5
- Fachmodul I<sup>2)</sup>
- Fachmodul II<sup>2)</sup>
- Fachmodul III
- Profilbereich (gem FPO § 3 Abs 2
- . . Profilmodul Germanistische
- Linguistik<sup>3)</sup>
- Profilmodul Neuere deutsche
- Literaturwissenschaft<sup>3)</sup>
- Profilmodul Germanistische
- Mediävistik<sup>3)</sup>
- Oberseminar/Kolloquium
- Interdisziplinäre und praktische M
- Workshop
- Projektmodul
- Extradisziplinäres Modul I
- Abschlussmodul
- Masterarbeit
- Abschlussprüfung
- Freier Bereich (Es sind Module i
- Fachmodul IV<sup>4)</sup>
- Fachmodul V
- Lektüremodul I
- (5) Fachmodulegemäß §
- Profilbereich (gem. FP
- Profilmodul
- Germanistische Linguistik<sup>3)</sup>
- Profilmodul Neuere
- deutsche Literatur- wissenschaft<sup>3)</sup>
- Germanistische Mediävistik<sup>3)</sup>
- Oberseminar/ Kllim
- ooquu Interdisziplinäre und pr
- odu Abschlussmodul
- Freier Bereich (Es sin

### MA Germanistik 20100608 i.d.F. 20230323.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20230323.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20230323.md)

**Pflichtmodule (33):**
- Pflichtbereich Fachmodulegemäß § 5
- Fachmodul I<sup>2)</sup>
- Fachmodul II<sup>2)</sup>
- Fachmodul III
- Profilbereich (gem. FPO § 3 Abs. 2
- Profilmodul Germanistische
- Linguistik<sup>3)</sup>
- Profilmodul Neuere deutsche
- Literaturwissenschaft<sup>3)</sup>
- Mediävistik<sup>3)</sup>
- Oberseminar/Kolloquium
- Interdisziplinäre und praktische M
- Workshop
- Projektmodul
- Extradisziplinäres Modul I
- Abschlussmodul
- Masterarbeit
- Abschlussprüfung
- Freier Bereich (Es sind Module i
- Fachmodul IV<sup>4)</sup>
- Fachmodul V
- Lektüremodul I
- (5) Fachmodulegemäß §
- Profilbereich (gem. FP
- Profilmodul
- Germanistische Linguistik<sup>3)</sup>
- Profilmodul Neuere
- deutsche Literatur- wissenschaft<sup>3)</sup>
- Germanistische Mediävistik<sup>3)</sup>
- Oberseminar/ Kllim
- ooquu Interdisziplinäre und pr
- odu Abschlussmodul
- Freier Bereich (Es sin

### MA Germanistik 20180213 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20180213-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20180213-aes.md)

**Pflichtmodule (7):**
- Masterarbeit LING
- (IV LING 1)
- Abschlussprüfung LING (IV LING 2)
- Masterarbeit NDL (IV NDL 1)
- Abschlussprüfung NDL (IV NDL 2)
- Masterarbeit ÄDL (IV MED 1)
- Abschlussprüfung ÄDL (IV MED 2)

### MA Germanistik 20200610 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20200610-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20200610-aes.md)

**Pflichtmodule (1):**
- gen.) 2

### MA Germanistik FPOGerm 20210113 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-fpogerm-20210113-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-fpogerm-20210113-aes.md)

**Pflichtmodule (23):**
- Fachmodul I<sup>2)</sup>
- Fachmodul II<sup>2)</sup>
- Fachmodul III
- Profilbereich (gem. FPO
- Profilmodul
- Germanistische Linguistik<sup>3)</sup>
- Profilmodul Neuere
- deutsche Literatur- wissenschaft<sup>3)</sup>
- Germanistische Mediävistik<sup>3)</sup>
- Oberseminar/ Klli
- ooquum Interdisziplinäre undpr
- Workshop
- Projektmodul
- Extradisziplinäres Modul I
- Masterarbeit
- Abschlussprüfung
- Freier Bereich (Es sind
- Fachmodul IV<sup>4)</sup>
- Fachmodul V
- Lektüremodul I
- Lektüremodul II
- Extradisziplinäres Modul II
- Extradisziplinäres Modul III

### MA Islamisch-Religiöse Studien FPOIRS 20150515 i.d.F. 20190802.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-islamisch-religioese-studien-fpoirs-20150515-idf-20190802.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-islamisch-religioese-studien-fpoirs-20150515-idf-20190802.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Islamisch-Religiöse Studien FPOIRS 20190802 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-islamisch-religioese-studien-fpoirs-20190802-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-islamisch-religioese-studien-fpoirs-20190802-aes.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Kunstgeschichte MFPOKunstGesch 20100608 i.d.F. 20180618.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20100608-idf-20180618.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20100608-idf-20180618.md)

**Pflichtmodule (6):**
- Grundlagen der Museologie
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul
- Oberseminar
- Summ

### MA Kunstgeschichte MFPOKunstGesch 20100608 i.d.F. 20200214.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20100608-idf-20200214.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20100608-idf-20200214.md)

**Pflichtmodule (3):**
- Grundlagen der Museologie I
- Grundlagen der Museologie II
- Grundlagen der Informatik

### MA Kunstgeschichte MFPOKunstGesch 20200214 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20200214-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20200214-aes.md)

**Pflichtmodule (7):**
- Grundlagen der Museologie I
- Grundlagen der Museologie II
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul
- Oberseminar
- Summ

### MA Kunstgeschichte MFPOKunstGesch 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20230822.md)

**Pflichtmodule (6):**
- Grundlagen der Museologie I
- Grundlagen der Museologie II
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul
- nd ECTS-Punkte

### MA Linguistik FPOLing 20180618 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20180618-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20180618-aes.md)

**Pflichtmodule (6):**
- Masterarbeit
- WP 3/1 Mastermodul Linguistik
- (Germanistik)
- WP 3/1 Mastermodul Linguistik (Anglistik)
- WP 3/1 Mastermodul Linguistik (Romanistik)
- mind. 2,5 Summ

### MA Linguistik FPOLing 20210812 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20210812-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20210812-aes.md)

**Pflichtmodule (4):**
- Masterarbeit
- WP Mastermodul Linguistik (Germanistik)
- WP Mastermodul Linguistik (Anglistik)
- WP Mastermodul Linguistik (Romanistik)

### MA Literaturstudien FPOLitStud 20100608 i.d.F. 20180515.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-fpolitstud-20100608-idf-20180515.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-fpolitstud-20100608-idf-20180515.md)

**Pflichtmodule (13):**
- Interdisziplinäres Basismodul zur Einführun in den Theoriekomlex
- Hauptseminar
- Basismodul Aktuelle Interkulturalitäts-
- und Intermedialitätstheorien
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und
- Kulturalität Aufbaumodul Intermediale/
- interkulturelleLiteraturanalyse
- Masterarbeit
- Masterarbeit me SWS undECTS
- Kulturalität
- Afbmdl Intrmdil/
- uauou eeae interkulturelleLiteraturanalyse
- mme SWS und ECTS

### MA Literaturstudien FPOLitStud 20240430.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-fpolitstud-20240430.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-fpolitstud-20240430.md)

**Pflichtmodule (16):**
- Interdisziplinäres Basismodul zur Einführung in den
- Theoriekomplex Literatur/Kultur/Medien
- Einführungsmodul: Theorien und
- Methoden
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität
- und Kulturalität
- Kernfachgemäß§ 4<sup>1)</sup>
- Masterarbeit im Kernfach
- Masterarbeit
- und ECTS-Punkte
- Theorienkomplex Literatur/Kultur/Medien
- Hauptseminar
- Einführungsmodul: Theorien und Methoden
- Interdisziplinäres Basismodul zur konkreten Analyse von
- Medialität und Kulturalität
- mind .

### MA Literaturstudien MFPOLitStud 20180515 Äs.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-mfpolitstud-20180515-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-mfpolitstud-20180515-aes.md)

**Pflichtmodule (8):**
- Interdisziplinäres Basismodul zur Einführung in den Theoriekomplex
- Literatur/Kultur/Medien
- Basismodul Aktuelle Interkulturali-
- täts- und Intermedialitätstheorien
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität
- und Kulturalität
- Masterarbeit
- mme SWS und ECTS

### MA Mittelalter und Frühe Neuzeit FPOMiFNZ 20100608 i.d.F. 20190809.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20100608-idf-20190809.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20100608-idf-20190809.md)

**Pflichtmodule (10):**
- Grundlagen der Germanistischen Mediävistik (Med 1)<sup>2</sup>
- Interdisziplinäres Kolloquium
- Masterfach
- Fachmodul I<sup>3</sup> Masterfach
- Fachmodul II<sup>3</sup> Masterfach
- Fachmodul III<sup>3</sup> Masterfach
- Oberseminar <sup>4</sup>
- Profilfach
- Fachmodul I<sup>3</sup> Profilfach
- Fachmodul II<sup>3</sup>

### MA Mittelalter und Frühe Neuzeit FPOMiFNZ 20240131.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20240131.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20240131.md)

**Pflichtmodule (10):**
- Grundlagen der Germanistischen Mediävistik (Med1)<sup>2</sup>
- Interdisziplinäres Kolloquium
- Masterfach
- Fachmodul I<sup>3</sup> Masterfach
- Fachmodul II<sup>3</sup> Masterfach
- Fachmodul III<sup>3</sup> Masterfach
- Oberseminar <sup>4</sup>
- Profilfach
- Fachmodul I<sup>3</sup> Profilfach
- Fachmodul II<sup>3</sup>

### MA Nahoststudien FPONahOstStud 20100608 i.d.F. 20180817 .pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20100608-idf-20180817.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20100608-idf-20180817.md)

**Pflichtmodule (10):**
- Raum und Reion
- Einführung in das Studium des Nahen Ostens
- Transregionale Themen und Methoden I
- Transregionale Themen und Methoden II
- Forschungskolloquium Schwerpunkt Sprache und Litera
- Arabische Sprachwissenschaft
- Zweite Semitische Sprache
- Klassische Arabische Literatur
- Moderne Arabische Literatur
- Masterarbeit

### MA Nahoststudien FPONahOstStud 20180817 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20180817-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20180817-aes.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Nahoststudien FPONahOstStud 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20230822.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA North American Studies FPONoAmStud 20100608 i.d.F. 20210812.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-north-american-studies-fponoamstud-20100608-idf-20210812.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-north-american-studies-fponoamstud-20100608-idf-20210812.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA North American Studies FPONoAmStud 20230928.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-north-american-studies-fponoamstud-20230928.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-north-american-studies-fponoamstud-20230928.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Philosophie FPOPhilo 20190520 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-philosophie-fpophilo-20190520-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-philosophie-fpophilo-20190520-aes.md)

**Pflichtmodule (3):**
- Masterarbeit
- S und ECTS-Punkte 20
- S und ECTS-Punkte:

### MA Philosophie FPOPhilo 20240904.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-philosophie-fpophilo-20240904.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-philosophie-fpophilo-20240904.md)

**Pflichtmodule (3):**
- Masterarbeit
- S und ECTS-Punkte
- S und ECTS-Punkte: 20

### MA Politikwissenschaft FPO MA Politikwissenschaft 20100608 i.d.F. 20190702.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-politikwissenschaft-fpo-ma-politikwissenschaft-20100608-idf-20190702.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-politikwissenschaft-fpo-ma-politikwissenschaft-20100608-idf-20190702.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Politikwissenschaft FPO MA Politikwissenschaft 20100608 i.d.F. 20210113.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-politikwissenschaft-fpo-ma-politikwissenschaft-20100608-idf-20210113.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-politikwissenschaft-fpo-ma-politikwissenschaft-20100608-idf-20210113.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Politikwissenschaft FPO MA Politikwissenschaft 20210113 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-politikwissenschaft-fpo-ma-politikwissenschaft-20210113-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-politikwissenschaft-fpo-ma-politikwissenschaft-20210113-aes.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Politikwissenschaft FPO MA Politikwissenschaft 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-politikwissenschaft-fpo-ma-politikwissenschaft-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-politikwissenschaft-fpo-ma-politikwissenschaft-20230822.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Schriftmedienkultur und Digitale Transformation FPO M.A. SMK 20100608 i.d.F. 20230223.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-schriftmedienkultur-und-digitale-transformation-fpo-m-a-smk-20100608-idf-20230223.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-schriftmedienkultur-und-digitale-transformation-fpo-m-a-smk-20100608-idf-20230223.md)

**Pflichtmodule (10):**
- Kernmodul 1: Rahmenbedingungen
- Hauptseminar II
- Kernmodul 2: Praktiken
- Projekt
- Projektarbeit
- Masterarbeit
- ind.) und ECTS-Punkte
- Mtbit
- aserare
- mind.) und ECTS-Punkte

### MA The Americas Las Americas FPOAm 20100608 i.d.F. 20180130.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-the-americas-las-americas-fpoam-20100608-idf-20180130.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-the-americas-las-americas-fpoam-20100608-idf-20180130.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA The Americas Las Americas FPOAm 20100608 i.d.F. 20210812.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-the-americas-las-americas-fpoam-20100608-idf-20210812.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-the-americas-las-americas-fpoam-20100608-idf-20210812.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA The Americas Las Americas FPOAm 20180130 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-the-americas-las-americas-fpoam-20180130-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-the-americas-las-americas-fpoam-20180130-aes.md)

**Pflichtmodule (1):**
- Masterarbeit

### MSc Digitale Japanstudien MA DIJAS 20230426 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/msc-digitale-japanstudien-ma-dijas-20230426-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/msc-digitale-japanstudien-ma-dijas-20230426-aes.md)

**Pflichtmodule (4):**
- MA-BM1 Politik & Gesellschaft
- Japans
- MA-BM2 Medien in Jaan
- MA-BM3 Diitale Methoden

### Modulstudien Digital Humanities POM-DH 20210729 i.d.F. 20220808.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/modulstudien-digital-humanities-pom-dh-20210729-idf-20220808.md`](../pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/modulstudien-digital-humanities-pom-dh-20210729-idf-20220808.md)

**Pflichtmodule (9):**
- Grundlagen der Informatik
- (GdI-Kompakt)
- Bereich DH Schwerpunkt
- DH-Modul 1: Schwerpunkt Sprache und Text
- DH-Modul 2: Schwerpunkt Gesellschaft und Raum
- DH-Modul 3: Schwerpunkt Bild und Medien
- Grundlagen der Informatik (GdI-Kompakt)
- Theoretische Informatik für Wirtschaftsinformatik und Lehramts- studierende
- Grundlagen der Computerlinguistik II (statistischeVerfahren)

### Modulstudien Digital Humanities POM-DH 20210729.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/modulstudien-digital-humanities-pom-dh-20210729.md`](../pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/modulstudien-digital-humanities-pom-dh-20210729.md)

**Pflichtmodule (9):**
- Grundlagen der Informatik
- (GdI-Kompakt)
- Bereich DH Schwerpunkt
- DH-Modul 1: Schwerpunkt Sprache und Text
- DH-Modul 2: Schwerpunkt Gesellschaft und Raum
- DH-Modul 3:
- Grundlagen der Informatik (GdI-Kompakt)
- Theoretische Informatik für Wirtschaftsinformatik und Lehramts-
- studierende Wahlpflichtbereich Spezialisierung (5- Bereich Data Literacy <sup>4</sup>

### PO ZS Geow im LA 20250320 .pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/po-zs-geow-im-la-20250320.md`](../pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/po-zs-geow-im-la-20250320.md)

**Pflichtmodule (4):**
- Grundlagen der Geowissenschaften I
- Rohstoffe und Nachhaltigkeit
- Dynamik des Systems Erde
- Kompetenzseminar zum Klimawandel

### 24. November 2009

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/1aenderungssatzung-ma-20medienethikreligion.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/1aenderungssatzung-ma-20medienethikreligion.md)

**Pflichtmodule (9):**
- Grundlagen der Kommunikationswissenschaft
- Medienkunde Zeitung
- Medienkunde elektronische Medien
- Oder: Vertiefung Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach)
- Medienethik und Medienrecht —
- — ; Einfthrung Medienrecht
- Theorie und Praxis des Journalismus
- Theorie und Praxis des Fernsehjournalismus (Projekt
- Praxismodul

### 7. Dezember 2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/2aenderungssatzung-ma-20medienethikreligion.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/2aenderungssatzung-ma-20medienethikreligion.md)

**Pflichtmodule (3):**
- Grundlagen der Kommunikationswissenschaft
- SEM Methoden empirische Kommunikationsforschung
- Oder:Vertiefung Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach)

### 13. November 2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/3aes-ma-medien-ethik-religion.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/3aes-ma-medien-ethik-religion.md)

**Pflichtmodule (8):**
- Grundlagen der Kommunikations‐
- oder Medienwissenschaft (Importmodul)
- _Oder_: Vertiefung der Kommunikations‐ oder Medienwissenschaft (je nach bisherigem Studienfach<sup>1</sup>) (Importmodul)
- Medienethik
- SEM Grundzüge der Medienethik
- SEM Medienkunde
- Medienkunde, Journalismus und PR/Öffentlichkeitsarbeit
- SEM Grundlagen der PR‐Theorie und Projekt Öffentlichkeitsarbeit

### 8. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/4aes-ma-medien-ethik-religion.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/4aes-ma-medien-ethik-religion.md)

**Pflichtmodule (16):**
- Grundlagen der Kommunikations-
- oder Medienwissenschaft (Importmodul)
- Oder: Vertiefung der Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach<sup>1</sup>) (Importmodul)
- Medienethik
- SEM Grundzüge der Medienethik
- SEM Grundzüge Theologie für Nicht- Theologen
- VL oder SEM Einführung Altes Testament<sup>2</sup>
- VL oder SEM Einführung Neues Testament<sup>2</sup>
- Einführung theologische und religi- onswissenschaftliche Grundlagen
- VL oder SEM Einführung Systema- tik<sup>2</sup>
- VL oder SEM Einführung Praktische Theologie<sup>2</sup>
- VL oder SEM Einführung Religions- wissenschaft<sup>2</sup>
- Oder: Vertiefungsmodul Theologie<sup>3</sup> (Importmodul)
- Praxismodul I
- Mdikd Jli d
- eenune, ournasmus un PR/Öffentlichkeitsarbeit

### Evangelische Theologie StuPO EvTheol 20150811 i.d.F. 20200916.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20200916.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20200916.md)

**Pflichtmodule (27):**
- Basismodule (Pflichtberei Propädeuticum
- Propäd – Grundlagen des
- Theologiestudiums / Pro-
- pädeuticum
- Fächergruppe AT/NT:Es Punkte) gewählt werden. In
- AT1-A – Basismodul
- Altes Testament
- Modulprüfung
- AT1-B – Basismodul
- Alt Ttt
- es esamen
- NT1-A – Basismodul
- Neues Testament
- NT1-B – Basismodul
- N Ttt
- eues esamen
- Fächergruppe ST/KG:Es Punkte) gewählt werden. In
- KG1-A – Basismodul
- Kirchengeschichte<sup>4</sup>
- KG1-B – Basismodul <sup>4</sup>
- Kirchengeschichte
- V Grundzüge der Dogmatik
- ST1-A – Basismodul
- Systematische Theologie
- ST1-B – Basismodul
- Ü Übung
- V/Ü Weitere interdisziplinäre Lehrveranstaltung

### Evangelische Theologie StuPO EvTheol 20150811 i.d.F. 20230314.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20230314.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20230314.md)

**Pflichtmodule (27):**
- Basismodule (Pflichtberei Propädeuticum
- Propäd – Grundlagen des
- Theologiestudiums / Pro-
- pädeuticum
- Fächergruppe AT/NT:Es Punkte) gewählt werden. In
- AT1-A – Basismodul
- Altes Testament
- Modulprüfung
- AT1-B – Basismodul
- Alt Ttt
- es esamen
- weere erveransaung
- NT1-A – Basismodul
- Neues Testament
- NT1-B – Basismodul
- N Ttmnt
- eues esae Fächergruppe ST/KG:Es Punkte) gewählt werden. In
- KG1-A – Basismodul
- Kirchengeschichte<sup>4</sup>
- KG1-B – Basismodul <sup>4</sup>
- Kirchengeschichte
- V Grundzüge der Dogmatik
- ST1-A – Basismodul
- Systematische Theologie
- ST1-B – Basismodul
- Ü Übung
- S/Ü Interdisziplinäre Veranstaltung

### Evangelische Theologie StuPO EvTheol 20200916 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20200916-aes.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20200916-aes.md)

**Pflichtmodule (26):**
- Basismodule (Pflichtberei Propädeuticum
- Propäd – Grundlagen des
- Theologiestudiums / Pro-
- pädeuticum
- Fächergruppe AT/NT:Es Punkte) gewählt werden. In
- AT1-A – Basismodul
- Altes Testament
- Modulprüfung
- AT1-B – Basismodul
- PS Einführung in die exegetischen Methoden AT
- tes estament
- V/Ü weitere Lehrveranstaltung
- NT1-A – Basismodul
- Neues Testament
- NT1-B – Basismodul
- V/Ü weitere Lehrveranstaltun
- Fächergruppe ST/KG:Es Punkte) gewählt werden. In
- KG1-A – Basismodul
- Kirchengeschichte<sup>4</sup>
- KG1-B – Basismodul Kircheneschichte<sup>4</sup>
- PSEinführungindieMethodender KG
- V Grundzüge der Dogmatik
- ST1-A – Basismodul
- Systematische Theologie
- ST1-B–Basismodul
- V/Ü Weitere interdisziplinäre Lehrveranstaltung

### PDF vom 05.10.2007

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/fachstuo-pro-religion.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/fachstuo-pro-religion.md)

**Pflichtmodule (6):**
- Klausur oder mündliche Prüfung
- Mündlicher Vortrag und Prüfung oder schriftliche Hausarbeit (3LP)
- Studienleistung (Regelmäßige Teilnahme, abgeprüft durch Pro- tokolle/Referate)
- Referat und mündliche Prüfung
- Pflicht
- Pflicht (Wenn keine Arbeit, dann 2Übungen)

### MA Christliche Medienkommunikation FPO C-M-K 20150611 i.d.F. 20180711.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20150611-idf-20180711.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20150611-idf-20180711.md)

**Pflichtmodule (2):**
- Masterarbeit
- Kolloquium zur Masterarbeit

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20180711.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20180711.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20180711.md)

**Pflichtmodule (40):**
- Grundlagen der Kommunikations- wissenschaftII
- Vertiefung Kommunikationswissensc
- Vertiefun der Kommunikations-
- VL oder SEM Einführung in das Mediensystem
- ste Vertiefung der Kommunikations-
- e wissenschaftII
- . Sem Medienwissenschaft Dii d Mdil d
- vgl. FPO M.A. TheaterMedien
- sueen
- Medienethik
- Mediensysteme/Journalismus
- SEM Mediensysteme
- Mediensysteme, Journalismus und Öffentlichkeitsarbeit
- SEMÖffentlichkeitsarbeit (Theorie undPraxis)
- SEM Medienrecht
- Praxismodul
- SEM PraxisfeldMedien I
- Praxisfeld Medien
- SEM PraxisfeldMedien III
- ter Schwerpunktbereich(Wahl en
- SEMGrundzügeTheologiefür Nicht-Theologen
- em Theologische Grundlagen
- .S (Christentum und Medien)<sup>3</sup>
- VLoderSEM Theologische Grundlagen III
- Vertiefung Theologie (Christentum und Medien)<sup>3</sup>
- Grundlagen Kommunikation
- Grundlagen der KommunikationswissenschaftI
- Grundlagen der Kommunikationswissenschaft II
- Vertiefung Kommunikationsw
- Vertiefung der
- KommunikationswissenschaftI
- Vertiefung der Kommunikationswissenschaft II
- Medienwissenschaft
- Dimensionen des Medialen und Visuellen
- Medienkunde/Journalismus
- SEM Medienssteme
- Mediensysteme, Journalismus d Öfflihkibi
- un entcetsaret
- SEM Praxisfeld Medien I
- SEM Praxisfeld Medien III

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20191212.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20191212.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20191212.md)

**Pflichtmodule (34):**
- Grundlagen der Kommunikations- wissenschaftI
- Grundlagen der Kommunikations- wissenschaftII
- Vertiefung Kommunikationswissensc Vtif d Kikti
- r ereung er ommunaons- wissenschaftI
- este Vertiefung der Kommunikations-
- wissenschaftII
- . Sem Medienwissenschaft
- vgl. FPO M.A. TheaterMedien<sup>2</sup>
- Medienethik
- Mediensysteme/Journalismus
- SEM Mediensysteme
- Mediensysteme, Journalismus und Öffentlichkeitsarbeit
- SEMÖffentlichkeitsarbeit (Theorie undPraxis)
- SEM Medienrecht
- Praxismodul
- SEM PraxisfeldMedien I
- Praxisfeld Medien
- SEM PraxisfeldMedien III
- Grundlagen Kommunikations
- Grundlagen der KommunikationswissenschaftI
- Grundlagen der Kommunikationswissenschaft II
- Vertiefung Kommunikations
- Vertiefung der KommunikationswissenschaftI
- Vertiefung der
- Kommunikationswissenschaft II
- Medienwissenschaft
- Dimensionen des Medialen und Visuellen
- Medienkunde/Journalismus
- Mediensysteme, Journalismus Ö
- und ffentlichkeitsarbeit
- SEM Praxisfeld Medien I
- SEM Praxisfeld Medien III
- Masterarbeit
- Kolloquium zur Masterarbeit

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20200909.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20200909.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20200909.md)

**Pflichtmodule (25):**
- Grundlagen der Kommunikatio
- Grundlagen der Kommunikations-
- wissenschaft
- Grundzüge der Theologie(Es is
- Grundzüge der Theologie für Nicht-
- Theologen (ChristentumundMedien)
- Grundzüge der Theologie für Nicht- Theologen
- (IslamundMedien)
- Medienethik
- Mediensysteme/Journalismus(
- SEM Mediensysteme
- Mediensysteme, Journalismus und Öfftlihkitbit
- encesare
- SEM Medienrecht
- Praxismodul
- SEM PraxisfeldMedien I
- Praxisfeld Medien
- SEM PraxisfeldMedien III
- Masterarbeit
- Kolloquium zur Masterarbeit
- Grundlagen der Kommunikations- wissenschaft
- Grundzüge der Theologie(Es i
- Mediensysteme/Journalismus
- Mediensysteme, Journalismus und Öffntlihkitrbit
- ecesae

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20230731.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20230731.md)

**Pflichtmodule (24):**
- Grundlagen der Kommunikatio
- Grundlagen der Kommunikations-
- wissenschaft
- Grundzüge der Theologie(Es is
- Grundzüge der Theologie für Nicht-
- Theologen (Christentum und Medien)
- Grundzüge der Theologie für Nicht- Theologen
- (Islam und Medien)
- Medienethik
- Mediensysteme/Journalismus
- SEM Mediensysteme
- Mediensysteme, Journalismus und Öfflihkibi
- entcetsaret
- SEM Medienrecht
- Praxismodul
- SEM Praxisfeld Medien I
- Praxisfeld Medien
- SEM Praxisfeld Medien III
- Masterarbeit
- Kolloquium zur Masterarbeit
- Grundlagen der Kommunikations- wissenschaft
- Grundzüge der Theologie(Es i Grundzüge der Theologie für Nicht-
- Mediensysteme, Journalismus und Öfftlihkitbit
- encesare

### MA Medien-Ethik-Religion FPO M-E-R 20180711 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20180711-aes.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20180711-aes.md)

**Pflichtmodule (40):**
- Grundlagen der Kommunikations- wissenschaftI
- Grundlagen der Kommunikations- wissenschaftII
- Vertiefung Kommunikationswissensc Vif d Kiki
- r erteung er ommunatons- wissenschaftI
- este Vertiefung der Kommunikations-
- Sem wissenschaftII Medienwissenschaft
- vgl. FPO M.A. TheaterMedien
- Visuellen
- Medienethik
- Mediensysteme/Journalismus
- SEM Mediensysteme
- Mediensysteme, Journalismus und Ö
- ffentlichkeitsarbeit
- SEM Medienrecht
- Praxismodul
- SEM PraxisfeldMedien I
- er Praxisfeld Medien
- SEM PraxisfeldMedien III
- eme Schwerpunktbereich(Wahl ent
- SEMGrundzügeTheologiefür Nicht-Theologen
- VLoderSEM Theologische Grundlagen I
- (Christentum und Medien)<sup>3</sup>
- VLoderSEM Theologische Grundlagen III
- Vertiefung Theologie (ChristentumundMedien)<sup>3</sup>
- Grundlagen Kommunikation
- Grundlagen der KommunikationswissenschaftI
- Grundlagen der Kommunikationswissenschaft II
- Vertiefung Kommunikations
- Vertiefung der
- KommunikationswissenschaftI
- Vertiefung der Kommunikationswissenschaft II
- Medienwissenschaft
- Dimensionen des Medialen und Visuellen
- Medienkunde/Journalismus
- SEM Mdintm
- Mediensysteme, Journalismus d Öfflihkibi
- un entcetsaret
- SEM Praxisfeld Medien I
- Praxisfeld Medien
- SEM Praxisfeld Medien III

### MA Medien-Ethik-Religion FPO M-E-R 20200909 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20200909-aes.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20200909-aes.md)

**Pflichtmodule (21):**
- Grundlagen der Kommunikatio
- Grundlagen der Kommunikations- wissenschaft
- Grundzüge der Theologie(Es is
- Grundzüge der Theologie für Nicht-
- Theologen (ChristentumundMedien)
- Grundzüge der Theologie für Nicht- Theologen
- Il dMdi
- (samun een)
- Medienethik
- Mediensysteme/Journalismus(
- SEM Mediensysteme
- Mediensysteme, Journalismus und Öfftlihkitbit
- encesare
- SEM Medienrecht
- Praxismodul
- SEM PraxisfeldMedien I
- Praxisfeld Medien
- SEM PraxisfeldMedien III
- Masterarbeit
- Kolloquium zur Masterarbeit
- (IslamundMedien)

### MA Medien-Ethik-Religion FPO M-E-R 20240904.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20240904.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20240904.md)

**Pflichtmodule (1):**
- r beiden Module z

### PDF vom 09.12.2008

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-20ma-medien-ethik-relig.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-20ma-medien-ethik-relig.md)

**Pflichtmodule (8):**
- Grundlagen der Kommunikations- wissenschaft (Import)
- Medienethik und
- Medienrecht
- Theorie und Praxis des Journalismus
- Theorie und Praxis des Radiojour- nalismus
- Theorie und Praxis des Fernseh- journalismus
- Öffentlichkeitsarbeit und Präsentation
- Praxismodul

### PDF vom 11.06.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-christliche-medienkommunikation.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-christliche-medienkommunikation.md)

**Pflichtmodule (2):**
- Masterarbeit
- Kolloquium zur Masterarbeit Summe

### PDF vom 09.12.2008 i.d.F. 05.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-aug2015.md)

**Pflichtmodule (3):**
- Masterarbeit
- (Christentum und Medien)
- (Islam und Medien)

### PDF vom 09.12.2008 i.d.F. 07.12.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-dez2010.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-dez2010.md)

**Pflichtmodule (8):**
- Grundlagen der Kommunikationswis- senschaft
- SEM Methoden empirische Kom- munikationsforschung
- Oder:Vertiefung Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach)
- VL Einführung Ethik
- Medienethik
- Medienkunde und Journalistik
- SEM Medienkunde elektronische Medien incl. Medienrecht SEM Grundfragen der Journalistik und Einführung in die journalisti- schen Darstellungsformen
- Praxismodul I

### PDF vom 09.12.2008 i.d.F. 08.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-juli2014.md)

**Pflichtmodule (28):**
- Grundlagen der Kommunikations- oder Medienwissen- schaft
- (Importmodul)
- _Oder_: Vertiefung der Kommunikations- oder Medienwissen- schaft (je nach bisherigem Studienfach<sup>1</sup>)
- ~~(~~ ~~d l)~~ Medienethik
- SEM Grundzüge der Medienethik
- SEM Medienkunde
- Medienkunde, Journalismus und
- PR/Öffentlichkeitsarbeit
- SEM Medienökonomie und Medienrecht
- Praxismodul I
- SEM Printjournalismus<sup>2</sup>
- SEM Buch und Verlag²
- Vertiefung Medienkunde und Journalismus (Theorie und Praxis)
- SEM Onlinejournalismus²
- SEM Fernsehjournalismus²
- Grundlagen der Kommunikations-
- oder Medienwissenschaft (Importmodul)
- Oder: Vertiefung der Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach<sup>1</sup>)
- Medienethik
- SEMGrundzüge der Medienethik
- SEM Grundzüge Theologie für Nicht- Theologen
- VL oder SEM Einführung Altes Testa- ment<sup>2</sup>
- VL oder SEM Einführung Neues Testa- ment<sup>2</sup>
- Einführung theologische und religi- onswissenschaft-liche Grundlagen
- VL oder SEM EinführungSystematik<sup>~~2~~</sup>
- VL oder SEM Einführung Praktische Theologie<sup>2</sup>
- VL oder SEM Einführung Religionswis- senschaft<sup>2</sup>
- Oder: Vertiefungsmodul Theologie<sup>3</sup> (Importmodul)

### PDF vom 09.12.2008 i.d.F. 13.11.2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-nov2013.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-nov2013.md)

**Pflichtmodule (8):**
- Grundlagen der Kommunikations‐
- oder Medienwissenschaft (Importmodul)
- _Oder_: Vertiefung der Kommunikations‐ oder Medienwissenschaft (je nach bisherigem Studienfach<sup>1</sup>) (Importmodul)
- Medienethik
- SEM Grundzüge der Medienethik
- SEM Medienkunde
- Medienkunde, Journalismus und PR/Öffentlichkeitsarbeit
- SEM Grundlagen der PR‐Theorie und

### PDF vom 09.12.2008 i.d.F. 24.11.2009

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/proma-medienethikrelig.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/proma-medienethikrelig.md)

**Pflichtmodule (9):**
- Grundlagen der Kommunikations-
- wissenschaft
- Medienkunde elektronische Medien
- Oder:Vertiefung Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach)
- Mdithik d Mdiht
- eene un eenrec
- Theorie und Praxis des Printjourna- lismus (Grundkurs)
- Theorie und Praxis des Journalis- mus
- Praxismodul I

### PDF vom 11.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/stpo-evangelische-theologie-neu.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/stpo-evangelische-theologie-neu.md)

**Pflichtmodule (20):**
- Grundlagen des Theolo-
- giestudiums / Propädeuti-
- PS Einführung in die exegetischen Methoden AT
- Altes Testament
- Modulprüfung
- PS Einführung in die exegetischen Methoden NT
- Neues Testament
- V/Ü weitere Lehrveranstaltung
- Kirchengeschichte
- VGrundzüge der Dogmatik
- PS Einführung in die Methoden der Systemati- schen Theologie
- Systematische Theologie
- V Praktische Theologie
- PS Homiletik / Liturgik / Poimenik / Publizistik
- Basismodul Praktische Theologie
- Theoriebegleitetes Prakti-
- S Interdisziplinäres Seminar (2 SWS)
- Interdisziplinäres Basismodul
- V Religionswissenschaft im Überblick
- Religionswissenschaft

### PDF vom 27. Juli 2012

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/stuo-magister-20theologiae.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/stuo-magister-20theologiae.md)

**Pflichtmodule (26):**
- Grundlagen des Theologie-
- studiums/ Propädeuticum
- Das Biblicum ist i Das Modul ist nur
- Altes Testa- ment
- V/Ü weitere Lehrveranstaltung (2 SWS)
- Proseminararbeit oder Modulprü-
- fung
- Veranstaltung
- Neues Testa- ment
- Kirchen- geschichte
- PS Einführung in die Methoden der KG (2 SWS)
- Proseminararbeit oder Modulprü- fung
- Basismodul Systematische Theologie
- Ü Übung zur Vorlesung „Grund- züge der Dogmatik“(2SWS)
- Basismodul Praktische
- Theologie
- PS Religions- u Gemeindepäda- gogik/Diakonik/ Gemeindeaufbau/Pastoral- theologie (2SWS)
- schriftliche Ausarbeitung zu einem
- der Proseminare
- Basismodul Gemeinde- praktikum
- Inter- disziplinäres
- Seminararbeit oder Prüfung zum interdisziplinären Seminar
- V/S/Ü Weitere interdisziplinäre Lehrveranstaltung (2 SWS)
- Prüfung zur Lehrveranstaltung
- Basismodul Religions- wissenschaft
- Proseminararbeit oder mündliche Modulprüfung

### PDF vom 25.09.1980 i.d.F. 28.12.2004

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/zwischenpruefungso.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/zwischenpruefungso.md)

**Pflichtmodule (13):**
- Basismodul 1: Sprachwissen- schaft
- Basismodul 2: Literaturwissen- schaft
- Basismodul 3: Sprachpraktische Grundlagen
- Basismodul 4:
- Sprachproduktion
- Basismodul 5: Landeskunde
- Basismodul 1 _Linguistik_
- Basismodul 2 _Literatur- und_
- _Kulturwissenschaft_
- Literaturwiss.
- oder
- Kulturwissenschaft
- Dauer der schriftlichen Prüfung

### 11. August 2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/2aes-20wtb-ma-20multimediadidaktik.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/2aes-20wtb-ma-20multimediadidaktik.md)

**Pflichtmodule (3):**
- Hausaufgabe, Referat (einschl. Präsentation) Hausaufgabe Referat (einschl. Präsentation)
- Referat (einschl. Präsentation)
- mündl. Prüfung

### MA EdT 20190828.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/ma-edt-20190828.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/ma-edt-20190828.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA EdT 20240926.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/ma-edt-20240926.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/ma-edt-20240926.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 07.03.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-organisationpersonalentw-weiterbld-ma.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-organisationpersonalentw-weiterbld-ma.md)

**Pflichtmodule (24):**
- Grundlagen der Organisations- und
- Personalentwicklung
- Teambuilding
- Qualifikationsplanung und Personal-
- entwicklung
- Grundlagen Organisation
- Einführung in die Konzepte der Organisations- entwicklung
- Konzepte der Organisationsentwicklung
- Konzepte der Organisationsentwicklung in der Praxis
- Change Management
- Umsetzung von Organisationsentwick-
- lungsprozessen
- Moderation und Präsentation
- Grundlage Personal
- Kompetenzmessung
- Methoden und Instrumente der Personalentwicklung
- Neue Lernformen im Betrieb
- Personalmanagement
- Personalmanagement und Arbeitsrecht
- Arbeitsrecht
- Management und Führung
- Instrumente der Mitarbeiterführung
- Bildungsmanagement
- Betriebliches Bildungsmanagement

### PDF vom 25.09.1980 i.d.F. 28.12.2004

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/zwischenpruefungso.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/zwischenpruefungso.md)

**Pflichtmodule (13):**
- Basismodul 1: Sprachwissen- schaft
- Basismodul 2: Literaturwissen- schaft
- Basismodul 3: Sprachpraktische Grundlagen
- Basismodul 4:
- Sprachproduktion
- Basismodul 5: Landeskunde
- Basismodul 1 _Linguistik_
- Basismodul 2 _Literatur- und_
- _Kulturwissenschaft_
- Literaturwiss.
- oder
- Kulturwissenschaft
- Dauer der schriftlichen Prüfung

### 28. Februar 2008

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/1aesa-kunstgesch.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/1aesa-kunstgesch.md)

**Pflichtmodule (1):**
- Protokoll oder mündlicher Vortrag und Hausarbeit

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20140718 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20180730.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20180730.md)

**Pflichtmodule (3):**
- Bachelorarbeit und –prüfung
- Oberseminar
- Bachelorarbeit<sup>5</sup>

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20140718 i.d.F. 20190220.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20190220.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20190220.md)

**Pflichtmodule (3):**
- Bachelorarbeit und -prüfung
- Bachelorarbeit<sup>5</sup>
- Bachelorarbeit

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20180730 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20180730-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20180730-aes.md)

**Pflichtmodule (3):**
- Bachelorarbeit und -prüfung
- Oberseminar
- Bachelorarbeit<sup>5</sup>

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20190220 ÄS zu 2ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20190220-aes-zu-2aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20190220-aes-zu-2aes.md)

**Pflichtmodule (17):**
- Basismodule: Kulturentwicklun Prähistorische Archäologie – Ä
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäoloie:
- Übung zur prähistorischen Klikl E
- Prähistorische Archäologie – J
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Übung zur prähistorischen
- Klassische Archäologie – Griec
- Klassische Archäologie: Griechische Archäologie I A
- Klassische Archäologie:
- Griechische Archäologie I B
- Kulturgeschichte
- Klassische Archäologie – Römi
- Klassische Archäologie: Römische Archäologie I A
- Italisch-römische Archäologie I B
- Christliche Archäologie – Kultu
- Christliche Archäologie: Kulturgeschichte I A

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20240430.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20240430.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20240430.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach (Ar
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Buchwissenschaft FPO B.A. BuWi 20181207 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-buchwissenschaft-fpo-b-a-buwi-20181207-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-buchwissenschaft-fpo-b-a-buwi-20181207-aes.md)

**Pflichtmodule (1):**
- Bachelorarbeit<sup>3</sup>

### 2-Fach-BA Computerlinguistik FPO CompLing 20071005 i.d.F. 20220411.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-computerlinguistik-fpo-compling-20071005-idf-20220411.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-computerlinguistik-fpo-compling-20071005-idf-20220411.md)

**Pflichtmodule (13):**
- PO INF
- nes der drei Module im Um
- ale Geistes- und senschaften
- ngAmS Zwei-Fach
- anistik Zwei-Fach
- esamt 12,5 ECTS-Punkten
- Bachelorarbeit im Erstfach (Computerlinguistik)
- Bachelorarbeit Bachelorarbeit
- ach-Bachelorstudium:
- S Zwei-Fach
- Grundlagen der Germanistischen Linguistik 1 (LingBM 1)
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2 Fach BA Digitale Geistes- und Sozialwissenschaften 20180829 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-digitale-geistes-und-sozialwissenschaften-20180829-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-digitale-geistes-und-sozialwissenschaften-20180829-aes.md)

**Pflichtmodule (2):**
- Bachelorarbeit<sup>3</sup>
- Bachelorarbeit

### 2-Fach-BA English and American Studies 20071004 i.d.F. 20200124.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20071004-idf-20200124.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20071004-idf-20200124.md)

**Pflichtmodule (5):**
- § 4a)
- Bachelorarbeit<sup>10</sup>
- Zwei-Fach-Bachelorstudium:
- tfachs
- i-Fach-B

### 2-Fach-BA English and American Studies 20200124 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20200124-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20200124-aes.md)

**Pflichtmodule (4):**
- Bachelorarbeit<sup>10</sup>
- wei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfa
- Bachelorarbeit

### 2-Fach-BA FPO BA SKAND 20071004 i.d.F. 20190520.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20190520.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20190520.md)

**Pflichtmodule (14):**
- Basismodule: Es müssen alle Ba
- Literaturwissenschaft 1
- Literaturwissenschaft 2
- Literaturwissenschaft 3
- Nordische Kulturgeschichte 1
- Nordische Kulturgeschichte 2
- Nordische Erstsprache 1
- Nordische Erstsprache 2
- Sprachanalyse
- Bachelorarbeit (nur im Erstfach):
- Abhldl Bhlbi
- scussmou aceoraret
- Bachelorarbeit
- SWS<sup>7</sup>und ECTS-Punkte:

### 2-Fach-BA FPO BA SKAND 20071004 i.d.F. 20211201.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20211201.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20211201.md)

**Pflichtmodule (3):**
- im Zwei-Fach-Ba
- tfachs
- i-Fach-Ba

### 2-Fach-BA Frankoromanistik 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-20210624-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-20210624-aes.md)

**Pflichtmodule (4):**
- Bachelorarbeit
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- eraurwssensca ule imUmfang von insgesamt 25 ECTS

### 2-Fach-BA Frankoromanistik FPO BA Frankorom 20071004 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-fpo-ba-frankorom-20071004-idf-20210624.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-fpo-ba-frankorom-20071004-idf-20210624.md)

**Pflichtmodule (5):**
- Bachelorarbeit im Erstfach (Fr
- Bachelorarbeit
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische
- Literaturwissenschaft 2.Studienphase: Es sind Mod

### 2-Fach-BA Germanistik FPO BA Germ 20071004 i.d.F. 20220914.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-ba-germ-20071004-idf-20220914.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-ba-germ-20071004-idf-20220914.md)

**Pflichtmodule (8):**
- Bachelorarbeit im Erstfach (Germa Abschlussmodule<sup>5</sup>
- Ling Finit
- Abschlussmodul Bachelorarbeit
- Linguistik
- NdL Finit Abschlussmodul Bachelorarbeit
- Neuere deutsche Literaturwissen- schaft
- Grundlagen der Neueren
- deutschen Literaturwissenschaft 2

### 2-Fach-BA Germanistik FPO Germanistik Zwei-Fach 20190708 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-germanistik-zwei-fach-20190708-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-germanistik-zwei-fach-20190708-aes.md)

**Pflichtmodule (18):**
- Grundlagen der Germanistischen Linguistik 2(LingBM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft2(NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1(MedBM 1)
- Grundlagen der Germanistischen Mediävistik 2(MedBM 2)
- Bachelorarbeit im Erstfach (Germa Abschlussmodule
- Abschlussmodul Bachelorarbeit
- Linguistik (Ling Finit)
- Abschlussmodul Bachelorarbeit Neuere deutsche Literaturwissen-
- schaft(NdL Finit)
- Abschlussmodul Bachelorarbeit Mediävistik(MedFinit)
- Bachelorarbeit
- Basismodule Grundlagen der Germanistischen Linguistik 1(LingBM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen
- Mediävistik 2(MedBM 2)
- Bachelorarbeit im Erstfach (German
- ECTS-Punkte im Zwei-Fach-Bachelorstudium:

### 2-Fach-BA Germanistik FPO Germanistik Zwei-Fach 20220914 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-germanistik-zwei-fach-20220914-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-germanistik-zwei-fach-20220914-aes.md)

**Pflichtmodule (11):**
- Bachelorarbeit im Erstfach (Germ Abschlussmodule<sup>5</sup>
- Ling Finit Abschlussmodul Bachelorarbeit
- Linguistik
- NdL Finit Abschlussmodul Bachelorarbeit
- Neuere deutsche Literaturwissen- schaft
- Med Finit Abschlussmodul Bachelorarbeit
- Mediävistik
- TS-Punkte im Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach
- Bachelorarbeit
- im Zwei-Fach-Bachelorstudium:

### 2-Fach-BA Iberoromanistik 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-20210624-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-20210624-aes.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### 2-Fach-BA Iberoromanistik FPO BA Iberorom 20071004 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-fpo-ba-iberorom-20071004-idf-20210624.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-fpo-ba-iberorom-20071004-idf-20210624.md)

**Pflichtmodule (6):**
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Spanische Sprachpraxis 3<sup>2</sup>
- Gramática y estilísticaI
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-B

### 2-Fach-BA  Islamisch Religiöse Studien BA IRS Zwei-Fach 20140718 i.d.F. 20200909.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-islamisch-religioese-studien-ba-irs-zwei-fach-20140718-idf-20200909.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-islamisch-religioese-studien-ba-irs-zwei-fach-20140718-idf-20200909.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach
- Bachelorarbeit
- mme ECTS-Punkte im Zwei-F

### 2-Fach-BA Islamisch-Religiöse Studien BA IRS Zwei-Fach 20200909 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-islamisch-religioese-studien-ba-irs-zwei-fach-20200909-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-islamisch-religioese-studien-ba-irs-zwei-fach-20200909-aes.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach
- Bachelorarbeit
- umme ECTS-Punkte im Zwei-F

### 2-Fach-BA Italoromanistik 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-italoromanistik-20210624-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-italoromanistik-20210624-aes.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfac
- Bachelorarbeit
- stfachs
- Fach-Bachelorstudium:

### 2-Fach-BA Italoromanistik FPO BA Italorom 20071004 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-italoromanistik-fpo-ba-italorom-20071004-idf-20210624.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-italoromanistik-fpo-ba-italorom-20071004-idf-20210624.md)

**Pflichtmodule (12):**
- Basismodul Italienische
- Sprachpraxis 1
- Corso di italiano intermedio II
- Basismodul Italienische Sprachpraxis 2<sup>2</sup>
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Liihf
- teraturwssenscat
- Bachelorarbeit im Erstfac
- Bachelorarbeit
- stfachs
- Fach-Bachel

### 2-Fach-BA Japanologie FPO BA Japanologie 20071004 i.d.F. 20210729.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20071004-idf-20210729.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20071004-idf-20210729.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach(
- Bachelorarbeit
- ECTS-Punkte im Zwei-Fach-Bachelorstudium
- Bachelorarbeit im Erstfach

### 2-Fach-BA Japanologie FPO BA-Japanologie 20210729 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20210729-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20210729-aes.md)

**Pflichtmodule (5):**
- Bachelorarbeit im Erstfach(
- Bachelorarbeit
- ECTS-Punkte im Zwei-Fa
- Bachelorarbeit im Erstfach
- ECTS-Punkte im Zwei-Fach-Bachelorstudium

### 2-Fach-BA Japanologie FPO BA Japanologie 20230615.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20230615.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20230615.md)

**Pflichtmodule (22):**
- Propädeutikum
- BA-BM2 Theorien und Methoden
- BA-JK3 Japanisch 3<sup>3</sup>
- BA-JK4 Japanisch 4<sup>4</sup>
- Medien in Japan
- BA-AM1 Medien und Kultur
- BA-AM2 Politik und
- Gesellschaft
- BA-JK5 Jnih 5<sup>5</sup>
- apasc
- BA-AM3 Aktuelle
- Japanforschung
- BA-AM4 Fachliteratur
- Mentorat
- Summ Zweitfach (Kombinationsmögli
- Module des Zweitfachs
- Bachelorarbeit im Erstfach (Ja
- Forschungswerkstatt
- Bachelorarbeit
- me ECTS-Punkte im Zwei-Fac
- Erstfachs
- ach-Bachelorstudium

### 2-Fach-BA Kulturgeographie FPO Kulturgeo Zwei-Fach 20071005 i.d.F. 20200827.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20071005-idf-20200827.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20071005-idf-20200827.md)

**Pflichtmodule (25):**
- Grundlagen der KG I
- GZB 2: Grundlagen der KG II
- GZB 3: Seminar KG mit Geländetag
- GZB 4: Grundlagen der PG I
- GZB 5: Grundlagen der PG II
- GZB 6: Seminar PG mit Geländetag
- GZB 7: Kartographie und Geoinformation
- GZB 8: Qualitative und Quantitative Methoden
- GZB 9: Geländepraktikum
- GZB 10:
- Seminar EmpirischeSozialforschung
- Methoden der Geographie
- GZB 11:
- KG vertieft
- GZB 12: Spezielle Themenfelder der KG und
- der Regionalen Geographie I
- GZB 13: Spezielle Themenfelder der KG und
- der Regionalen Geographie II
- Zweitfach gemäß Kombinationsmögl
- Module des Zweitfachs<sup>2</sup>
- Bachelorarbeit im Erstfach
- GZB 14: Bachelorarbeit
- Summ
- Bachelorarbeit
- ECTS-Punkte im Zwei-Fach-Bachelorstudium:

### 2-Fach-BA Kulturgeographie FPO Kulturgeo Zwei-Fach 20071005 i.d.F. 20221011.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20071005-idf-20221011.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20071005-idf-20221011.md)

**Pflichtmodule (5):**
- Bachelorarbeit im Erstfach
- GZB 14: Bachelorarbeit
- nkte im Zwei-Fach-Bachelorstudium:
- Bachelorarbeit
- kte im Zwei-Fach-Bachelorstudium:

### 2-Fach-BA Kulturgeographie FPO Kulturgeo Zwei-Fach 20200827 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20200827-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20200827-aes.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach
- Bachelorarbeit
- SummeECT

### 2-Fach-BA Kulturgeographie FPO Kulturgeo Zwei-Fach 20221011 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20221011-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20221011-aes.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach
- GZB 14: Bachelorarbeit
- nkte im Zwei-Fach-Bachelorstudium:
- Bachelorarbeit

### 2-Fach-BA Kulturgeographie FPO Kulturgeo  Zwei-Fach 20230928.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20230928.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20230928.md)

**Pflichtmodule (5):**
- Bachelorarbeit im Erstfach
- GZB 14: Bachelorarbeit
- nkte im Zwei-Fach-Bachelorstudium:
- Bachelorarbeit
- kte im Zwei-Fach-Bachelorstudium:

### 2-Fach-BA Kunstgeschichte FPO BA KuGe 20071005 i.d.F. 20200813.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20071005-idf-20200813.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20071005-idf-20200813.md)

**Pflichtmodule (14):**
- Grundlagen der Graphischen Künste
- Grundlagen der angewandten Künste
- Grundlagen der Denkmalpflege
- Digitales Lernen und Lehren
- Berufsorientierung Kunstgeschichte
- Kunstgeschichte Italiens I
- Kunstgeschichte Italiens II
- Bachelorarbeit im Erstfach (Kunstgeschichte)
- Bhlbit
- aceorare
- Bachelorarbeit
- SummeECTS-Punkteim
- Bachelorarbeit im Erstfach
- SummeECTS-Punkteim Zw

### 2-Fach-BA Kunstgeschichte FPO BA KuGe 20071005 i.d.F. 20230323.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20071005-idf-20230323.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20071005-idf-20230323.md)

**Pflichtmodule (9):**
- Grundlagen der Graphischen Künste
- Grundlagen der angewandten Künste
- Grundlagen der Denkmalpflege
- Digitales Lernen und Lehren
- Bachelorarbeit im Erstfach(Kunstgeschicht
- Bachelorarbeit
- Bachelorarbeit im Erstfach
- Bachelorarbeit vgl. FPO des
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:

### 2-Fach-BA Kunstgeschichte FPO BA KuGe 20200813 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20200813-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20200813-aes.md)

**Pflichtmodule (13):**
- Grundlagen der Graphischen Künste
- Grundlagen der angewandten Künste
- Grundlagen der Denkmalpflege
- Digitales Lernen und Lehren
- Berufsorientierung Kunstgeschichte
- Kunstgeschichte Italiens I
- Kunstgeschichte Italiens II
- Bachelorarbeit im Erstfach (Kunstgeschichte)
- Kolloquium
- Bachelorarbeit
- SummeECTS-Punkteim
- Bachelorarbeit im Erstfach
- SummeECTS-Punkteim Zw

### 2-Fach-BA Kunstgeschichte FPO BA KuGe 20230323 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20230323-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20230323-aes.md)

**Pflichtmodule (9):**
- Grundlagen der Graphischen Künste
- Grundlagen der angewandten Künste
- Grundlagen der Denkmalpflege
- Digitales Lernen und Lehren
- Bachelorarbeit im Erstfach(Kunstgeschichte
- Kolloquium
- Bachelorarbeit
- Bachelorarbeit im Erstfach
- ach-Bachelorstudium:

### 2-Fach-BA Lateinische Philologie 20071004 i.d.F. 20180928.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-lateinische-philologie-20071004-idf-20180928.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-lateinische-philologie-20071004-idf-20180928.md)

**Pflichtmodule (5):**
- Basismodul 2: Einführungindielateinische Schrift
- Einführung in die Indogermanistik<sup>9</sup>
- Einführung in das Germanische<sup>10</sup>
- Bachelorarbeit<sup>8</sup>
- (10) Bachelorarbeit

### 2 Fach-BA Lateinische Philologie 20180928 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-lateinische-philologie-20180928-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-lateinische-philologie-20180928-aes.md)

**Pflichtmodule (4):**
- eulatein
- tik und
- Bachelorarbeit<sup>8</sup>
- Bachelorarbeit

### 2-Fach-BA Linguistische Informatik FPO LingInf 20220411 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-linguistische-informatik-fpo-linginf-20220411-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-linguistische-informatik-fpo-linginf-20220411-aes.md)

**Pflichtmodule (12):**
- PO INF
- fang von in
- ale Geistes- und senschaften
- ngAmS Zwei-Fach
- anistik Zwei-Fach
- Bachelorarbeit im Erstfach (Computerlinguistik)
- Bachelorarbeit Bachelorarbeit
- Fach-Bachelorstudium:
- Basismodul II: Linguistics (A)
- Grundlagen der Germanistischen Linguistik 1 (LingBM 1)
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA Mittel- und Neulatein FPO Mittellatein Zwei-Fach 20071005 i.d.F. 20190614.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20071005-idf-20190614.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20071005-idf-20190614.md)

**Pflichtmodule (14):**
- Bachelorarbeit im Erstfach (Mittellatein und Neulatein)
- Bachelorarbeit
- achelorstudium:
- Basismodul 2:
- Einführung in die lateinische Schrift
- (Paläographie)
- Basismodul 3A: Das Klassische Erbe A<sup>3</sup> (gemäß§4a)
- Basismodul 3B:
- Das Klassische Erbe B<sup>3</sup>
- Basismodul 4:
- Europäische Mediävistik I (gemäß§4a)
- Basismodul 5: Europäische Mediävistik II
- (gemäß§4a)
- (10) Bachelorarbeit vgl. FPO des Erstfachs

### 2-Fach-BA Mittel-und Neulatein FPO Mittellatein Zwei-Fach 20190614 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20190614-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20190614-aes.md)

**Pflichtmodule (13):**
- Basismodul 2:
- Einführung in die lateinische Schrift
- (Paläographie)
- Basismodul 3B:
- Das Klassische Erbe B<sup>2</sup>
- Basismodul 5: Europäische Mediävistik II
- Bachelorarbeit im Erstfach (Mittell
- Bachelorarbeit
- CTS-Punkte im Zwei-Fach-Bachelorstudium:
- Das Klassische Erbe B<sup>3</sup>
- ereungsmoue Vertiefungsmodul 1: Mittellateinische Philologie
- Bachelorarbeit im Erstfach (Mitte
- ECTS-Punkte im Zwei-Fach-Bachelorstudium: 180

### 2-Fach-BA Mittel- und Neulatein FPO Mittellatein Zwei-Fach 20240430.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20240430.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20240430.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach (Mittellatein und Neulatein)
- Bachelorarbeit 10
- Bachelorarbeit vgl. FPO des Erstfach

### 2-Fach-BA Ökonomie FPO Ökon Zwei-Fach 20071005 i.d.F. 20190916.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20071005-idf-20190916.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20071005-idf-20190916.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach(Ökonomie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Ökonomie FPO Ökon Zwei-Fach 20071005 i.d.F. 20200923.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20071005-idf-20200923.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20071005-idf-20200923.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach(Ökonomie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Ökonomie FPO Ökon Zwei-Fach 20071005 i.d.F. 20210225.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20071005-idf-20210225.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20071005-idf-20210225.md)

**Pflichtmodule (10):**
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Wirtschaftsprivatrecht
- Vertiefung Wirtschaftswissenschaften I
- Vertiefung Wirtschaftswissenschaften II
- Vertiefung Wirtschaftswissenschaften III
- fang)und ECTS-Punkte im Erstfach: mäß Anlage 3 der ABMStPO/Phil)
- Module des Zweitfachs<sup>3</sup>
- Bachelorarbeit im Erstfach (Ökonomie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Ökonomie FPO Ökon Zwei-Fach 20190916 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20190916-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20190916-aes.md)

**Pflichtmodule (5):**
- Bachelorarbeit im Erstfach (Ökonomie)
- Bachelorarbeit
- Summ
- Bachelorarbeit im Erstfach
- mme ECTS-Punkte im Zwei-Fach-Bachelorstudium:

### 2-Fach-BA Orientalistik FPO Orient 20071005 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-orientalistik-fpo-orient-20071005-idf-20180730.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-orientalistik-fpo-orient-20071005-idf-20180730.md)

**Pflichtmodule (1):**
- Bachelorarbeit<sup>2</sup>

### 2-Fach-BA Orientalistik FPO Orient 20071005 i.d.F. 20210225.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-orientalistik-fpo-orient-20071005-idf-20210225.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-orientalistik-fpo-orient-20071005-idf-20210225.md)

**Pflichtmodule (3):**
- rstfach(Orientalistik)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Orientalistik FPO Orient 20210225 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-orientalistik-fpo-orient-20210225-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-orientalistik-fpo-orient-20210225-aes.md)

**Pflichtmodule (3):**
- rstfach(Orientalistik)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Pädagogik 20210225 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-paedagogik-20210225-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-paedagogik-20210225-aes.md)

**Pflichtmodule (13):**
- Grundlagen der Pädagogik
- Pädagogische Forschung I
- Pädagogische Institutionen und Handlungsfelder
- Pädagogische Arbeitsfelder
- Einführung in pädagogische
- Bereiche
- Pkik
- ratum
- Pädih Fh II<sup>4)</sup>
- agogsce orscung
- Bachelorarbeit im Erstfach
- Bachelorarbeit
- SummeECTS-Punk

### 2-Fach-BA Pädagogik FPO Päd-Zwei-Fach 20071005 i.d.F. 20210225.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-paedagogik-fpo-paed-zwei-fach-20071005-idf-20210225.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-paedagogik-fpo-paed-zwei-fach-20071005-idf-20210225.md)

**Pflichtmodule (13):**
- Grundlagen der Pädagogik
- Pädagogische Forschung I
- Seminar 2
- Pädagogische Institutionen und Handlungsfelder 2
- Pädagogische Arbeitsfelder
- Einführung in pädagogische
- Bereiche
- Pktik
- raum
- Pädagogische Forschung II<sup>4)</sup>
- Bachelorarbeit im Erstfach
- Bachelorarbeit
- SummeECTS-Punk

### 2-Fach-BA Philosophie FPO B.A. Philosophie 20210122 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-philosophie-fpo-b-a-philosophie-20210122-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-philosophie-fpo-b-a-philosophie-20210122-aes.md)

**Pflichtmodule (17):**
- Grundkurs Praktische Philosophie
- Grundkurs Theoretische Philosophie
- Historisch-systematische Einführung (Proseminar)
- Philosophie
- Praktische Philosophie
- Historische-systematische Einführung (Proseminar)
- Theoretische Philosophie
- Philosohieeschichte<sup>3</sup>
- Philhi ttih<sup>4</sup>
- osope sysemasc
- Bachelorarbeit im Erstfach (Phil
- Bachelorarbeit
- <sup>4</sup>
- Philosophiegeschichte
- <sup>5</sup>
- Philosophie systematisch
- Bachelorarbeit im Erstfach

### 2-Fach BA Philosophie FPO B.A. Philosophie Zwei-Fach 20071005 i.d.F. 20210122.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-philosophie-fpo-b-a-philosophie-zwei-fach-20071005-idf-20210122.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-philosophie-fpo-b-a-philosophie-zwei-fach-20071005-idf-20210122.md)

**Pflichtmodule (12):**
- Grundkurs Praktische Philosophie
- Grundkurs Theoretische Philosophie
- Historisch-systematische Einführung (Proseminar)
- Philosophie
- Praktische Philosophie
- Historische-systematische Einführung (Proseminar)
- Theoretische Philosophie
- Philosohieeschichte<sup>3</sup>
- Philosohie sstematisch<sup>4</sup>
- Bachelorarbeit im Erstfach (P
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Politikwissenschaft 20071005 i.d.F. 20210122.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-20071005-idf-20210122.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-20071005-idf-20210122.md)

**Pflichtmodule (12):**
- Bachelorarbeit im Erstfach (Politikwissenscha
- Bachelorarbeit
- Politische Systeme I
- Politische Systeme II
- Außereuroäische Reionen I
- Außereuropäische Regionen II
- Internationale Beziehungen I
- Internationale Beziehungen II
- Politische Theorie & Ideeneschichte I
- Politische Theorie & Ideengeschichte II
- Bachelorarbeit im Erstfach
- mme ECTS-Punkte im Z

### 2-Fach-BA Politikwissenschaft 20260305.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-20260305.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-20260305.md)

**Pflichtmodule (9):**
- Grundlagen des Politischen Denkens
- Einführung in die Methoden der
- Politikwissenschaft
- Politische Systeme I
- Politische Systeme II
- Internationale Beziehungen I
- Internationale Beziehungen II
- Politische Theorie & Ideengeschichte I
- Politische Theorie & Ideengeschichte II

### 2-Fach-BA Politikwissenschaft FPO B.A. Politik 20210122 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-fpo-b-a-politik-20210122-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-fpo-b-a-politik-20210122-aes.md)

**Pflichtmodule (12):**
- Politische Systeme I
- Politische Systeme II
- uereuropsce egonen
- Außereuropäische Regionen II
- Internationale Beziehunen I
- Internationale Beziehungen II
- Politische Theorie & Ideengeschichte I
- Politische Theorie & Ideengeschichte II
- Bachelorarbeit im Erstfach (Politikwissenscha
- Bachelorarbeit
- Bachelorarbeit im Erstfach
- mme ECTS-Punkte im Z

### 2-Fach-BA Skandinavistik FPO BA SKAND 20190520 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-skandinavistik-fpo-ba-skand-20190520-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-skandinavistik-fpo-ba-skand-20190520-aes.md)

**Pflichtmodule (6):**
- Bachelorarbeit (nur im Erstfach):
- Übung 1
- Abhldl Bhlbi
- scussmou aceoraret
- Bachelorarbeit
- me SWS<sup>7</sup>und ECTS-Punkte: 0 mind. 34

### 2-Fach-BA Skandinavistik FPO BA SKAND 20211201 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-skandinavistik-fpo-ba-skand-20211201-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-skandinavistik-fpo-ba-skand-20211201-aes.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach (Ska
- Abschlussmodul Bachelorarbeit
- des Ers
- ei-Fach-B

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20071005 i.d.F. 20190806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20190806.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20190806.md)

**Pflichtmodule (14):**
- Pflichtbereich Einführung
- (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Einführung in die sozio- logische Methodenlehre
- (SozM-E)
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Qualifikationsprofil I
- (SozQ-I), vgl. § 5
- Qualifikationsprofil II
- (SozQ-II), vgl. § 5
- Bachelorarbeit

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20071005 i.d.F. 20200818.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20200818.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20200818.md)

**Pflichtmodule (2):**
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20190806 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20190806-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20190806-aes.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- umme ECTS-Punkte im Zwei

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20200818 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20200818-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20200818-aes.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- me ECTS-Punkte im Zwe

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20230822.md)

**Pflichtmodule (13):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Einführung in die sozio- logische Methodenlehre (SozM-E)
- Statistische Analyseverfahren I
- (SozS-I)
- Statistische Analyseverfahren II
- (SozS-II)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Qualifikationsprofil II (SozQ-II), vgl. § 5
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Theater- und Medienwissenschaft FPO B.A. Theatermedien 20071004 i.d.F. 20190815.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20071004-idf-20190815.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20071004-idf-20190815.md)

**Pflichtmodule (13):**
- Basisseminar Theo/Histo
- Medienwissenschaft
- Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Technik
- Bachelorarbeit im Erstfac
- Bachelorarbeit
- Forschungsfragen 2
- wei-Fach-Bachelorstudium:
- Thik
- Zwei-Fach-Bachelorstudium:

### 2-Fach-BA Theater- und Medienwissenschaft FPO B.A. Theatermedien 20071004 i.d.F. 20220512.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20071004-idf-20220512.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20071004-idf-20220512.md)

**Pflichtmodule (12):**
- Bachelorarbeit im Erstfac
- Bachelorarbeit
- Forschungsfragen 2
- Zwei-Fach-Bachelorstu-
- Basisseminar Theo/Histo
- Medienwissenschaft
- Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Technik
- Bachelorarbeit im Erstfa

### 2-Fach-BA Theater- und Medienwissenschaft FPO B.A. Theatermedien 20190815 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20190815-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20190815-aes.md)

**Pflichtmodule (11):**
- Bachelorarbeit im Erstfa
- Bachelorarbeit
- Forschungsfragen 2
- Zwei-Fach-Bachelorstudium:
- Basisseminar Theo/Histo
- Medienwissenschaft
- Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Theorien der Praxis
- raxs

### 17. Februar 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2aes-2fachba-oeffentlichesrecht.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2aes-2fachba-oeffentlichesrecht.md)

**Pflichtmodule (13):**
- Grundlagen-modul
- Staats-
- organisationsrecht
- Grundrechte
- Allgemeine
- Grundlagen des Verwaltungsrechts
- Europa- und
- Völkerrecht I
- Polizeirecht
- Verwaltungs-recht I
- Völkerecht II
- Verwaltungs-recht
- Umweltrecht I Summe:

### 2Fach Geschichte 20071004 i.d.F. 20180911.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fach-geschichte-20071004-idf-20180911.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fach-geschichte-20071004-idf-20180911.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- umme SWS und ECTS-Punkte:

### 2Fach Geschichte 20180911 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fach-geschichte-20180911-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fach-geschichte-20180911-aes.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 18.07.2014 i.d.F. 11.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fachba-archaeologischewissenschaften-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fachba-archaeologischewissenschaften-aug2015.md)

**Pflichtmodule (1):**
- Bachelorarbeit<sup>6)</sup>

### PDF vom 18.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fachba-archaeologischewissenschaften.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fachba-archaeologischewissenschaften.md)

**Pflichtmodule (1):**
- Bachelorarbeit<sup>6)</sup>

### 4. März 2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/3aesa-2fachba-20mittneulatein.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/3aesa-2fachba-20mittneulatein.md)

**Pflichtmodule (4):**
- Benotete Hausarbeit (mind. 12 Seiten)
- Studienleistung: Schriftlicher Kurzbericht
- Studienleistung: Klausur (90 Min.)
- Bachelorarbeit

### 5. August 2011

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/5aes-2fachba-20geschichte.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/5aes-2fachba-20geschichte.md)

**Pflichtmodule (8):**
- (10) Basismodul I
- (5) Überblicksvorlesung
- (5) Proseminar
- (10) Basismodul II
- (20) Grundlagen- und Orientierungsprüfung
- (5) Modul Methodische Grundlagen
- Praxisübung I: Quellen und Hilfswissen- schaften
- Praxisübung II: Quellen,

### 7. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/5aes-2fachba-japanologie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/5aes-2fachba-japanologie.md)

**Pflichtmodule (15):**
- V/Ü Geschichte/Kultur
- Japanologie 1
- Grundlagen Japanologie 2
- Sprachkurs
- Japanisch 3
- Japanisch 4
- Grundlaen
- g Japanologie 3<sup>1</sup>
- Grundlagen Japanologie 4<sup>1</sup>
- V/Ü Literatur/Film
- Japanische Literatur
- und Film
- Japanisch 5
- V/ÜTheater
- apansces Theater<sup>1</sup>

### 11. August 2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/5aes-englischamerican.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/5aes-englischamerican.md)

**Pflichtmodule (4):**
- (101) Basismodul I Language
- (102) Basismodul II Linguistics
- (103) Basismodul III Literature
- (104) Basismodul IV Culture

### 25. Juli 2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-griechphilologie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-griechphilologie.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### 9. Mai 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-indogermindoiran.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-indogermindoiran.md)

**Pflichtmodule (5):**
- EinführungindieIndogermanistik
- Einführungindas Germanische
- SanskritI
- SanskritII
- Bachelorarbeit

### 22. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-linguistische-informatik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-linguistische-informatik.md)

**Pflichtmodule (14):**
- Grundlagen der Computerlinguistik I
- Arbeitstechniken
- Grundlagen der Informatik (Importmodul)
- Grundlagen der Computerlinguistik II
- ÜbungCL 2
- Grundseminar Programmierung
- Programmerung
- Vtifdl Ctliitik
- ereungsmou ompuerngus I
- Konzeptionelle Modellierung (Importmodul)
- ereungsmou ompuerngus II
- Korpuslinguistik
- Übung Statistik
- Bachelorarbeit*

### 15. Juli 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-theater-und-medien.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-theater-und-medien.md)

**Pflichtmodule (9):**
- Basisseminar Theo/Histo
- Medienwissenschaft
- Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Theorien der Praxis
- Bachelorarbeit
- (fakultativ)

### 11. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fach-ba-linginformatik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fach-ba-linginformatik.md)

**Pflichtmodule (11):**
- Grundlagen der Computerlinguistik I
- Arbeitstechniken
- Grundlagen der Informatik (Importmodul)
- VorlesungCL 2
- Computerlinguistik II
- Programmierung I
- Programmierung II
- Proseminar Computerlinguistik
- Werkzeuge und Infrastrukturen
- Konzeptionelle Modellierung (Importmodul)
- Bachelorarbeit<sup>2)</sup>

### 25. Juli 2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fachba-englishamericanstudies.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fachba-englishamericanstudies.md)

**Pflichtmodule (12):**
- (2) Basismodul I L Grundseminar
- (2) anguage Aufbauseminar
- (2) Basismodul II Grundseminar
- (2) Linguistics Aufbauseminar
- (1) Basisvorlesung
- (2) Basismodul III Litt Grundseminar
- (2) eraure Aufbauseminar
- (2) Basismodul IV Cl Grundseminar mit Projektarbeit
- (2) uture Aufbauseminar
- erden, bei der W
- SWS Gesamt ECTS‐Punktepro Sem
- Bachelorarbeit

### 7. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fachba-germanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fachba-germanistik.md)

**Pflichtmodule (6):**
- Einführunskurs: Einführun in die
- Germanistischen Linguistik (Ling1)
- Alternative für ausländische Studierende: Grundlagen der Germanistischen Linguistik (DaF) (Ling1a)
- Grundlagen der Germanistischen Mediävistik (Med 1)
- Grundlagen der Neueren deutschen Literatur
- (NdL 1)

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aesa-2fachba-nordphilologie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aesa-2fachba-nordphilologie.md)

**Pflichtmodule (4):**
- Bachelorarbeit (nur im Erstfach): 10
- Ahll Bhli
- bscussmodu aceorarbet
- Bachelorarbeit

### 10. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-iberoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-iberoromanistik.md)

**Pflichtmodule (2):**
- Basismodul Einführung in die
- Iberoromanistik

### 10. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-italoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-italoromanistik.md)

**Pflichtmodule (8):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I
- Corso di italiano intermedio II
- Basismodul Italienische Sprachpraxis 2
- Tecniche di lettura
- Basisseminar ItalienischeSprachwissenschaft
- Basismodul Einführung in die Italoromanistik
- Phonetik und Phonologie des Italienischen

### 2. Juni 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-philosophie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-philosophie.md)

**Pflichtmodule (12):**
- Grundkurs PraktischePhilosophie
- Grundkurs Theoretische Philosophie
- Historisch-systematische Ein- führung (Proseminar)
- Philosophie
- Praktische Philosophie
- Historische-systematische Einführung (Proseminar)
- Theoretische Philosophie
- Philosophiegeschichte<sup>2</sup>
- Philosophie systematisch<sup>3</sup>
- Vifl
- erteungsmodue Vertiefungsmodul
- Bachelorarbeit

### 3. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fachba-mittelneulatein.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fachba-mittelneulatein.md)

**Pflichtmodule (13):**
- Basismodul 1:
- Einführung in die Sprache und Literatur des lateinischen
- Europas
- Basismodul 2:
- Einführung in die lateinische
- Schrift (Paläographie)
- Basismodul 3A: Das Klassische Erbe A<sup>2</sup>
- Basismodul 3B:
- Das Klassische Erbe B<sup>2</sup>
- Basismodul 4: Europäische Mediävistik I
- Basismodul 5: Europäische Mediävistik
- Mittellateinische Philologie
- Bachelorarbeit

### 12. Juni 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aesa-2fba-sinologie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aesa-2fba-sinologie.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### 22. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aes-2fachba-soziologie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aes-2fachba-soziologie.md)

**Pflichtmodule (11):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Statistische
- Analyseverfahren I (SozS-I)
- Analyseverfahren II (SozS-II)
- Qualifikationsprofil I
- (SozQ-I)
- Qualifikationsprofil II (SozQ-II)

### 28. Juli 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-frankoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-frankoromanistik.md)

**Pflichtmodule (7):**
- Basismodul Französische Sprachpraxis 1
- Introduction à la civilisation
- Basismodul Französische Sprachpraxis 2
- Phonétique pratique, orthophonie et intonation
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Bachelorarbeit

### 28. Juli 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-iberoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-iberoromanistik.md)

**Pflichtmodule (6):**
- Basismodul Spanische Sprachpraxis 1
- Español intermedio II
- Basismodul Spanische Sprachpraxis 2
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Bachelorarbeit

### 28. Juli 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-italoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-italoromanistik.md)

**Pflichtmodule (7):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I
- Corso di italiano intermedio II
- Basismodul Italienische Sprachpraxis 2
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft

### PDF vom 05.10.2007

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20buchwiss.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20buchwiss.md)

**Pflichtmodule (3):**
- cht): B
- Typografische Grundlagen
- Bachelorarbeit

### PDF vom 04.10.2007

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20frankorom.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20frankorom.md)

**Pflichtmodule (5):**
- Einführung in die romanistische Sprachwissenschaft
- Einführung in die romanistische Literaturwissenschaft
- Proseminar
- Expression écrite I
- Mittelseminar

### PDF vom 04.10.2007

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20germanist.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20germanist.md)

**Pflichtmodule (7):**
- Basismodul: Grundlagen der Germanistischen Lingu- istik
- Grundkurs: Einführung in die Germanistische Linguistik
- Proseminar: Angewandte Sprachwissenschaft
- Für ausländische Studie- rende
- Basismodul: Grundlagen der Germanistischen Lingu- istik (DaF)
- Basismodul: Grundlagen der Germanistischen Mediä- vistik
- Grundkurs: Einführungindie

### PDF vom 04.10.2007

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20geschichte.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20geschichte.md)

**Pflichtmodule (2):**
- Grundlagen- und Orientierungs- prüfung
- Modul II) Vertiefungsmodul Alte und Mittelalterliche Geschichte: a) Vorlesung Alte oder Mittelal- terliche Geschichte b) Proseminar Alte Geschichte

### PDF vom 05.10.2007 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-ba-kunstgesch-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-ba-kunstgesch-aug2017.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-englstudies-feb2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-englstudies-feb2014.md)

**Pflichtmodule (12):**
- (2) Basismodul I L Grundseminar
- (2) anguage Aufbauseminar
- (2) Basismodul II Grundseminar
- (2) Linguistics Aufbauseminar
- (1) Basisvorlesung
- (2) Basismodul III Literature Grundseminar
- (2) Aufbauseminar
- (2) Basismodul IV Cl Grundseminar mit Projektarbeit
- (2) uture Aufbauseminar
- erden, bei der W
- SWS Gesamt ECTS‐Punktepro Sem
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 25.07.2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-englstudies-juli2013.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-englstudies-juli2013.md)

**Pflichtmodule (12):**
- (2) Basismodul I L Grundseminar
- (2) anguage Aufbauseminar
- (2) Basismodul II Grundseminar
- (2) Linguistics Aufbauseminar
- (1) Basisvorlesung
- (2) Basismodul III Literature Grundseminar
- (2) Aufbauseminar
- (2) Basismodul IV Cl Grundseminar mit Projektarbeit
- (2) uture Aufbauseminar
- erden, bei der W
- SWS Gesamt ECTS‐Punktepro Sem
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 08.03.2011

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-englstudies-maerz2011.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-englstudies-maerz2011.md)

**Pflichtmodule (4):**
- (101) Basismodul I Language
- (102) Basismodul II Linguistics
- (103) Basismodul III Literature
- (104) Basismodul IV Culture

### PDF vom 04.10.2007 i.d.F. 11.08.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-englstudies.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-englstudies.md)

**Pflichtmodule (4):**
- (101) Basismodul I Language
- (102) Basismodul II Linguistics
- (103) Basismodul III Literature
- (104) Basismodul IV Culture

### PDF vom 04.10.2007 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-fbo-b-a-theatermedienaug2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-fbo-b-a-theatermedienaug2017.md)

**Pflichtmodule (9):**
- Basisseminar Theo/Histo
- Medienwissenschaft
- Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Theoriender Praxis
- Bachelorarbeit
- fragen (fakultativ)

### PDF vom 04.10.2007 i.d.F. 10.06.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankorom-10juni2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankorom-10juni2014.md)

**Pflichtmodule (8):**
- Basismodul Französische Sprachpraxis 1
- Communication orale
- Vocabulaire, idiomatique et civilisation II
- Basismodul Französische Sprachpraxis 2
- Phonétique pratique, orthophonie et intonation
- Bidl Eifüh i di Fkitik
- assmou nrung n e ranoromans
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F: 28.07.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankoromjuli2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankoromjuli2017.md)

**Pflichtmodule (8):**
- Basismodul Französische Srachraxis 1
- Communication orale
- Introduction à la civilisation
- Basismodul Französische Sprachpraxis 2
- Phonétique pratique, orthophonie et intonation
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 05.08.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-aug2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-aug2016.md)

**Pflichtmodule (8):**
- Grundlagen der Germanistischen Linguistik 1 Li BM 1
- (ng )
- Grundlagen der Germanistischen Linguistik
- Analyseseminar 2
- Grundlagen der Neueren deutschen Literaturwissenschaft 1(NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft2(NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1(Med BM 1)
- Grundlagen der Germanistischen Mediävistik 2(MedBM 2)

### PDF vom 04.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-februar2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-februar2014.md)

**Pflichtmodule (8):**
- Basismodul: Grundlagen der Germanistischen Linguistik
- Einführungskurs: Einführung in die GermanistischeLinguistik
- Für ausländische Studierende
- Basismodul: Grundlagen der Germanistischen Linguistik (DaF)
- Basismodul: Grundlagen der Germanistischen Mediävistik
- Einführungskurs: Einführung in die GermanistischeMediävistik
- Basismodul: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die Neuere deutsche Literatur- wissenschaft

### PDF vom 04.10.2007 i.d.F. 08.03.2011

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-maerz2011.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-maerz2011.md)

**Pflichtmodule (8):**
- Basismodul: Grundlagen der Germanistischen Linguistik
- Einführungskurs: Einführung in die GermanistischeLinguistik
- Für ausländische Studierende
- Basismodul: Grundlagen der Germanistischen Linguistik (DaF)
- Basismodul: Grundlagen der Germanistischen Mediävistik
- Einführungskurs: Einführung in die Germanistische Mediävistik
- Basismodul: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die Neuere deutsche Literatur- wissenschaft

### PDF vom 04.10.2007 i.d.F. 04.05.2012

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-mai2012.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-mai2012.md)

**Pflichtmodule (8):**
- Basismodul: Grundlagen der Germanistischen Linguistik
- Einführungskurs: Einführung in die GermanistischeLinguistik
- Für ausländische Studierende
- Basismodul: Grundlagen der Germanistischen Linguistik (DaF)
- Basismodul: Grundlagen der Germanistischen Mediävistik
- Einführungskurs: Einführung in die Germanistische Mediävistik
- Basismodul: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die Neuere deutsche Literatur- wissenschaft

### PDF vom 04.10.2007 i.d.F. 05.11.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist.md)

**Pflichtmodule (8):**
- Basismodul: Grundlagen der Germanistischen Linguistik
- Einführungskurs: Einführung in die GermanistischeLinguistik
- Für ausländische Studierende
- Basismodul: Grundlagen der Germanistischen Linguistik (DaF)
- Basismodul: Grundlagen der Germanistischen Mediävistik
- Einführungskurs: Einführung in die GermanistischeMediävistik
- Basismodul: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die Neuere deutsche Literatur- wissenschaft

### PDF vom 04.10.2007 i.d.F. 05.08.2011

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-geschichte-august2011.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-geschichte-august2011.md)

**Pflichtmodule (9):**
- (10) Basismodul I
- (5) Überblicksvorlesung
- (5) Proseminar
- (10) Basismodul II
- (20) Grundlagen- und Orientie- rungsprüfung
- (5) Modul Methodische Grund- lagen
- Praxisübung I: Quellen und Hilfswissenschaften
- Praxisübung II: Quellen, Theorie und Methode
- (10) Basismodul III

### PDF vom 04.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-geschichte-februar2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-geschichte-februar2014.md)

**Pflichtmodule (9):**
- (10) Basismodul I
- (5) Überblicksvorlesung
- (5) Proseminar
- (10) Basismodul II
- (20) Grundlagen- und Orientie- rungsprüfung
- (5) Modul Methodische Grund- lagen
- Praxisübung I: Quellen und Hilfswissenschaften
- Praxisübung II: Quellen, Theorie und Methode
- (10) Basismodul III

### PDF vom 04.10.2007 i.d.F. 08.03.2011

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-geschichte-maerz2011.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-geschichte-maerz2011.md)

**Pflichtmodule (8):**
- Grundlagen- und Orientierungsprüfung
- Modul II) Basismodul Alte und Mittelalterliche Geschichte: Vorlesung Alte oder Mittelalterliche Geschichte Proseminar Alte Geschichte Proseminar Mittelalterliche Geschichte
- Modul III) Basismodul Neuere und Neueste Geschichte: Vorlesung Neuere oder Neueste Geschichte Proseminar Neuere Geschichte Proseminar Neueste Geschichte
- (20) Basismodule=Modul II und III
- Mindestgesamtleistung nach 4 Semester
- Modul IV) Aufbaumodul Alte und Mittelalterliche Geschichte:<sup>~~3~~</sup> Vorlesung Alte oder Mittelalterliche Geschichte Hauptseminar Alte oder Mittel- alterliche Geschichte
- Modul V) Aufbaumodul Neuere und Neueste Geschichte:<sup>~~4~~</sup> Vorlesung Neuere oder Neueste Geschichte Hauptseminar Neuere oder Neueste
- Geschichte

### PDF vom 04.10.2007 i.d.F. 05.11.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-geschichte.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-geschichte.md)

**Pflichtmodule (7):**
- Grundlagen- und Orientierungsprüfung
- Modul II) Basismodul Alte und Mittelalterliche Geschichte: Vorlesung Alte oder Mittelalterliche Geschichte Proseminar Alte Geschichte Proseminar Mittelalterliche Geschichte
- Modul III) Basismodul Neuere und Neueste Geschichte: Vorlesung Neuere oder Neueste Geschichte Proseminar Neuere Geschichte Proseminar Neueste Geschichte
- (20) Basismodule=Modul II und III
- Mindestgesamtleistung nach 4 Semester
- Modul IV) Aufbaumodul Alte und Mittelalterli- che Geschichte:<sup>~~3~~</sup> Vorlesung Alte oder Mittelalterliche Geschichte Hauptseminar Alte oder Mittel- alterliche Geschichte
- Modul V) Aufbaumodul Neuere und Neueste Geschichte:<sup>~~4~~</sup> Vorlesung Neuere oder Neueste Geschichte Hauptseminar Neuere oder Neueste Geschichte

### PDF vom 05.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-griechphil-februar2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-griechphil-februar2014.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 25.07.2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-griechphil-juli2013.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-griechphil-juli2013.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 28.07.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-iberoromjuli2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-iberoromjuli2017.md)

**Pflichtmodule (4):**
- Basismodul Spanische Sprachpraxis 2
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 09.05.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-indogerm-indoiran-mai2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-indogerm-indoiran-mai2016.md)

**Pflichtmodule (5):**
- Einführung in die Indoger- manistik
- Einführung in das Germani- sche
- Sanskrit I
- Sanskrit II
- Bachelorarbeit

### PDF vom 22.07.2008 i.d.F. 02.06.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-informatik-juni2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-informatik-juni2016.md)

**Pflichtmodule (18):**
- Grundlagen der Informatik
- Konzeptionelle Modellierung
- Mathematik
- Theoretische Informatik für Wirtschaftsinformatik und
- Thtih Iftik
- eoresce norma
- Grundlagen der Logik in der
- Informatik
- Mathematische Modellbildung
- und Statistik
- Kernmodul 1: Einführung in die Diitl Git d Sil
- gaen eses- un oza- wissenschaften
- Kernmodul 2: Nutzung digitaler
- Daten in den Geistes- und So-
- zialwissenschaften
- Kernmodul 3: Wissenschaft d Gllhft i diitl
- un esesca m gaen Zeitalter
- Praxismodul

### PDF vom 04.10.2007 i.d.F. 10.06.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italorom-10juni2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italorom-10juni2014.md)

**Pflichtmodule (7):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I 2
- Corso di italiano intermedio II 6
- Basismodul Italienische Sprachpraxis 2
- Tecniche di lettura 1
- Basisseminar ItalienischeSprachwissenschaft
- Basismodul Einführung in die Italoromanistik

### PDF vom 04.10.2007 i.d.F. 28.07.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italoromjuli2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italoromjuli2017.md)

**Pflichtmodule (8):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I
- Corso di italiano intermedio II
- Basismodul Italienische Sprachpraxis 2
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 11.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-kultgeo-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-kultgeo-aug2015.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 25.06.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-nordphil-juni2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-nordphil-juni2015.md)

**Pflichtmodule (10):**
- Basismodule:
- Nordistische Linguistik 1<sup>2</sup>
- Nordistische Linguistik 2<sup>2</sup>
- Nordistische Literatur- und Kulturwissenschaft 1<sup>2</sup>
- Nordistische Literatur- und Kulturwissenschaft2<sup>2</sup>
- Altnordisch 1<sup>2</sup>
- Altnordisch 2<sup>2</sup>
- Nordische Erstsprache 1<sup>2</sup>
- Nordische Erstsprache 2<sup>2</sup>
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-nordphilaug2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-nordphilaug2017.md)

**Pflichtmodule (9):**
- Basismodule: Es müssen alle Basis
- Nordistische Literaturwissenschaft 1
- Nordistische Literaturwissenschaft 2
- Nordistische Literaturwissenschaft 3
- Nordische Kulturgeschichte 1
- Nordische Kulturgeschichte 2
- Nordische Erstsprache 1
- Nordische Erstsrache 2
- Seminar Sprachanalyse

### PDF vom 05.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-orient-feb2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-orient-feb2014.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 21.05.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-orient-mai2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-orient-mai2015.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 02.07.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-paed-juli2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-paed-juli2015.md)

**Pflichtmodule (9):**
- Grundlagen der Pädagogik
- Pädagogische Forschung I
- Pädagogische Institutionen undHandlungsfelder 2
- Pädagogische Arbeitsfelder
- Einführung in pädagogische
- Bereiche
- Praxisreflexion
- Pädagogische Forschung II
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 02.06.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-philosophie-juni2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-philosophie-juni2016.md)

**Pflichtmodule (11):**
- Grundkurs PraktischePhilosophie
- Grundkurs TheoretischePhilosophie
- Basismodul Philhi
- osope
- Basismodul Praktische Philosohie
- Textseminar (Mittelseminar)
- Historische-systematische Einführung (Proseminar)
- Theoretische Philosophie
- Philosophiegeschichte<sup>2</sup>
- Philosophie systematisch<sup>3</sup>
- Bachelorarbeit Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 02.06.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-politik-juni2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-politik-juni2016.md)

**Pflichtmodule (9):**
- Politische Systeme I
- Politische Systeme II
- Außereuroäische Reionen I
- Außereuropäische Regionen II
- Internationale Beziehungen I
- Internationale Beziehungen II
- Politische Theorie & Ideeneschichte I
- Politische Theorie & Ideengeschichte II
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 29.07.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-juli2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-juli2016.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 12.06.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-juni2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-juni2017.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 15.07.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-theater-juli2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-theater-juli2016.md)

**Pflichtmodule (8):**
- Basisseminar Theo/Histo
- Medienwissenschaft
- Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Bachelorarbeit
- (fakultativ)

### PDF vom 05.10.2007 i.d.F. 22.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-juli2014.md)

**Pflichtmodule (8):**
- Grundlagen der Computerlinguistik I
- Arbeitstechniken
- Grundlagen der Informatik (Importmodul)
- VorlesungCL 2
- Computerlinguistik II
- Grundseminar Programmierung
- rogrammerung
- Bachelorarbeit*

### FPO 2-Fach BA DGSW 20080722 i.d.F. 20180829.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-2-fach-ba-dgsw-20080722-idf-20180829.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-2-fach-ba-dgsw-20080722-idf-20180829.md)

**Pflichtmodule (11):**
- Grundlagen der Logik in der Informatik<sup>2</sup>
- Mathematische Modell- bildung und Statistik für Naturwissenschaftler
- DH-Modul 1: Schwerpunkt
- Sprache und Text
- DH-Modul 2: Schwerpunkt
- Gesellschaft und Raum
- DH-Modul 3: Schwerpunkt
- Bild und Medien
- Praxis-/Projektmodul
- Bachelorarbeit<sup>3</sup>
- Bachelorarbeit

### FPO BA BuWi 20071005 i.d.F. 20181207.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-buwi-20071005-idf-20181207.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-buwi-20071005-idf-20181207.md)

**Pflichtmodule (1):**
- Bachelorarbeit<sup>3)</sup>

### FPO BA Sino Zwei-Fach 20071005 i.d.F. 20190828.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-20071005-idf-20190828.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-20071005-idf-20190828.md)

**Pflichtmodule (5):**
- Bachelorarbeit im Erstfach (Sinologie)
- Bachelorarbeit
- ach-Bachelorstudium:
- Bachelorarbeit im Erstfach
- umme ECTS-Punkte im Zwei-Fa

### FPO BA Sino Zwei-Fach 20230615.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-20230615.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-20230615.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach (Sinologie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach
- ECTS-Punkte im Studiengang:

### FPO BA Sino Zwei-Fach ÄS 20190828.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-aes-20190828.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-aes-20190828.md)

**Pflichtmodule (3):**
- Bachelorarbeit
- Bachelorarbeit im Erstfach
- umme ECTS-Punkte im Zwei-Fac

### FPO Griechisch Zwei-Fach 20071005 i.d.F. 20200806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20071005-idf-20200806.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20071005-idf-20200806.md)

**Pflichtmodule (5):**
- Bachelorarbeit im Erstfach (Mittellatein und Neulatein)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-B
- Bachelorarbeit im Erstfach
- Bachelorarbeit vgl. FPO des Erstfachs

### FPO Griechisch Zwei-Fach 20200806 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20200806-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20200806-aes.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach (Mittellatein und Neulatein)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach
- Bachelorarbeit im Erstfach

### FPO Griechisch Zwei-Fach 20250131.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20250131.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20250131.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach(Mitt
- Bachelorarbeit
- nkte im Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### Indogermanistik und Indoiranistik Zwei-Fach FPO Indo 20250131.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/indogermanistik-und-indoiranistik-zwei-fach-fpo-indo-20250131.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/indogermanistik-und-indoiranistik-zwei-fach-fpo-indo-20250131.md)

**Pflichtmodule (9):**
- Einführung in die Indogermanistik
- Einführung in das Germanische
- Sanskrit I
- Sanskrit II
- Bachelorarbeit im Erstfach (Indogerma
- Bachelorarbeit
- -Punkte im Zwei-F
- Bachelorarbeit im Erstfach
- TS-Punkte im Zwei

### PO LLM Recht und Informatik PO Rinf 20230502 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/rw/rewi/po-llm-recht-und-informatik-po-rinf-20230502-idf-20230731.md`](../pruefungsordnungen/rw/rewi/po-llm-recht-und-informatik-po-rinf-20230502-idf-20230731.md)

**Pflichtmodule (1):**
- Masterarbeit/Abschlussar- beit

### PO LLM Recht und Informatik PO Rinf 20230502 i.d.F. 20240328.pdf

PO-Quelle: [`pruefungsordnungen/rw/rewi/po-llm-recht-und-informatik-po-rinf-20230502-idf-20240328.md`](../pruefungsordnungen/rw/rewi/po-llm-recht-und-informatik-po-rinf-20230502-idf-20240328.md)

**Pflichtmodule (1):**
- Masterarbeit/Abschlussar- beit

### PO LLM Recht und Informatik PO Rinf 20230502 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/rw/rewi/po-llm-recht-und-informatik-po-rinf-20230502-idf-20240926.md`](../pruefungsordnungen/rw/rewi/po-llm-recht-und-informatik-po-rinf-20230502-idf-20240926.md)

**Pflichtmodule (1):**
- Masterarbeit/Abschlussar- beit

### PO LLM Recht und Informatik PO Rinf 20230502.pdf

PO-Quelle: [`pruefungsordnungen/rw/rewi/po-llm-recht-und-informatik-po-rinf-20230502.md`](../pruefungsordnungen/rw/rewi/po-llm-recht-und-informatik-po-rinf-20230502.md)

**Pflichtmodule (1):**
- Masterarbeit/Abschlussar- beit

### 30. Juli 2010

PO-Quelle: [`pruefungsordnungen/rw/wiso/7aes-ba-20wiwi.md`](../pruefungsordnungen/rw/wiso/7aes-ba-20wiwi.md)

**Pflichtmodule (1):**
- m und

### BA International Business Studies FPO BA IBS 20170810 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-international-business-studies-fpo-ba-ibs-20170810-idf-20180730.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-international-business-studies-fpo-ba-ibs-20170810-idf-20180730.md)

**Pflichtmodule (22):**
- Übersicht/Welt des Unternehmens
- Unternehmensplanspiel
- Unternehmer und Unternehmen
- Methodische Grundlagen
- Buchführung
- IT und E-Business
- Intercultural competence
- Statistik
- Internationale Unternehmen und ihr Geschäft
- Absatz
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- Internationale Unternehmen und ihre
- Makroökonomie
- Mikroökonomie
- Internationale Politik I
- Internationalpolitics II
- Kernbereich des Schwerpunkts IBS
- Internationale Wirtschaft
- Europäisches und internationales Recht
- Sprachen IBS 2
- Internationale Unternehmensführung

### BA International Business Studies FPO BA IBS 20170810 i.d.F. 20190731.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-international-business-studies-fpo-ba-ibs-20170810-idf-20190731.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-international-business-studies-fpo-ba-ibs-20170810-idf-20190731.md)

**Pflichtmodule (22):**
- Übersicht/Welt des Unternehmens
- Unternehmensplanspiel
- Unternehmer und Unternehmen
- Methodische Grundlagen
- Buchführung
- IT und E-Business
- Intercultural competence
- Statistik
- Internationale Unternehmen und ihr Geschäft
- Absatz
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- Internationale Unternehmen und ihre Umwelt
- Makroökonomie
- Mikroökonomie
- Global Governance
- Internationalpolitics II
- Kernbereich des Schwerpunkts IBS
- Internationale Wirtschaft
- Europäisches und internationales Recht
- Sprachen IBS 2
- Internationale Unternehmensführung

### BA Sozialökonomik FPO BA SozÖk 20170810 i.d.F. 20180801.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20180801.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20180801.md)

**Pflichtmodule (17):**
- Pflichtbereich Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissenschaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswisse
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik: Analysis und Lineare Algebra
- Statistik
- BWL/VWL
- Absatz
- Mikroökonomie

### BA Sozialökonomik FPO BA SozÖk 20170810 i.d.F. 20190220.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20190220.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20190220.md)

**Pflichtmodule (28):**
- Pflichtbereich Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissenschaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswisse
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik: Analysis und Lineare Algebra
- Statistik
- BWL/VWL
- Absatz
- Mikroökonomie
- Grundlagen des öffentlichen Rechts und
- desZivilrechts
- Kernbereich des Schwerpunkts Internati
- Europäisches und internationales Recht
- Internationale Kommunikation
- Global governance
- International business relations
- Globalisierung und Internationalisierung
- Sprachen 1.2
- Sprachen 2.1
- Sprachen 2.2

### BA Sozialökonomik FPO BA SozÖk 20170810 i.d.F. 20190806.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20190806.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20190806.md)

**Pflichtmodule (17):**
- Pflichtbereich Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissenschaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswisse
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik: Analysis und Lineare Algebra
- Statistik
- BWL/VWL
- Absatz
- Mikroökonomie

### BA Sozialökonomik FPO BA SozÖk 20170810 i.d.F. 20200902.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20200902.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20200902.md)

**Pflichtmodule (11):**
- Grundlagen des öffentlichen Rechts und dZiilh
- esvrects
- Kernbereich des Schwerpunkts Internati
- Europäisches und internationales Recht
- Internationale Kommunikation
- Global governance
- International business relations
- Globalisierung und Internationalisierung
- Sprachen 1.2
- Sprachen 2.1
- Sprachen 2.2

### BA Sozialökonomik FPO BA SozÖk 20170810 i.d.F. 20220301.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20220301.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20220301.md)

**Pflichtmodule (41):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissenschaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissensc
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik
- Data Science: Datenauswertung
- Data Science: Statistik
- BWL/VWL
- Absatz
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Schlüsselualifikationen
- q Sprachen
- Kernbereich des Schwerpunkts Verhaltenswissen
- Emirische Methoden und Statistik
- Personal und Organisation I
- Digital Technologies & Society
- Sozialpolitische Grundlagen
- Pflichtbereich Sozialökonomische Grundlagen
- Grundzüge der Kommunikationswissen- schaft
- Methodische Grundlagen der Wirtschaftswisse
- Emirische Sozialforschun II
- Grundlagen des öffentlichen Rechts und des Zivilrechts Shlüllifikti
- cssequaaonen
- Sprachen 1.1
- Kernbereich des Schwerpunkts International
- Europäisches und internationales Recht
- Internationale Kommunikation
- Global governance
- International business relations
- Globalisierung und Internationalisierung
- Sprachen 1.2
- Sprachen 2.1
- Sprachen 2.2

### BA Sozialökonomik FPO BA SozÖk 20230822.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20230822.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20230822.md)

**Pflichtmodule (9):**
- Grundlagen des öffentlichen Rechts und
- des Zivilrechts
- Kernbereich des Schwerpunkts Verhalte
- Empirische Methoden und Statistik
- Personal und Organisation I
- VP<sup>5)</sup>
- Digital Technologies & Society
- Sozialpolitische Grundlagen
- haften 2

### BA Sozialökonomik FPO BA SozÖk 20240807.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20240807.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20240807.md)

**Pflichtmodule (2):**
- Grundlagen des öffentlichen Rechts und
- des Zivilrechts

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20190222.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20190222.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20190222.md)

**Pflichtmodule (16):**
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Wirtschaftsprivatrecht
- Kernbereich des Schwerpunkts BWL
- Kostenrechnung und Controlling
- Internationale Unternehmensführung
- Investition und Finanzierung
- Integriertes Management
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Kernbereich des Schwerpunkts WiPäd I
- Grundlagen der Wirtschafts- und Betriebs-
- pädagogik
- Betriebliche Aus- und Weiterbildung
- Präsentations- und Moderationstechniken
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Kernbereich des Schwerpunkts WiPäd II

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20190731.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20190731.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20190731.md)

**Pflichtmodule (15):**
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Wirtschaftsprivatrecht
- Kernbereich des Schwerpunkts BWL
- Kostenrechnung und Controlling
- Internationale Unternehmensführung
- Investition und Finanzierung
- Integriertes Management
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Kernbereich des Schwerpunkts WiPäd I
- Grundlagen der Wirtschafts- und Betriebs-
- pädagogik
- Betriebliche Aus- und Weiterbildung
- Präsentations- und Moderationstechniken
- Betriebspädagogisches Seminar
- Schulpraktische Studien

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20200902.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20200902.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20200902.md)

**Pflichtmodule (22):**
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Wirtschaftsprivatrecht
- Studium Integrale
- Mathematik
- Buchführung und Reporting
- Sprachen
- Kernbereich des Schwerpunkts BWL
- Kostenrechnung und Controlling
- Internationale Unternehmensführung
- Investition und Finanzierung
- Integriertes Management
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Kernbereich des Schwerpunkts VWL
- Internationale Wirtschaft
- Ökonomie des öffentlichen Sektors
- Arbeitsmarktpolitik
- Wettbewerbstheorie und -politik
- Kernbereich des Schwerpunkts WI
- Innovation strategy
- E-Business-Management
- ITMt
- -anagemen

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20210122.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20210122.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20210122.md)

**Pflichtmodule (11):**
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Wirtschaftsprivatrecht
- Studium Integrale
- Mathematik
- Buchführung und Reporting
- Sprachen
- Kernbereich des Schwerpunkts BWL
- Kostenrechnung und Controlling
- Internationale Unternehmensführung
- Investition und Finanzierung
- Integriertes Management

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20210806.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20210806.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20210806.md)

**Pflichtmodule (11):**
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Wirtschaftsprivatrecht
- Studium Integrale
- Mathematik
- Buchführung
- Sprachen
- Kernbereich des Schwerpunkts BWL
- Kostenrechnung und Controlling
- Internationale Unternehmensführung
- Investition und Finanzierung
- Integriertes Management

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20230323.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20230323.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20230323.md)

**Pflichtmodule (1):**
- Grundlagen des öffentlichen Rechts und desZivilrechts

### BA Wirtschaftswissenschaften FPO BA WiWi 20200902 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20200902-aes.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20200902-aes.md)

**Pflichtmodule (30):**
- Pflichtbereich Übersicht/Welt des Unternehmens
- Unternehmensplanspiel
- Unternehmen, Märkte, Volkswirtschaften
- Unternehmer und Unternehmen
- Data Science
- Data Science: Machine Learning und Data
- Driven Business
- Data Science: Datenauswertung
- Data Science: Statistik
- Data Science: Datenmanagement und -analyse
- Data Science: Ökonometrie
- BWL/Unternehmen und ihr Geschäft
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- VWL/Unternehmen und ihr Umfeld
- Makroökonomie
- Data Science: Machine Learning und Data Driven Business
- satz
- Uth d Uth
- nernemer un nernemen
- Methodische Grundlagen der Wirtschaftswiss
- Data Science: Datenauswertun
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Wirtschaftsprivatrecht
- Studium Integrale
- Mathematik
- Buchführung und Reporting
- Kernbereich des Schwerpunkts WiPäd II
- Präsentations- und Moderationstechniken
- Grundlagen der Wirtschafts- und Betriebs-

### BA Wirtschaftswissenschaften FPO BA WiWi 20220727 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20220727-aes.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20220727-aes.md)

**Pflichtmodule (1):**
- Grundlagen des öffentlichen Rechts und desZivilrechts

### BSc International Business Studies FPO BA IBS 20170810 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-international-business-studies-fpo-ba-ibs-20170810-idf-20180730.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-international-business-studies-fpo-ba-ibs-20170810-idf-20180730.md)

**Pflichtmodule (6):**
- Kernbereich des Schwerpunkts IBS
- Internationale Wirtschaft
- Europäisches und internationales
- Recht
- Sprachen IBS 2
- Internationale Unternehmensführung

### BSc International Business Studies FPO BA IBS 20170810 i.d.F. 20190731.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-international-business-studies-fpo-ba-ibs-20170810-idf-20190731.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-international-business-studies-fpo-ba-ibs-20170810-idf-20190731.md)

**Pflichtmodule (22):**
- Pflichtbereich Übersicht/Welt des Unternehmens
- Unternehmensplanspiel
- Unternehmer und Unternehmen
- Methodische Grundlagen
- Buchführung
- IT und E-Business
- Intercultural competence
- Statistik
- Internationale Unternehmen und ihr Ge
- Absatz
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- Internationale Unternehmen und ihre U
- Makroökonomie
- Mikroökonomie
- Global Governance
- Internationalpolitics II
- Kernbereich des Schwerpunkts IBS
- Internationale Wirtschaft
- Europäisches und internationales Recht
- Sprachen IBS 2
- Internationale Unternehmensführung

### BSc Wirtschaftsinformatik FPO BA WInf 20170810 i.d.F. 20180615.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20180615.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20180615.md)

**Pflichtmodule (17):**
- Pflichtbereich Übersicht/Welt des Unternehmens
- Buchführung (GOP)
- Wirtschaftsinformatik
- IT und E-Business für Wirtschaftsinformatik (GOP)
- Mathematik
- Mathematik: Analysis und Lineare Algebra (GOP)
- Mathematik: Finanzmathematik (GOP)
- Informatik
- Algorithmen und Datenstrukturen (GOP)
- Theoretische Informatik für Wirtschaftsinformatik
- Grundlagen der Logik in der Informatik
- Unternehmer und Unternehmen
- Absatz
- Produktion, Logistik, Beschaffung
- Data & knowledge
- Digital business
- Architectures & development

### BSc Wirtschaftsinformatik FPO BA WInf 20170810 i.d.F. 20190815.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20190815.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20190815.md)

**Pflichtmodule (1):**
- vgl.§2a

### BSc Wirtschaftsinformatik FPO BA WInf 20170810 i.d.F. 20200902.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20200902.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20200902.md)

**Pflichtmodule (22):**
- Pflichtbereich Wirtschaftswissenschaften
- Unternehmer und Unternehmen (GOP)
- Absatz
- Produktion, Logistik, Beschaffung
- Pflichtbereich Informatik Alrithmn & Dtntrktrn
- goe aesuue (für Medizintechnik) (AuD-MT-V) (GOP)
- Algorithmen & Datenstrukturen
- (für Medizintechnik) (AuD-MT-UE) (GOP)
- Konzeptionelle Modellierung
- Grundlagen der Logik in der Informatik
- Softwareentwicklung in Großprojekten
- Theoretische Informatik für Wirtschaftsinformatik
- Pflichtbereich Wirtschaftsinformatik
- WIN-Projektwoche
- Business and Information Systems Engineering (GOP)
- Pflichtbereich Methodische Grundlagen
- DS: Datenauswertung
- DS: Statistik
- Bachelorarbeit
- Modul Bachelorarbeit
- arbeit
- mind. 128

### BSc Wirtschaftsinformatik FPO BA WInf 20170810 i.d.F. 20210222.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210222.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210222.md)

**Pflichtmodule (22):**
- Pflichtbereich Wirtschaftswissenschaften
- Unternehmer und Unternehmen (GOP)
- Absatz
- Produktion, Logistik, Beschaffung
- Pflichtbereich Informatik Alrithmn & Dtntrktrn
- goe aesuue (für Medizintechnik) (AuD-MT-V) (GOP)
- Algorithmen & Datenstrukturen
- (für Medizintechnik) (AuD-MT-UE) (GOP)
- Konzeptionelle Modellierung
- Grundlagen der Logik in der Informatik
- Softwareentwicklung in Großprojekten
- Theoretische Informatik für Wirtschaftsinformatik
- Pflichtbereich Wirtschaftsinformatik
- WIN-Projektwoche
- Business and Information Systems Engineering (GOP)
- Pflichtbereich Methodische Grundlagen
- Data Science: Datenauswertung
- Data Science: Statistik
- Bachelorarbeit
- Modul Bachelorarbeit
- arbeit
- mind. 128

### BSc Wirtschaftsinformatik FPO BA WInf 20170810 i.d.F. 20210806.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210806.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210806.md)

**Pflichtmodule (7):**
- Pflichtbereich Methodische Grundlagen
- Data Science: Datenauswertung
- Data Science: Statistik
- Bachelorarbeit
- Modul Bachelorarbeit
- arbeit
- mind. 128

### BSc Wirtschaftsinformatik FPO BA WInf 20200902 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20200902-aes.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20200902-aes.md)

**Pflichtmodule (8):**
- Pflichtbereich Informatik Alih & Dk
- gortmen atenstruturen (für Medizintechnik) (AuD-MT-V) (GOP)
- Algorithmen & Datenstrukturen
- (für Medizintechnik) (AuD-MT-UE) (GOP)
- Konzeptionelle Modellierung
- Grundlagen der Logik in der Informatik
- Softwareentwicklung in Großprojekten
- Theoretische Informatik für Wirtschaftsinformatik

### BSc Wirtschaftsinformatik FPO BA WInf 20230822.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20230822.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20230822.md)

**Pflichtmodule (7):**
- Pflichtbereich Methodische Grundlagen
- Data Science: Datenauswertung
- Data Science: Statistik
- Bachelorarbeit
- Modul Bachelorarbeit
- arbeit
- mind. 128

### BSc Wirtschaftsinformatik FPO BA WInf ÄSa 20250616.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-aesa-20250616.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-aesa-20250616.md)

**Pflichtmodule (3):**
- ft2f
- Bachelorarbeit
- SummeSWS””bzw.ECTS-Punkte

### PDF vom 10.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-wirtschaftsinformatik.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-wirtschaftsinformatik.md)

**Pflichtmodule (18):**
- Pflichtbereich Übersicht/Welt des Unternehmens
- Buchführung (GOP)
- Wirtschaftsinformatik
- IT und E-Business für Wirtschaftsinformatik (GOP)
- Mathematik
- Mathematik: Analysis und Lineare Algebra (GOP)
- Mathematik: Finanzmathematik (GOP)
- Informatik
- Algorithmen und Datenstrukturen (GOP)
- Theoretische Informatik für Wirtschaftsinformatik
- Grundlagen der Logik in der Informatik
- Kbih
- ernerec BWL
- Unternehmer und Unternehmen
- Absatz
- Produktion, Logistik, Beschaffung
- Innovation strategy
- E-Business-Management

### PDF vom 10.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-wiwiaug2017.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-wiwiaug2017.md)

**Pflichtmodule (21):**
- Pflichtbereich Übersicht/Welt des Unternehmens
- Unternehmensplanspiel
- Unternehmen, Märkte, Volkswirtschaften
- Unternehmer und Unternehmen
- Methodische Grundlagen der Wirtschaftswiss
- Buchführung
- IT und E-Business
- Mathematik: Analysis und Lineare Algebra
- Mathematik: Finanzmathematik
- Statistik
- BWL/Unternehmen und ihr Geschäft
- Absatz
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- VWL/Unternehmen und ihr Umfeld
- Makroökonomie
- Mikroökonomie
- Wirtschaft und Staat
- Methodische Grundlagen der Wirtschaftswis
- Uth d Uth
- nernemer un nernemen

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/5aesa-fpowipaed.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/5aesa-fpowipaed.md)

**Pflichtmodule (1):**
- Mindesten

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-fpo-ma-sozialoekonomik.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-fpo-ma-sozialoekonomik.md)

**Pflichtmodule (1):**
- Masterarbeit

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-fpomanagement.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-fpomanagement.md)

**Pflichtmodule (13):**
- Pflichtbereich I
- Business strategy
- Produktions- und Supply Chain Ma- nagement
- Personalmanage- ment
- Finanzielle Grund- lagen des Manage- ments
- Technology and innovation ma- nagement
- Pflichtbereich II
- Angewandte Ma- nagementmetho- den
- Fallstudien und Projekte im Ma- nagement
- Teamfähigkeit, Präsentations- und Verhandlungstech- niken
- Fortgeschrittene Methoden der Managementfor- schung
- Masterarbeit
- umme SWS und ECTS 12 5 8 Mindestens 25 SWS

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-fpomscaup.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-fpomscaup.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Mas- terarbeit 2 Summe SWS und ECTS 25 14 34 mind. 73

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-ma-fpo-iis.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-ma-fpo-iis.md)

**Pflichtmodule (1):**
- Masterarbeit

### 10. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/7aesa-ma-fpoeco.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/7aesa-ma-fpoeco.md)

**Pflichtmodule (1):**
- Masterarbeit

### 10. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/8aesa-ma-fpofact.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/8aesa-ma-fpofact.md)

**Pflichtmodule (8):**
- Controlling of business systems
- Kapitalmarktorien- tierte Unterneh- mensbesteuerung
- Versicherungs- und Risikotheorie
- Steuerliche Ge- winnermittlung
- Unternehmenssteu- errecht
- Konzernrechnungs- legung
- Masterarbeit
- SWS (mind.) und ECTS

### PDF vom 17.07.2009

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuo-pro-20ma-arbmarktpers.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuo-pro-20ma-arbmarktpers.md)

**Pflichtmodule (1):**
- ca. 6

### PDF vom 20.07.2009 i.d.F. 10.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-economicsaug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-economicsaug2017.md)

**Pflichtmodule (2):**
- (2) Masterarbeit Masterarbeit Seminar zur Masterarbeit
- mind. 11 mind. 5 Mind. 60 SWS

### PDF vom 08.07.2010 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-iis-aug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-iis-aug2017.md)

**Pflichtmodule (2):**
- Masterarbeit (30 ECTS)
- Masterarbeit

### PDF vom 17.07.2009 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpo-ma-arb-marktpersonalaug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpo-ma-arb-marktpersonalaug2017.md)

**Pflichtmodule (1):**
- Masterarbeit Masterarbeit Seminar zur Masterarbeit Summe SWS undECTS 25

### PDF vom 24.07.2009 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpo-ma-management-aug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpo-ma-management-aug2017.md)

**Pflichtmodule (12):**
- Pflichtbereich I
- Business strategy
- Produktions- und Supply Chain Management
- Personalmanagement
- Finanzielle Grundlagen des Managements
- Technology and innovation management
- Pflichtbereich II
- Angewandte Managementmethoden
- Fallstudien und Projekte im Management
- Teamfähigkeit, Präsentations- und Verhandlungstechniken
- Fortgeschrittene Methoden der Managementforschung
- Masterarbeit

### PDF vom 01.12.2009 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpo-ma-wipaed-aug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpo-ma-wipaed-aug2017.md)

**Pflichtmodule (1):**
- (20) Masterarbeit

### FPOAuP 20090717 i.d.F. 20191203.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20191203.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20191203.md)

**Pflichtmodule (1):**
- Masterarbeit Masterarbeit Seminar zur Masterarbeit 2 Summe SWS undECTS 25 14 34 mind. 73

### FPOAuP 20090717 i.d.F. 20200221.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200221.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200221.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOAuP 20090717 i.d.F. 20200731.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200731.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200731.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit 2

### FPOAuP 20090717 i.d.F. 20210726.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20210726.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20210726.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit Summe SWS undECTS 25

### FPOAuP 20090717 i.d.F. 20250227.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20250227.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20250227.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit Summe SWS und ECTS 25

### FPOECO 20090720 i.d.F. 20210311.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20210311.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20210311.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

### FPOECO 20090720 i.d.F. 20220328.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20220328.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20220328.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

### FPOECO 20250320.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20250320.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20250320.md)

**Pflichtmodule (1):**
- mind. 11 mind.5 mind. 60 SWS

### FPOManagement 20090724 i.d.F. 20190205.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20190205.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20190205.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOManagement 20090724 i.d.F. 20191203.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20191203.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20191203.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOMiGG 20150515 i.d.F. 20191120.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomigg-20150515-idf-20191120.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomigg-20150515-idf-20191120.md)

**Pflichtmodule (8):**
- Kostenträger I
- Ambulantes Management I
- Krankenhausmanagement I
- Pharmamanagement I
- Gesundheitsökonomie I
- Medizin
- Gesundheitsökonomische Evaluationen I
- Masterarbeit

### FPOMiGG 20240229.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomigg-20240229.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomigg-20240229.md)

**Pflichtmodule (8):**
- Kostenträger I
- Ambulantes Management I
- Krankenhausmanagement I
- Pharmamanagement I
- Gesundheitsökonomie I
- Medizin
- Gesundheitsökonomische Evaluationen I
- Masterarbeit

### FPOMiGG 20250227 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomigg-20250227-aes.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomigg-20250227-aes.md)

**Pflichtmodule (8):**
- Kostenträger I
- Ambulantes Management I
- Krankenhausmanagement I
- Pharmamanagement I
- Gesundheitsökonomie I
- Medizin
- Gesundheitsökonomische Evaluationen I
- Masterarbeit

### FPOSozialökonomik 20090902 i.d.F. 20191203.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20090902-idf-20191203.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20090902-idf-20191203.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOSozialökonomik 20090902 i.d.F. 20220727.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20090902-idf-20220727.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20090902-idf-20220727.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOSozialökonomik 20240807.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20240807.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20240807.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Finance Auditing Controlling Taxation 20090720 i.d.F. 20180829.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/ma-finance-auditing-controlling-taxation-20090720-idf-20180829.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/ma-finance-auditing-controlling-taxation-20090720-idf-20180829.md)

**Pflichtmodule (7):**
- Controlling of business systems
- Kapitalmarktorientierte Unternehmens- steuerung
- Versicherungs- und Risikotheorie
- Steuerliche Gewinnermittlung
- Unternehmenssteuerrecht
- Konzernrechnungslegung
- Masterarbeit

### MSc Finance Auditing Controlling Taxation FPOFACT 20090720 i.d.F. 20191120.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20090720-idf-20191120.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20090720-idf-20191120.md)

**Pflichtmodule (7):**
- Masterarbeit
- Controlling of business systems
- Kapitalmarktorientierte Unternehmens- steuerung
- Versicherungs- und Risikotheorie
- Steuerliche Gewinnermittlung
- Unternehmenssteuerrecht
- Konzernrechnungslegung

### MSc Finance Auditing Controlling Taxation FPOFACT 20090720 i.d.F. 20210311.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20090720-idf-20210311.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20090720-idf-20210311.md)

**Pflichtmodule (7):**
- Controlling of business systems
- Kapitalmarktorientierte Unternehmens- steuerung
- Versicherungs- und Risikotheorie
- Steuerliche Gewinnermittlung
- Unternehmenssteuerrecht
- Konzernrechnungslegung
- Masterarbeit

### MSc Finance Auditing Controlling Taxation FPOFACT 20090720 i.d.F. 20220721.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20090720-idf-20220721.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20090720-idf-20220721.md)

**Pflichtmodule (7):**
- Controlling of business systems
- Kapitalmarktorientierte Unternehmens- steuerung
- Versicherungs- und Risikotheorie
- Steuerliche Gewinnermittlung
- Unternehmenssteuerrecht
- Konzernrechnungslegung
- Masterarbeit

### MSc Finance Auditing Controlling Taxation FPOFACT 20230615 i.d.F. 20240229.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20230615-idf-20240229.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20230615-idf-20240229.md)

**Pflichtmodule (8):**
- Controlling of business systems
- Kapitalmarktorientierte Unternehmens- steuerung
- Versicherungs- und Risikotheorie
- Steuerliche Gewinnermittlung
- Unternehmenssteuerrecht
- Konzernrechnungslegung
- Masterarbeit
- Kapitalmarktorientierte Unternehmenssteuerung

### MSc Finance Auditing Controlling Taxation FPOFACT 20230615.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20230615.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20230615.md)

**Pflichtmodule (7):**
- Controlling of business systems
- Kapitalmarktorientierte Unternehmens- steuerung
- Versicherungs- und Risikotheorie
- Steuerliche Gewinnermittlung
- Unternehmenssteuerrecht
- Konzernrechnungslegung
- Masterarbeit

### MSc FPOWiPäd 20091201 i.d.F. 20180928.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-fpowipaed-20091201-idf-20180928.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-fpowipaed-20091201-idf-20180928.md)

**Pflichtmodule (1):**
- Masterarbeit

### MSc FPOWiPäd 20091201 i.d.F. 20191129.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-fpowipaed-20091201-idf-20191129.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-fpowipaed-20091201-idf-20191129.md)

**Pflichtmodule (1):**
- Masterarbeit

### MSc FPOWiPäd 20091201 i.d.F. 20200731.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-fpowipaed-20091201-idf-20200731.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-fpowipaed-20091201-idf-20200731.md)

**Pflichtmodule (1):**
- Masterarbeit

### MSc FPOWiPäd 20091201 i.d.F. 20210812.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-fpowipaed-20091201-idf-20210812.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-fpowipaed-20091201-idf-20210812.md)

**Pflichtmodule (1):**
- Masterarbeit

### MSc FPOWiPäd 20230615.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-fpowipaed-20230615.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-fpowipaed-20230615.md)

**Pflichtmodule (1):**
- Masterarbeit

### MSc Internationale Wirtschaftsinformatik IIS FPOIIS 20100708 i.d.F. 20180615.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-internationale-wirtschaftsinformatik-iis-fpoiis-20100708-idf-20180615.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-internationale-wirtschaftsinformatik-iis-fpoiis-20100708-idf-20180615.md)

**Pflichtmodule (2):**
- Masterarbeit (30 ECTS)
- Masterarbeit

### MSc Internationale Wirtschaftsinformatik IIS FPOIIS 20100708 i.d.F. 20190815.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-internationale-wirtschaftsinformatik-iis-fpoiis-20100708-idf-20190815.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-internationale-wirtschaftsinformatik-iis-fpoiis-20100708-idf-20190815.md)

**Pflichtmodule (2):**
- Masterarbeit (30 ECTS)
- Masterarbeit

### MSc Internationale Wirtschaftsinformatik IIS FPOIIS 20100708 i.d.F. 20191203.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-internationale-wirtschaftsinformatik-iis-fpoiis-20100708-idf-20191203.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-internationale-wirtschaftsinformatik-iis-fpoiis-20100708-idf-20191203.md)

**Pflichtmodule (2):**
- Masterarbeit (30 ECTS)
- Masterarbeit

### MSc Marketing FPOMarketing 20090902 i.d.F. 20210812.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-marketing-fpomarketing-20090902-idf-20210812.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-marketing-fpomarketing-20090902-idf-20210812.md)

**Pflichtmodule (1):**
- Masterarbeit

### MSc Marketing FPOMarketing 20180730 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-marketing-fpomarketing-20180730-aes.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-marketing-fpomarketing-20180730-aes.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 20.07.2009 i.d.F. 10.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/po-ma-finance-auditing-controlling-taxation-aug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/po-ma-finance-auditing-controlling-taxation-aug2017.md)

**Pflichtmodule (7):**
- Controlling of business systems
- Kapitalmarktorientierte Unternehmensbesteuerung
- Versicherungs- und Risikotheo- rie
- Steuerliche Gewinnermittlung
- Unternehmenssteuerrecht
- Konzernrechnungslegung
- Masterarbeit

### PDF vom 20.07.2009 i.d.F. 05.12.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/po-ma-finance-auditing-controlling-taxation-dez2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/po-ma-finance-auditing-controlling-taxation-dez2017.md)

**Pflichtmodule (7):**
- Controlling of business systems
- Kapitalmarktorientierte Unternehmens- steuerung
- Versicherungs- und Risikotheorie
- Steuerliche Gewinnermittlung
- Unternehmenssteuerrecht
- Konzernrechnungslegung
- Masterarbeit

### PDF vom 02.09.2009 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/po-ma-marketing-aug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/po-ma-marketing-aug2017.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 02.09.2009 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/po-ma-sozialoekonomik-aug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/po-ma-sozialoekonomik-aug2017.md)

**Pflichtmodule (3):**
- Masterarbeit
- Mtbit
- aserare

### PDF vom 17.09.2007

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/st-po-master-intern-wirtschaftsinformatik.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/st-po-master-intern-wirtschaftsinformatik.md)

**Pflichtmodule (2):**
- (30) Masterarbeit
- (30) Master Thesis WI+I

### Modulstudien Berufspädagogik POMBPäd 20240807.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/modul-und-zusatzstudien/modulstudien-berufspaedagogik-pombpaed-20240807.md`](../pruefungsordnungen/rw/wiso/modul-und-zusatzstudien/modulstudien-berufspaedagogik-pombpaed-20240807.md)

**Pflichtmodule (7):**
- Grundlagen der Wirtschafts- und Betriebspädagogik
- (2) Schulorganisation und Bildungssystem
- Betriebliche Aus- und Weiterbildung
- (2) Betriebspädagogisches Seminar
- Schulpraktische Studien
- (4) Berufspädagogische Vertiefung
- Unterrichtsfach (Zweitfach) inkl. Fachdidaktik

### PDF vom 01.08.2006 i.d.F. 24.02.2011

PO-Quelle: [`pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-24feb2011.md`](../pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-24feb2011.md)

**Pflichtmodule (1):**
- m und

### PDF vom 01.08.2006 i.d.F. 24.02.2012

PO-Quelle: [`pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-24feb2012.md`](../pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-24feb2012.md)

**Pflichtmodule (1):**
- m und

### PDF vom 01.08.2006 i.d.F. 01.08.2012

PO-Quelle: [`pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-aug2012.md`](../pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-aug2012.md)

**Pflichtmodule (1):**
- m und

### PDF vom 01.08.2006 i.d.F. 13.02.2013

PO-Quelle: [`pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-feb2013.md`](../pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-feb2013.md)

**Pflichtmodule (1):**
- m und

### PDF vom 01.08.2006 i.d.F. 10.01.2014

PO-Quelle: [`pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-jan2014.md`](../pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-jan2014.md)

**Pflichtmodule (1):**
- m und

### PDF vom 01.08.2006 i.d.F. 26.07.2013

PO-Quelle: [`pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-juli2013.md`](../pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-juli2013.md)

**Pflichtmodule (1):**
- m und

### PDF vom 01.08.2006 i.d.F. 30.07.2010

PO-Quelle: [`pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-neu-ws2010-2011.md`](../pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-neu-ws2010-2011.md)

**Pflichtmodule (1):**
- m und

### berufsbegl. WTB MA Health Business Administration PO MHBA 20180706.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20180706.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20180706.md)

**Pflichtmodule (10):**
- Grundlagen des Gesundheits- wesens I: Kostenträger dr
- oe Grundlagen des Gesundheits- wesens I: Kostenträger
- Modul 4: (Pflichtmodul)
- Grundlagen des Gesundheits- wesens II: Leistungserbringer
- oder Grundlagen des Gesundheits-
- wesens II:
- Leistungserbringer
- Modul 5: (Wahlpflichtmodul)
- Ambulante Versorgung
- oder Ambulante Versorgung

### berufsbegl. WTB MA Health Business Administration PO MHBA 20231207 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20231207-idf-20240926.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20231207-idf-20240926.md)

**Pflichtmodule (5):**
- Grundlagen des Gesundheitswesens I:
- Kostenträger
- oder
- Grundlagen des Gesundheitswesens I: Kostenträger
- Fernstudium

### berufsbegl. WTB MA Health Business Administration PO MHBA 20231207.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20231207.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20231207.md)

**Pflichtmodule (5):**
- Grundlagen des Gesundheitswesens I:
- Kostenträger
- oder
- Grundlagen des Gesundheitswesens I: Kostenträger
- Fernstudium

### berufsbegl WTB MBA Business Management PO MBA 20200902.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-mba-business-management-po-mba-20200902.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-mba-business-management-po-mba-20200902.md)

**Pflichtmodule (1):**
- Masterarbeit

### berufsbegl WTB MBA Business Management und MBA Global Business Management PO MBA BM-GBM 20230615.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-mba-business-management-und-mba-global-business-management-po-mba-bm-gbm-20230615.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-mba-business-management-und-mba-global-business-management-po-mba-bm-gbm-20230615.md)

**Pflichtmodule (1):**
- Masterarbeit

### PO Sustainability Management MBA SM 20230323 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/po-sustainability-management-mba-sm-20230323-idf-20240926.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/po-sustainability-management-mba-sm-20230323-idf-20240926.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 01.10.2007 i.d.F. 06.06.2014

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/pro-wtb-ma-healthbusadmin-juni2014.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/pro-wtb-ma-healthbusadmin-juni2014.md)

**Pflichtmodule (6):**
- Grundlagen des Gesund- heitswesens I: Kostenträger
- Mdl 4
- Fernstudium
- Grundlagen des Gesund- heitswesens II:
- Leistungserbringer
- Modul 5: (Wahlpflichtmodul)

### PDF vom 13.11.2013

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/pro-wtb-mba-neu.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/pro-wtb-mba-neu.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 18.02.2014

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/wtb-pro-marketing-management.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/wtb-pro-marketing-management.md)

**Pflichtmodule (2):**
- Pflichtmodul:
- Marketing- und Vertriebs- Strategie

### 3. Juli 2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/3aes-ba-ma-chemicaleng-nct.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/3aes-ba-ma-chemicaleng-nct.md)

**Pflichtmodule (1):**
- Masterarbeit mit Referat

### 2. Juli 2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/7aes-ba-ma-energietechnik.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/7aes-ba-ma-energietechnik.md)

**Pflichtmodule (9):**
- VTE 1
- VTE 2
- MWT 1a
- MWT 1b
- EET 1
- EET 2
- TuU1
- TuU 2
- TuU 3

### BA-MA Chemie- und Bioingenieurwesen FPOCBI 20240328.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/ba-ma-chemie-und-bioingenieurwesen-fpocbi-20240328.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/ba-ma-chemie-und-bioingenieurwesen-fpocbi-20240328.md)

**Pflichtmodule (19):**
- rungsprung (GOP)
- Mathematik für CBI 1
- Allgemeine und Anorganische Chemie
- Experimentalphysik
- Konstruktionslehre
- Mhik Sik M
- esstecn: ensor und essver- fahren
- Chemische und Biologische Prozess- technik
- Wahlmodul aus dem Angebot der FAU
- Mathematik für CBI 2
- Physikalische Chemie
- Mathematik für CBI 3
- Organische Chemie
- rungsprüfung
- (GOP)
- Praktikum CBI 1
- Praktikum CBI 2
- Prozessmaschinen und Anlagenbau
- Bachelorarbeit

### BSc MSc Chemical Engineering FPOCEN 20230426 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/bsc-msc-chemical-engineering-fpocen-20230426-aes.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/bsc-msc-chemical-engineering-fpocen-20230426-aes.md)

**Pflichtmodule (10):**
- Mathematik für CEN 1
- Allgemeine und Anorganische Chemie
- Experimentalphysik
- Konstruktionslehre
- Messtechnik: Sensorik und Messverfahren
- Nachhaltie Chemische Prozesstechnik
- Mathematik für CEN 2
- Physikalische Chemie
- Mathematik für CEN 3
- Masterarbeit mit Hauptseminar

### FPO-BA-MA ChemEngin-NachhaltigeChemTechn 20110607 i.d.F. 20230426.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-20110607-idf-20230426.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-20110607-idf-20230426.md)

**Pflichtmodule (5):**
- rungsprüfung (GOP)
- s.FPO LSE
- Masterarbeit mit Hauptse- minar
- Masterarbeit mit Hauptseminar
- Masterarbeit mit Hauptse- minar 2

### PDF vom 07.06.2011 i.d.F. 26.01.2016

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-jan2016.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-jan2016.md)

**Pflichtmodule (1):**
- Masterarbeit mit Referat

### PDF vom 07.06.2011 i.d.F. 03.07.2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-juli2015.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-juli2015.md)

**Pflichtmodule (1):**
- Masterarbeit mit Referat

### PDF vom 15.12.2008 i.d.F. 02.07.2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-energietechnik-ba-ma-juli2015.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-energietechnik-ba-ma-juli2015.md)

**Pflichtmodule (9):**
- VTE 1
- VTE 2
- MWT 1a
- MWT 1b
- EET 1
- EET 2
- TuU1
- TuU2
- TuU 3

### 3. Juli 2017

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/13aesa-fpoeei.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/13aesa-fpoeei.md)

**Pflichtmodule (24):**
- Hochfrequenztechnik
- Photonik 1
- Sensoren und Aktoren der Mechatronik
- Leistungselektronik
- Elektromagnetische Verträglichkeit
- Analoge elektronische Systeme
- Regelungstechnik B(Zustandsraummethoden)
- Modellbildungin der Regelungstechnik
- Linearantriebe
- Sensorik
- Digitale Signalverarbeitung
- Digitale Übertragung
- Kommunikationsnetze
- Information Theoryand Coding/Informationstheorie und Codierung
- Kommunikationselektronik
- Leistungshalbleiter-Bauelemente
- Hochleistungsstromrichter für die EEV
- Pulsumrichter für elektrische Antriebe
- Schaltnetzteile
- Digitale elektronische Systeme
- Transceiver-Systementwurf
- Prozessintegration und Bauelementearchitekturen
- Entwurf Integrierter Schaltungen I
- Technologie integrierter Schaltungen oder Entwurf Integrierter Schaltungen II

### 17. Januar 2011

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/5aes-ba-20ma-eei.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/5aes-ba-20ma-eei.md)

**Pflichtmodule (3):**
- (2) Grundlagen der Elektrischen Antriebstechnik
- (2) Signale und Systeme I
- (4) _Studienrichtung:_Kernmodule 28

### BA-MA Elektrotechnik, Elektronik und Informationstechnik FPOEEI 20070920 i.d.F. 20190809.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/ba-ma-elektrotechnik-elektronik-und-informationstechnik-fpoeei-20070920-idf-20190809.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/ba-ma-elektrotechnik-elektronik-und-informationstechnik-fpoeei-20070920-idf-20190809.md)

**Pflichtmodule (29):**
- Hochfrequenztechnik
- Photonik 1
- Sensoren und Aktoren der Mechatronik
- Leistungselektronik
- Elektromagnetische Verträglichkeit
- Analoge elektronische Systeme
- Regelungstechnik B(Zustandsraummethoden)
- Modellbildungin der Regelungstechnik
- Linearantriebe
- Sensorik
- Elektrische Antriebstechnik I
- Betriebsmittel und Komponenten elektrischer Energiesysteme
- Elektrische Antriebstechnik II
- Betriebsverhalten elektrischer Energiesysteme
- Elektrische Maschinen I
- Digitale Signalverarbeitung
- Digitale Übertragung
- Kommunikationsnetze
- Information Theory and Coding/Informationstheorie und Codierung
- Kommunikationselektronik
- Leistungshalbleiter-Bauelemente
- Hochleistungsstromrichter für die EEV
- Pulsumrichter für elektrische Antriebe
- Schaltnetzteile
- Digitale elektronische Systeme
- Transceiver-Systementwurf
- Prozessintegration und Bauelementearchitekturen
- Entwurf Integrierter Schaltungen I
- Technologie integrierter Schaltungen oder Entwurf Integrierter Schaltungen II

### BA-MA Elektrotechnik, Elektronik und Informationstechnik FPOEEI 20070920 i.d.F. 20210701.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/ba-ma-elektrotechnik-elektronik-und-informationstechnik-fpoeei-20070920-idf-20210701.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/ba-ma-elektrotechnik-elektronik-und-informationstechnik-fpoeei-20070920-idf-20210701.md)

**Pflichtmodule (29):**
- Hochfrequenztechnik
- Photonik 1
- Mechatronic components and systems
- Leistungselektronik
- Elektromagnetische Verträglichkeit
- Analoge elektronische Systeme
- Regelungstechnik B(Zustandsraummethoden)
- Modellbildungin der Regelungstechnik
- Linearantriebe
- Sensorik
- Elektrische Antriebstechnik I
- Betriebsmittel und Komponenten elektrischer Energiesysteme
- Elektrische Antriebstechnik II
- Betriebsverhalten elektrischer Energiesysteme
- Elektrische Maschinen I
- Digitale Signalverarbeitung
- Digitale Übertragung
- Kommunikationsnetze
- Information Theory and Coding/Informationstheorie und Codierung
- Kommunikationselektronik
- Leistungshalbleiter-Bauelemente
- Hochleistungsstromrichter für die EEV
- Pulsumrichter für elektrische Antriebe
- Schaltnetzteile
- Digitale elektronische Systeme
- Transceiver-Systementwurf
- Prozessintegration und Bauelementearchitekturen
- Entwurf Integrierter Schaltungen I
- Technologie integrierter Schaltungen oder Entwurf Integrierter Schaltungen II

### BSc-MSc Autonomy Technologies FPO AT 20230426 en.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-en.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-en.md)

**Pflichtmodule (1):**
- S (semester

### BSc-MSc Autonomy Technologies FPO AT 20230426 i.d.F. 20240430 en.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20240430-en.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20240430-en.md)

**Pflichtmodule (1):**
- S (semester

### BSc-MSc Autonomy Technologies FPO AT 20230426 i.d.F. 20240430.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20240430.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20240430.md)

**Pflichtmodule (20):**
- module Human-System Interfaces
- Human-centered Mechatronics and Robotics
- Robot Mechanisms and User Interfaces
- Human Computer Interaction
- Intent Detection and Feedback
- module Networking & Collaboration
- Digital Communications
- Information Theoryand Coding
- MIMO Communication Systems
- Machine Learningin Communications
- module Planning & Control
- Robotics I
- Nonlinear Control Systems
- Numerical optimization and modelpredictive control
- Introduction to DeepLearning
- module Sensing & Perception
- Radar,RFID and Wireless Sensor Systems
- Statistical Signal Processing
- Image,Video,and Multidimensional Signal Processing
- Machine Learningin Signal Processing

### BSc-MSc Autonomy Technologies FPO AT 20230426 i.d.F. 20241219 en.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20241219-en.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20241219-en.md)

**Pflichtmodule (1):**
- S (semester

### BSc-MSc Autonomy Technologies FPO AT 20230426 i.d.F. 20241219.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20241219.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20241219.md)

**Pflichtmodule (20):**
- module Human-System Interfaces
- Human-centered Mechatronics and Robotics
- Robot Mechanisms and User Interfaces
- Human Computer Interaction
- Intent Detection and Feedback
- module Networking & Collaboration
- Digital Communications
- Information Theoryand Coding
- MIMO Communication Systems
- Machine Learningin Communications
- module Planning & Control
- Robotics I
- Nonlinear Control Systems
- Numerical optimization and modelpredictive control
- Introduction to DeepLearning
- module Sensing & Perception
- Radar,RFID and Wireless Sensor Systems
- Statistical Signal Processing
- Image,Video,and Multidimensional Signal Processing
- Machine Learningin Signal Processing

### BSc-MSc Autonomy Technologies FPO AT 20230426.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426.md)

**Pflichtmodule (20):**
- module Human-System Interfaces
- Human-centered Mechatronics and Robotics
- Robot Mechanisms and User Interfaces
- Human Computer Interaction
- Intent Detection and Feedback
- module Networking & Collaboration
- Digital Communications
- Information Theoryand Coding
- MIMO Communication Systems
- Machine Learningin Communications
- module Planning & Control
- Robotics I
- Nonlinear Control Systems
- Numerical optimization and modelpredictive control
- Introduction to DeepLearning
- module Sensing & Perception
- Radar,RFID and Wireless Sensor Systems
- Statistical Signal Processing
- Image,Video,and Multidimensional Signal Processing
- Machine Learningin Signal Processing

### BSc-MSc Elektrotechnik, Elektronik und Informationstechnik FPOEEI 20070920 i.d.F. 20220629.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-elektrotechnik-elektronik-und-informationstechnik-fpoeei-20070920-idf-20220629.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-elektrotechnik-elektronik-und-informationstechnik-fpoeei-20070920-idf-20220629.md)

**Pflichtmodule (30):**
- Hochfrequenztechnik
- Photonik 1
- Mechatronic components and systems
- Leistungselektronik
- Felder und Wellen in optoelektronischen Bauelementen
- Analoge elektronische Systeme
- Regelungstechnik B (Zustandsraummethoden)
- Modellbildunginder Regelungstechnik
- Linearantriebe
- Sensorik
- Elektrische Antriebstechnik I
- Betriebsmittel und Komponenten elektrischer Energiesysteme
- Elektrische Antriebstechnik II
- Betriebsverhalten elektrischer Energiesysteme
- Elektrische Maschinen I
- Digitale Signalverarbeitung
- Digitale Übertragung
- Kommunikationsnetze
- Information Theoryand Coding/Informationstheorie und Codierung
- Kommunikationselektronik
- Halbleitertechnik III – Leistungshalbleiterbauelemente(HL III)
- Elektromagnetische Verträglichkeit
- Hochleistungsstromrichter für die EEV
- Pulsumrichter für elektrische Antriebe
- Schaltnetzteile
- Digitale elektronische Systeme
- Transceiver-Systementwurf
- Entwurf Integrierter Schaltungen I
- Halbleitertechnologie I – Technologie integrierter Schaltungen(HLT I)
- Entwurf integrierter Schaltungen II

### Elite-MA Advanced Signal Processing Communications Engineering FPOASC 20160229 i.d.F. 20240807.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/elite-ma-advanced-signal-processing-communications-engineering-fpoasc-20160229-idf-20240807.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/elite-ma-advanced-signal-processing-communications-engineering-fpoasc-20160229-idf-20240807.md)

**Pflichtmodule (10):**
- (5) Mathematical Optimization in Communications and Signal Processing
- (5) Information Theoryand Coding
- (5) Statistical Signal Processing
- (5) Machine Learning in Signal Processing
- (5) Deep Learning
- Selected Topics in ASC
- (5) Kick-off Seminar,Winter & Summer School
- (15) Research Project (Major)
- (30) Master Thesis
- Summ

### PDF vom 20.09.2007 i.d.F. 03.07.2017

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/fpo-ba-ma-eei-juli2017.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/fpo-ba-ma-eei-juli2017.md)

**Pflichtmodule (29):**
- Hochfrequenztechnik
- Photonik 1
- Sensoren und Aktoren der Mechatronik
- Leistungselektronik
- Elektromagnetische Verträglichkeit
- Analoge elektronische Systeme
- Regelungstechnik B(Zustandsraummethoden)
- Modellbildungin der Regelungstechnik
- Linearantriebe
- Sensorik
- Elektrische Antriebstechnik I
- Betriebsmittel und Komponenten elektrischer Energiesysteme
- Elektrische Antriebstechnik II
- Betriebsverhalten elektrischer Energiesysteme
- Elektrische Maschinen I
- Digitale Signalverarbeitung
- Digitale Übertragung
- Kommunikationsnetze
- Information Theory and Coding/Informationstheorie und Codierung
- Kommunikationselektronik
- Leistungshalbleiter-Bauelemente
- Hochleistungsstromrichter für die EEV
- Pulsumrichter für elektrische Antriebe
- Schaltnetzteile
- Digitale elektronische Systeme
- Transceiver-Systementwurf
- Prozessintegration und Bauelementearchitekturen
- Entwurf Integrierter Schaltungen I
- Technologie integrierter Schaltungen oder Entwurf Integrierter Schaltungen II

### FPOCME 20230822.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/fpocme-20230822.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/fpocme-20230822.md)

**Pflichtmodule (1):**
- Masterarbeit

### 3. Dezember 2009

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/2aesa-20ba-ma-20compeng.md`](../pruefungsordnungen/technische-fakultaet/informatik/2aesa-20ba-ma-20compeng.md)

**Pflichtmodule (6):**
- Simulation und wissenschaftliches Rechnen 1 (7.5 ECTS) Simulation and Modeling 1 (5ECTS)
- Mathematik A4 (5 ECTS) Numerik 2 (mind. 2.5ECTS)
- Mathematik A3 (5 ECTS) Numerik 1 (mind.5ECTS)
- Mathematik A2 (10 ECTS)
- Mathematik A1 (7.5 ECTS)
- Mathematik fest

### 2. Dezember 2009

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/2aesa-ba-20ma-inf.md`](../pruefungsordnungen/technische-fakultaet/informatik/2aesa-ba-20ma-inf.md)

**Pflichtmodule (1):**
- unbenoteter Schein

### 29. Juli 2013

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/5aes-ba-ma-computengineering.md`](../pruefungsordnungen/technische-fakultaet/informatik/5aes-ba-ma-computengineering.md)

**Pflichtmodule (5):**
- Festlegung der Module im Studienkonzept
- Funktionalanalysis für Ingenieure (5 ECTS) Optimierung für Inge- nieure(7,5 ECTS)
- mind. 20 ECTS
- aus den Wahlpflic
- Mathematik

### 24. Juli 2014

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/6aes-ba-ma-computengineering.md`](../pruefungsordnungen/technische-fakultaet/informatik/6aes-ba-ma-computengineering.md)

**Pflichtmodule (1):**
- Masterarbeit

### 7. Oktober 2013

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/7aes-ba-ma-informatik.md`](../pruefungsordnungen/technische-fakultaet/informatik/7aes-ba-ma-informatik.md)

**Pflichtmodule (17):**
- Grundlagen der Technischen Informatik
- Parallele und funktionale Programmierung
- Grundlagen der Rechnerarchitektur und -organisation
- Grundlagen der Schaltungstechnik
- Systemprogrammierung
- Grundlagen der Logik und Logikprogrammierung
- Softwareentwicklungin Großprojekten
- Berechenbarkeit und Formale Sprachen
- Theorie der Programmierung
- Rechnerkommunikation
- Algorithmik kontinuierlicher Systeme
- Implementierungvon Datenbanksystemen
- Seminar (Schlüsselqualifikation)
- Mathematik für INF 1<sup>1)</sup>
- Mathematik für INF 2<sup>1)</sup>
- Mathematik für INF 3<sup>1)</sup>
- Mathematik für INF 4<sup>1)</sup>

### 4. August 2014

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/8aes-ba-ma-informatik.md`](../pruefungsordnungen/technische-fakultaet/informatik/8aes-ba-ma-informatik.md)

**Pflichtmodule (21):**
- Grundlagen der Technischen Informatik
- Parallele und funktionale Programmierung
- Grundlagen der Rechnerarchitektur und -organisation
- Grundlagen der Schaltungstechnik
- Systemprogrammierung
- Grundlagen der Logik in der Informatik
- Softwareentwicklungin Großprojekten
- Berechenbarkeit und Formale Sprachen
- Theorie der Programmierung
- Rechnerkommunikation
- Algorithmik kontinuierlicher Systeme
- Implementierungvon Datenbanksystemen
- Seminar(Schlüsselqualifikation)
- Mathematik für INF 1<sup>1)</sup>
- Mathematik für INF 2<sup>1)</sup>
- Mathematik für INF 3<sup>1)</sup>
- Mathematik für INF 4<sup>1)</sup>
- Bachelorarbeit Begleitseminar mit Referat zur Ba- chelorarbeit
- PfP: PL (K, 90 min.) und SL
- m, zusätzlich K, 60 min., wenn „Data Warehousing“ gewähltwird
- PfP: PL (K, 90 min.) und SL (ÜbL)

### BA-MA-Medizintechnik FPOMT 20090915 i.d.F. 20180828 en.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20180828-en.md`](../pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20180828-en.md)

**Pflichtmodule (8):**
- Foundations of anatomy and physiology for non-medical stu- dents
- Signals and systems II
- Passive components and their RF properties
- Circuit technology
- Automatic control A (foundations)
- Medical electronics
- Medical engineering I (bio- materials)
- Material surfaces in medicine

### BA-MA-Medizintechnik FPOMT 20090915 i.d.F. 20180828.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20180828.md`](../pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20180828.md)

**Pflichtmodule (7):**
- Pattern Recognition
- Pattern Analysis
- Signale und Systeme II
- Passive Bauelemente und deren HF-Verhalten
- Schaltungstechnik
- Regelungstechnik A (Grundlagen)
- Medizinelektronik

### BA-MA-Medizintechnik FPOMT 20090915 i.d.F. 20190710 en.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20190710-en.md`](../pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20190710-en.md)

**Pflichtmodule (3):**
- Foundations of anatomy and physiology for non-medical stu- dents
- Medical engineering I (bio- materials)
- Material surfaces in medicine

### BA-MA-Medizintechnik FPOMT 20090915 i.d.F. 20190710.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20190710.md`](../pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20190710.md)

**Pflichtmodule (9):**
- ECTS Name
- vgl. § 44a Abs. 8
- Pattern Recognition
- Pattern Analysis
- Signale und Systeme II
- Passive Bauelemente und deren HF-Verhalten
- Schaltungstechnik
- Regelungstechnik A (Grundlagen)
- Medizinelektronik

### berufsbegl BSc Informatik-IT-Sicherheit BPOITS 20150116 i.d.F. 20190815.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/berufsbegl-bsc-informatik-it-sicherheit-bpoits-20150116-idf-20190815.md`](../pruefungsordnungen/technische-fakultaet/informatik/berufsbegl-bsc-informatik-it-sicherheit-bpoits-20150116-idf-20190815.md)

**Pflichtmodule (22):**
- Grundlagen der Programmierung
- Mathematik 1
- Konzeptionelle Modellierung
- Mathematik 2
- Rechnerstrukturen
- Systemsicherheit 1
- Algorithmen und Datenstrukturen
- Theoretische Informatik
- Kryptographie 1
- Systemnahe Programmierung
- Systemsicherheit 2
- Proseminar IT-Sicherheit
- Einführung in die digitale Forensik
- Compilerbau
- Netzsicherheit 1
- Kryptographie 2
- Netzsicherheit 2
- Realisierung von Softwareprojekten
- Seminar IT-Sicherheit
- Bachelorarbeit
- Klli
- ooquum

### BSc-MSc Computational Engineering 20070919 i.d.F. 20180116.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180116.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180116.md)

**Pflichtmodule (26):**
- Bachelorarbeit
- Technisches Anwendungsfach
- (3) Einführungin die Regelungstechnik
- (2) Regelungstechnik B(Zustandsraummethoden)
- Regelungstechnisches Praktikum für MB u. CE
- (2) Modellbildungin der Regelungstechnik
- (2) Einführung in die Grundlagen der Elektrotechnik für CE-Studierende
- Signale und Systeme I
- Signale und Systeme II
- (3) Information Theory and Coding/Informations- theorie und Codierung
- (3) Digitale Signalverarbeitung
- (4) Grundlagen der Elektrotechnik I
- (2) Grundlagen der Elektrotechnik III
- (1) Elektromagnetische Felder I
- (2) Sensorik
- (4) Experimentalphysik 3: Optik und Quanteneffekte
- (2) Moderne Optik I: Fortgeschrittene Optik
- (2) Photonik 1
- (2) Photonik 2
- Statik,Elastostatik und Festigkeitslehre
- Dynamik starrer Körper
- (3) Technische Thermodynamik I
- (3) Technische Thermodynamik II
- (2) Strömungsmechanik I
- (3) Wärme- und Stoffübertragung
- Masterarbeit

### BSc-MSc Computational Engineering 20070919 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180730.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180730.md)

**Pflichtmodule (26):**
- Bachelorarbeit
- Technisches Anwendungsfach
- (3) Einführungin die Regelungstechnik
- (2) Regelungstechnik B(Zustandsraummethoden)
- Regelungstechnisches Praktikum für MB u. CE
- (2) Modellbildungin der Regelungstechnik
- (4) Grundlagen der Elektrotechnik I
- (2) Grundlagen der Elektrotechnik III
- (1) Elektromagnetische Felder I
- (2) Sensorik
- (2) Einführung in die Grundlagen der Elektrotechnik für CE-Studierende
- Signale und Systeme I
- Signale und Systeme II
- (3) Information Theory and Coding/Informations- theorie und Codierung
- (3) Digitale Signalverarbeitung
- (3) Technische Thermodynamik I
- (3) Technische Thermodynamik II
- (2) Strömungsmechanik I
- (3) Wärme- und Stoffübertragung
- Statik,Elastostatik und Festigkeitslehre
- Dynamik starrer Körper
- (4) Experimentalphysik 3: Optik und Quanteneffekte
- (2) Moderne Optik I: Fortgeschrittene Optik
- (2) Photonik 1
- (2) Photonik 2
- Masterarbeit

### BSc-MSc Computational Engineering 20180116 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20180116-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20180116-aes.md)

**Pflichtmodule (24):**
- Technisches Anwendungsfach
- (3) Einführung in die Regelungstechnik
- (2) Regelungstechnik B (Zustandsraummethoden)
- Regelungstechnisches Praktikum für MB u. CE
- (2) Modellbildung in der Regelungstechnik
- (2) Einführung in die Grundlagen der Elektrotechnik für CE-Studierende
- Signale und Systeme I
- Signale und Systeme II
- (3) Information Theory and Coding/Informations- theorie und Codierung
- (3) Digitale Signalverarbeitung
- (4) Grundlagen der Elektrotechnik I
- (2) Grundlagen der Elektrotechnik III
- (1) Elektromagnetische Felder I
- (2) Sensorik
- (4) Experimentalphysik 3: Optik und Quanteneffekte
- (2) Moderne Optik I: Fortgeschrittene Optik
- (2) Photonik 1
- (2) Photonik 2
- (5) Statik, Elastostatik und Festigkeitslehre
- (3) Dynamik starrer Körper
- (3) Technische Thermodynamik I
- (3) Technische Thermodynamik II
- (2) Strömungsmechanik I
- (3) Wärme- und Stoffübertragung

### BSc-MSc Computational Engineering 20180730 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20180730-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20180730-aes.md)

**Pflichtmodule (26):**
- Technisches Anwendungsfach
- (3) Einführungin die Regelungstechnik
- (2) Regelungstechnik B(Zustandsraummethoden)
- Regelungstechnisches Praktikum für MB u. CE
- (2) Modellbildungin der Regelungstechnik
- (4) Grundlagen der Elektrotechnik I
- (2) Grundlagen der Elektrotechnik III
- (1) Elektromagnetische Felder I
- (2) Sensorik
- (2) Einführung in die Grundlagen der Elektrotechnik für CE-Studierende
- Signale und Systeme I
- Signale und Systeme II
- (3) Information Theory and Coding/Informations- theorie und Codierung
- (3) Digitale Signalverarbeitung
- (3) Technische Thermodynamik I
- (3) Technische Thermodynamik II
- (2) Strömungsmechanik I
- (3) Wärme- und Stoffübertragung
- (5) Statik,Elastostatik und Festigkeitslehre
- (3) Dynamik starrer Körper
- (4) Experimentalphysik 3: Optik und Quanteneffekte
- (2) Moderne Optik I: Fortgeschrittene Optik
- (2) Photonik 1
- (2) Photonik 2
- Masterarbeit
- SummeECTS

### BSc-MSc Computational Engineering 20220421 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20220421-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20220421-aes.md)

**Pflichtmodule (8):**
- Technisches Anwendungsfach
- Einführungin die Regelungstechnik<sup>1</sup>
- (3) Regelungstechnisches Praktikum für CE
- Regelungstechnik B(Zustandsraummethoden)
- Digitale Regelung
- Grundlagen der Elektrotechnik I
- Grundlagen der Elektrotechnik III
- Sensorik

### BSc-MSc Computational Engineering FPOCE 20070919 i.d.F. 20220421.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20070919-idf-20220421.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20070919-idf-20220421.md)

**Pflichtmodule (46):**
- Grundlagen der Programmierung (GOP)
- Grundlagen der Logik in der Informatik
- Einführungin die Algorithmik(GOP)
- Computational Engineering1(GOP)
- Systemprogrammierung
- Simulation und Modellierung1
- Simulation und wissenschaftliches Rechnen 1
- Simulation und wissenschaftliches Rechnen 2
- Mathematik
- Mathematik für CE 1<sup>1</sup><sup>)</sup> (GOP)
- Mathematik für CE 2<sup>1</sup><sup>)</sup> (GOP)
- Mathematik für CE 3<sup>1</sup><sup>)</sup>
- Mathematik für CE 4<sup>1</sup><sup>)</sup>
- Numerik I für Ingenieure
- Numerik II für Ingenieure
- Technisches Anwendungsfach (TAF), mind. 35 ECTS-Punkte<sup>2</sup>)
- Experimentalphysik für Naturwissenschaftler I(GOP)
- Experimentalphysik für Naturwissenschaftler II(GOP)
- Computational Engineering2(GOP)
- TAF – Module<sup>3)</sup>
- Technische Wahlmodule, max. 17,5 ECTS- Punkte<sup>4)</sup>
- Bachelorarbeit
- Technisches Anwendungsfach
- Einführungin die Regelungstechnik<sup>1</sup>
- (3) Regelungstechnisches Praktikum für CE
- Regelungstechnik B(Zustandsraummethoden)
- Digitale Regelung
- Grundlagen der Elektrotechnik I
- Grundlagen der Elektrotechnik III
- Sensorik
- (2) Einführung in die Grundlagen der Elektrotechnik für CE-Studierende
- Signale und SystemeI
- Signale und SystemeII
- (3) Information Theory and Coding/Informations-the- orie und Codierung
- (3) Digitale Signalverarbeitung
- (3) Technische Thermodynamik I
- (3) Technische Thermodynamik II
- (2) Strömungsmechanik I
- (3) Wärme- und Stoffübertragung
- Statik,Elastostatik und Festigkeitslehre
- Dynamik starrer Körper
- (4) Experimentalphysik 3: Optik und Quanteneffekte
- (2) Moderne Optik I: Fortgeschrittene Optik
- (2) Photonik 1
- (2) Photonik 2
- Masterarbeit

### BSc-MSc Computational Engineering FPOCE 20220421 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20220421-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20220421-aes.md)

**Pflichtmodule (8):**
- Technisches Anwendungsfach
- Einführungin die Regelungstechnik1
- Regelungstechnisches Praktikum für CE
- Regelungstechnik B(Zustandsraummethoden)
- (2) Digitale Regelung
- Grundlagen der Elektrotechnik I
- Grundlagen der Elektrotechnik III
- Sensorik

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20180801.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20180801.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20180801.md)

**Pflichtmodule (24):**
- (4) Grundlagen der Technischen Informatik
- (2) Parallele und funktionale Programmierung
- (2) Grundlagen der Rechnerarchitektur und -organisation
- (2) Grundlagen der Schaltungstechnik
- (4) Systemprogrammierung
- (2) Grundlagen der Logik in der Informatik
- (2) Softwareentwicklungin Großprojekten
- (4) Berechenbarkeit und Formale Sprachen
- (4) Theorie der Programmierung
- (2) Rechnerkommunikation
- (4) Algorithmik kontinuierlicher Systeme
- (2) Implementierungvon Datenbanksystemen
- Seminar(Schlüsselqualifikation)
- (4) Mathematik für INF 1<sup>1)</sup>
- (4) Mathematik für INF 2<sup>1)</sup>
- (4) Mathematik für INF 3<sup>1)</sup>
- (4) Mathematik für INF 4<sup>1)</sup>
- Bachelorarbeit Begleitseminar mit Referat zur Ba- chelorarbeit
- Summ
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- m, zusätzlich K, 60 Min., wenn „Data Warehousing“ gewählt wird
- PL (K, 90 Min.) und SL (ÜbL)

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20190306.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20190306.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20190306.md)

**Pflichtmodule (9):**
- Bachelorarbeit
- SWS und ECTS-Punkte:
- Masterarbeit
- Summ
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- PL (K, 90 Min.) und SL (ÜbL)
- m, 30 Min. oder K, 90 Min. und SL(ÜbL)

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20191203.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20191203.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20191203.md)

**Pflichtmodule (24):**
- Grundlagen der Technischen
- Informatik
- Parallele und funktionale
- Programmierung
- Grundlagen der Rechner-
- architektur und -organisation
- Grundlagen der Schaltungs-
- technik
- Systemprogrammierung
- Systemprogrammierung UE
- Grundlagen der Logik in der
- Softwareentwicklung in
- Großprojekten
- Berechenbarkeit und
- Formale Sprachen
- Bachelorarbeit
- SWS und ECTS-Punkte:
- Masterarbeit
- Summ
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- PL (K, 90 Min.) und SL (ÜbL)
- m, 30 Min. oder K, 90 Min. und SL(ÜbL)

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20200820.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20200820.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20200820.md)

**Pflichtmodule (8):**
- Masterarbeit
- Summ
- und ECTS-Punkte:
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- PL (K, 90 Min.) und SL (ÜbL)
- m, 30 Min. oder K, 90 Min. und SL(ÜbL)

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20210701.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20210701.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20210701.md)

**Pflichtmodule (11):**
- Bachelorarbeit
- S und ECTS-Punkte: 5
- Masterarbeit
- Summ
- und ECTS-Punkte:
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- PL (K, 90 Min.) und SL (ÜbL)
- m, 30 Min. oder K, 90 Min. und SL(ÜbL)
- K, 60/90 Min. oder m, 30 Min.

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20220301.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20220301.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20220301.md)

**Pflichtmodule (34):**
- Grundlagen der Program-
- mierung
- Grundlagen der Logik in der
- Informatik
- Sichere Ssteme
- Sichere Systeme UE
- Grundlagen der Technischen
- Einführun in die Alorithmik
- Einführung in die Algorithmik UE
- Systemprogrammierung V
- Systemprogrammierung
- Grundlagen der Rechner-
- architektur und -organisation
- Rhkiki
- ecnerommunaton
- Parallele und funktionale
- Programmierung
- Softwareentwicklung in
- Großprojekten
- Bachelorarbeit
- n SWS und ECTS-Punkte:
- Masterarbeit
- S und ECTS-Punkte:
- SL (ÜbL)
- PL (K, 60 Min.)
- PL (K, 90 Min.) und SL(ÜbL)
- PL (K, 90 Min.)
- PL (m, 30 Min. oder K,90 Min.)
- PL (m, 30 Min. oder K, 90 Min.) und SL(ÜbL)
- PL (m, 30 Min.)
- PL (K, 90 Min. oder m,30 Min.)
- PL (K, 60/90 Min. oder m,30 Min.)
- PL (K, 60 Min.) und SL(ÜbL)
- PL (K, 90 Min)

### BSc-MSc Informatik FPOINF 20070921 i.d.F. 20220726.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070921-idf-20220726.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070921-idf-20220726.md)

**Pflichtmodule (36):**
- Grundlagen der Programmie-
- rung
- Grundlagen der Logik in der
- Informatik
- Sichere Systeme V
- Sichere Systeme
- Grundlagen der Technischen
- Eifüh i di Alithik
- nrung n e gorm
- Sstemrorammierun
- ypgg
- Grundlagen der Rechner-
- architektur und -organisation
- Rechnerkommunikation V
- Rechnerkommunikation
- Parallele und funktionale
- Programmierung
- Einführung in das Software
- Engineering
- Bachelorarbeit
- WS und ECTS-Punkte:
- Masterarbeit
- n SWS und ECTS-Punkte:
- und ECTS-Punkte:
- SL (ÜbL)
- PL (K, 60 Min.)
- PL (K, 90 Min.) und SL(ÜbL)
- PL (K, 90 Min.)
- PL (m, 30 Min. oder K,90 Min.)
- PL (m, 30 Min. oder K, 90 Min.) und SL(ÜbL)
- PL (m, 30 Min.)
- PL (K, 90 Min. oder m,30 Min.)
- PL (K, 60/90 Min. oder m,30 Min.)
- PL (K, 60 Min.) und SL(ÜbL)
- PL (K, 90 Min)
- PL (K, 90 Min oder m,30 Min.)

### BSc-MSc Informatik FPOINF 20070921 i.d.F. 20230426.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070921-idf-20230426.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070921-idf-20230426.md)

**Pflichtmodule (17):**
- Bachelorarbeit
- WS und ECTS-Punkte:
- Masterarbeit
- n SWS und ECTS-Punkte:
- und ECTS-Punkte:
- SL (ÜbL)
- PL (K, 60 Min.)
- PL (K, 90 Min.) und SL(ÜbL)
- PL (K, 90 Min.)
- PL (m, 30 Min. oder K,90 Min.)
- PL (m, 30 Min. oder K, 90 Min.) und SL (ÜbL)
- PL (m, 30 Min.)
- PL (K, 90 Min. oder m,30 Min.)
- PL (K, 60/90 Min. oder m,30 Min.)
- PL (K, 60 Min.) und SL(ÜbL)
- PL (K, 90 Min)
- PL (K, 90 Min oder m,30 Min.)

### BSc-MSc Informatik FPOINF 20190306 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20190306-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20190306-aes.md)

**Pflichtmodule (9):**
- Bachelorarbeit
- ECTS-Punkte:
- Masterarbeit
- n SWS und ECTS-Punkte:
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- PL (K, 90 Min.) und SL (ÜbL)
- m, 30 Min. oder K, 90 Min. und SL(ÜbL)

### BSc-MSc Informatik FPOINF 20200820 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20200820-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20200820-aes.md)

**Pflichtmodule (4):**
- Bachelorarbeit
- SWS und ECTS-Punkte:
- Masterarbeit
- und ECTS-Punkte:

### BSc-MSc Informatik FPOINF 20220301 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20220301-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20220301-aes.md)

**Pflichtmodule (9):**
- SL (ÜbL)
- PL (K, 60 Min.)
- PL (K, 90 Min.) und SL(ÜbL)
- PL (K, 90 Min.)
- PL (m, 30 Min. oder K,90 Min.)
- PL (m, 30 Min. oder K, 90 Min.) und SL(ÜbL)
- PL (m, 30 Min.)
- PL (K, 90 Min. oder m,30 Min.)
- PL (K, 60/90 Min. oder m,30 Min.)

### BSc-MSc Informatik FPOINF 20240328.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328.md)

**Pflichtmodule (29):**
- Grundlagen der Programmierung V
- Programmierung
- Grundlagen der Logik in der
- Informatik
- Sih St
- cere yseme
- Grundlagen der Technischen
- Einführung in die Algorithmik
- Einführung in die Algorithmik UE
- Sstemrorammierun
- ypgg
- Grundlagen der Rechner-
- architektur und -organisation
- Rechnerkommunikation V
- Rechnerkommunikation
- Parallele und funktionale
- Masterarbeit
- nd ECTS-Punkte:
- PL (K, 60 Min.)
- PL (K, 90 Min.) und SL(ÜbL)
- PL (K, 90 Min.)
- PL (m, 30 Min. oder K,90 Min.)
- PL (m, 30 Min. oder K, 90 Min.) und SL (ÜbL)
- PL (m, 30 Min.)
- PL (K, 90 Min. oder m,30 Min.)
- PL (K, 60/90 Min. oder m,30 Min.)
- PL (K, 60 Min.) und SL(ÜbL)
- PL (K, 90 Min oder m,30 Min.)
- PL (K, 90 Min)

### BSc-MSc-Medizintechnik FPOMT 20090915 i.d.F. 20220413.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20220413.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20220413.md)

**Pflichtmodule (11):**
- Anatomie und Physiologie für Nichtmediziner
- Pattern Recognition
- Pattern Analysis
- Signale und Systeme II
- Passive Bauelemente und deren HF- Verhalten
- Schaltungstechnik
- Regelungstechnik A (Grundlagen)
- Medizinelektronik
- Medizintechnik I (Biomaterialien)
- Surfaces of Biomaterials
- Robotics 1

### BSc-MSc-Medizintechnik FPOMT 20090915 i.d.F. 20230426 en.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20230426-en.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20230426-en.md)

**Pflichtmodule (1):**
- Pattern analysis

### BSc-MSc-Medizintechnik FPOMT 20090915 i.d.F. 20230426.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20230426.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20230426.md)

**Pflichtmodule (11):**
- Anatomie und Physiologie für Nichtmediziner
- Pattern Recognition
- Pattern Analysis
- Signale und Systeme II
- Passive Bauelemente und deren HF- Verhalten
- Schaltungstechnik
- Regelungstechnik A (Grundlagen)
- Medizinelektronik
- Medizintechnik I (Biomaterialien)
- Surfaces of Biomaterials
- Robotics 1

### BSc-MSc-Medizintechnik FPOMT 20090915 i.d.F. 20230731 en.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20230731-en.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20230731-en.md)

**Pflichtmodule (1):**
- Pattern analysis

### BSc-MSc-Medizintechnik FPOMT 20090915 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20230731.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20230731.md)

**Pflichtmodule (11):**
- Anatomie und Physiologie für Nichtmediziner
- Pattern Recognition
- Pattern Analysis
- Signale und Systeme II
- Passive Bauelemente und deren HF- Verhalten
- Schaltungstechnik
- Regelungstechnik A (Grundlagen)
- Medizinelektronik
- Medizintechnik I (Biomaterialien)
- Surfaces of Biomaterials
- Robotics 1

### BSc-MSc-Medizintechnik FPOMT 20180828 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20180828-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20180828-aes.md)

**Pflichtmodule (9):**
- Grundlagen der Anatomie und Physiologie für Nichtmediziner
- Pattern Recognition
- Pattern Analysis
- Passive Bauelemente und deren HF-Verhalten
- Schaltungstechnik
- Regelungstechnik A (Grundlagen)
- Medizinelektronik
- Medizintechnik I (Biomaterialien)
- Werkstoffoberflächen in der Medizin/Material Surfaces in Medicine

### BSc-MSc Medizintechnik FPOMT 20190710 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20190710-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20190710-aes.md)

**Pflichtmodule (2):**
- Pattern Recognition
- Pattern Analysis

### BSc-MSc Medizintechnik FPOMT 20220413 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20220413-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20220413-aes.md)

**Pflichtmodule (10):**
- Anatomie und Physiologie für Nichtmediziner
- Pattern Recognition
- Pattern Analysis
- Signale und Systeme II
- Passive Bauelemente und deren HF- Verhalten
- Schaltungstechnik
- Regelungstechnik A (Grundlagen)
- Medizinelektronik
- Medizintechnik I (Biomaterialien)
- Surfaces of Biomaterials

### PDF vom 19.09.2007 i.d.F. 18.01.2016

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-jan2016.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-jan2016.md)

**Pflichtmodule (5):**
- Bachelorarbeit
- Begleitseminar + Referat Bachelor
- Schriftliche Bachelorarbeit
- SummeECTS
- Masterarbeit

### PDF vom 19.09.2007 i.d.F. 31.07.2012

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-juli2012.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-juli2012.md)

**Pflichtmodule (6):**
- Simulation und wissenschaftliches Rechnen 1 (7.5 ECTS) Simulation and Modeling 1 (5 ECTS)
- Mathematik für CE 4<sup>~~1)~~</sup> (5 ECTS) Numerik 2 (mind.5ECTS)
- Mathematik für CE 3<sup>~~1)~~</sup> (5 ECTS) Numerik 1 (mind. 5 ECTS)
- Mathematik für CE 2<sup>~~1)~~</sup> (10 ECTS)
- Mathematik für CE 1<sup>~~1)~~</sup> (7.5 ECTS)
- Mathematik fest

### PDF vom 19.09.2007 i.d.F. 29.07.2013

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-juli2013.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-juli2013.md)

**Pflichtmodule (6):**
- Simulation und wissenschaftliches Rechnen 1 (7.5 ECTS) Simulation and Modeling 1 (5 ECTS)
- Mathematik für CE 4<sup>~~1)~~</sup> (5 ECTS) Numerik 2 (mind.5ECTS)
- Mathematik für CE 3<sup>~~1)~~</sup> (5 ECTS) Numerik 1 (mind. 5 ECTS)
- Mathematik für CE 2<sup>~~1)~~</sup> (10 ECTS)
- Mathematik für CE 1<sup>~~1)~~</sup> (7.5 ECTS)
- Mathematik fest

### PDF vom 19.09.2007 i.d.F. 24.07.2014

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-juli2014.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-juli2014.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 19.09.2007 i.d.F. 30.07.2010

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-neu.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-neu.md)

**Pflichtmodule (6):**
- Simulation und wissenschaftliches Rechnen 1 (7.5 ECTS) Simulation and Modeling 1 (5 ECTS)
- Mathematik A4 (5 ECTS) Numerik 2 (mind.5ECTS)
- Mathematik A3 (5 ECTS) Numerik 1 (mind. 5 ECTS)
- Mathematik A2 (10 ECTS)
- Mathematik A1 (7.5 ECTS)
- Mathematik fest

### PDF vom 21.09.2007 i.d.F. 04.08.2014

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-august2014.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-august2014.md)

**Pflichtmodule (21):**
- Grundlagen der Technischen Informatik
- Parallele und funktionale Programmierung
- Grundlagen der Rechnerarchitektur und -organisation
- Grundlagen der Schaltungstechnik
- Systemprogrammierung
- Grundlagen der Logik in der Informatik
- Softwareentwicklungin Großprojekten
- Berechenbarkeit und Formale Sprachen
- Theorie der Programmierung
- Rechnerkommunikation
- Algorithmik kontinuierlicher Systeme
- Implementierungvon Datenbanksystemen
- Seminar(Schlüsselqualifikation)
- Mathematik für INF 1<sup>1)</sup>
- Mathematik für INF 2<sup>1)</sup>
- Mathematik für INF 3<sup>1)</sup>
- Mathematik für INF 4<sup>1)</sup>
- Bachelorarbeit Begleitseminar mit Referat zur Ba- chelorarbeit
- PfP: PL (K, 90 min.) und SL
- m, zusätzlich K, 60 min., wenn „Data Warehousing“ gewähltwird
- PfP: PL (K, 90 min.) und SL(ÜbL)

### PDF vom 21.09.2007 i.d.F. 31.07.2012

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-juli2012.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-juli2012.md)

**Pflichtmodule (1):**
- unbenoteter Schein

### PDF vom 21.09.2007 i.d.F. 11.06.2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-juni2015.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-juni2015.md)

**Pflichtmodule (21):**
- Grundlagen der Technischen Informatik
- Parallele und funktionale Programmierung
- Grundlagen der Rechnerarchitektur und -organisation
- Grundlagen der Schaltungstechnik
- Systemprogrammierung
- Grundlagen der Logik in der Informatik
- Softwareentwicklungin Großprojekten
- Berechenbarkeit und Formale Sprachen
- Theorie der Programmierung
- Rechnerkommunikation
- Algorithmik kontinuierlicher Systeme
- Implementierungvon Datenbanksystemen
- Seminar(Schlüsselqualifikation)
- Mathematik für INF 1<sup>1)</sup>
- Mathematik für INF 2<sup>1)</sup>
- Mathematik für INF 3<sup>1)</sup>
- Mathematik für INF 4<sup>1)</sup>
- Bachelorarbeit Begleitseminar mit Referat zur Ba- chelorarbeit
- PfP: PL (K, 90 min.) und SL
- m, zusätzlich K, 60 min., wenn „Data Warehousing“ gewähltwird
- PfP: PL (K, 90 min.) und SL(ÜbL)

### PDF vom 21.09.2007 i.d.F. 08.10.2012

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-oktober2012.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-oktober2012.md)

**Pflichtmodule (1):**
- unbenoteter Schein

### PDF vom 21.09.2007 i.d.F. 07.10.2013

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-oktober2013.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-oktober2013.md)

**Pflichtmodule (18):**
- Grundlagen der Technischen Informatik
- Parallele und funktionale Programmierung
- Grundlagen der Rechnerarchitektur und -organisation
- Grundlagen der Schaltungstechnik
- Systemprogrammierung
- Grundlagen der Logik und Logikprogrammierung
- Softwareentwicklungin Großprojekten
- Berechenbarkeit und Formale Sprachen
- Theorie der Programmierung
- Rechnerkommunikation
- Algorithmik kontinuierlicher Systeme
- Implementierungvon Datenbanksystemen
- Seminar (Schlüsselqualifikation)
- Mathematik für INF 1<sup>1)</sup>
- Mathematik für INF 2<sup>1)</sup>
- Mathematik für INF 3<sup>1)</sup>
- Mathematik für INF 4<sup>1)</sup>
- unbenoteter Schein

### PDF vom 21.09.2007 i.d.F. 07.07.2010

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik.md)

**Pflichtmodule (1):**
- unbenoteter Schein

### FPOAI 20201111 i.d.F. 20220726.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111-idf-20220726.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111-idf-20220726.md)

**Pflichtmodule (2):**
- Masterarbeit
- S-Punkte<sup>3)</sup>:

### FPOAI 20201111 i.d.F. 20230323.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111-idf-20230323.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111-idf-20230323.md)

**Pflichtmodule (2):**
- Masterarbeit
- S-Punkte<sup>3)</sup>:

### FPOAI 20201111.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111.md)

**Pflichtmodule (2):**
- Masterarbeit
- nkte<sup>2)</sup>:

### FPOMScAI 20240328.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpomscai-20240328.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpomscai-20240328.md)

**Pflichtmodule (2):**
- Masterarbeit
- Punkte<sup>3)</sup>:

### PDF vom 16.01.2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/sto-po-ba-it-sicherheit.md`](../pruefungsordnungen/technische-fakultaet/informatik/sto-po-ba-it-sicherheit.md)

**Pflichtmodule (19):**
- Grundlagen der Programmierung
- Mathematik 1
- Konzeptionelle Modellierung
- Mathematik 2
- Rechnerstrukturen
- Systemsicherheit 1
- Algorithmen und Datenstrukturen
- Theoretische Informatik
- Kryptographie 1
- Systemnahe Programmierung
- Systemsicherheit 2
- Proseminar
- Einführung in die digitale Forensik
- Compilerbau
- Netzsicherheit 1
- Kryptographie 2
- Netzsicherheit 2
- Realisierung von Softwareprojekten
- Bachelorarbeit

### PDF vom 03.03.2003 i.d.F. 22.02.2007

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/maschinenbau/fpo-maschinenbau-neu.md`](../pruefungsordnungen/technische-fakultaet/maschinenbau/fpo-maschinenbau-neu.md)

**Pflichtmodule (1):**
- ECTS- Punkte

### 2. Juli 2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/7aes-ba-ma-nanotechnologie.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/7aes-ba-ma-nanotechnologie.md)

**Pflichtmodule (11):**
- M1 Nanocharakterisierung (Pflicht)
- (2) Elektronenmikroskopie
- (2) NanoSpektroskopie
- (2) Rastersondenmikroskopie/ Nanoinden- tierung
- M3 Computational Nanoscience (Pflicht)
- (2) Computational Nanoscience
- M4 Top-Down Nanostrukturierung (Pflicht)
- (2) Nanoelektronik
- (2) Photolithographie
- (2) Beschichtungstechnologie
- (2) MolekulareNanostrukturen

### Elite-MA Advanced Materials and Processes FPO MAP 20060515 i.d.F. 20190115.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-20060515-idf-20190115.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-20060515-idf-20190115.md)

**Pflichtmodule (2):**
- Masterarbeit Kolloquium
- Masterarbeit

### Elite-MA Advanced Materials and Processes FPO MAP-M 20190115 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-m-20190115-aes.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-m-20190115-aes.md)

**Pflichtmodule (2):**
- Masterarbeit Kolloquium
- Masterarbeit

### PDF vom 25.09.2007 i.d.F. 17.01.2011

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/fpo-ba-ma-ww-17jan2011.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/fpo-ba-ma-ww-17jan2011.md)

**Pflichtmodule (2):**
- otete Studienleist
- er Regel im Kernfach das Modul M1 (Kernfach) sein. S auf Übungen und Praktika kann beliebig erfolgen.

### PDF vom 15.12.2008 i.d.F. 02.07.2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/fpo-nanotechnologie-ba-ma-juli2015.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/fpo-nanotechnologie-ba-ma-juli2015.md)

**Pflichtmodule (1):**
- (130) Umfang
