---
kind: "campo-pflichtmodule-aus-po"
po_files_with_pflicht_modules: 792
total_pflicht_modules: 8076
scraped_at: 2026-05-21T21:42:11+00:00
---

# Pflichtmodule — direkt aus PO-Anlagen extrahiert

Diese Datei sammelt strukturierte Pflichtmodul-Listen, die wir aus den *Studienverlaufsplan*- und *Curricular-Übersicht*-Tabellen der FAU-Prüfungsordnungen gelesen haben (Markdown-Tables, vom PyMuPDF4LLM-Konverter aus den PDF-Anlagen erzeugt). Pro PO wird die Sektion verfolgt — Module aus Sektionen *Grundlagen*, *Pflichtbereich*, *Basismodule*, *Kernbereich*, *Bachelorarbeit*, *Masterarbeit* gelten als Pflicht. *Wahlpflicht*, *Wahlbereich*, *Aufbaumodule*, *Vertiefungsmodule*, *Schwerpunkte* und *Schlüsselqualifikationen* werden ausgenommen.

## Vorbehalte

* **Vollständigkeit:** ~74 % der PO-Markdown-Dateien enthalten   überhaupt erkennbare Tabellen; davon haben wieder nur ~30 %   klare Pflicht-Section-Marker. Etwa die Hälfte aller POs liefert   hier deshalb noch kein Ergebnis — bei vielen ist die Anlage als   **Bild** im PDF eingebettet (typisches Beispiel: *Curricular-  Übersicht* als Diagramm) und entzieht sich der Text-Extraktion.
* **Modul-Name vs. Veranstaltungs-Titel:** ein Pflichtmodul   *Analysis I* erscheint in Campo als *Vorlesung Analysis I* +   *Übung Analysis I* + *Tafelübung Analysis I*. Hier wird nur das   Modul gelistet; das Cross-Mapping zu Campo-Veranstaltungen   übernimmt die Heuristik in `pflichtveranstaltungen.md` bzw.   ein RAG-Agent zur Anfragezeit.
* **Modul-Reihenfolge:** Module erscheinen in der Reihenfolge des   Studienverlaufsplans (typisch nach Fachsemester sortiert).

**Statistik:** 792 POs lieferten zusammen 8076 eindeutige Pflichtmodul-Einträge.

## Pro PO

### 30. September 2015

PO-Quelle: [`pruefungsordnungen/lehramt/7aes-lapo-allgemein.md`](../pruefungsordnungen/lehramt/7aes-lapo-allgemein.md)

**Pflichtmodule (5):**
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungs- kompetenzen in der Mittel- schule
- Basismodul Berufsorientierung1
- Masterarbeit

### BMPO BP-T 20230928 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/bmpo-bp-t-20230928-aes.md`](../pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/bmpo-bp-t-20230928-aes.md)

**Pflichtmodule (1):**
- vgl.§ 4 FPO WiWi

### PO ZS Geow im LA 20250320 .pdf

PO-Quelle: [`pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/po-zs-geow-im-la-20250320.md`](../pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/po-zs-geow-im-la-20250320.md)

**Pflichtmodule (4):**
- Grundlagen der Geowissenschaften I
- Rohstoffe und Nachhaltigkeit
- Dynamik des Systems Erde
- Kompetenzseminar zum Klimawandel

### pdf vom 19.02.2009

PO-Quelle: [`pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/sto-po-berufspaedagogik-eei.md`](../pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/sto-po-berufspaedagogik-eei.md)

**Pflichtmodule (34):**
- Grundlagen der Elektrotechnik, Energie und Antriebstechnik
- Grundlagen der Elektrotechnik I (GOP)
- Grundlagen der Elektrotechnik II (GOP)
- Grundlagen der Elektrotechnik III
- Praktikum Grundlagen der Elektrotechnik
- Grundlagen der Elektrischen Antriebstechnik
- Grundlagen der Elektrischen Energieversorgung
- Informatik und Mathematik
- Mathematik A1 oder B1 (GOP)
- Mathematik A2 oder B2 (GOP)
- Mathematik A3 oder B3
- Grundlagen der Informatik (GOP)
- Hochfrequenztechnik
- Hochfrequenztechnik I
- Passive Bauelemente und deren HF-Verhalten
- Kommunikationselektronik und Schaltungstechnik
- Digitaltechnik
- Halbleiterbauelemente
- Schaltungstechnik
- Praktikum Schaltungstechnik
- Kommunikationselektronik
- Systeme und Regelungen
- Regelungstechnik A (Grundlagen)
- Einführung in die Systemtheorie
- Seminar und Laborpraktikum aus der Elektro- und Informationstech- nik
- Fachdidaktik Elektrotechnik und Informationstechnik I
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

**Pflichtmodule (5):**
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungs- kompetenzen in der Mittel- schule
- Basismodul Berufsorientierung1
- Masterarbeit

### pdf vom 23.02.2009 i.d.F. 01.12.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lapo-lehramt.md`](../pruefungsordnungen/lehramt/lapo-lehramt.md)

**Pflichtmodule (2):**
- Basismodul Lernprozesse gestal- ten:
- Theor. und method. Grundlagen

### 24. September 2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-franzoesisch-abws2010-2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-franzoesisch-abws2010-2011.md)

**Pflichtmodule (2):**
- Abschlussmodul Schriftliche Hausarbeit
- Schriftliche Hausarbeit

### 24. September 2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-franzoesisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-franzoesisch.md)

**Pflichtmodule (2):**
- Abschlussmodul Schriftliche Hausarbeit
- Schriftliche Hausarbeit

### 24. September 2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-italienisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-italienisch.md)

**Pflichtmodule (2):**
- Abschlussmodul Schriftliche Hausarbeit
- Schriftlichen Hausarbeit

### 24. September 2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-spanisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aes-20la-spanisch.md)

**Pflichtmodule (2):**
- Abschlussmodul Schriftliche Hausarbeit
- Schriftliche Hausarbeit

### 14. September 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aes-la-arbeitslehre.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aes-la-arbeitslehre.md)

**Pflichtmodule (7):**
- Grundlagen der Fachdidaktik (GFD)
- Grundlagen der Fachwissenschaft (GFW)
- Medien und Methoden I (MuM I)
- Seminar mit Methodenschwerpunkt
- Medien und Methoden II (MuM II)2
- methodische Begleitveranstaltung zum Praktikum
- Arbeit und Beruf

### 26. Juni 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aesa-la-mathe.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aesa-la-mathe.md)

**Pflichtmodule (33):**
- Analysis I
- Übung Analysis I
- Tafelübung Analysis I
- Lineare Algebra I
- Übun Lineare Alebra I
- Tafelübung Lineare Algebra I
- Analysis II
- Übung Analysis II
- Tafelübung Analysis II
- Lineare Algebra II
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II
- Angewandte Mathematik
- Stochastische ModellbildungIa
- Stochastische Mo- dellbildung Ib
- Tafelübung Stochastische Mo-
- dellbildung
- Algebra Ia
- Vorlesung Algebra
- Algebra Ib
- Elemente der Linearen Al- gebra I1
- oresung emene er Linearen Alebra I
- Übung Elemente der Linearen Algebra I
- Elemente der Linearen Al- gebra IIa2
- Elemente der Linearen Al- gebra IIb2
- Elemente der Analysis I2
- Übung Elemente der Analysis I
- Elemente der Analysis IIa~~1~~
- Elemente der Analysis IIb1
- Analytische Geometrie1
- Übung Analytische Geometrie
- Aufbaumodul Analysis2
- Übung Elemente der Analysis III

### 21. Oktober 2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-20la-mathematik.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-20la-mathematik.md)

**Pflichtmodule (26):**
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
- Aufbaumodul Analysis (AmAn)~~1~~
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

**Pflichtmodule (2):**
- Grundlagen der anorga- nisch-chemischen Labor- praxis
- Prüfungsvorbereitung

### 29. September 2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-franzoesisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-franzoesisch.md)

**Pflichtmodule (10):**
- Basismodul Französische Sprachpraxis 1
- Vocabulaire, idiomatique et civilisation I
- Communication orale
- Basismodul Französische Sprachpraxis 2
- Grammaire cours élémentaire II (groupe verbal)
- Phonétique pratique, orthophonie et intonation
- Basismodul Einführung in die Frankoromanistik
- Basisseminar französische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen
- Proseminar Fachdidaktik Französisch

### 27. September 2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-griechisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-griechisch.md)

**Pflichtmodule (6):**
- Vorlesung aus der Lateinischen Philologie_oder_Übung aus der Indogermanistik
- Prosa
- Lektüre
- Sprachübungen I
- SpracheIb
- Poesie

### 29. September 2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-italienisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-italienisch.md)

**Pflichtmodule (7):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I
- Basismodul Italienische Sprachpraxis 2
- Foneticapratica
- Tecniche di lettura
- Basismodul Einführung in die Italoromanistik
- Basisseminar Italienische Literaturwissenschaft

### 29. September 2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-spanisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-spanisch.md)

**Pflichtmodule (8):**
- Basismodul Spanische Sprachpraxis 1
- Cultura y comunicación oral
- Basismodul Spanische Sprachpraxis 2
- Fonética práctica
- Basismodul Einführung in die Iberoromanistik
- Basisseminar Spanische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen
- Proseminar Fachdidaktik Spanisch

### 27. Februar 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-wirtschaftswiss.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-wirtschaftswiss.md)

**Pflichtmodule (7):**
- Grundlagen der Fachdidaktik Wirtschaftswissenschaft en(Gymnasium)
- Praxisfelder der Fachdidaktik
- Seminar Planung, Durchführung und Reflexion im ökonomischen Fachunterricht
- Grundlagen der Fachdidaktik Wirtschaftswissenschaft en(Realschule)
- Berufsfeldorientierung
- Praxisfelder der Fachdidaktik Wirtschaftswissenschaft en
- Planung, Durchführung und Reflexion im Ökonomischen Fachunterricht

### 18. September 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/3aes-la-chemie.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/3aes-la-chemie.md)

**Pflichtmodule (2):**
- Grundlagen der anorga- nisch-chemischen Labor- praxis
- Prüfungsvorbereitung

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
- Tennis o. Tischtennis o. Badminton II inkl. Bewegungslernen und –beobachtung
- (4) Kompetenz in Bewegung und Gesundheit II
- Stärkung Gesundheitsressourcen 1
- StärkungGesundheitsressourcen 2
- (6) Kompetenz in Bewegung und Gesundheit III
- (3S) Interventionskonzepte und QM
- (3S) Projekt „Entwicklung und Umsetzung von Interventionen zur Gesundheitsförderung“
- Grundlagen der Sportpädagogik I (FD)*
- Ausgewählte Aspekte des Schulsports (FD)*
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

**Pflichtmodule (10):**
- Basismodul Französische Sprachpraxis 1
- Communication orale
- Basismodul Französische Sprachpraxis 2
- Parcoursgrammatical II
- Phonétiquepratique,orthophonie et intonation
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen
- der romanischen Sprachen1)
- Proseminar Fachdidaktik Französisch

### 8. August 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-italienisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-italienisch.md)

**Pflichtmodule (7):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I
- Basismodul Italienische Sprachpraxis 2
- Foneticapratica
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft

### 8. August 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-spanisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-spanisch.md)

**Pflichtmodule (10):**
- Basismodul Spanische Sprachpraxis 1
- Cultura y comunicación oral
- Español intermedio II
- Basismodul Spanische Sprachpraxis 2
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen
- Didaktik der romanischen
- Sprachen1)
- Proseminar Fachdidaktik Spanisch

### 2. April 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/4aes-la-griechisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/4aes-la-griechisch.md)

**Pflichtmodule (8):**
- Vorlesung Lateinische Philologie _oder_ÜbungIndogermanistik
- Prosa
- Lektüre
- Shüb I
- pracungen
- Poesie
- Sprachübungen II
- Sprache IIb

### 25. Oktober 2016

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/4aesa-la-sozialkunde.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/4aesa-la-sozialkunde.md)

**Pflichtmodule (14):**
- Grundlagen der politi- schen Bildung
- PolitischesLernen
- Methodik und Wertorien- tierung im Politikunterricht
- Methodik des PU: Metho- dik-Methoden-Modelle
- Grundlagen der politischen Bildung
- Methodik, Praxis und Wertorientierung im Politikunterricht
- Methodik des PU: Me- thodik-Methoden-Modelle
- Übung zur Planung, Durchführung und Kon- trolle des Politikunter- richts
- Methodik, Praxis und Wertorientierung im PU (FG GS)
- Methodik und Wertorientierung im Politikunterricht
- Praxis des Politikunterrichts
- Übung zur Planung, Durchführung und Kon- trolle desPU
- Praxisprobleme der Politischen Bil- dung
- Seminar zur Politikdidak- tik

### 14. Dezember 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/5aesa-la-ev-religion.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/5aesa-la-ev-religion.md)

**Pflichtmodule (31):**
- Basismodul: Theologie und wissenschaftliches Arbeiten
- Tutorium zum Einführungskurs
- RU in der Sek 1 (FD)
- Biblisches Grundwissen (Lehramt GS/MS/RS)
- Biblisches Grundwissen 2 (NT)
- Grundlagen der Theologie und Religionspädagogik
- Themen der Theologie im RU
- Biblih Thli 1 AT
- sce eooge ()
- Biblische Theologie 2 (NT)
- NT - Synoptische Evangelien/Jesus
- Biblih Thli 3
- sce eooge
- Systematische Theologie 1: Dogmatik (GMRS)
- Grundfragen der Dogmatik
- Systematische Theologie 2: Ethik (GMRS)
- Grundfragen christlicher Ethik
- Kirchengeschichte 1
- Religiöses Lernen und Kirchengeschichte
- Kihhiht 2
- rcengescce
- RU in der Grundschule bzw. Mittelschule (FD)
- Biblische Theologie 1 (AT)
- AT – Geschichte Israels
- Biblische Theologie 3
- NT – Themen neutestamentl. Theologie: Paulus
- Kirchengeschichte 2
- Christliche Kirchen und Gruppen – Ökumene
- Religionswissenschaft
- Judentum
- Islam

### 16. Januar 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/6aes-la-deutsch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/6aes-la-deutsch.md)

**Pflichtmodule (6):**
- Grundlagen der Germanistischen Linguistik (Ling1)
- Grundlagen der Germanistischen Mediävistik (Med 1)
- Grundlagen der Neueren deutschen Literatur (NdL 1)
- Grundlagen der Fachdidaktik Deutsch (BM FDD)
- Proseminar: Einführung in die Literatur- Sprach- und Mediendidaktik
- Vorlesung2

### 24. September 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/7aes-la-deutsch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/7aes-la-deutsch.md)

**Pflichtmodule (13):**
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

### 27. September 2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/7aes-la-englisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/7aes-la-englisch.md)

**Pflichtmodule (18):**
- Basismodul I Language
- Aufbauseminar
- Basismodul II Liii
- ngustcs
- Basismodul III Literature
- Basismodul IV Culture/Landeskunde
- Grundseminar mit Projektgruppen
- Zwischenmodul L‐GYM Linguistics
- Seminar (Sprachgeschichte)
- Zwischenmodul L‐GYM Literature
- Textanalyseseminar: Engl./Am. Literatur
- Zwischenmodul L‐GYM Language
- Phonetics I: Theory
- Phonetics II: Error Treatment
- Conversation Practice
- Basismodul Englischdidaktik
- Proseminar
- Basismodul Language

### 10. November 2016

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/8aes-la-dt-didaz.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/8aes-la-dt-didaz.md)

**Pflichtmodule (20):**
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1) Grundlagen der
- Analyseseminar 1 Einführungsseminar: Historische
- Germanistischen Linguistik 2 (Ling BM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1 (Med BM 1)
- Grundlagen der Germanistischen Mediävistik 2 (Med BM 2)
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Analyseseminar 1
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
- Analyseseminar 2
- Grundlagen der Germanistischen Mediävistik 2(Med BM 2)
- Basismodul DiDaZ (LA GS)
- Seminar2
- Tutorium
- Tutorium oder5Kolloquium
- Basismodul DiDaZ (LA MS)
- Seminar aus dem Bereich „Theorie und Praxis des Zweitspracherwerbs / der Mehrsprachigkeit“
- Seminar aus dem Bereich „Methoden, Verfahren,ArbeitsformenundMedien“
- Tutorium oder3Kolloquium

### FPO LA DaZ 20200203 i.d.F. 20201123.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-daz-20200203-idf-20201123.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-daz-20200203-idf-20201123.md)

**Pflichtmodule (20):**
- Basismodul DaZ (LA GS)
- Seminar2
- Tutorium
- Tutorium oder Kolloquium
- Basismodul DaZ (LA MS)
- Seminar aus dem Bereich „Theorie und Praxis desZweitspracherwerbs / der Mehrsprachigkeit“
- Seminar aus dem Bereich „Methoden, Verfahren, ArbeitsformenundMedien“
- Grundlagen des Deutschen als Zweit- sprache
- Theorie und Praxis der Sprach- vermittlung
- Sprache im Fachunterricht
- Linguistische Grundlagen
- Sprachsystem und Zithb
- wespracerwer
- Lehren und Lernen in der zweiten Sprache
- Medien im DaZ-Kontext
- Sprachgebrauch und Sprach- vermittlung
- Sprachvergleich unter didaktischen Aspekten3
- Sprachmodul 13
- Sprachmodul 23
- Praktikumsmodul

### FPO LA DaZ 20250702.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-daz-20250702.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-daz-20250702.md)

**Pflichtmodule (1):**
- Basismodul Partnersprache5

### FPO LA DiDaZ 20200203.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-didaz-20200203.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-didaz-20200203.md)

**Pflichtmodule (20):**
- Basismodul DiDaZ (LA GS)
- Seminar2
- Tutorium
- Tutorium oder Kolloquium
- Basismodul DiDaZ (LA MS)
- Seminar aus dem Bereich „Theorie und Praxis desZweitspracherwerbs / der Mehrsprachigkeit“
- Seminar aus dem Bereich „Methoden, Verfahren, ArbeitsformenundMedien“
- Grundlagen des Deutschen als Zweit- sprache
- Theorie und Praxis der Sprach- vermittlung
- Sprache im Fachunterricht
- Linguistische Grundlagen
- Sprachsystem und Zithb
- wespracerwer
- Lehren und Lernen in der zweiten Sprache
- Medien im DaZ-Kontext
- Sprachgebrauch und Sprach- vermittlung
- Sprachvergleich unter didak- tischen Aspekten
- Sprachmodul 1
- Sprachmodul 2
- Praktikumsmodul

### FPO LA Mathe 20151111 i.d.F. 20191010.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20191010.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20191010.md)

**Pflichtmodule (22):**
- Analysis I1)
- Übung Analysis I
- Tafelübung Analysis I
- Lineare Algebra I1)
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- Analysis II1)
- Übung Analysis II
- Tafelübung Analysis II
- Lineare Algebra II1)
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II
- Algebra2)
- Übung Algebra
- Tafelübung Algebra
- Körpertheorie2)
- Übung Körpertheorie
- Analysis für Lehramt
- Übung Analysis für Lehramt
- Tafelübung Analysis für Lehramt
- Funktionentheorie2)
- Übung Funktionentheorie I

### FPO LA Mathe 20151111 i.d.F. 20201029.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20201029.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20201029.md)

**Pflichtmodule (22):**
- Analysis I1)
- Übung Analysis I
- Tafelübung Analysis I
- Lineare Algebra I1)
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- Analysis II1)
- Übung Analysis II
- Tafelübung Analysis II
- Lineare Algebra II1)
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II
- Algebra2)
- Übung Algebra
- Tafelübung Algebra
- Körpertheorie2)
- Übung Körpertheorie
- Analysis für Lehramt
- Übung Analysis für Lehramt
- Tafelübung Analysis für Lehramt
- Funktionentheorie2)
- Übung Funktionentheorie I

### FPO LA Mathe 20151111 i.d.F. 20230426.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20230426.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20230426.md)

**Pflichtmodule (34):**
- Analysis I1)
- Übung Analysis I
- Tafelübung Analysis I
- Lineare Algebra I1)
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- Analysis II1)
- Übung Analysis II
- Tafelübung Analysis II
- Lineare Algebra II1)
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II
- Algebra2)
- Übung Algebra
- Tafelübung Algebra
- Körpertheorie2)
- Übung Körpertheorie
- Analysis für Lehramt
- Übung Analysis für Lehramt
- Tafelübung Analysis für Lehramt
- Funktionentheorie2)
- Übung Funktionentheorie I
- Elemente der Linearen Algebra I1)
- Übung Elemente der Linearen AlgebraI
- Elemente der Linearen Algebra II2)
- Übung Elemente der Linearen Algebra II
- Elemente der Analysis I2)
- Übung Elemente der Analysis I
- Elemente der Analysis II1)
- Übung Elemente der Analysis II
- Analytische Geometrie1)
- Übung Analytische Geometrie
- Aufbaumodul Analysis2)
- Übung Elemente der Analysis III

### FPO LA Mathe 20260331.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20260331.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20260331.md)

**Pflichtmodule (35):**
- Analysis I1)
- Übung Analysis I
- Tafelübung Analysis I
- Vorlesung Lineare Algebra I
- Lineare Algebra I1)
- Tafelübung Lineare Algebra I
- Analysis II1)
- Übung Analysis II
- Tafelübung Analysis II
- Vorlesung Lineare Algebra II
- Lineare Algebra II1)
- Tafelübung Lineare Algebra II
- Algebra2)
- Übung Algebra
- Tafelübung Algebra
- Körpertheorie2)
- Übung Körpertheorie
- Analysis für Lehramt
- Übung Analysis für Lehramt
- Tafelübung Analysis für Lehramt
- Funktionentheorie2)
- Übung Funktionentheorie I
- Mathematikdidaktik 1: Gymnasium (MD1Gym)
- Vorlesung: Didaktik im Bereich Zahl und Operation, Muster und funktionaler Zusammenhang _oder_ Vorlesung: Didaktik im Bereich Raum und Form
- Elemente der Analysis II1)
- Übung Elemente der Analysis II
- Analytische Geometrie1)
- Übung Analytische Geometrie
- Aufbaumodul Analysis2)
- Übung Elemente der Analysis III
- Mathematikdidaktik 1: Sekundarstufe I (MD1SekI)
- Vorlesung: Didaktik im Bereich Zahl und Operation, Muster und funktionaler Zusammenhang
- Mathematikdidaktik Planung (MDPlan)
- Zentrale Gegenstände der Sekundarstufenmathemati k (MSMathe)
- Vorlesung mit Übung: Zentrale Gegenstände im Bereich Raum und Form, Daten und Zufall

### LA Arbeitslehre FPO LA ArbL 20090727 i.d.F. 20190913.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-arbeitslehre-fpo-la-arbl-20090727-idf-20190913.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-arbeitslehre-fpo-la-arbl-20090727-idf-20190913.md)

**Pflichtmodule (7):**
- Grundlagen der Fach- didaktik (GFD)
- Grundlagen der Fach- wissenschaft (GFW)
- Medien und Methoden I (MuM I)
- Seminar mit Methoden- schwerpunkt
- Medien und Methoden II (MuM II)2
- methodische Begleitveran- staltung zum Praktikum
- Arbeit und Beruf (AuB)

### LA Beruf und Wirtschaft FPO LA BuW 20090727 i.d.F. 20210301.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-beruf-und-wirtschaft-fpo-la-buw-20090727-idf-20210301.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-beruf-und-wirtschaft-fpo-la-buw-20090727-idf-20210301.md)

**Pflichtmodule (7):**
- Grundlagen der Fach- wissenschaft (GFW)
- Grundlagen der Fach- didaktik (GFD)
- Medien und Methoden I (MuM I)
- Seminar mit Methoden- schwerpunkt
- Medien und Methoden II (MuM II)2
- methodische Begleitveran- staltung zum Praktikum
- Arbeit und Beruf (AuB)

### LA Chin ÄSa 20260331.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-chin-aesa-20260331.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-chin-aesa-20260331.md)

**Pflichtmodule (2):**
- Basismodul Chinesischdi- daktik
- Übung zum Seminar: Chine- sischdidaktik I

### LA Deutsch FPO LA Deutsch 20090226 i.d.F. 20200203.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20200203.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20200203.md)

**Pflichtmodule (18):**
- Grundlagen der Germanistischen Linguistik 1(LingBM 1)
- Grundlagen der Germanistischen Linguistik 2(LingBM 2)
- Grundlagen der Neueren deut- schen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deut- schen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1 (Med BM 1)
- Grundlagen der Germanistischen Mediävistik 2(MedBM 2)
- Basismodul Fachdidaktik Deutsch (BM FDD)
- Proseminar
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

### LA Deutsch FPO LA Deutsch 20090226 i.d.F. 20200923.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20200923.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20200923.md)

**Pflichtmodule (14):**
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1(MedBM 1)
- Grundlagen der Germanistischen Mediävistik 2(MedBM 2)
- Basismodul Fachdidaktik Deutsch (BM FDD)
- Proseminar
- Grundlagen der Neueren deutschen Literatur- wissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literatur- wissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik (Med-BM-LANV)
- Grundlagen der Germanistischen Linguistik 1 (LingBM 1)
- Grundlagen der Germanistischen Linguistik 2 (LingBM 2)
- Grundlagen der Germanistischen Mediävistik(MedBM LANV)

### LA Deutsch FPO LA Deutsch 20090226 i.d.F. 20220914.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20220914.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20220914.md)

**Pflichtmodule (14):**
- Basismodul Fachdidaktik Deutsch (BM FDD)
- Proseminar
- Ling BM-12 Grundlagen der germanisti- schen Linguistik
- NdL BM-14 Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- ren der Neueren deutschen
- Literaturwissenschaft 1
- Ling BM-22 Grundlagen der historischen Linguistik
- Geschichte der deutschen Sprache
- NdL BM-24 Grundlagen der Neueren deut- schen Literaturwissenschaft 2
- Literaturwissenschaft 2
- Med BM nv4 Grundlagen der Germanisti- schen Mediävistik – nicht ver- tieftes LA
- Einführungsseminar: Mediävisti-
- sche Literatur- und Kulturwissen-
- schaft

### LA Deutsch FPO LA Deutsch 20200203 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20200203-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20200203-aes.md)

**Pflichtmodule (2):**
- Basismodul Fachdidaktik Deutsch (BM FDD)
- Proseminar

### LA Deutsch FPO LA Deutsch 20220914 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20220914-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20220914-aes.md)

**Pflichtmodule (11):**
- Ling BM-12 Grundlagen der germanistischen Linguistik
- Lit BM4 Grundlagen des wissenschaftli- chen Arbeitens in der Literatur- wissenschaft
- NdL BM-15 Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- Ling BM-22 Grundlagen der historischen Linguistik
- Geschichte der deutschen Sprache
- Med BM6 Grundlagen der Germanisti- schen Mediävistik
- NdL BM-25 Grundlagen der Neueren deut- schen Literaturwissenschaft 2
- Ling BM-12 Grundlagen der germanisti- schen Linguistik
- NdL BM-14 Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- NdL BM-24 Grundlagen der Neueren deut- schen Literaturwissenschaft 2
- Med BM nv4 Grundlagen der Germanisti- schen Mediävistik – nicht ver- tieftes LA

### LA Englisch 20090226 i.d.F. 20200124.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20090226-idf-20200124.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20090226-idf-20200124.md)

**Pflichtmodule (28):**
- Basismodul I Language
- GLC(II)
- Basismodul II Linguistics (A)
- Basismodul III
- Linguistics (B)
- Basismodul IV Literature(A)
- Basismodul V Literature(B)
- Basismodul VI Culture
- Basismodul VII Landeskunde
- Landeskunde Workshop
- Zwischenmodul L-GYM Linguistics
- Seminar (Sprachgeschichte)
- Zwischenmodul L-GYM Literature
- Textanalyseseminar: Engl./Am. Literatur
- Zwischenmodul L-GYM Language
- Writing Skills
- Basismodul Englischdidaktik
- Mittelseminar
- Basismodul Language
- GLC II
- Elementarmodul L-UF Linguistics I
- Elementarmodul L-UF Linguistics II
- Elementarmodul L-UF Literature I
- Elementarmodul L-UF Literature II
- LK US/UK
- Elementarmodul L-UF Ldkd
- anesune
- Zwischenmodul L-UF Language

### LA Englisch 20200124 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20200124-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20200124-aes.md)

**Pflichtmodule (28):**
- Basismodul I Language
- GLC(II)
- Basismodul II Linguistics (A)
- Basismodul III
- Linguistics (B)
- Basismodul IV Literature(A)
- Basismodul V Literature(B)
- Basismodul VI Culture
- Basismodul VII Landeskunde
- Landeskunde Workshop
- Zwischenmodul L-GYM Linguistics
- Seminar (Sprachgeschichte)
- Zwischenmodul L-GYM Literature
- Textanalyseseminar: Engl./Am. Literatur
- Zwischenmodul L-GYM Language
- Writing Skills
- Basismodul Englischdidaktik
- Mittelseminar
- Basismodul Language
- GLC II
- Elementarmodul L-UF Linguistics I
- Elementarmodul L-UF Linguistics II
- Elementarmodul L-UF Literature I
- Elementarmodul L-UF Literature II
- LK US/UK
- Elementarmodul L-UF Ldkd
- anesune
- Zwischenmodul L-UF Language

### LA Erweiterungsfach Chinesisch FPO LA Chin. 20161111 i.d.F. 20190828.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20161111-idf-20190828.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20161111-idf-20190828.md)

**Pflichtmodule (2):**
- Basismodul Chine- sischdidaktik
- Übung zum Seminar: Chinesischdidaktik I

### LA Erweiterungsfach Chinesisch FPO LA Chin. 20230822 i.d.F. 20260331.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822-idf-20260331.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822-idf-20260331.md)

**Pflichtmodule (2):**
- Basismodul Chinesischdidak- tik
- Übung zum Seminar: Chinesisch- didaktik I

### LA Erweiterungsfach Chinesisch FPO LA Chin. 20230822.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822.md)

**Pflichtmodule (2):**
- Basismodul Chinesischdi- daktik
- Übung zum Seminar: Chine- sischdidaktik I

### LA Französisch 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-20210624-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-20210624-aes.md)

**Pflichtmodule (7):**
- Basismodul Französische Sprachwissenschaft3
- Basismodul Französische Literaturwissenschaft4
- Französische Sprachpraxis 32
- Traduction version1
- Communication orale et civilisation5
- Basismodul Didaktik der romanischen Sprachen
- Proseminar Fachdidaktik Französisch

### LA Französisch FPO LA Französisch 20090309 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-fpo-la-franzoesisch-20090309-idf-20210624.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-fpo-la-franzoesisch-20090309-idf-20210624.md)

**Pflichtmodule (7):**
- Basismodul Französische Sprachwissenschaft3
- Basismodul Französische Literaturwissenschaft4
- Französische Sprachpraxis 32
- Traduction version1
- Communication orale et civilisation5
- Basismodul Didaktik der romanischen Sprachen
- Proseminar Fachdidaktik Französisch

### LA Geschichte FPO LA Geschichte 20090310 i.d.F. 20180911.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20090310-idf-20180911.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20090310-idf-20180911.md)

**Pflichtmodule (14):**
- Basismodul I
- Basismodul II
- Basismodul III
- Basismodul IV
- Methodische und Theoretische Grundlagen
- Methodische Grundlagen
- Theoretische Grundlagen
- Landesgeschichte
- Basismodul Didaktik der Geschichte
- Konkretion Geschichtskultur
- Basismodul I2
- Basismodul II3
- Basismodul III4
- Konkretion Ge- schichtskultur

### LA Geschichte FPO LA Geschichte 20180911 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20180911-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20180911-aes.md)

**Pflichtmodule (9):**
- Basismodul I
- Basismodul II
- Basismodul III
- Basismodul IV
- Basismodul Didaktik der Geschichte
- Konkretion Geschichtskultur
- Basismodul I2
- Basismodul II3
- Landesgeschichte

### LA Griechisch FPO LA Griechisch 20090310 i.d.F. 20200806.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-griechisch-fpo-la-griechisch-20090310-idf-20200806.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-griechisch-fpo-la-griechisch-20090310-idf-20200806.md)

**Pflichtmodule (9):**
- Vorlesung Lateinische Philologie_o-_ _der_ ÜbungIndogermanistik
- Prosa
- Lektüre
- Shüb I
- pracungen
- Poesie
- rosa
- Sprachübungen II
- Sprache IIb

### LA Informatik FPO LA INF 20220421.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20220421.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20220421.md)

**Pflichtmodule (24):**
- Grundlagen der Programmierung
- Grundlagen der Programmierung UE
- Sichere Systeme
- Sichere Systeme UE
- Einführung in die Algorithmik
- Einführung in die Algorithmik UE
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende UE
- Parallele und funktionale Programmierung
- Parallele und funktionale Programmierung UE
- Softwareentwicklung in Großprojekten*
- Softwareentwicklung in GroßprojektenUE
- Konzeptionelle Modellierung und Grundlagen von Datenbanken
- Konzeptionelle Modellie- rung und Grundlagen von DatenbankenUE
- Grundlagen der Systemprogrammie- rung
- Grundlagen der System- programmierung UE
- Grundlagen des Maschinellen Lernens und der Künstlichen Intelligenz
- Softwareentwicklung in Großprojekten UE
- Konzeptionelle Modellie- rung und Grundlagen von Datenbanken
- Konzeptionelle Modellie- rung und Grundlagen von Datenbanken UE
- Praktikum Maschinen- programmierung
- Grundlagen der Programmie- rung UE
- Konzeptionelle Modellierung und Grundlagen von Datenbanken UE
- Praktikum Informatik

### LA Informatik FPO LA INF 20240904.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20240904.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20240904.md)

**Pflichtmodule (27):**
- Grundlagen der Programmierung
- Grundlagen der Programmierung UE
- Sichere Systeme
- Sichere Systeme UE
- Einführung in die Algorithmik
- Einführung in die Algorithmik UE
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende UE
- Parallele und funktionale Programmierung
- Parallele und funktionale Programmierung UE
- Einführung in das Software Engineering
- Einführung in das Softwareengineering UE
- Einführung in Datenbanken
- Einführung in Datenbanken UE
- Praktikum Maschinenprogrammierung
- Grundlagen der Systemprogrammierung
- Grundlagen der Systemprogrammierung UE
- Grundlagen des Maschinellen Lernens und der Künstlichen Intelligenz
- Einführung in das Software Engineering UE
- Theoretische Informatik für Wirtschaftsinformatik
- Praktikum Informatik
- Praktikum Maschinen- programmierung
- Grundlagen der Informatik(GdI-Kompakt)
- Grundlagender InformatikUE
- Didaktik der Informatik 1
- Curriculare Themen der Fachdidaktik Informatik VÜ
- Praktikum zur Anwendung von Informatiksystemen aus fachdidaktischerSicht

### LA Italienisch 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-20210624-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-20210624-aes.md)

**Pflichtmodule (10):**
- Basismodul Italienische Sprachpraxis 11
- Mündliche Sprachkompetenz I (Comprensione e produzione oraleI)
- Basismodul Italienische Sprachpraxis 21, 2
- Fonetica pratica
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft4
- Basismodul Italienische Literaturwissenschaft5
- Basismodul Didaktik der romanischen Sprachen
- der romanischen Sprachen1
- Proseminar Fachdidaktik Italienisch

### LA Italienisch FPO LA Italienisch 20090325 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-fpo-la-italienisch-20090325-idf-20210624.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-fpo-la-italienisch-20090325-idf-20210624.md)

**Pflichtmodule (10):**
- Basismodul Italienische Sprachpraxis 11
- Mündliche Sprachkompetenz I (Comprensione e produzione oraleI)
- Basismodul Italienische Sprachpraxis 21, 2
- Fonetica pratica
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft4
- Basismodul Italienische Literaturwissenschaft5
- Basismodul Didaktik der romanischen Sprachen
- der romanischen Sprachen1
- Proseminar Fachdidaktik Italienisch

### LA Katholische Religionslehre 20210415 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-20210415-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-20210415-aes.md)

**Pflichtmodule (2):**
- Basismodul Grundlagen der Fachdidaktik
- Hauptseminar systematische Theologie und ihre Didaktik

### LA Katholische Religionslehre FPO LA KathRel 20090727 i.d.F. 20210415.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20090727-idf-20210415.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20090727-idf-20210415.md)

**Pflichtmodule (2):**
- Basismodul Grundlagen der Fachdidaktik
- Hauptseminar systematische Theologie und ihre Didaktik

### LA Katholische Religionslehre FPO LA KathRel 20240118.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20240118.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20240118.md)

**Pflichtmodule (3):**
- Basismodul Grundlagen der Fachdidaktik
- Hauptseminar Religiöses Lernen
- Hauptseminar Religiöses Ler- nen

### LA Mathematik  FPO LA Mathe 20191010 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-fpo-la-mathe-20191010-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-fpo-la-mathe-20191010-aes.md)

**Pflichtmodule (22):**
- Analysis I1)
- Übung Analysis I
- Tafelübung Analysis I
- Lineare Algebra I1)
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- Analysis II1)
- Übung Analysis II
- Tafelübung Analysis II
- Lineare Algebra II1)
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II
- Algebra2)
- Übung Algebra
- Tafelübung Algebra
- Körpertheorie2)
- Übung Körpertheorie
- Analysis für Lehramt
- Übung Analysis für Lehramt
- Tafelübung Analysis für Lehramt
- Funktionentheorie2)
- Übung Funktionentheorie I

### LA Mathematik FPO LA Mathe 20201029 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-fpo-la-mathe-20201029-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-fpo-la-mathe-20201029-aes.md)

**Pflichtmodule (22):**
- Analysis I1)
- Übung Analysis I
- Tafelübung Analysis I
- Lineare Algebra I1)
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- Analysis II1)
- Übung Analysis II
- Tafelübung Analysis II
- Lineare Algebra II1)
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II
- Algebra2)
- Übung Algebra
- Tafelübung Algebra
- Körpertheorie2)
- Übung Körpertheorie
- Analysis für Lehramt
- Übung Analysis für Lehramt
- Tafelübung Analysis für Lehramt
- Funktionentheorie2)
- Übung Funktionentheorie I

### pdf vom 11.11.2015 i.d.F. 26.06.2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-juni2017.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-juni2017.md)

**Pflichtmodule (30):**
- Stochastische Modellbildung Ia
- Stochastische Modellbildung Ib
- Tafelübung Stochastische
- Modellbildung
- Algebra Ia
- Vorlesung Algebra
- bung Algebra
- gebra b
- aeung gera
- Vorlesung Körpertheorie
- örperteore
- ung rperteore
- Analysis für Lehramt Ia
- Analysis für
- LehramtIb
- Geometrie
- Elemente der Linearen Algebra I1
- Vorlesung Elemente der LiAlbI
- nearengera
- Übung Elemente der Linearen Algebra I
- Elemente der Linearen Algebra IIa2
- Elemente der Linearen Algebra IIb2
- Elemente der Analysis I2
- Übung Elemente der Analysis I
- Elemente der Analysis IIa1
- Elemente der Analysis IIb1
- Analytische Geometrie1
- Übung Analytische Geometrie
- Aufbaumodul Analysis2
- Übung Elemente der Analysis III

### pdf vom 11.11.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-ws2015-2016.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-ws2015-2016.md)

**Pflichtmodule (31):**
- Analysis I
- Übung Analysis I
- Tafelübung Analysis I
- Lineare Algebra I
- ÜbungLineare Algebra I
- Tafelübung Lineare Algebra I
- Analysis II
- ÜbungAnalysis II
- Tafelübung Analysis II
- Lineare Algebra II
- ÜbungLineare Algebra II
- Tafelübung Lineare Algebra II
- Angewandte Mathematik
- Stochastische Modellbildung
- Übung Stochastische Modellbil- dung
- Tafelübung Stochastische Mo- dellbildung
- Algebra
- Übung Algebra
- Tafelübung Algebra
- Körpertheorie
- Elemente der Linearen Algebra I1
- Vorlesung Elemente der
- Linearen Algebra I
- Übung Elemente der Linearen AlgebraI
- Elemente der Linearen Algebra II2
- Linearen Algebra II
- Übung Elemente der Linearen Algebra II
- Elemente der Analysis I2
- Übung Elemente der Analysis I
- Elemente der Analysis II1
- Übung Elemente der AnalysisII

### LA Musik 20220601 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-musik-20220601-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-musik-20220601-aes.md)

**Pflichtmodule (10):**
- Grundlagen fachbezogenen Leh- rens und Lernens
- Fachdidaktisches Lernen, Lehren und Beurteilen
- Grundlagen und musikalische Praxis
- Musikalische Praxis 1
- Musikalische Praxis 2
- FachbezogenesLehrenundLernen
- Modelle musikalischer Praxis
- Grundlagen des Musikunterrichts
- Fachbezogenes Lehren und Lernen: Praxis des Musikunterrichts
- Fachwissenschaft

### LA Musik FPO LA Musik 20090326 i.d.F. 20220601.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-musik-fpo-la-musik-20090326-idf-20220601.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-musik-fpo-la-musik-20090326-idf-20220601.md)

**Pflichtmodule (9):**
- Grundlagen fachbezogenen Lehrens und Lernens
- Fachdidaktisches Lernen, Lehren und Beurteilen
- Grundlagen und musikalische Praxis
- Musikalische Praxis 1
- Musikalische Praxis 2
- FachbezogenesLehrenundLernen
- Modelle musikalischer Praxis
- Grundlagen des Musikunterrichts
- Fachwissenschaft

### LA Spanisch 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-spanisch-20210624-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-spanisch-20210624-aes.md)

**Pflichtmodule (9):**
- Basismodul Spanische Sprachwissenschaft5
- Basismodul Spanische Literatur- wissenschaft6
- Spanische Sprachpraxis 31, 3
- Gramática y estilística I
- Basismodul Didaktik der romanischen Spra- chen
- Didaktik der romanischen
- Sprachen1
- Proseminar Fachdidaktik
- Spanisch

### LA Spanisch FPO LA Spanisch 20090401 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-spanisch-fpo-la-spanisch-20090401-idf-20210624.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-spanisch-fpo-la-spanisch-20090401-idf-20210624.md)

**Pflichtmodule (6):**
- Basismodul Spanische Sprachwissenschaft5
- Basismodul Spanische Literatur- wissenschaft6
- Spanische Sprachpraxis 31, 3
- Gramática y estilística I
- Basismodul Didaktik der romanischen Sprachen
- Proseminar Fachdidaktik Spanisch

### LA Wirtschaftswissenschaften FPO LA WiWi 20090401 i.d.F. 20210225.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-wirtschaftswissenschaften-fpo-la-wiwi-20090401-idf-20210225.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-wirtschaftswissenschaften-fpo-la-wiwi-20090401-idf-20210225.md)

**Pflichtmodule (9):**
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Wirtschaftsprivatrecht
- Grundlagen der Fachdidaktik Wirtschaftswissenschaften (Gymnasium)
- Praxisfelder der Fachdidaktik
- Seminar Planung, Durchführung und Reflexion im ökonomischen Fachunterricht
- Grundlagen der Fachdidaktik Wirtschaftswissenschaften (Realschule)
- Berufsfeldorientierung
- Praxisfelder der Fachdidaktik Wirtschaftswissenschaften
- Planung, Durchführung und Reflexion im Ökonomischen Fachunterricht

### pdf vom 26.02.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20deutsch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20deutsch.md)

**Pflichtmodule (20):**
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
- Einführungskurs~~1~~: Einführung in die Neuere deutsche Literatur- wissenschaft
- Kolloquium zur Besprechung der SchriftlicheHausarbeit
- Examensvorbereitung
- ExamenskursNDL
- Examenskurs Sprachwissenschaft
- Grundkurs: Einführung in die GermanistischeLinguistik
- Einführungskurs~~2~~: Einführung in die Neuere deutsche Literatur- wissenschaft
- VorlesungmitÜbung: Fachdidak-

### pdf vom 26.02.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20ev-20religion.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20ev-20religion.md)

**Pflichtmodule (1):**
- (4) Pflichtmodul Praktikum

### pdf vom 09.03.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20franzoesisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20franzoesisch.md)

**Pflichtmodule (16):**
- Vertiefungsmodul Französische Sprachwissenschaft 2
- Mittelseminar
- Vertiefungsmodul Französische Literatur- und Kulturwissenschaft 2
- Abschlussmodul Schriftliche Hausarbeit
- Kolloquium zur Besprechung der Schriftlichen Hausarbeit
- SchriftlicheHausarbeit
- Abschlussmodul Schriftliche
- Hausarbeit
- Fachdidaktisches Modul 1: Einführung
- in die Didaktik des Französischen
- Übung: Einführung in die Fachdidaktik desFranzösischen
- Proseminar / Übung
- Fachdidaktisches Modul 2: Didaktik des Französischen (Lehramt Realschulen)
- Übung zur Didaktik der französischen Sprache an RS
- Mittelseminar: Französische Sprach- und Kulturvermittlung an RS
- Angeleitete Lektüre

### pdf vom 25.03.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20informatik.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20informatik.md)

**Pflichtmodule (2):**
- Grundlagen der Technischen Informatik
- Systemprogrammierung

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
- Vorlesung: Lateinische Literatur (Prosa)
- Proseminar: Lateinische Literatur (Prosa)
- Basismodul: Lateinische Sprachwissenschaft und Sprachpraxis (SPR 1)
- Übung: Deutsch-lateinische Ü- bersetzung (Grundlagen 1)
- Übung: Deutsch-lateinische Ü- bersetzung (Grundlagen 2)
- Übung: Lateinisch-deutsche Ü- bersetzung (Grundlagen)
- Basismodul: Altertumswissen- schaft für Latinisten (AWS 1)
- Vorlesung / Übung Alte Ge- schichte
- Vorlesung / Übung Klassische Archäologie
- Exkursion mit Vorbereitungskurs
- ammen 6
- Examensvorbereitung
- Examenskurs zur Klausurvorbe- reitung
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
- Orientierungsseminar~~2~~(OrSe)
- Teil 1
- Teil 2
- Algebra(Alg)
- Übungen
- Stochastische Modellbildung (StMo)
- Mehrdimensionale Integration (MInt)
- Vorlesung/Übung
- Angewandte Mathematik1 (AMLA)
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

**Pflichtmodule (9):**
- Grundlagen der Germanistischen Linguistik (Ling1)
- Grundlagen der Germanisti- schen Mediävistik (Med1)
- Grundlagen der Neueren deutschen Literatur (NdL 1)
- Grundlagen der Fachdidaktik Deutsch (BM FDD)
- Proseminar: Einführung in die Literatur- Sprach-undMediendidaktik
- Grundlagen der Germanisti- schen Linguistik (Ling1)
- Grundlagen der Neueren deut- schen Literatur (NdL 1)
- Proseminar: Einführung in die Literatur- Sprach- und Mediendidaktik
- Vorlesung2

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
- Einführungskurs~~1~~: Einführung in die Neuere deutsche Literatur- wissenschaft
- Basismodul: Grundlagen der Fachdi- daktik Deutsch
- Basismodul: Grundlagen der Germa- nistischen Linguistik
- Grundkurs: Einführung in die Germanis- tischeLinguistik
- Basismodul: Grundlagen der Neue- ren deutschen Literatur
- Einführungskurs~~2~~: Einführung in die Neuere deutsche Literaturwissenschaft
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
- Einführungskurs~~1~~: Einführung in die Neuere deutsche Literatur- wissenschaft
- Basismodul: Grundlagen der Fachdi- daktik Deutsch
- Basismodul: Grundlagen der Germa- nistischen Linguistik
- Grundkurs: Einführung in die Germanis- tischeLinguistik
- Basismodul: Grundlagen der Neue- ren deutschen Literatur
- Einführungskurs~~2~~: Einführung in die Neuere deutsche Literaturwissenschaft
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
- Einführungskurs~~1~~: Einführung in die Neuere deutsche Literatur- wissenschaft
- Basismodul: Grundlagen der Fachdi- daktik Deutsch
- Basismodul: Grundlagen der Germa- nistischen Linguistik
- Grundkurs: Einführung in die Germanis- tischeLinguistik
- Basismodul: Grundlagen der Neue- ren deutschen Literatur
- Einführungskurs~~2~~: Einführung in die Neuere deutsche Literaturwissenschaft
- Proseminar: Einführung in die Litera- tur-, Sprach- und Mediendidaktik Deutsch

### pdf vom 26.02.2009 i.d.F. 24.09.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-sept2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-sept2015.md)

**Pflichtmodule (22):**
- Grundlagen der Germanistischen Linguistik (Ling1)
- Grundlagen der Germanisti- schen Mediävistik (Med 1)
- Grundlagen der Neueren deutschen Literatur (NdL 1)
- Grundlagen der Fachdidaktik Deutsch (BM FDD)
- Proseminar: Einführung in die Literatur- Sprach-undMediendidaktik
- Grundlagen der Germanisti- schen Linguistik (Ling1)
- Grundlagen der Neueren deut- schen Literatur (NdL 1)
- Proseminar: Einführung in die Literatur- Sprach- und Mediendidaktik
- Vorlesung2
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
- Einführungskurs~~1~~: Einführung in die Neuere deutsche Literatur- wissenschaft
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
- Einführungskurs~~2~~: Einführung in die Neuere deutscheLiteraturwissenschaft

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

**Pflichtmodule (23):**
- Basismodul I Language
- Aufbauseminar
- Basismodul II Liii
- ngustcs
- Basismodul III Literature
- Basismodul IV Culture/Landeskunde
- Grundseminar mit Projektgruppen
- Zwischenmodul L‐GYM Linguistics
- Seminar (Sprachgeschichte)
- Zwischenmodul L‐GYM Literature
- Textanalyseseminar: Engl./Am. Literatur
- Zwischenmodul L‐GYM Language
- Phonetics I: Theory
- Phonetics II: Error Treatment
- Conversation Practice
- Basismodul Englischdidaktik
- Proseminar
- Basismodul Language
- Elementarmodul L‐UF Linguistics
- Elementarmodul L‐UF Literature
- Lektüreseminar
- Elementarmodul L‐UF
- Landeskunde

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

**Pflichtmodule (22):**
- Basismodul: Theologie und wissenschaftliches Arbeiten
- Tutorium zum Einführungskurs
- RU in der Sek 1 (FD)
- Biblisches Grundwissen (Lehramt GS/MS/RS)
- Biblisches Grundwissen 2 (NT)
- Grundlagen der Theologie und Religionspädagogik
- Themen der Theologie im RU
- Biblische Theologie 1 (AT)
- AT – Geschichte Israels
- Biblische Theologie 2 (NT)
- NT - Synoptische Evangelien/Jesus
- Biblische Theologie 3
- NT – Themen neutestamentl. Theologie: Paulus
- Systematische Theologie 1: Dogmatik (GMRS)
- Grundfragen der Dogmatik
- Systematische Theologie 2: Ethik (GMRS)
- Grundfragen christlicher Ethik
- Kirchengeschichte 1
- Religiöses Lernen und Kirchengeschichte
- Kirchengeschichte 2
- Christliche Kirchen und Gruppen – Ökumene
- RU in der Grundschule bzw. Mittelschule (FD)

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

**Pflichtmodule (12):**
- Basismodul Französische Sprachpraxis 1
- Communication orale
- Basismodul Französische Sprachpraxis 2
- Parcoursgrammatical II
- Phonétique pratique, orthophonie et intonation
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen
- Proseminar Fachdidaktik Französisch
- Introduction à la civilisation
- Bidl Föih Shi 2
- assmou ranzssce pracpraxs

### pdf vom 09.03.2009 i.d.F. 24.09.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-neu-ws2010-2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-neu-ws2010-2011.md)

**Pflichtmodule (12):**
- Abschlussmodul Schriftliche Hausarbeit
- Schriftliche Hausarbeit
- Französische Sprachpraxis 5
- Expression écrite III
- Traduction thème niveau avancé (A – F)
- Traduction version niveau avancé (F – A)
- Fachdidaktisches Modul 1: Einführung in die Didaktik des Französi- schen
- Übung: Einführung in die Fachdidaktik des Französischen
- Proseminar / Übung
- Fachdidaktisches Modul 2: Didaktik des Französischen (Lehramt Re- alschulen)
- Mittelseminar: Französische Sprach-, Litera- tur-und Kulturvermittlung
- Angeleitete Lektüre

### pdf vom 09.03.2009 i.d.F. 24.09.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-neu.md)

**Pflichtmodule (6):**
- Vertiefungmodul Französische Sprachwissenschaft 2
- Mittelseminar
- Vertiefungsmodul Französische Literatur und Kulturwissenschaft 2
- Abschlussmodul Schriftliche Hausarbeit
- Kolloquium zur Besprechung der schriftlichen Hausarbeit
- Schriftliche Hausarbeit

### pdf vom 09.03.2009 i.d.F. 29.09.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-sept2014.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-sept2014.md)

**Pflichtmodule (10):**
- Basismodul Französische Sprachpraxis 1
- Vocabulaire, idiomatique et civilisation I
- Communication orale
- Vocabulaire,idiomatique et civilisation II
- Grammaire cours élémentaire II(groupe verbal)
- Basismodul Französische Sprachpraxis 2
- Basismodul Einführung in die Frankoro- manistik
- Basisseminar französische Literaturwissenschaft
- Basismodul Didaktik der roma- nischen Sprachen
- Proseminar Fachdidaktik Französisch

### pdf vom 10.03.2009 i.d.F. 02.04.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-april2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-april2015.md)

**Pflichtmodule (8):**
- Vorlesung Lateinische Philologie _oder_Übung Indogermanistik
- Prosa
- Lektüre
- Shüb I
- pracungen
- Poesie
- Sprachübungen II
- Sprache IIb

### pdf vom 10.03.2009 i.d.F. 23.07.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-juli2014.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-juli2014.md)

**Pflichtmodule (6):**
- Vorlesung aus der Lateinischen Philologie_oder_Übung aus der Indogermanistik
- Prosa
- Lektüre
- Sprachübungen I
- Sprache Ib
- Poesie

### pdf vom 10.03.2009 i.d.F. 27.09.2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-sept2013.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-sept2013.md)

**Pflichtmodule (6):**
- Vorlesung aus der Lateinischen Philologie_oder_Übung aus der Indogermanistik
- Prosa
- Lektüre
- Sprachübungen I
- SpracheIb
- Poesie

### pdf vom 25.03.2009 i.d.F. 28.03.2011

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-informatik-neu-maerz2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-informatik-neu-maerz2011.md)

**Pflichtmodule (2):**
- Grundlagen der Technischen Informatik
- Systemprogrammierung

### pdf vom 25.03.2009 i.d.F. 22.11.2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-informatik-neu-nov2013.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-informatik-neu-nov2013.md)

**Pflichtmodule (2):**
- Grundlagen der Technischen Informatik
- Systemprogrammierung

### pdf vom 25.03.2009 i.d.F. 31.03.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-informatik-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-informatik-neu.md)

**Pflichtmodule (2):**
- Grundlagen der Technischen Informatik
- Systemprogrammierung

### pdf vom 25.03.2009 i.d.F. 08.08.2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-aug2017.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-aug2017.md)

**Pflichtmodule (9):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione eproduzione orale I
- Basismodul Italienische Sprachpraxis 2
- Foneticapratica
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen
- Proseminar Fachdidaktik Italienisch

### pdf vom 25.03.2009 i.d.F. 24.09.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-neu.md)

**Pflichtmodule (3):**
- Abschlussmodul Schriftliche Hausarbeit
- Kolloquium zur Besprechung der Schriftli- chen Hausarbeit
- SchriftlicheHausarbeit

### pdf vom 25.03.2009 i.d.F. 29.09.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-sept2014.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-sept2014.md)

**Pflichtmodule (7):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I
- Basismodul Italienische Sprachpraxis 2
- Foneticapratica
- Tecniche di lettura
- Basismodul Einführung in die Italoromanistik
- Basisseminar Italienische Literaturwissenschaft

### pdf vom 26.03.2009 i.d.F. 26.03.2012

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-latein-maerz2012.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-latein-maerz2012.md)

**Pflichtmodule (16):**
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
- Examensvorbereitung
- Examenskurs zur Klausurvorbereitung
- Übung Interpretation
- Übung Texterstellung

### pdf vom 26.03.2009 i.d.F. 21.10.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-latein-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-latein-neu.md)

**Pflichtmodule (16):**
- Basismodul: Lateinische Lite- raturwissenschaft I (LIT 1)
- Übung: Einführung in die Lateini- sche Philologie
- Vorlesung: Lateinische Literatur (Prosa)
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
- Examenskurs zur Klausurvorbe- reitung
- Übung Interpretation
- Übung Texterstellung

### pdf vom 26.03.2009 i.d.F. 14.03.2012

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-maerz2012.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-mathematik-maerz2012.md)

**Pflichtmodule (43):**
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
- Orientierungsseminar (OrSe)1,2
- Teil 1
- Teil 2
- Mehrdimensionale Integration (MInt)
- Übungen
- Stochastische Modellbildung (StMo)
- Algebra (Alg)
- Vertiefungsmodul Körpertheorie (VKT)
- Angewandte Mathematik(AMLA)~~1~~
- Geometrie (Geom)~~2~~
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
- Aufbaumodul Analysis (AmAn)~~1~~
- Elemente der Analysis III
- Elementare Stochastik (EStoch)
- Mathematisches Seminar in elemen- tarer Stochastik (SemEStoch)
- Geometrie für das Lehramt (GeoL)
- Mathematisches Seminar in Geomet- rie für das Lehramt (SemGeoL)
- Elementare Zahlentheorie (EZth)
- Mathematisches Seminar in elemen- tarer Zahlentheorie (SemEZth)

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
- Orientierungsseminar (OrSe)1,2
- Teil 1
- Teil 2
- Mehrdimensionale Integration (MInt)
- Übungen
- Stochastische Modellbildung (StMo)
- Algebra (Alg)
- Vertiefungsmodul Körpertheorie (VKT)
- Angewandte Mathematik(AMLA)~~1~~
- Geometrie (Geom)~~2~~
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
- Aufbaumodul Analysis (AmAn)~~1~~
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
- Orientierungsseminar~~2~~(OrSe)
- Teil 1
- Teil 2
- Algebra(Alg)
- Übungen
- Stochastische Modellbildung (StMo)
- Mehrdimensionale Integration (MInt)
- Vorlesung/Übung
- Angewandte Mathematik1 (AMLA)
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
- Aufbaumodul Analysis~~1~~(AmAn)
- Elemente der Analysis III
- Mathematisches Seminar (MSnv) (nicht vertieft)2

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
- Orientierungsseminar(OrSe)1,2
- Teil 1
- Teil 2
- Mehrdimensionale Integration(MInt)
- Übungen
- Stochastische Modellbildung (StMo)
- Algebra(Alg)
- Vertiefungsmodul Körpertheorie(VKT)
- Angewandte Mathematik(AMLA)~~1~~
- Geometrie(Geom)~~2~~
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
- Aufbaumodul Analysis (AmAn)~~1~~
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
- Orientierungsseminar (OrSe)1,2
- Teil 1
- Teil 2
- Mehrdimensionale Integration (MInt)
- Übungen
- Stochastische Modellbildung (StMo)
- Algebra (Alg)
- Vertiefungsmodul Körpertheorie (VKT)
- Angewandte Mathematik(AMLA)~~1~~
- Vorlesung/Übung oderSeminar
- Gewöhnliche Differentialgleichungen (GDgl)
- Geometrie (Geom)~~2~~
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
- Aufbaumodul Analysis (AmAn)~~1~~
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

**Pflichtmodule (14):**
- Grundlagen der politi- schen Bildung
- PolitischesLernen
- Methodik und Wertorien- tierung im Politikunterricht
- Methodik des PU: Metho- dik-Methoden-Modelle
- Grundlagen der politischen Bildung
- Methodik, Praxis und Wertorientierung im Politikunterricht
- Methodik des PU: Me- thodik-Methoden-Modelle
- Übung zur Planung, Durchführung und Kon- trolle des Politikunter- richts
- Methodik, Praxis und Wertorientierung im PU (FG GS)
- Methodik und Wertorientierung im Politikunterricht
- Praxis des Politikunterrichts
- Übung zur Planung, Durchführung und Kon- trolle desPU
- Praxisprobleme der Politischen Bil- dung
- Seminar zur Politikdidak- tik

### pdf vom 01.04.2009 i.d.F. 08.08.2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-aug2017.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-aug2017.md)

**Pflichtmodule (8):**
- Basismodul Spanische Sprachpraxis 1
- Culturaycomunicación oral
- Basismodul Spanische
- Sprachpraxis 2
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen
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

**Pflichtmodule (10):**
- Basismodul Spanische Sprachpraxis 1
- Cultura y comunicación oral
- Basismodul Spanische Sprachpraxis 2
- Fonética práctica
- Basismodul Einführung in die Iberoromanistik
- Basisseminar Spanische Literaturwissen- schaft
- Basismodul Didaktik der romanischen Sprachen
- Didaktik der romanischen
- Sprachen1)
- Proseminar Fachdidaktik Spanisch

### pdf vom 01.04.2009 i.d.F. 22.03.2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-sport-maerz2013.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-sport-maerz2013.md)

**Pflichtmodule (16):**
- (1V) Grundlagen der Sportpädagogik
- (3) Sportpädagogische /-didaktische Kompetenz II
- (2S) Normative und empirische Sportpädagogik /-didaktik (FD)*
- (4) Sportpädagogische /-didaktische Kompetenz III
- Grundlagen der Sportdidaktik (FD)*
- Grundlagen der Sportpädagogik I(FD)*
- Ausgewählte Aspekte des Schulsports (FD)*
- (5) Sportdidaktische/-pädagogische Kompetenz II
- Normative und empirische Sportpädagogik / -didaktik (FD)*
- Klettern o. Wassersport o. MTB o. Inlineskaten o. Triathlon o. Zirkus- o. Kampfkünste o. entsprechendeAngebote
- (2S) Lehrübungen für den Sportunterricht (FD)*
- (5) Kompetenz in Bewegung und Gesundheit II
- „Stärkung Gesundheitsressourcen 1“ Elementare Bewegungs- und Spielerziehung musisch-ästhetische + kompensatorischeBewegungsformen
- Interventionskonzepte und QM
- (4) Kompetenz in Bewegung und Gesundheit III
- (4) Projekt „Entwicklung und Umsetzung zur Gf“

### pdf vom 01.04.2009 i.d.F. 27.02.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-wiwi-februar2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-wiwi-februar2015.md)

**Pflichtmodule (7):**
- Grundlagen der Fachdidaktik Wirtschaftswissenschaft en(Gymnasium)
- Praxisfelder der Fachdidaktik
- Seminar Planung, Durchführung und Reflexion im ökonomischen Fachunterricht
- Grundlagen der Fachdidaktik Wirtschaftswissenschaft en(Realschule)
- Berufsfeldorientierung
- Praxisfelder der Fachdidaktik Wirtschaftswissenschaft en
- Planung, Durchführung und Reflexion im Ökonomischen Fachunterricht

### pdf vom 27.07.2009 i.d.F. 14.09.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lehramt-arbeitslehre-sept2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lehramt-arbeitslehre-sept2015.md)

**Pflichtmodule (7):**
- Grundlagen der Fachdi- daktik (GFD)
- Grundlagen der Fach- wissenschaft (GFW)
- Medien und Methoden I (MuM I)
- Seminar mit Methoden- schwerpunkt
- Medien und Methoden II (MuM II)2
- methodische Begleit- veranstaltung zum Praktikum
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

**Pflichtmodule (5):**
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungs- kompetenzen in der Mittel- schule
- Basismodul Berufsorientierung1
- Masterarbeit

### StuPO LAPO 20090223 i.d.F. 20200513.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/stupo-lapo-20090223-idf-20200513.md`](../pruefungsordnungen/lehramt/stupo-lapo-20090223-idf-20200513.md)

**Pflichtmodule (5):**
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungs- kompetenzen in der Mittel- schule
- Basismodul Berufsorientierung1
- Masterarbeit

### StuPO LAPO 20090223 i.d.F. 20220808.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/stupo-lapo-20090223-idf-20220808.md`](../pruefungsordnungen/lehramt/stupo-lapo-20090223-idf-20220808.md)

**Pflichtmodule (5):**
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungskom- petenzen in der Mittelschule
- Basismodul Berufsorientierung1
- Masterarbeit

### StuPO LAPO 20240918 i.d.F. 20250806.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/stupo-lapo-20240918-idf-20250806.md`](../pruefungsordnungen/lehramt/stupo-lapo-20240918-idf-20250806.md)

**Pflichtmodule (4):**
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungskompetenzen in der Mittelschule
- Masterarbeit

### StuPO LAPO 20240918.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/stupo-lapo-20240918.md`](../pruefungsordnungen/lehramt/stupo-lapo-20240918.md)

**Pflichtmodule (5):**
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungskompetenzen in der Mittelschule
- Basismodul Berufsorientierung1
- Masterarbeit

### 22. Juli 2014

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/4aes-ba-ma-molekularemedizin.md`](../pruefungsordnungen/medizinische-fakultaet/4aes-ba-ma-molekularemedizin.md)

**Pflichtmodule (11):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch-chemisches Praktikum
- Biochemie und Grundzüge der Molekularen Medizin
- Tutorium
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Grundlagen der Physiologie des Menschen und Grundlagen der Bioinformatik
- Bioinformatik
- Organische Chemie

### 18. Februar 2016

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/5aes-ba-ma-molekulare-medizin.md`](../pruefungsordnungen/medizinische-fakultaet/5aes-ba-ma-molekulare-medizin.md)

**Pflichtmodule (9):**
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Computer- based tutorial
- Research Design
- Laboratory Animal Science and Biological Safety
- Animal Handling
- Lecture Biological Safety

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20070928 i.d.F. 20210113.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210113.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210113.md)

**Pflichtmodule (9):**
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Computer-based tutorial
- Research Design
- Laboratory Animal Science and Biological Safety
- Animal Handling
- Lecture Biological Safety

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20070928 i.d.F. 20210429.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210429.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210429.md)

**Pflichtmodule (9):**
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Computer-based tutorial
- Research Design
- Laboratory Animal Science and Biological Safety
- Animal Handling
- Lecture Biological Safety

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20210113 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20210113-aes.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20210113-aes.md)

**Pflichtmodule (9):**
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Computer-based tutorial
- Research Design
- Laboratory Animal Science and Biological Safety
- Animal Handling
- Lecture Biological Safety

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20230822 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822-idf-20240926.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822-idf-20240926.md)

**Pflichtmodule (25):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch- chemisches Praktikum 3)
- Biochemie und Grundzüge der Mlkl Mdii
- Propädeutik- l
- voresung
- Tutorium
- oeuaren ezn
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Grundlagen der Physiologie des Menschen und Grundlagen der Bioinformatik
- Bioinformatik
- Organische Chemie
- Bachelorarbeit
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Computer-based tutorial
- Research Design
- Laboratory Animal Science and Biological Safety
- Animal Handling or Alternative Methods Training
- Lecture Biological Safety
- Masterarbeit mit Masterkolloquium

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20230822 i.d.F. 20250711.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822-idf-20250711.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822-idf-20250711.md)

**Pflichtmodule (10):**
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Computer-based tutorial
- Research Design
- Laboratory Animal Science and Biological Safety
- Animal Handling or Alternative Methods Training
- Lecture Biological Safety
- Masterarbeit mit Masterkolloquium

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20230822.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822.md)

**Pflichtmodule (25):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch- chemisches Praktikum 3)
- Biochemie und Grundzüge der Mlkl Mdii
- Propädeutik- l
- voresung
- Tutorium
- oeuaren ezn
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Grundlagen der Physiologie des Menschen und Grundlagen der Bioinformatik
- Bioinformatik
- Organische Chemie
- Bachelorarbeit
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Computer-based tutorial
- Research Design
- Laboratory Animal Science and Biological Safety
- Animal Handling or Alternative Methods Training
- Lecture Biological Safety
- Masterarbeit mit Masterkolloquium

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed ÄS 20250711.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-aes-20250711.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-aes-20250711.md)

**Pflichtmodule (26):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch- chemisches Praktikum4)
- Biochemie und Grundzüge der Mlkl Mdii
- Tutorium
- oeuaren ezn
- Funktionelle Anatomie des Menschen für Molekulare Medizin
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Grundlagen der Physiologie des Menschen und
- Bioinformatik
- Grundlagen der Bioinformatik
- Organische Chemie
- Praktikum4)
- Vegetative Physiologie
- Neuroanatomie
- Neurophysiologie und Neuroanatomie
- Biochemie und Molekularbiologie I
- Seminare
- Biochemie und Molekularbiologie II
- Biochemisches Praktikum I
- Biochemisches Praktikum II
- Mikrobiologie, Immunologie und Virologie
- Strahlenschutz in der experimentellen Medizin
- Humangenetik
- Bachelorarbeit

### MSc Medical Process Management MPM 20081107 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/msc-medical-process-management-mpm-20081107-idf-20230731.md`](../pruefungsordnungen/medizinische-fakultaet/msc-medical-process-management-mpm-20081107-idf-20230731.md)

**Pflichtmodule (3):**
- (29) Zusatzmodule ........................................................................................................................... 16
- (30) Zertifikat „Projektmanagement“ ................................................................................................ 17
- (31) In-Kraft-Treten, Übergangsvorschriften .................................................................................... 17

### MSc Medical Process Management MPM 20240807.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/msc-medical-process-management-mpm-20240807.md`](../pruefungsordnungen/medizinische-fakultaet/msc-medical-process-management-mpm-20240807.md)

**Pflichtmodule (10):**
- MPM-Propädeutikum
- Demonstrationen zur Funktionellen Anatomie des Menschen
- Einführung in die Arzneimittelthera- pie
- Grundlagen und Organisation der Versorgung
- Kommunikations- und Kooperation- saspekte im
- Strategisches Qualitätsmanage- ment
- Informationssysteme im Gesund- heitswesen
- Public Health und evidenzbasierte Medizin
- Medizinisches Qualitätsmanage- ment
- Spezielle Aspekte des deutschen Gesundheitssystems

### PDF vom 28.09.2007 i.d.F. 18.02.2016

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-feb2016.md`](../pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-feb2016.md)

**Pflichtmodule (26):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch-chemisches Praktikum
- Propädeutikvorlesung
- Biochemie und Grundzüge der
- Molekularen Medizin
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Grundlagen der Physiologie des Menschen und Grundlagen der Bioinformatik
- Bioinormatik
- Oranische Chemie
- Bachelorarbeit
- SummeECTS:
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Computer-based tutorial
- Research Design
- Laboratory Animal Science and Biological Safety
- Animal Handling
- Lecture Biological Safety
- Masterarbeit (30 ECTS-Leistungspunkte)
- Master’s Thesis
- Master’s Colloquium

### PDF vom 28.09.2007 i.d.F. 22.07.2014

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-juli2014.md`](../pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-juli2014.md)

**Pflichtmodule (11):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch-chemisches Prakti- kum
- Propädeutikvorlesung
- Biochemie und Grundzüge der
- Molekularen Medizin
- Funktionelle Anatomie des Men- schen
- Allgemeine Histologie und Emb- ryologie
- Spezielle Histologie und Orga- nogenese
- Grundlagen der Physiologie des Menschen und Grundlagen der Bioinformatik
- Bioinformatik

### Weiterbildungsstudiengang Zahnerhaltung StuPO ZahnE 20250131.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/weiterbildungsstudiengang-zahnerhaltung-stupo-zahne-20250131.md`](../pruefungsordnungen/medizinische-fakultaet/weiterbildungsstudiengang-zahnerhaltung-stupo-zahne-20250131.md)

**Pflichtmodule (1):**
- Masterarbeit

### 15. August 2011

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/2aes-20ba-20bio-20-20ma-20zellmolek-1.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/2aes-20ba-20bio-20-20ma-20zellmolek-1.md)

**Pflichtmodule (1):**
- PL: Klausur ca. 90 Min. doppeltgewichtet

### PDF vom 22.07.2015 i.d.F. 05.08.2016

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bio-zellmolekbio-neu-aug2016.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bio-zellmolekbio-neu-aug2016.md)

**Pflichtmodule (16):**
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
- Masterarbeit
- Verteidigung

### (PDF vom 22.07.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bio-zellmolekbio-neu.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bio-zellmolekbio-neu.md)

**Pflichtmodule (15):**
- Basismodul Englisch
- Fachmodul A (Teil 1)
- Fachmodul B (Teil 1)
- Fachmodul C (Teil 1)
- Fachmodul A (Teil 2)
- Fachmodul B (Teil 2)
- Fachmodul C (Teil 2)
- Kernmodul I
- Kernmodul II
- Mastermodul 1
- Mastermodul 2
- Mastermodul 3
- Mastermodul 4
- Masterarbeit
- Verteidigung

### FPO BSc-MSc ILS FPO BAMA ILS 20191028.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20191028.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20191028.md)

**Pflichtmodule (22):**
- Itdti t Sttiti d
- Ttil f Itdti t
- nroucon o ascs an Statistical Prorammin
- Lab class Statistical Programming
- Mathematical Modelling and Systems Biology, vgl.
- Biomathematics
- Tutorial for Biomathematics
- Systems Biology
- Laboratory course Systems Biology
- Bioimaging and Biophysics, vgl. §§ 50
- Bioimaging & Biophysics A
- Laboratory course for Bioimaging & Biophysics I
- Bioimaging & Biophysics II
- Bioimaging & Biophysics B
- Lbt f
- aoraory course or Bioimaging& Biophysics II
- Biological Structures and Processes, vgl. §§ 50 und 51
- Interactions of Biological Macromolecules A
- Seminar/Tutorial for Interactions of Biological Macromolecules A
- Intrtin f Bilil
- eacos o oogca Mll B
- acromoecues

### FPO BSc-MSc ILS FPO BAMA ILS 20230822 i.d.F. 20260331.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20230822-idf-20260331.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20230822-idf-20260331.md)

**Pflichtmodule (12):**
- Introduction to Statistics and Statistical Program- ming
- Tutorial for Introduction to Statistics (Problem Ses- sion)
- Lab class Statistical Programming
- Biomathematics
- Tutorial for Biomathema- tics
- Systems Biology
- Laboratory course Sys- tems Biology
- Bioimaging & Biophysics A
- Interactions of Biological Macromolecules A
- Seminar/Tutorial for Interactions of Biological Macromolecules A
- Interactions of Biological Macromolecules B
- Seminar/Tutorial for Interactions of Biological Macromolecules B

### FPO BSc-MSc ILS FPO BAMA ILS 20230822.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20230822.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20230822.md)

**Pflichtmodule (14):**
- Introduction to Statistics and Statistical Program- ming
- Tutorial for Introduction to Statistics (Problem Ses- sion)
- Lab class Statistical Programming
- Biomathematics
- Tutorial for Biomathema- tics
- Systems Biology
- Laboratory course Sys- tems Biology
- Bioimaging & Biophysics A
- Laboratory course for Bioimaging & Biophysics I
- Interactions of Biological Macromolecules A
- Seminar/Tutorial for Interactions of Biological Macromolecules A
- Interactions of Biological Macromolecules B
- Seminar/Tutorial for Interactions of Biological Macromolecules B
- Laboratory course for Bioimaging& Biophysics I

### PDF vom 05.08.2008 i.d.F. 15.08.2011

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-august2011.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-august2011.md)

**Pflichtmodule (2):**
- PL: Klausur ca. 90 Min. doppeltgewichtet
- PL: Klausur ca. 90 Min. doppelt gewichtet

### PDF vom 05.08.2008 i.d.F. 15.02.2013

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-feb2013.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-feb2013.md)

**Pflichtmodule (1):**
- PL: Klausur ca. 90 Min. doppeltgewichtet

### PDF vom 05.08.2008 i.d.F. 06.10.2014

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-okt2014.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/po-biologie-bama-okt2014.md)

**Pflichtmodule (1):**
- PL: Klausur ca. 90 Min. doppeltgewichtet

### FPO BAMA Chemie MolSci 20260305.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/chemie-und-pharmazie/fpo-bama-chemie-molsci-20260305.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/chemie-und-pharmazie/fpo-bama-chemie-molsci-20260305.md)

**Pflichtmodule (6):**
- (5) Quantum Chemistry I
- (6) Multi-Scale Simulation Me- thods
- (7) Programming & Numerical Si- mulations
- (8) Introduction to Machine Lear- ning
- (9) Molecular Mechanics and Data Analysis2)
- (16) Masterarbeit

### BA-MA Kulturgeographie FPO Kulturgeo 20200827 i.d.F. 20221011.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20200827-idf-20221011.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20200827-idf-20221011.md)

**Pflichtmodule (11):**
- Kulturgeographische Theorien
- Vorlesung Raumtheorie
- Wahlmodul Kulturgeographie
- Gesellschaft, Technik, Raum
- Methoden der digitalen Geistes- und Sozialwissenschaften
- KGV: Vertiefte Kulturgeo- graphie
- EE: Externe Expertise4)
- Externe Expertise II
- LF: Lehrforschung
- RGV: Vertiefte Regionale Geographie
- Großes Geländeseminar (mindestens 10 Tage)

### BA-MA Kulturgeographie FPO Kulturgeo 20200827.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20200827.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20200827.md)

**Pflichtmodule (5):**
- Kulturgeographische Theorien
- Vorlesung Raumtheorie
- ARB: Masterarbeit
- Masterarbeit
- Verteidigung

### BA-MA Kulturgeographie FPO Kulturgeo 20230822.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20230822.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20230822.md)

**Pflichtmodule (11):**
- Kulturgeographische Theorien
- Vorlesung Raumtheorie
- Wahlmodul Kulturgeographie
- Gesellschaft, Technik, Raum
- Methoden der digitalen Geistes- und Sozialwissenschaften
- KGV: Vertiefte Kulturgeographie
- EE: Externe Expertise4)
- Externe Expertise II
- LF: Lehrforschung
- RGV: Vertiefte Regionale Geographie
- Großes Geländeseminar (mindestens 10 Tage)

### PDF vom 29.02.2016 i.d.F. 02.03.2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-maerz2017.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-maerz2017.md)

**Pflichtmodule (38):**
- Grundlagen der Geowissenschaften I
- Minerale und Gesteine
- Übungen zur V Minerale und Gesteine
- Mathematik
- Übungen zur V Mathem. für Nat.wiss.
- Biologie
- Chemie
- Anorganisch-chemisches Praktikum für Nebenfächler
- Geowissenschaftliche Arbeitsmethoden I
- Geländeübung I
- Grundlagen der Geowissenschaften II
- Dynamik des Systems Erde
- Mineralogie I
- Symmetrie und Eigenschaften der Minerale
- Physik
- Übungen zur Physik für LA Geogra- phie, Geowissenschaften
- Paläobiologie I
- Evolution des Lebens
- Paläobiologie II
- Übungen zur V Paläobio- diversität
- Physikalisches Praktikum
- Angewandte Geologie I
- Strukturgeologie und Lagerstättenkunde
- Strukturgeologie
- Geowissenschaftliche Arbeitsmethoden II
- Kartierübung
- Mineralogie II
- Angewandte Mineralogie
- Regionale Geologie
- Geländeübung II
- Sedimentologie
- Geochemie
- Globale Stoffkreisläufe
- Petrologie
- Petrologische Systeme
- Angewandte Geologie II
- Wissenschaftliches geow. Arbeiten und Präsentieren
- Geophysik

### PDF vom 29.02.2016 i.d.F. 30.09.2016

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-sept2016.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-sept2016.md)

**Pflichtmodule (33):**
- Grundlagen der Geowissenschaften I
- Minerale und Gesteine
- Übungen zur V Minerale und Gesteine
- Mathematik
- Übungen zur V Mathem. für Nat.wiss.
- Biologie
- Chemie
- Anorganisch-chemisches Praktikum für Nebenfächler
- Geowissenschaftliche Arbeitsmethoden I
- Geländeübung I
- Grundlagen der Geowissenschaften II
- Dynamik des Systems Erde
- Mineralogie I
- Symmetrie und Eigenschaften der Minerale
- Physik
- Übungen zur Physik für LA Geogra- phie, Geowissenschaften
- Paläobiologie I
- Evolution des Lebens
- Paläobiologie II
- Physikalisches Praktikum
- Angewandte Geologie I
- Strukturgeologie und Lagerstättenkunde
- Geowissenschaftliche Arbeitsmethoden II
- Mineralogie II
- Regionale Geologie
- Sedimentologie
- Geochemie
- Petrologie
- Angewandte Geologie II
- Wissenschaftliches geow. Arbeiten und Präsentieren
- Geophysik
- Masterarbeit
- Verteidigung der Masterarbeit

### PDF vom 29.02.2016

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften.md)

**Pflichtmodule (33):**
- Grundlagen der Geowissenschaften I
- Minerale und Gesteine
- Übungen zur V Minerale und Gesteine
- Mathematik
- Übungen zur V Mathem. für Nat.wiss.
- Biologie
- Chemie
- Anorganisch-chemisches Praktikum für Nebenfächler
- Geowissenschaftliche Arbeitsmethoden I
- Geländeübung I
- Grundlagen der Geowissenschaften II
- Dynamik des Systems Erde
- Mineralogie I
- Symmetrie und Eigenschaften der Minerale
- Physik
- Übungen zur Physik für LA Geogra- phie, Geowissenschaften
- Paläobiologie I
- Evolution des Lebens
- Paläobiologie II
- Physikalisches Praktikum
- Angewandte Geologie I
- Strukturgeologie und Lagerstättenkunde
- Geowissenschaftliche Arbeitsmethoden II
- Mineralogie II
- Regionale Geologie
- Sedimentologie
- Geochemie
- Petrologie
- Angewandte Geologie II
- Wissenschaftliches geow. Arbeiten und Präsentieren
- Geophysik
- Masterarbeit
- Verteidigung der Masterarbeit

### FPO BAMA Geow 20191028 i.d.F. 20200604.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028-idf-20200604.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028-idf-20200604.md)

**Pflichtmodule (2):**
- Schriftliche Masterarbeit
- Verteidigung der Masterarbeit

### FPO BAMA Geow 20191028 i.d.F. 20220908.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028-idf-20220908.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028-idf-20220908.md)

**Pflichtmodule (2):**
- Schriftliche Masterarbeit
- Verteidigung der Masterarbeit

### FPO BAMA Geow 20191028.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028.md)

**Pflichtmodule (2):**
- Schriftliche Masterarbeit
- Verteidigung der Masterarbeit

### FPO BAMA Geow 20250513.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20250513.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20250513.md)

**Pflichtmodule (2):**
- Schriftliche Masterarbeit
- Verteidigung der Masterarbeit

### FPO Kulturgeo 20221011 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-kulturgeo-20221011-aes.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-kulturgeo-20221011-aes.md)

**Pflichtmodule (9):**
- Kulturgeographische Theorien
- Vorlesung Raumtheorie
- Wahlmodul Kulturgeographie
- Gesellschaft, Technik, Raum
- Methoden der digitalen Geistes- und Sozialwissenschaften
- KGV: Vertiefte Kulturgeo- graphie
- EE: Externe Expertise4)
- Externe Expertise II
- LF: Lehrforschung

### PO ZS Geow im LA 20250320 .pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/po-zs-geow-im-la-20250320.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/po-zs-geow-im-la-20250320.md)

**Pflichtmodule (4):**
- Grundlagen der Geowissenschaften I
- Rohstoffe und Nachhaltigkeit
- Dynamik des Systems Erde
- Kompetenzseminar zum Klimawandel

### PDF vom 01.10.2007 i.d.F. 05.08.2008

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/pro-ba-ma-geowissenschaften.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/pro-ba-ma-geowissenschaften.md)

**Pflichtmodule (12):**
- Bachelorprüfung.................................................................................. 11
- Bachelorarbeit...................................................................................... 14
- Verteidigung der Bachelorarbeit ........................................................ 15
- Wiederholung von Prüfungen............................................................. 15
- Masterprüfung ........................................................................................ 16
- Qualifikation zum Masterstudium ...................................................... 16
- Masterprüfung...................................................................................... 16
- Masterarbeit ......................................................................................... 17
- Verteidigung der Masterarbeit............................................................ 18
- Wiederholung von Prüfungen............................................................. 18
- Schlussvorschriften............................................................................... 18
- In-Kraft-Treten, Übergangsvorschriften............................................. 18

### BSc-MSc Data Science FPODataScience 20210805 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/bsc-msc-data-science-fpodatascience-20210805-aes.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/bsc-msc-data-science-fpodatascience-20210805-aes.md)

**Pflichtmodule (11):**
- (1) Mathematics of Learning
- Practical Mathemat- ical Data Science
- (2) Deep Learning
- (3) Selected Topics in Mathematics of Learning
- Übung Ma- thematics of Learning
- cences
- (4) Wahlpflicht- module aus dem
- Katalog der ge- ählt Ht
- aupsuenrcung
- (5) vgl. Modulkatalog gem. § 51 Abs. 4
- eensuenrcung

### BSc-MSc Data Science FPODataScience 20220328 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/bsc-msc-data-science-fpodatascience-20220328-aes.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/bsc-msc-data-science-fpodatascience-20220328-aes.md)

**Pflichtmodule (7):**
- eep earnng
- (3) Selected Topics in Mathematics of Learning
- Übung Mathematics of Learning
- (4) vgl. Modulkatalog gem. § 51 Abs. 4
- (6) vgl. Modulkatalog gem. § 52 Abs. 3
- (7) Wahlmodule der Tech- nischen Schlüsselquali- fiki äß 53
- aton gem §

### PDF vom 11.03.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-mathematik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-mathematik.md)

**Pflichtmodule (15):**
- Analysis I
- Übung Analysis I
- Tafelübung Analysis I
- Analysis II
- Übung Analysis II
- Tafelübung Analysis II
- Analysis III
- Übung Analysis III
- Tafelübung Analysis III
- Lineare Algebra I
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- Lineare Algebra II
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II

### PDF vom 11.03.2015 i.d.F. 27.02.2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik-feb2017.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik-feb2017.md)

**Pflichtmodule (39):**
- Analysis I
- Übung Analysis I
- Tafelübung Analysis I
- Analysis II
- Übung Analysis II
- Tafelübung Analysis II
- Analysis III
- Übung Analysis III
- Tafelübung Analysis III
- Lineare Algebra I
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- Lineare Algebra II
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II
- Lineare und Kombinatorische Optimierung
- Übung Lineare und Kombinatorische Optimierung
- Stochastische Modellbildung
- Übung Stochastische Modellbildung
- Tafelübung Stochastische Modellbil- dung
- Numerische Mathematik
- Übung Num. Math. Numerische Mathematik
- Rechnerübung Numerische Mathematik
- Diskretisierung und numerische Optimierung
- Übung Diskretisierung und numeri- sche Optimierung
- Numerik partieller Differential- gleichungen
- Übung Numerik partieller Differenzi- algleichungen
- Mathematische Modellierung Theorie
- Übung Mathematische ModellierungTheorie
- Nichtlineare Optimierung
- Übung Nichtlineare Optimierung
- Gewöhnliche Differentialglei- chungen
- Übung Gewöhnliche Differentialglei- chungen
- Funktionalanalysis
- Übung Funktionalanalysis
- Partielle Differenzialgleichungen I
- Übung Partielle Differenzialgleichun- gen I
- Bachelorseminar
- Bachelorarbeit

### PDF 27th of February 2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik-fpotechnomathe-20150311-idf-20170227-en.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik-fpotechnomathe-20150311-idf-20170227-en.md)

**Pflichtmodule (5):**
- Vorlesung Analysis I
- Vorlesung Analysis II
- Vorlesung Lineare Algebra I
- Vorlesung Lineare Algebra II
- (GM)

### PDF vom 11.03.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik.md)

**Pflichtmodule (39):**
- Analysis I
- Übung Analysis I
- Tafelübung Analysis I
- Analysis II
- Übung Analysis II
- Tafelübung Analysis II
- Analysis III
- Übung Analysis III
- Tafelübung Analysis III
- Lineare Algebra I
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- Lineare Algebra II
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II
- Lineare und Kombinatorische Optimierung
- Übung Lineare und Kombinatorische Optimierung
- Stochastische Modellbildung
- Übung Stochastische Modellbildung
- Tafelübung Stochastische Modellbil- dung
- Numerische Mathematik
- Übung Num. Math. Numerische Mathematik
- Rechnerübung Numerische Mathematik
- Diskretisierung und numerische Optimierung
- Übung Diskretisierung und numeri- sche Optimierung
- Numerik partieller Differential- gleichungen
- Übung Numerik partieller Differenzi- algleichungen
- Mathematische Modellierung Theorie
- Übung Mathematische ModellierungTheorie
- Nichtlineare Optimierung
- Übung Nichtlineare Optimierung
- Gewöhnliche Differentialglei- chungen
- Übung Gewöhnliche Differentialglei- chungen
- Funktionalanalysis
- Übung Funktionalanalysis
- Partielle Differenzialgleichungen I
- Übung Partielle Differenzialgleichun- gen I
- Bachelorseminar
- Bachelorarbeit

### PDF vom 11.03.2015 i.d.F. 13.03.2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik-maerz2017.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik-maerz2017.md)

**Pflichtmodule (16):**
- Analysis I
- Analysis II
- Analysis III
- Lineare Algebra I
- Lineare Algebra II
- Lineare und Kombinatorische Optimierung1
- Übung Lineare und Kombinatorische Optimierung
- Projektseminar Optimierung2
- Stochastische Modellbildung1
- Übung Stochastische Modellbildung.
- Tafelübung Stochastische Modellbil- dung
- Introduction to Statistics and Statistical Programming2
- Übung Introduction to Statistics and Statistical Programming
- Rechnerübung Introduction to Statistics and Statistical Program- ming
- und Optimierung (PSO)
- Abschlussarbeit

### PDF vom 11.03.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik.md)

**Pflichtmodule (16):**
- Analysis I
- Analysis II
- Analysis III
- Lineare Algebra I
- Lineare Algebra II
- Lineare und Kombinatorische Optimierung1
- Übung Lineare und Kombinatorische Optimierung
- Projektseminar Optimierung2
- Stochastische Modellbildung1
- Übung Stochastische Modellbildung.
- Tafelübung Stochastische Modellbil- dung
- Introduction to Statistics and Statistical Programming2
- Übung Introduction to Statistics and Statistical Programming
- Rechnerübung Introduction to Statistics and Statistical Program- ming
- und Optimierung (PSO)
- Abschlussarbeit

### FPODataScience 20200820 i.d.F. 20210311.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210311.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210311.md)

**Pflichtmodule (7):**
- (1) Seminar Data Science in Forschung und Industrie
- (2) Einführung in die mathematische Datenanalyse
- Übung zur Einführung in die mathematische Daten- analyse
- (3) Wahlpflichtmodule aus dem Katalog für Machine Learning gem. § 42
- (4) Wahlpflichtmodule aus dem Katalog für Projekt Data Science gem. § 42
- (9) Masterar- beit
- Masterkol- loquium

### FPODataScience 20200820 i.d.F. 20210805.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210805.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210805.md)

**Pflichtmodule (22):**
- (1) Seminar Data Science in Forschung und Industrie
- (2) Einführung in die mathematische Datenanalyse
- Übung zur Einführung in die mathematische Daten- analyse
- (3) Wahlpflichtmodule aus dem Katalog für Machine Learning gem. § 42
- (4) Wahlpflichtmodule aus dem Katalog für Projekt Data Science gem. § 42
- (1) Mathematics of Learning
- Practical Mathemati- cal Data Science
- (2) Deep Learning
- (3) Selected Topics in Mathematics of Learning
- Übung Ma- thematics of Learning
- cences
- (4) Wahlpflicht- module aus
- dem Katalog der ählt Ht-
- aupsuenrcung
- (5) vgl. Modulkatalog gem. § 51 Abs. 4
- eensuenrcung
- (6) Wahlpflicht- module aus dem
- Katalog der Adfh-
- (9) Masterar- beit
- Masterkol- loquium
- Practical Mathemati- cal Data Sci- ence
- Katalog der ge- ählt Ht-

### FPODataScience 20200820 i.d.F. 20220328.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20220328.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20220328.md)

**Pflichtmodule (18):**
- (1) Seminar Data Science in Forschung und Industrie
- (2) Einführung in die mathematische Datenanalyse
- Übung zur Einführung in die mathematische Daten- analyse
- (3) Wahlpflichtmodule aus dem Katalog für Machine Learning gem. § 42
- (4) Wahlpflichtmodule aus dem Katalog für Projekt Data Science gem. § 42
- Master- bit
- (1) Mathematics of Learning
- Practical Mathe- matical Data Science
- (2) Deep Learning
- (3) Selected Topics in Mathematics of Learning
- Übung Mathe- matics of Learning
- (4) Wahlpflichtmodule aus dem
- Katalog der gewählten Httdiiht
- eep earnng
- Übung Mathema- tics of Learning
- (4) vgl. Modulkatalog gem. § 51 Abs. 4
- (6) vgl. Modulkatalog gem. § 52 Abs. 3
- Übung Mathe- matics of Learn- ing

### FPODataScience 20200820.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820.md)

**Pflichtmodule (7):**
- (1) Seminar Data Science in Forschung und Industrie
- (2) Einführung in die mathematische Datenanalyse
- Übung zur Einführung in die mathematische Daten- analyse
- (3) Wahlpflichtmodule aus dem Katalog für Machine Learning gem. § 42
- (4) Wahlpflichtmodule aus dem Katalog für Projekt Data Science gem. § 42
- (9) Masterar- beit
- Masterkol- loquium

### FPODataScience 20260305.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20260305.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20260305.md)

**Pflichtmodule (16):**
- (1) Seminar Data Science in Forschung und Industrie
- (2) Methoden für die mathema- tische Datenanalyse
- (3) Wahlpflichtmodule aus dem Katalog für Machine Learn- ing gem.§47
- (4) Wahlpflichtmodule aus dem Katalog für Projekt Data Sci- ence gem. § 47
- (5) Mathematik für Data Science 1 GOP
- (6) Mathematik für Data Science 2 GOP
- (7) Grundlagen der Programmierung GOP
- (8) Einführung in die Algorith- mik GOP
- (9) Knowledge Discovery in Databases mit Übung GOP
- (1) Mathematics of Learning
- Übung Mathematics of Learning
- (2) Deep Learning
- (3) Selected Topics in Mathematics of Learning
- Übung Selected Topics in Mathematics of Learning
- (3) Selected Topics in Mathe- matics of Learning
- Übung Selected Top- ics in Mathematics of Learning

### FPOMathe 20150311 i.d.F. 20190715.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20150311-idf-20190715.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20150311-idf-20190715.md)

**Pflichtmodule (15):**
- (1) Analysis I
- Übung Analysis I
- Tafelübung Analysis I
- (2) Analysis II
- Übung Analysis II
- Tafelübung Analysis II
- (3) Analysis III
- Übung Analysis III
- Tafelübung Analysis III
- (4) Lineare Algebra I
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- (5) Lineare Algebra II
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II

### FPOMathe 20150311 i.d.F. 20210805.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20150311-idf-20210805.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20150311-idf-20210805.md)

**Pflichtmodule (15):**
- (1) Analysis I
- Übung Analysis I
- Tafelübung Analysis I
- (2) Analysis II
- Übung Analysis II
- Tafelübung Analysis II
- (3) Analysis III
- Übung Analysis III
- Tafelübung Analysis III
- (4) Lineare Algebra I
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- (5) Lineare Algebra II
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II

### FPOMathe 20190715 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20190715-aes.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20190715-aes.md)

**Pflichtmodule (15):**
- (1) Analysis I
- Übung Analysis I
- Tafelübung Analysis I
- (2) Analysis II
- Übung Analysis II
- Tafelübung Analysis II
- (3) Analysis III
- Übung Analysis III
- Tafelübung Analysis III
- (4) Lineare Algebra I
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- (5) Lineare Algebra II
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II

### FPOMathe 20260305.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20260305.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20260305.md)

**Pflichtmodule (17):**
- (1) Analysis I
- Übung Analysis I
- Tafelübung Analysis I
- (2) Analysis II
- Übung Analysis II
- Tafelübung Analysis II
- (3) Analysis III
- Übung Analysis III
- Tafelübung Analysis III
- (4) Lineare Algebra I
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- (5) Lineare Algebra II
- Übung Lineare Algebra II
- (11) Bachelorarbeit
- Masterarbeit
- Masterkolloquium

### FPOTechnoMathe 20150311 i.d.F. 20190715.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20190715.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20190715.md)

**Pflichtmodule (11):**
- (1) Modeling and Analysis in Continuum Mechanics I
- Tutorials to Part I
- (2) Modeling and Analysis in Continuum Mechanics II
- Tutorials to Part II
- (3) Modeling, Simulation and Optimization
- (4) Programming Techniques for Super- computers in CAM
- Tutorials to Program- ming Techniques for Supercomputers
- (5) Architectures of Super- computers
- Tutorials to Architectures of Supercomputers
- Programming Techniques for Supercomputers in CAM
- Tutorials to Programming Techniques for Super- computers

### FPOTechnoMathe 20150311 i.d.F. 20200820.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20200820.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20200820.md)

**Pflichtmodule (12):**
- (1) MApA
- (3) MApA/ NASi/ Opti
- (4) Programming Techniques for Super- computers in CAM
- (5) Architectures of Super- computers
- Modeling and Analysis in Continuum Mechanics I
- Tutorials to Part I
- Modeling and Analysis in Continuum Mechanics II
- Tutorials to Part II
- Modeling, Simulation and Optimization
- Programming Techniques for Supercomputers in CAM
- Tutorials to Program- ming Techniques for Supercomputers
- (5) Tutorials to Architectures of Supercomputers

### FPOTechnoMathe 20150311 i.d.F. 20210805.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20210805.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20210805.md)

**Pflichtmodule (5):**
- (1) MApA
- (3) MApA/ NASi/ Opti
- (4) Programming Techniques for Super- computers in CAM
- (5) Architectures of Super- computers
- Programming Techniques for Supercomputers in CAM

### FPOTechnoMathe 20150311 i.d.F. 20220811.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20220811.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20220811.md)

**Pflichtmodule (12):**
- MApA
- MApA/ NASi/ Opti
- Programming Techniques for Super- computers in CAM
- Architectures of Super- computers
- Modeling and Analysis in Continuum Mechanics I
- Tutorials to Part I
- Modeling and Analysis in Continuum Mechanics II
- Tutorials to Part II
- Modeling, Simulation and Optimization
- Tutorials to Program- ming Techniques for Supercomputers
- Tutorials to Architectures of Supercomputers
- Programming Techniques for Supercomputers in CAM

### FPOTechnomathe 20260305.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20260305.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20260305.md)

**Pflichtmodule (10):**
- Modeling and Analysis in Continuum Mechanics I
- Tutorials to Part I
- Modeling and Analysis in Continuum Mechanics II
- Tutorials to Part II
- Modeling, Simulation and Optimization
- Programming Techniques for Super- computers in CAM
- Tutorials to Program- ming Techniques for Supercomputers
- Architectures of Super- computers
- Tutorials to Architectures of Supercomputers
- Programming Techniques for Supercomputers in CAM

### FPOWiMathe 20150311 i.d.F. 20200820.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpowimathe-20150311-idf-20200820.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpowimathe-20150311-idf-20200820.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOWiMathe 20150311 i.d.F. 20210805.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpowimathe-20150311-idf-20210805.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpowimathe-20150311-idf-20210805.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOWiMathe 20260305.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpowimathe-20260305.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpowimathe-20260305.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 25.09.1980 i.d.F. 28.12.2004

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/modul-und-zusatzstudien/zwischenpruefungso.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/modul-und-zusatzstudien/zwischenpruefungso.md)

**Pflichtmodule (14):**
- Basismodul 1: Sprachwissen- schaft
- Basismodul 2: Literaturwissen- schaft
- Basismodul 3: Sprachpraktische Grundlagen
- Basismodul 4: Sprachproduktion
- Basismodul 5: Landeskunde
- Basismodul 1
- _Linguistik_
- Basismodul 2
- _Literatur- und_
- _Kulturwissenschaft_
- Literaturwiss.
- oder
- Kulturwissenschaft
- Dauer der schriftlichen Prüfung

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
- Lehrveranstaltungen an der Partneruniversität~~2~~
- Grundlagen des Electronic Publishing und Electronic Commerce
- Typografische Grundlagen
- Literatur und Buch D – F
- Bachelorarbeit

### PDF vom 03.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1fachba-literatur-und-buch.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1fachba-literatur-und-buch.md)

**Pflichtmodule (26):**
- Basismodul Französische Sprach- praxis 1
- Vocabulaire, idiomatique et civilisation I
- Communication orale
- Grundlagen der Neueren deut- schen Literatur(NdL 1)
- Grundlagen der Buchwissenschaft
- Übungbegleitend zur Vorlesung
- Einführung in das wissenschaftli- che Arbeiten Buchwissenschaft
- Grundlagen wiss. Arbeitens, Übungbegleitend zur VL
- Basismodul Französische Sprach- praxis 2
- Grammaire cours élémentaire II
- Phonétique pratique, orthophonie et intonation
- Einführung französische Literatur- wissenschaft
- Systematische Aspekte der Litera- turwissenschaft (LitS)
- Vorlesung: Einführung in systematische Aspekte der Literaturwissenschaft
- Lesen und Lese(r)geschichte im Überblick
- Proseminar Schwerpunktthema A (Geschichte), alternativ zu Schwerpunktthema B
- Proseminar Schwerpunktthema B (Gegenwart), alternativ zu SchwerpunktthemaA
- Lehrveranstaltungen an der Part- neruniversität*
- Grundlagen E-Publishing/E- Commerce
- Hauptseminar Schwerpunktthema A (E-Publishing), alternativ zu SchwerpunktthemaB
- Hauptseminar Schwerpunktthema B (E-Commerce), alternativ zu Schwerpunktthema A
- Typographie Grundlagen
- Angewandte Typographie
- Literatur und Buch D – F
- Buchwirtschaftliches Praktikum
- Bachelorarbeit

### PDF vom 18.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1fachba-soziologie.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1fachba-soziologie.md)

**Pflichtmodule (13):**
- Grundlagen der soziologischen Analyse (SozG)
- PS „Der Soziologische Blik“
- PS „Wissenschaftstheorie“
- Qualifikationsprofil I (SozQ-I)
- Statistische Analyseverfahren I (SozS-I)
- V Statistische Analyse- fhI
- veraren
- Ü Statistische Analysever- fahren I
- Statistische Analyseverfahren II (SozS-II)
- Ü Statistische Analyse- verfahren II
- Einführung in die soziologische Methodenlehre (SozM-E)
- Vertiefung Soziologische Metho- denlehre (SozM-V)
- Ü Statistische Analyseverfahren II

### 22. Juli 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/2aes-1fachba-islamischreligioesestudien.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/2aes-1fachba-islamischreligioesestudien.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- Begleitkurs

### 21. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/3aes-1fachba-archaeologwissenschaften.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/3aes-1fachba-archaeologwissenschaften.md)

**Pflichtmodule (4):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Vorlesung zur prähistorischen KulturentwicklungEuropas
- Prähistorische Archäologie: Ältere Urgeschichte I

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/6aesa-ba-ma-psychologie.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/6aesa-ba-ma-psychologie.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M 1Multivariate Statistik
- M 2Forschungsmethoden
- Metaanalyse oder Umfrage- forschung
- M 3Psychologische Diagnostik
- Spezielle Diagnostik

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
- Kompetenzreflexion (Schlüsselqualifikation)
- Tagungsteilnahme IV

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20200911.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20200911.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20200911.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1Multivariate Statistik
- M2Forschungsmethoden
- Metaanalyse oder Umfrage- forschung
- M3Psychologische Diagnostik
- Spezielle Diagnostik

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20210806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20210806.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20210806.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1Multivariate Statistik
- M2Forschungsmethoden
- Metaanalyse oder Umfrage- forschung
- M3Psychologische Diagnostik
- Spezielle Diagnostik

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20220328.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20220328.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20220328.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- Vorlesung Multivariate Verfahren
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20220328 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20220328-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20220328-aes.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- Vorlesung Multivariate Verfahren
- M1 Multivariate Statistik
- M2 Fhthd
- orscungsmeoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20240229.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240229.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240229.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- Multivariate Verfahren mit computergestützter Datenauswertung
- M2 Forschungsmethoden
- Seminar VertiefungForschungsmethoden
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240926.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240926.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- Vorlesung Multivariate Verfahren
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20241219.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- Multivariate Verfahren mit computergestützter Datenauswertung
- M2 Forschungsmethoden
- Seminar Vertiefung Forschungsmethoden
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- Vorlesung Multivariate Verfahren
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20071009 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20180730.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20180730.md)

**Pflichtmodule (9):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Übung zur prähistorischen Kulturentwicklung Europas
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Bachelorarbeit und –prüfung
- Bachelorarbeit

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20071009 i.d.F. 20190220.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20190220.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20190220.md)

**Pflichtmodule (13):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Übung zur prähistorischen Kultur- entwicklung Europas
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Übung zur prähistorischen Kulturentwicklung Europas
- Klassische Archäologie
- Klassische Archäologie: Griechische Archäologie I A
- Klassische Archäologie: Griechische Archäologie I B
- Bachelorarbeit und -prüfung
- Bachelorarbeit

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20180730 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20180730-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20180730-aes.md)

**Pflichtmodule (9):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Übung zur prähistorischen Kulturentwicklung Europas
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Bachelorarbeit und -prüfung
- Bachelorarbeit

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20190220 ÄS zu 5ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20190220-aes-zu-5aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20190220-aes-zu-5aes.md)

**Pflichtmodule (20):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Übung zur prähistorischen Kultur- entwicklung Europas
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Klassische Archäologie
- Klassische Archäologie: Griechische Archäologie I A
- Klassische Archäologie: Griechische Archäologie I B
- Übung zur griechischen Kultur- geschichte
- Klassische Archäologie: Römische Archäologie I A
- Klassische Archäologie: Römische Archäologie I B
- Übung zur römischen Kultur- geschichte
- Christliche Archäologie
- Christliche Archäologie: Kulturgeschichte I A
- Christliche Archäologie: Kulturgeschichte I B
- Übung zur Kulturgeschichte des Christentums vom 3. bis ins 8. Jh.
- Bachelorarbeit und -prüfung
- Bachelorarbeit

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20240430.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20240430.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20240430.md)

**Pflichtmodule (9):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Übung zur prähistorischen KulturentwicklungEuropas
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Bachelorarbeit und -prüfung
- Bachelorarbeit

### Ein-Fach-BA  Islamisch Religiöse Studien BA IRS Ein-Fach 20121109 i.d.F. 20180709.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20121109-idf-20180709.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20121109-idf-20180709.md)

**Pflichtmodule (3):**
- Bachelorarbeit
- Bhlbi
- aceoraret

### Ein-Fach-BA  Islamisch Religiöse Studien BA IRS Ein-Fach 20121109 i.d.F. 20200909.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20121109-idf-20200909.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20121109-idf-20200909.md)

**Pflichtmodule (3):**
- Bachelorarbeit
- Bhlbi
- aceoraret

### Ein-Fach-BA  Islamisch Religiöse Studien BA IRS Ein-Fach 20180709 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20180709-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20180709-aes.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- Begleitkurs

### Ein-Fach-BA Islamisch-Religiöse Studien BA IRS Ein-Fach 20210318 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20210318-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20210318-aes.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- Begleitkurs

### Ein-Fach-BA  Islamisch Religiöse Studien FPO BA IRS Ein-Fach 20121109 i.d.F. 20210318.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-fpo-ba-irs-ein-fach-20121109-idf-20210318.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-fpo-ba-irs-ein-fach-20121109-idf-20210318.md)

**Pflichtmodule (4):**
- Bachelorarbeit
- Bhlbi
- aceoraret
- Begleitkurs

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20140718 i.d.F. 20190806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20190806.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20190806.md)

**Pflichtmodule (12):**
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Ü Methoden der empirischen Sozialforschung
- Vertiefung Soziologische Metho- denlehre(SozM-V)
- Einführung Soziologische Theo- rien(SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Qualifikationsprofil II (SozQ-II), vgl. § 5
- Bachelorarbeit

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20140718 i.d.F. 20200818.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20200818.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20200818.md)

**Pflichtmodule (16):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Ü Methoden der empirischen Sozialforschung
- Vertiefung Soziologische Methodenlehre (SozM-V)
- Einführung Soziologische Theorien(SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Bachelorarbeit
- Übung Statistik I
- Grundlagen der soziologischen Analyse I(SozB)
- Grundlagen der soziologischen Analyse II(SozW)

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20190806 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20190806-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20190806-aes.md)

**Pflichtmodule (9):**
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Ü Methoden der empirischen Sozial- forschung
- Vertiefung Soziologische Methoden- lehre(SozM-V)
- Bachelorarbeit

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20200818 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20200818-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20200818-aes.md)

**Pflichtmodule (16):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Ü Methoden der empirischen Sozialforschung
- Vertiefung Soziologische Methodenlehre (SozM-V)
- Einführung Soziologische Theorien(SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Bachelorarbeit
- Einführung Soziologische Theorien (SozT-E)
- Übung Statistik I
- Übung Statistik II

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20230822.md)

**Pflichtmodule (15):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Grundlagen der soziologischen Analyse I(SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische Methodenlehre(SozM-E)
- Vertiefung Soziologische Methodenlehre (SozM-V)
- Einführung Soziologische Theorien(SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Bachelorarbeit
- Einführung in die soziologische Methodenlehre (SozM-E)
- Übung Statistik I
- Grundlagen der soziologischen Analyse II(SozW)

### PDF vom 03.08.2015 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fachba-literatur-und-buch-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fachba-literatur-und-buch-aug2017.md)

**Pflichtmodule (14):**
- Basismodul Französische Sprachpraxis 1
- Grundlagen der Neueren deutschen Literaturwissenschaft(NdL BM 1)
- Grundlagen der Buchwissenschaft
- Einführung in das wissenschaftliche Arbeiten
- Basismodul Französische Sprachpraxis 2
- Basismodul Französische Literaturwissenschaft
- Grundlagen der Neueren deutschen Literatur- wissenschaft 2(NdL BM 2)
- Lesen und Lese(r)geschichte im Überblick
- Lehrveranstaltungen an der Partneruniversität2
- Grundlagen des Electronic Publishing und Electronic Commerce
- Typografische Grundlagen
- Literatur und Buch D – F
- Buchwirtschaftliches Praktikum
- Bachelorarbeit

### PDF vom 09.10.2007 i.d.F. 06.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fachstuopro-archaeolwiss-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fachstuopro-archaeolwiss-aug2015.md)

**Pflichtmodule (14):**
- Basismodule: Kulturentwicklung
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I
- Proseminar zur prähistorischen Klttikl E
- uurenwcung uropas
- Übung zur prähistorischen Kulturentwicklung Europas
- Prähistorische Archäologie: Jüngere Urgeschichte I
- KulturentwicklungEuropas Übung zur prähistorischen Kulturentwicklung Europas
- Klassische Archäologie
- Klassische Archäologie: Vorgriechische und griechische Archäologie I
- Proseminar zur antiken Kulturgeschichte
- Übung zur antiken Kulturgeschichte
- Bachelorarbeit und -prüfung
- Bachelorarbeit

### PDF vom 09.10.2007 i.d.F. 21.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fachstuopro-archaeolwiss-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fachstuopro-archaeolwiss-juli2014.md)

**Pflichtmodule (6):**
- Basismodule: Kulturentwicklung
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I
- Prähistorische Archäologie: Jüngere Urgeschichte I
- Klassische Archäologie
- Klassische Archäologie: Vorgriechische und griechische Archäologie I

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

### FPOLitBuch 20150803 i.d.F. 20190906.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fpolitbuch-20150803-idf-20190906.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fpolitbuch-20150803-idf-20190906.md)

**Pflichtmodule (10):**
- Basismodul Französische Sprachpraxis 1
- Grundlagen der Neueren deutschen Literaturwissenschaft (NdL BM 1)
- Einführung
- Methoden
- Basismodul Französische Sprachpraxis 2
- Basismodul Französische Literaturwissen- schaft
- Grundlagen der Neueren deutschen Literatur- wissenschaft2(NdL BM 2)
- RezeptionundNutzung
- Lehrveranstaltungen an der Partneruniversität2
- Bachelorarbeit

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
- Lehrveranstaltungen an der Partneruniversität2
- Bachelorarbeit

### FPOLitBuch 20260305.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fpolitbuch-20260305.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/fpolitbuch-20260305.md)

**Pflichtmodule (10):**
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Schrift und Lesen in Kultur und Gesell- schaft
- Methoden
- Französische Sprachpraxis 2
- Basismodul Französische Literaturwis- senschaft
- Grundlagen der Neueren deutschen Lite- raturwissenschaft 2 (NdL BM 2)
- Mediennutzung und Leseverhalten
- Lehrveranstaltungen an der Partneruni- versität2
- Satz 3
- Bachelorarbeit

### PDF vom 28.09.2007 i.d.F. 11.08.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psycho.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psycho.md)

**Pflichtmodule (9):**
- VL EinführungindieDiagnostik
- psychologischen
- Diagnostik
- Sem. Leistungstests
- Diagnostische
- Verfahren
- VL KlinischePsychologie1
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 04.06.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psychojuni2010.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psychojuni2010.md)

**Pflichtmodule (8):**
- VL EinführungindieDiagnostik
- psychologischen Diagnostik
- Sem. Leistungstests
- Diagnostische
- Verfahren
- VL KlinischePsychologie1
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-ba-ma-psycho-bmstpo-psl-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-ba-ma-psycho-bmstpo-psl-aug2017.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M 1Multivariate Statistik
- M 2Forschungsmethoden
- Metaanalyse oder Umfrage- forschung
- M 3Psychologische Diagnostik
- Spezielle Diagnostik

### PDF vom 28.09.2007 i.d.F. 31.07.2012

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-ba-ma-psycho-juli2012.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-ba-ma-psycho-juli2012.md)

**Pflichtmodule (11):**
- VL EinführungindieDiagnostik
- psychologischen Diagnostik
- Sem. Leistungstests
- Diagnostische
- Verfahren
- VL KlinischePsychologie1
- Klinische
- Psychologie
- M14 Hauptformen der
- Psychotherapie
- Sem. Vertiefung II

### PDF vom 09.11.2012 i.d.F. 22.07.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/stuopro-ba-1fach-islam-relig-studien-juli2015.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/stuopro-ba-1fach-islam-relig-studien-juli2015.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- Begleitkurs

### 29. August 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/1aes-european-ma-lexicography.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/1aes-european-ma-lexicography.md)

**Pflichtmodule (14):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-13
- Basismodul B3-23
- Basismodul B3-33
- Basismodul B3-43
- Basismodul B3-53
- Basismodul B3-63
- Basismodul B3-73
- Basismodul B3-83
- Basismodul B3-93
- Masterarbeit
- Begleitseminar

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/6aesa-ba-ma-psychologie.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/6aesa-ba-ma-psychologie.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M 1Multivariate Statistik
- M 2Forschungsmethoden
- Metaanalyse oder Umfrage- forschung
- M 3Psychologische Diagnostik
- Spezielle Diagnostik

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20200911.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20200911.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20200911.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1Multivariate Statistik
- M2Forschungsmethoden
- Metaanalyse oder Umfrage- forschung
- M3Psychologische Diagnostik
- Spezielle Diagnostik

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20210806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20210806.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20210806.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1Multivariate Statistik
- M2Forschungsmethoden
- Metaanalyse oder Umfrage- forschung
- M3Psychologische Diagnostik
- Spezielle Diagnostik

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20220328.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20220328.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20220328.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- Vorlesung Multivariate Verfahren
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20220328 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20220328-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20220328-aes.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- Vorlesung Multivariate Verfahren
- M1 Multivariate Statistik
- M2 Fhthd
- orscungsmeoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20240229.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240229.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240229.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- Multivariate Verfahren mit computergestützter Datenauswertung
- M2 Forschungsmethoden
- Seminar VertiefungForschungsmethoden
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240926.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240926.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- Vorlesung Multivariate Verfahren
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20241219.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- Multivariate Verfahren mit computergestützter Datenauswertung
- M2 Forschungsmethoden
- Seminar Vertiefung Forschungsmethoden
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822.md)

**Pflichtmodule (7):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- Vorlesung Multivariate Verfahren
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20190308.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190308.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190308.md)

**Pflichtmodule (14):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-13
- Basismodul B3-23
- Basismodul B3-33
- Basismodul B3-43
- Basismodul B3-53
- Basismodul B3-63
- Basismodul B3-73
- Basismodul B3-83
- Basismodul B3-93
- Masterarbeit
- Begleitseminar

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20190723.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190723.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190723.md)

**Pflichtmodule (14):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-13
- Basismodul B3-23
- Basismodul B3-33
- Basismodul B3-43
- Basismodul B3-53
- Basismodul B3-63
- Basismodul B3-73
- Basismodul B3-83
- Basismodul B3-93
- Masterarbeit
- Begleitseminar

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20230223.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230223.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230223.md)

**Pflichtmodule (14):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-13
- Basismodul B3-23
- Basismodul B3-33
- Basismodul B3-43
- Basismodul B3-53
- Basismodul B3-63
- Basismodul B3-73
- Basismodul B3-83
- Im ersten Fachsemesters sollen die Studierenden gemäß Ziffer 3.2 Consortium Agreement Leistungen im Umfang von 25 - fortgesetzt wird.
- Masterarbeit
- Begleitseminar

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230731.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230731.md)

**Pflichtmodule (14):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-13
- Basismodul B3-23
- Basismodul B3-33
- Basismodul B3-43
- Basismodul B3-53
- Basismodul B3-63
- Basismodul B3-73
- Basismodul B3-83
- Im ersten Fachsemesters sollen die Studierenden gemäß Ziffer 3.2 Consortium Agreement Leistungen im Umfang von 25 - fortgesetzt wird.
- Masterarbeit
- Begleitseminar

### European MA Lexicography  MPOEMLex 20190723 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20190723-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20190723-aes.md)

**Pflichtmodule (14):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-13
- Basismodul B3-23
- Basismodul B3-33
- Basismodul B3-43
- Basismodul B3-53
- Basismodul B3-63
- Basismodul B3-73
- Basismodul B3-83
- Basismodul B3-93
- Masterarbeit
- Begleitseminar

### European MA Lexicography  MPOEMLex 20230223 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20230223-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20230223-aes.md)

**Pflichtmodule (14):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-13
- Basismodul B3-23
- Basismodul B3-33
- Basismodul B3-43
- Basismodul B3-53
- Basismodul B3-63
- Basismodul B3-73
- Basismodul B3-83
- Im ersten Fachsemesters sollen die Studierenden gemäß Ziffer 3.2 Consortium Agreement Leistungen im Umfang von 25 - fortgesetzt wird.
- Masterarbeit
- Begleitseminar

### POMAHR 20260115.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/pomahr-20260115.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/pomahr-20260115.md)

**Pflichtmodule (5):**
- Masterarbeit. Aus den folgenden Modulen sind entweder das Modul A oder die Module B1 und B2 zu
- A: Master’s Thesis
- B1: Master’s Thesis
- B2: Internship
- Masterarbeit. Aus den folgenden Modulen sind entweder das Modul A oder die Module B1 und B2 zu wählen:

### PDF vom 28.09.2007 i.d.F. 11.08.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-20ba-ma-psycho.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-20ba-ma-psycho.md)

**Pflichtmodule (9):**
- VL EinführungindieDiagnostik
- psychologischen
- Diagnostik
- Sem. Leistungstests
- Diagnostische
- Verfahren
- VL KlinischePsychologie1
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 04.06.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-20ba-ma-psychojuni2010.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-20ba-ma-psychojuni2010.md)

**Pflichtmodule (8):**
- VL EinführungindieDiagnostik
- psychologischen Diagnostik
- Sem. Leistungstests
- Diagnostische
- Verfahren
- VL KlinischePsychologie1
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-ba-ma-psycho-bmstpo-psl-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-ba-ma-psycho-bmstpo-psl-aug2017.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M 1Multivariate Statistik
- M 2Forschungsmethoden
- Metaanalyse oder Umfrage- forschung
- M 3Psychologische Diagnostik
- Spezielle Diagnostik

### PDF vom 28.09.2007 i.d.F. 31.07.2012

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-ba-ma-psycho-juli2012.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-ba-ma-psycho-juli2012.md)

**Pflichtmodule (11):**
- VL EinführungindieDiagnostik
- psychologischen Diagnostik
- Sem. Leistungstests
- Diagnostische
- Verfahren
- VL KlinischePsychologie1
- Klinische
- Psychologie
- M14 Hauptformen der
- Psychotherapie
- Sem. Vertiefung II

### PDF vom 04.09.2009 i.d.F. 29.08.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/stuopro-ma-lexicography-aug2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/stuopro-ma-lexicography-aug2016.md)

**Pflichtmodule (14):**
- Basismodul B1
- Basismodul B2-1 (Heimmodul)
- Basismodul B2-2 (Heimmodul)
- Basismodul B3-13
- Basismodul B3-23
- Basismodul B3-33
- Basismodul B3-43
- Basismodul B3-53
- Basismodul B3-63
- Basismodul B3-73
- Basismodul B3-83
- Basismodul B3-93
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

**Pflichtmodule (6):**
- Raum und Region
- Einführung in das Studium des Nahen Ostens
- Transregionale Themen und Methoden I
- Transregionale Themen und Methoden II
- Forschungskolloquium
- Bayerisches Orient- kolloquium

### 13. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-ma-philosophie.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-ma-philosophie.md)

**Pflichtmodule (2):**
- Masterarbeit Praktische Philo- sophie
- Masterarbeit Theoretische Philosophie

### 6. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-fpo-ma-archaeologwiss.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-fpo-ma-archaeologwiss.md)

**Pflichtmodule (1):**
- sich um eine Empfehlung. Näheres regelt das Modulhandbuch.

### 23. Februar 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-ma-geschichte.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-ma-geschichte.md)

**Pflichtmodule (2):**
- Masterarbeit(gem.§ 3Abs.6)
- Prüfungsmodul

### 2. März 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-ma-mittelalterfrueheneuzeit.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-ma-mittelalterfrueheneuzeit.md)

**Pflichtmodule (13):**
- Grundlagen der Germanistischen Mediävistik (Med 1)2
- Interdisziplinäres Kolloquium
- Masterfach
- Fachmodul I~~3~~ Masterfach
- Fachmodul II~~3~~ Masterfach
- Fachmodul III~~3~~ Masterfach
- Oberseminar Masterfach4
- Profilfach
- Fachmodul I~~3~~ Profilfach
- Fachmodul II~~3~~ Profilfach
- Masterarbeit
- Mastermodul
- Mündliche Prüfung

### 28. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-developeconominternstudies.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-developeconominternstudies.md)

**Pflichtmodule (14):**
- Pflichtbereich – es müssen alle Module belegt werden.
- Development Economics I
- Development Economics II
- International Economics I
- International Economics II
- Research Methods I
- Research Methods II
- International Business Ethics I
- International Business Ethics II
- Regionale Vertiefung– es müssen Module im Umfangvon 10 ECTS-Punkten belegt werden.
- Regional Module I
- Regional Module II
- Regional Module III
- Regional Module IV

### 13. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-komparatromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-komparatromanistik.md)

**Pflichtmodule (7):**
- Basismodul Französische Sprachpraxis 1
- Vocabulaire, idiomatique et civilisation I
- Communication orale
- Basismodul Französische Sprachpraxis 2
- Grammaire cours élémentaire II (groupe verbal)
- Phonétique pratique, orthophonie et intonation
- Expression écrite I

### 26. Januar 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-theaterpaedagogik.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-theaterpaedagogik.md)

**Pflichtmodule (17):**
- Grundlagen und Rahmen
- der Theaterpädagogik
- Theaterwissenschaft I: Dimensionen des Theatralen und Performativen
- Kulturpädagogik II: Handlungsfelder und Hand- lungsformen
- Angewandte theaterpäda- gogische Forschung
- Theaterwissenschaft II: Kulturen, Funktionen und Wahrnehmungsformen der theatralen Praktiken
- Theaterpädagogische Pra- xisreflexion
- Begleitseminar
- Theaterpädagogische For-
- schungspraxis
- Masterarbeit
- Grundlagen und Rahmen der Theaterpädagogik
- Kulturpädagogik II: Handlungsfelder und Handlungs- formen
- Angewandte theaterpädagogische Forschung
- Theaterwissenschaft II: Kulturen, Funktionen und Wahr- nehmungsformen der theatralen Praktiken
- Theaterpädagogische Praxisrefle- xion
- Theaterpädagogische For- schungspraxis

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aesa-ma-fposino.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aesa-ma-fposino.md)

**Pflichtmodule (8):**
- Basismodul Praktische Philosophie
- Basismodul Theoretische Philosophie
- Praktische Philosophie I2
- Praktische Philosophie II2
- Praktische Philosophie III2
- Theoretische Philosophie I2
- Theoretische Philosophie II2
- Theoretische Philosophie III2

### 17. Januar 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aesa-ma-soziologie.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aesa-ma-soziologie.md)

**Pflichtmodule (1):**
- Masterarbeit

### 28. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aes-ma-germanistik.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aes-ma-germanistik.md)

**Pflichtmodule (5):**
- Sprachnorm und Variation (I LING)
- Übung/Vorlesung
- Systematische Aspekte NDL (I NDL)
- Systematische Aspekte ÄDL (I MED)
- Es sind Aufbaumodule im

### 3. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aes-ma-mittelneulatein.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aes-ma-mittelneulatein.md)

**Pflichtmodule (1):**
- Masterarbeit

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aesa-ma-fpoansk.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aesa-ma-fpoansk.md)

**Pflichtmodule (1):**
- Masterarbeit

### 2. August 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4as-ma-englishstudies.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4as-ma-englishstudies.md)

**Pflichtmodule (2):**
- Siehe Anlage 1
- Siehe Anlage 2

### 8. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/5aesa-fpo-ma-kunstgeschichte.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/5aesa-fpo-ma-kunstgeschichte.md)

**Pflichtmodule (1):**
- Ohne Wahlpflicht- module, je nach Schwerpunkt 30-34 SWS

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/5aesa-ma-fporomanistikdocx.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/5aesa-ma-fporomanistikdocx.md)

**Pflichtmodule (7):**
- Basismodul Aktuelle Interkulturalitäts- und Intermedialitätstheorien
- América Latina: Cultura y literatura
- Modul 4: Sprachpraxis Sprache A: Es ist ein Modul zur Erweiterung bestehender Kenntnisse in der Schwerpunktsprache
- Französisch als Sprache A
- Italienischals Sprache A
- Spanischals Sprache A
- Masterarbeit

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/6aesa-ma-fpo-englstudies.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/6aesa-ma-fpo-englstudies.md)

**Pflichtmodule (7):**
- Masterarbeit
- MA Thesis Module: Linguistics and Applied Linguistics
- Masterarbeit (60-80 Seiten)
- Masterarbeit:Es ist eines der beiden Module zu wählen.
- Masterarbeit im Schwerpunkt Culture and Literature
- MA Thesis Module: Culture and Literature
- Masterarbeit im Schwerpunkt Linguistics and Applied Linguistics

### PDF vom 08.06.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuo-pro-20ma-20mittelaltrenaissance.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuo-pro-20ma-20mittelaltrenaissance.md)

**Pflichtmodule (2):**
- Masterarbeit
- Mündl. Prüfung

### PDF vom 08.06.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuo-pro-20ma-20nahoststudien.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuo-pro-20ma-20nahoststudien.md)

**Pflichtmodule (6):**
- Kernmodul: NOS 12: Sprache II - Zweite semitische Sprache
- Kernmodul: NOS 14: Literatur II - Moderne arabische Litera- tur
- Wahlmodul: „Transregionale Themen“ und Methoden
- Qualifikationsmodul Optional: NOS 01: For- schungskolloquium
- Wahlmodul: NOS 14: Literatur II - Mo- derne arabische Literatur
- Wahlmodul I: „Transregionale Themen“ und Methoden (Religions- wiss., Menschenrechte)

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

**Pflichtmodule (2):**
- Masterarbeit
- SummenSWS /ECTS

### PDF vom 08.06.2010 i.d.F. 26.01.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-archaeologischewiss-feb2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-archaeologischewiss-feb2016.md)

**Pflichtmodule (2):**
- Masterarbeit
- SummenSWS /ECTS

### PDF vom 08.06.2010 i.d.F. 28.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-developmenteconomicsinternstudies-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-developmenteconomicsinternstudies-juli2014.md)

**Pflichtmodule (14):**
- Pflichtbereich – es müssen alle Module
- Development Economics I
- Development Economics II
- International Economics I
- International Economics II
- Research Methods I
- Research Methods II
- International Business Ethics I
- International Business Ethics II
- Regionale Vertiefung– es müssen Module im Umfangvo
- Regional Module I
- Regional Module II
- Regional Module III
- Regional Module IV

### PDF vom 08.06.2010 i.d.F. 02.08.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2016.md)

**Pflichtmodule (5):**
- Masterarbeit
- MA Thesis
- Masterarbeit (60-80 Seiten)
- SieheAnlage1
- SieheAnlage2

### PDF vom 08.06.2010 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2017.md)

**Pflichtmodule (7):**
- Masterarbeit
- MA Thesis Module: Linguis- tics and Applied Linguistics
- Masterarbeit (60-80 Seiten)
- Masterarbeit:Es ist eines der beiden Module zu wählen.
- Masterarbeit im Schwerpunkt Culture and Literature
- MA Thesis Module: Culture and Literature
- Masterarbeit im Schwerpunkt Linguistics and Applied Linguistics

### PDF vom 08.06.2010 i.d.F. 07.03.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-maerz2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-maerz2017.md)

**Pflichtmodule (5):**
- Masterarbeit
- MA Thesis
- Masterarbeit (60-80 Seiten)
- SieheAnlage1
- SieheAnlage2

### PDF vom 08.06.2010 i.d.F. 28.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-germanistik-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-germanistik-juli2014.md)

**Pflichtmodule (5):**
- Sprachnorm und Variation (I LING)
- Übung/Vorlesung
- Systematische Aspekte NDL (I NDL)
- Systematische Aspekte ÄDL (I MED)
- Es sind Aufbaumodule im Umfang von insgesamt 30 ECTS-Punkten zu wählen.

### PDF vom 08.06.2010 i.d.F. 13.06.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2014.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2014.md)

**Pflichtmodule (7):**
- Basismodul Französi- sche Sprachpraxis 1
- Vocabulaire, idiomatique et civilisation I
- Communication orale
- Basismodul Französi- sche Sprachpraxis 2
- Grammaire cours élémentaire II (groupe verbal)
- Phonétique pratique, orthophonie et into- nation
- Expression écrite I

### PDF vom 08.06.2010 i.d.F. 11.06.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2015.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2015.md)

**Pflichtmodule (6):**
- Basismodul Französi- sche Sprachpraxis 1
- Vocabulaire, idiomatique et civilisation I
- Communication orale
- Basismodul Französi- sche Sprachpraxis 2
- Grammaire cours élémentaire II (groupe verbal)
- Phonétique pratique, orthophonie et into- nation

### PDF vom 08.06.2010 i.d.F. 09.03.2011

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-maerz2011.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-maerz2011.md)

**Pflichtmodule (8):**
- (8) Basismodul Sprachpraxis
- (4) Elementarkurs 1
- (4) Elementarkurs 2
- _2e: Wahlpflichtmodul: Optionsmodul Sprachpraxis (Italienisch, Spanisch)_
- (6) Optionsmodul Sprachpraxis
- (2) Sprachkurs 1
- (2) Sprachkurs 2
- (2) Sprachkurs 3

### PDF vom 08.06.2010 i.d.F. 08.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-aug2017.md)

**Pflichtmodule (5):**
- Grundlagen der Museologie
- Oberseminar
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul

### PDF vom 08.06.2010 i.d.F. 02.10.2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-okt2013.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-okt2013.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-aug2017.md)

**Pflichtmodule (13):**
- Grundlagen der Germanistischen Mediävistik (Med 1)2
- Interdisziplinäres Kolloquium
- Masterfach
- Fachmodul I3 Masterfach
- Fachmodul II3 Masterfach
- Fachmodul III3 Masterfach
- Oberseminar Masterfach4
- Profilfach
- Fachmodul I3 Profilfach
- Fachmodul II3 Profilfach
- Masterarbeit
- Mastermodul
- Mündliche Prüfung

### PDF vom 08.06.2010 i.d.F. 02.03.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-maerz2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-maerz2017.md)

**Pflichtmodule (13):**
- Grundlagen der Germanistischen Mediävistik (Med 1)2
- Interdisziplinäres Kolloquium
- Masterfach
- Fachmodul I~~3~~ Masterfach
- Fachmodul II~~3~~ Masterfach
- Fachmodul III~~3~~ Masterfach
- Oberseminar Masterfach4
- Profilfach
- Fachmodul I~~3~~ Profilfach
- Fachmodul II~~3~~ Profilfach
- Masterarbeit
- Mastermodul
- Mündliche Prüfung

### PDF vom 08.06.2010 i.d.F. 03.08.3015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelneulatein-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelneulatein-aug2015.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 13.06.2014 i.d.F. 13.06.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelneulatein-juni2014.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelneulatein-juni2014.md)

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
- Bayerisches Orientkollo- quium

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

**Pflichtmodule (7):**
- Basismodul Aktuelle Interkulturalitäts- und Intermedialitätstheorien
- América Latina: Cultura y literatura
- Modul 4: Sprachpraxis Sprache A: Es ist ein Modul z
- Französisch als Sprache A
- Italienisch als Sprache A
- Spanisch als Sprache A
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-sinologie-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-sinologie-aug2017.md)

**Pflichtmodule (8):**
- Basismodul Praktische Philosophie
- Basismodul Theoretische Philosophie
- Praktische Philosophie I2
- Praktische Philosophie II2
- Praktische Philosophie III2
- Theoretische Philosophie I2
- Theoretische Philosophie II2
- Theoretische Philosophie III2

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

**Pflichtmodule (17):**
- Grundlagen und Rahmen
- der Theaterpädagogik
- Theaterwissenschaft I: Dimensionen des Theatralen und Performativen
- Kulturpädagogik II: Handlungsfelder und Hand- lungsformen
- Angewandte theaterpäda- gogische Forschung
- Theaterwissenschaft II: Kulturen, Funktionen und Wahrnehmungsformen der theatralen Praktiken
- Theaterpädagogische Pra- xisreflexion
- Begleitseminar
- Theaterpädagogische For-
- schungspraxis
- Masterarbeit
- Grundlagen und Rahmen der Theaterpädagogik
- Kulturpädagogik II: Handlungsfelder und Handlungs- formen
- Angewandte theaterpädagogische Forschung
- Theaterwissenschaft II: Kulturen, Funktionen und Wahr- nehmungsformen der theatralen Praktiken
- Theaterpädagogische Praxis- reflexion
- Theaterpädagogische Forschungspraxis

### PDF vom 15.05.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-arabistik-islamwiss-semitistik.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-arabistik-islamwiss-semitistik.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPO MA DH 20190328.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-dh-20190328.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-dh-20190328.md)

**Pflichtmodule (2):**
- Masterarbeit
- Kolloquium

### FPO MA DH 20250411.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-dh-20250411.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-dh-20250411.md)

**Pflichtmodule (2):**
- Masterarbeit
- Kolloquium

### PDF vom 15.05.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-islamisch-relig-studien.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-islamisch-relig-studien.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 18.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-kunstvermittlung.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-kunstvermittlung.md)

**Pflichtmodule (6):**
- Grundlagen der Psychologie für Nichtpsychologen (Importmodul)
- Der Mensch im Spiegel des künst- lerischen Handelns
- Oberseminar
- Ästhetisches Handeln von Kindern, Jugendlichen und Erwachsenen
- Methoden der empirischen Bil- dungsforschung (Importmodul)
- Masterarbeit

### FPO MA L.D. 20230223 i.d.F. 20250320.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-l-d-20230223-idf-20250320.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-l-d-20230223-idf-20250320.md)

**Pflichtmodule (12):**
- Wissenschaftliches Basismodul
- Mediendidaktik
- Educational Techno- logy
- Einführung Educational Techno- logy
- Praxis Digital Educa- tion
- Motivieren und Moderieren
- Lernumgebungen
- Produktion Lernmedien
- E-Assessment
- Masterarbeit
- Masterabschluss- Modul
- Einführung Educational Technology

### FPO MA L.D. 20230223.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-l-d-20230223.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-l-d-20230223.md)

**Pflichtmodule (12):**
- Wissenschaftliches Basismodul
- Mediendidaktik
- Educational Techno- logy
- Einführung Educational Techno- logy
- Praxis Digital Educa- tion
- Motivieren und Moderieren
- Lernumgebungen
- Produktion Lernmedien
- E-Assessment
- Qualitätssicherung
- Masterarbeit
- Masterabschluss- Modul

### (PDF vom 30.07.2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-populaermedienkult-japans.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-populaermedienkult-japans.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOKunstPäd 20250320.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpokunstpaed-20250320.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpokunstpaed-20250320.md)

**Pflichtmodule (23):**
- Pädagogik
- Kulturpädagogische Grundlagen und Dynamiken
- Kunstgeschichte
- Kunst(geschichte) + Mu- seum I
- Kunst(geschichte) + Mu- seum II
- Kunstpädagogik
- Kunst & Bildung
- Kunstdidaktik 2
- Kunstpädagogische Forschung
- Künstlerische Praxis 1
- Seminar aus Kunstpraxis (A+V)
- Künstlerische Praxis 2
- Vermittlungspraxis
- Praktikum(3Wochen)
- Forschungsmethoden
- Einführung in die soziologi- sche Methodenlehre (SozM-E)
- Vertiefung Soziologische Methodenlehre (SozM-V)
- Kulturpädagogische Grund- lagen und Dynamiken
- Kunst(geschichte) + Mu- seum I-II
- Kunst(geschichte) + Mu- seum III
- Kunstdidaktik II
- Kunstpädagogi- sche Forschung
- Praktikum (6 Wo- chen)

### M.A. Learning Design ÄSa 20250320 20250702 .pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/m-a-learning-design-aesa-20250320-20250702.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/m-a-learning-design-aesa-20250320-20250702.md)

**Pflichtmodule (8):**
- Wissenschaftliches Basismodul
- Mediendidaktik
- Educational Technology
- Einführung Educational Technology
- Praxis Digital Education
- Motivieren und Moderieren
- Lernumgebungen
- Produktion Lernmedien

### MA Antike Sprachen und Kulturen FPOAnSK 20100608 i.d.F. 20190326.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20190326.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20190326.md)

**Pflichtmodule (13):**
- Pflichtmodul für alle Studienrichtungen
- Motive und Formen
- Proseminar mit begleitendem Eigenstudium1
- Indogermanistik und Indoiranistik
- Basisbereich Indogermanistik und Indoiranistik2
- Fragestellungen und Geschichte der Indogermanistik
- Hauptseminar Fragestellungen der Indo- germanistik
- Mykenisch und die griechischen Dialekte4
- Hauptseminar Die Kunstsprache Homers
- Indoiranisch
- Übung Altpersisch
- Historische Linguistik und Sprachwandel (II LING 2)
- Masterarbeit

### MA Antike Sprachen und Kulturen FPOAnSK 20100608 i.d.F. 20210222.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20210222.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20210222.md)

**Pflichtmodule (13):**
- Pflichtmodul für alle Studienrichtungen
- Motive und Formen
- Proseminar mit begleitendem Eigenstudium1
- Indogermanistik und Indoiranistik
- Basisbereich Indogermanistik und Indoiranistik2
- Fragestellungen und Geschichte der Indogermanistik
- Hauptseminar Fragestellungen der Indo- germanistik
- Mykenisch und die griechischen Dialekte4
- Hauptseminar Die Kunstsprache Homers
- Indoiranisch
- Übung Altpersisch
- Historische Linguistik und Sprachwandel (II LING 2)
- Masterarbeit

### MA Antike Sprachen und Kulturen FPOAnSK 20190326 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20190326-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20190326-aes.md)

**Pflichtmodule (12):**
- Pflichtmodul für alle Studienrichtungen
- Motive und Formen
- Proseminar mit begleitendem Eigenstudium1
- Indogermanistik und Indoiranistik
- Basisbereich Indogermanistik und Indoiranistik2
- Fragestellungen und Geschichte der Indogermanistik
- Hauptseminar Fragestellungen der Indo- germanistik
- Mykenisch und die griechischen Dialekte4
- Hauptseminar Die Kunstsprache Homers
- Indoiranisch
- Übung Altpersisch
- Historische Linguistik und Sprachwandel (II LING 2)

### MA Antike Sprachen und Kulturen FPOAnSk 20250131.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20250131.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20250131.md)

**Pflichtmodule (13):**
- Pflichtmodul für alle Studienrichtungen
- Motive und Formen
- Proseminar mit begleitendem Eigenstu- dium1
- Indogermanistik und Indoiranistik
- Basisbereich Indogermanistik und Indoiranistik2
- Fragestellungen und Geschichte der Indogermanistik
- Hauptseminar Fragestellungen der Indo- germanistik
- Mykenisch und die griechischen Dialekte4
- Hauptseminar Die Kunstsprache Ho- mers
- Indoiranisch
- Übung Altpersisch
- Historische Linguistik und Sprach- wandel
- Masterarbeit

### MA Arabistik Islamwissenschaft Semitistik FPOAIS 20150515 i.d.F. 20200813.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-arabistik-islamwissenschaft-semitistik-fpoais-20150515-idf-20200813.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-arabistik-islamwissenschaft-semitistik-fpoais-20150515-idf-20200813.md)

**Pflichtmodule (1):**
- Masterarbeit

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

### MA Archäologische Wissenschaften FPOArWi 20200214 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-archaeologische-wissenschaften-fpoarwi-20200214-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-archaeologische-wissenschaften-fpoarwi-20200214-aes.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Buchwissenschaft FPO M.A. BuWi 20100608 i.d.F. 20190611.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpo-m-a-buwi-20100608-idf-20190611.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpo-m-a-buwi-20100608-idf-20190611.md)

**Pflichtmodule (9):**
- Wissenschaftstheorie
- Transformationsprozesse
- Kernmodul 1: Medienkommunikation
- Hauptseminar
- Kernmodul 2: Medienwirtschaft
- Projekt
- Projektarbeit
- Forschungsperspektiven
- Masterarbeit

### MA Buchwissenschaft FPOBuWi 20190611 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpobuwi-20190611-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpobuwi-20190611-aes.md)

**Pflichtmodule (9):**
- Wissenschaftstheorie
- Transformationsprozesse
- Kernmodul 1: Medienkommunikation
- Hauptseminar
- Kernmodul 2: Medienwirtschaft
- Projekt
- Projektarbeit
- Forschungsperspektiven
- Masterarbeit

### MA Buchwissenschaft FPOBuWi 20230223 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpobuwi-20230223-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpobuwi-20230223-aes.md)

**Pflichtmodule (7):**
- Kernmodul 1: Rahmenbedingungen
- Hauptseminar I
- Hauptseminar II
- Kernmodul 2: Praktiken
- Projekt
- Projektarbeit
- Masterarbeit

### MA DEIS FPODEIS 20100608 i.d.F. 20180221.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20180221.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20180221.md)

**Pflichtmodule (12):**
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

### MA DEIS FPODEIS 20100608 i.d.F. 20190731.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20190731.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20190731.md)

**Pflichtmodule (10):**
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

### MA DEIS FPODEIS 20100608 i.d.F. 20200408.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20200408.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20200408.md)

**Pflichtmodule (12):**
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

### MA DEIS FPODEIS 20100608 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20230731.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20230731.md)

**Pflichtmodule (12):**
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

### MA DEIS FPODEIS 20180221 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20180221-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20180221-aes.md)

**Pflichtmodule (12):**
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

### MA DEIS FPODEIS 20240807.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20240807.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20240807.md)

**Pflichtmodule (8):**
- Development Economics I
- Development Economics II
- Research Methods I
- Research Methods II
- International Business Ethics I
- International Business Ethics II
- Masterarbeit
- Master Thesis

### MA Digitale Japanstudien FPO M.A DIJAS 20210429 i.d.F. 20230426.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-digitale-japanstudien-fpo-m-a-dijas-20210429-idf-20230426.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-digitale-japanstudien-fpo-m-a-dijas-20210429-idf-20230426.md)

**Pflichtmodule (24):**
- MA-BM1 Politik & Gesellschaft Japans
- MA-BM2 Medien in Japan
- MA-BM3 Digitale Methoden
- Masterarbeit
- MA-MA1 Masterarbeit
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

**Pflichtmodule (24):**
- MA-BM1 Politik & Gesellschaft Japans
- MA-BM2 Medien in Japan
- MA-BM3 Digitale Methoden
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

**Pflichtmodule (1):**
- the following modules in the specialisation Linguistics and Applied Linguistics.

### MA English Studies FPOEnStud 20100608 i.d.F. 202108012 en.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20100608-idf-202108012-en.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20100608-idf-202108012-en.md)

**Pflichtmodule (2):**
- hosen.
- the following modules in the specialisation Linguistics and Applied

### MA English Studies FPOEnStud 20100608 i.d.F. 20210812.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20100608-idf-20210812.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20100608-idf-20210812.md)

**Pflichtmodule (6):**
- Masterarbeit
- MA Thesis Module: Linguistics and Applied Linguistics
- Masterarbeit:Es ist eines der beiden Module zu wählen.
- Masterarbeit im Schwerpunkt Culture and Literature
- MA Thesis Module: Culture and Literature
- Masterarbeit im Schwerpunkt Linguistics and Applied Linguistics

### MA English Studies FPOEnStud 20210812 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20210812-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20210812-aes.md)

**Pflichtmodule (6):**
- Masterarbeit
- MA Thesis Module: Linguistics and Applied Linguistics
- Masterarbeit:Es ist eines der beiden Module zu wählen.
- Masterarbeit im Schwerpunkt Culture and Literature
- MA Thesis Module: Culture and Literature
- Masterarbeit im Schwerpunkt Linguistics and Applied Linguistics

### MA English Studies FPOEnStud 20250930.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20250930.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-english-studies-fpoenstud-20250930.md)

**Pflichtmodule (26):**
- Core Module Culture
- Selbststudium mit Kontaktzeit
- Core Module Literature
- Selbststudium mitKontaktzeit
- Academic Language Skills:Es
- Academic Discourse
- Advanced Grammar
- Discourse Structure
- Translation German-English
- Masterarbeit
- MA Thesis Module:
- Master Module I: Culture oder Literature
- Master Module II: Culture oder Literature
- Linguistics and Applied Linguistics:Es sind mind. 30 ECTS-Punkte aus den folgenden Modulen des Schwerpunkts Linguistics and Applied Linguistics zu wählen.
- Introductory Module Topics in Linguistic Theory and Language Acquisition Research
- Corpus Linguistics
- First Language Acquisition and Language Teaching
- Second Language Acquisi- tion and Language Teaching
- Language Variation
- Masterarbeit:Es ist eines der beiden Module zu wählen.
- Masterarbeit im Schwerpunkt Culture and Literature
- MA Thesis Module: Culture and Literature
- Masterarbeit im Schwerpunkt Linguistics and Applied Linguistics
- MA Thesis Module: Linguistics and Applied Linguistics
- W ETPk
- Masterarbeit (60-80 Sei- ten)

### MA Germanistik 20100608 i.d.F. 20180213.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20180213.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20180213.md)

**Pflichtmodule (11):**
- Sprachnorm und Variation (I LING)
- Übung/Vorlesung
- Systematische Aspekte NDL (I NDL)
- Systematische Aspekte ÄDL (I MED)
- Es sind Aufbaumodule im Umfang von insgesamt 30 ECTS-Punkten zu wählen.3)
- Masterarbeit LING (IV LING 1)
- Abschlussprüfung LING (IV LING 2)
- Masterarbeit NDL (IV NDL 1)
- Abschlussprüfung NDL (IV NDL 2)
- Masterarbeit ÄDL (IV MED 1)
- Abschlussprüfung ÄDL (IV MED 2)

### MA Germanistik 20100608 i.d.F. 20200610.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20200610.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20200610.md)

**Pflichtmodule (19):**
- Fachmodulegemäß§ 5
- Fachmodul I2)
- Übung/Kolleg
- Fachmodul II2)
- Fachmodul III
- Profilbereich (gem. FPO § 3 Abs. 2)
- Profilmodul Germanistische Linguistik3)
- Profilmodul Neuere deutsche Literaturwissenschaft3)
- Profilmodul Germanistische Mediävistik3)
- Oberseminar/Kolloquium
- Interdisziplinäre undpraktische Module
- Workshop
- Projektmodul
- Extradisziplinäres Modul I
- Abschlussmodul
- Masterarbeit
- Abschlussprüfung
- Freier Bereich (Es sind Module im
- Fachmodul IV4)

### MA Germanistik 20100608 i.d.F. 20210113.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20210113.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20210113.md)

**Pflichtmodule (23):**
- Fachmodul I2)
- Fachmodul II2)
- Fachmodul III
- Profilbereich (gem. FPO § 3 Abs. 2)
- Profilmodul Germanistische Linguistik3)
- Übung/Kolleg
- Profilmodul Neuere deutsche Literaturwissenschaft3)
- Profilmodul Germanistische Mediävistik3)
- Oberseminar/Kolloquium
- Interdisziplinäre und praktische Module
- Workshop
- Projektmodul
- Extradisziplinäres Modul I
- Abschlussmodul
- Masterarbeit
- Abschlussprüfung
- Freier Bereich (Es sind Module im
- Fachmodul IV4)
- Fachmodul V
- Lektüremodul I
- Profilmodul Neuere deutsche Literatur- wissenschaft3)
- Oberseminar/ Kolloquium
- Freier Bereich (Es sind Module im Umfang von 20 ECTS-Punkten zu belegen)5)

### MA Germanistik 20100608 i.d.F. 20230323.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20230323.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20230323.md)

**Pflichtmodule (23):**
- Fachmodul I2)
- Fachmodul II2)
- Fachmodul III
- Profilbereich (gem. FPO § 3 Abs. 2)
- Profilmodul Germanistische Linguistik3)
- Übung/Kolleg
- Profilmodul Neuere deutsche Literaturwissenschaft3)
- Profilmodul Germanistische Mediävistik3)
- Oberseminar/Kolloquium
- Interdisziplinäre und praktische Module
- Workshop
- Projektmodul
- Extradisziplinäres Modul I
- Abschlussmodul
- Masterarbeit
- Abschlussprüfung
- Freier Bereich (Es sind Module im
- Fachmodul IV4)
- Fachmodul V
- Lektüremodul I
- Profilmodul Neuere deutsche Literatur- wissenschaft3)
- Oberseminar/ Kolloquium
- Freier Bereich (Es sind Module im Umfang von 20 ECTS-Punkten zu belegen)5)

### MA Germanistik 20180213 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20180213-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20180213-aes.md)

**Pflichtmodule (11):**
- Sprachnorm und Variation (I LING)
- Übung/Vorlesung
- Systematische Aspekte NDL (I NDL)
- Systematische Aspekte ÄDL (I MED)
- Es sind Aufbaumodule im Umfang von insgesamt 30 ECTS-Punkten zu wählen.3
- Masterarbeit LING (IV LING 1)
- Abschlussprüfung LING (IV LING 2)
- Masterarbeit NDL (IV NDL 1)
- Abschlussprüfung NDL (IV NDL 2)
- Masterarbeit ÄDL (IV MED 1)
- Abschlussprüfung ÄDL (IV MED 2)

### MA Germanistik 20200610 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20200610-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20200610-aes.md)

**Pflichtmodule (18):**
- Fachmodul I2)
- Übung/Kolleg
- Fachmodul II2)
- Fachmodul III
- Profilbereich (gem. FPO § 3 Abs. 2)
- Profilmodul Germanistische Linguistik3)
- Profilmodul Neuere deutsche Literaturwissenschaft3)
- Profilmodul Germanistische Mediävistik3)
- Oberseminar/Kolloquium
- Interdisziplinäre und praktische
- Workshop
- Projektmodul
- Extradisziplinäres Modul I
- Abschlussmodul
- Masterarbeit
- Abschlussprüfung
- Freier Bereich (Es sind Module im Umfang von 20 ECTS-Punkten zu belegen.)
- Fachmodul IV4

### MA Germanistik 20250930.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20250930.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20250930.md)

**Pflichtmodule (27):**
- Fachmodul I2)
- Übung/Kolleg
- Fachmodul II2)
- Fachmodul III
- Profilbereich (gem. § 4 Abs. 2)
- Profilmodul Germanistische Linguistik3)
- Profilmodul Neuere deutsche Literaturwissenschaft3)
- Profilmodul Germanistische Mediävistik3)
- Oberseminar/Kolloquium
- Interdisziplinäre undpraktische Module
- Workshop
- Projektmodul
- Extradisziplinäres Modul I
- Abschlussmodul
- Masterarbeit
- Abschlussprüfung
- Fachmodulegemäß§ 6
- Profilbereich(gem. FPO§ 4 Abs. 2)
- Profilmodul Neuere deutsche Literatur- wissenschaft3)
- Oberseminar/ Kolloquium
- Freier Bereich(Es sind Module im Umfang von 20 ECTS-Punkten zu belegen)5)
- Fachmodul IV4)
- Fachmodul V
- Lektüremodul I
- Lektüremodul II
- Extradisziplinäres Modul II
- Extradisziplinäres Modul III

### MA Germanistik FPOGerm 20210113 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-fpogerm-20210113-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-fpogerm-20210113-aes.md)

**Pflichtmodule (22):**
- Fachmodul I2)
- Fachmodul II2)
- Fachmodul III
- Profilbereich (gem. FPO § 3 Abs. 2)
- Profilmodul Germanistische Linguistik3)
- Übung/Kolleg
- Profilmodul Neuere deutsche Literatur- wissenschaft3)
- Profilmodul Germanistische Mediävistik3)
- Oberseminar/ Kolloquium
- Interdisziplinäre undpraktische Module
- Workshop
- Projektmodul
- Extradisziplinäres Modul I
- Masterarbeit
- Abschlussprüfung
- Freier Bereich (Es sind Module im Umfang von 20 ECTS-Punkten zu belegen)5)
- Fachmodul IV4)
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

**Pflichtmodule (5):**
- Grundlagen der Museologie
- Oberseminar
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul

### MA Kunstgeschichte MFPOKunstGesch 20100608 i.d.F. 20200214.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20100608-idf-20200214.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20100608-idf-20200214.md)

**Pflichtmodule (6):**
- Grundlagen der Museologie I
- Grundlagen der Museologie II
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul
- Oberseminar

### MA Kunstgeschichte MFPOKunstGesch 20200214 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20200214-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20200214-aes.md)

**Pflichtmodule (6):**
- Grundlagen der Museologie I
- Grundlagen der Museologie II
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul
- Oberseminar

### MA Kunstgeschichte MFPOKunstGesch 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20230822.md)

**Pflichtmodule (6):**
- Grundlagen der Museologie I
- Grundlagen der Museologie II
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul
- Oberseminar

### MA Linguistik FPOLing 20100608 i.d.F. 20180618.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20100608-idf-20180618.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20100608-idf-20180618.md)

**Pflichtmodule (2):**
- Masterarbeit
- WP 3/1 Mastermodul Linguistik (Germanistik)

### MA Linguistik FPOLing 20100608 i.d.F. 20210812.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20100608-idf-20210812.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20100608-idf-20210812.md)

**Pflichtmodule (2):**
- Masterarbeit
- WP Mastermodul Linguistik (Germanistik)

### MA Linguistik FPOLing 20100608 i.d.F. 20220718.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20100608-idf-20220718.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20100608-idf-20220718.md)

**Pflichtmodule (2):**
- Masterarbeit
- WP Mastermodul Linguistik (Germanistik)

### MA Linguistik FPOLing 20180618 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20180618-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20180618-aes.md)

**Pflichtmodule (4):**
- Masterarbeit
- WP 3/1 Mastermodul Linguistik (Germanistik)
- WP 3/1 Mastermodul Linguistik (Anglistik)
- WP 3/1 Mastermodul Linguistik (Romanistik)

### MA Linguistik FPOLing 20210812 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20210812-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-linguistik-fpoling-20210812-aes.md)

**Pflichtmodule (4):**
- Masterarbeit
- WP Mastermodul Linguistik (Germanistik)
- WP Mastermodul Linguistik (Anglistik)
- WP Mastermodul Linguistik (Romanistik)

### MA Literaturstudien FPOLitStud 20100608 i.d.F. 20180515.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-fpolitstud-20100608-idf-20180515.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-fpolitstud-20100608-idf-20180515.md)

**Pflichtmodule (5):**
- Interdisziplinäres Basismodul zur Einführung in den Theoriekomplex Literatur/Kultur/Medien
- Hauptseminar
- Basismodul Aktuelle Interkulturalitäts- und Intermedialitätstheorien
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität
- Masterarbeit

### MA Literaturstudien FPOLitStud 20240430.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-fpolitstud-20240430.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-fpolitstud-20240430.md)

**Pflichtmodule (10):**
- Interdisziplinäres Basismodul zur Einführung in den Theoriekomplex Literatur/Kultur/Medien
- Hauptseminar
- Einführungsmodul: Theorien und Methoden
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität
- Kernfachgemäß§ 41)
- Masterarbeit im Kernfach
- Masterarbeit
- und ECTS-Punkte
- Interdisziplinäres Basismodul zur Einführung in den Theorienkomplex Literatur/Kultur/Medien
- mind .

### MA Literaturstudien MFPOLitStud 20180515 Äs.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-mfpolitstud-20180515-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-mfpolitstud-20180515-aes.md)

**Pflichtmodule (5):**
- Interdisziplinäres Basismodul zur Einführung in den Theoriekomplex Literatur/Kultur/Medien
- Hauptseminar
- Basismodul Aktuelle Interkulturali- täts- und Intermedialitätstheorien
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität
- Masterarbeit

### MA Mittelalter und Frühe Neuzeit FPOMiFNZ 20100608 i.d.F. 20190809.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20100608-idf-20190809.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20100608-idf-20190809.md)

**Pflichtmodule (13):**
- Grundlagen der Germanistischen Mediävistik (Med 1)2
- Interdisziplinäres Kolloquium
- Masterfach
- Fachmodul I3 Masterfach
- Fachmodul II3 Masterfach
- Fachmodul III3 Masterfach
- Oberseminar Masterfach4
- Profilfach
- Fachmodul I3 Profilfach
- Fachmodul II3 Profilfach
- Masterarbeit
- Mastermodul
- Mündliche Prüfung

### MA Mittelalter und Frühe Neuzeit FPOMiFNZ 20240131.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20240131.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20240131.md)

**Pflichtmodule (13):**
- Grundlagen der Germanistischen Mediävistik (Med1)2
- Interdisziplinäres Kolloquium
- Masterfach
- Fachmodul I3 Masterfach
- Fachmodul II3 Masterfach
- Fachmodul III3 Masterfach
- Oberseminar Masterfach4
- Profilfach
- Fachmodul I3 Profilfach
- Fachmodul II3 Profilfach
- Masterarbeit
- Mastermodul
- Mündliche Prüfung

### MA Nahoststudien FPONahOstStud 20100608 i.d.F. 20180817 .pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20100608-idf-20180817.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20100608-idf-20180817.md)

**Pflichtmodule (6):**
- Raum und Region
- Einführung in das Studium des Nahen Ostens
- Transregionale Themen und Methoden I
- Transregionale Themen und Methoden II
- Forschungskolloquium
- Masterarbeit

### MA Nahoststudien FPONahOstStud 20180817 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20180817-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20180817-aes.md)

**Pflichtmodule (6):**
- Raum und Region
- Einführung in das Studium des Nahen Ostens
- Transregionale Themen und Methoden I
- Transregionale Themen und Methoden II
- Forschungskolloquium
- Masterarbeit

### MA Nahoststudien FPONahOstStud 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20230822.md)

**Pflichtmodule (7):**
- Pflichtbereich(40 ECTS-Punkte)
- Raum und Region
- Einführung in das Studium des Nahen Ostens
- Transregionale Themen und Methoden I
- Transregionale Themen und Methoden II
- Forschungskolloquium
- Masterarbeit

### MA North American Studies FPONoAmStud 20100608 i.d.F. 20210812.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-north-american-studies-fponoamstud-20100608-idf-20210812.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-north-american-studies-fponoamstud-20100608-idf-20210812.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA North American Studies FPONoAmStud 20230928.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-north-american-studies-fponoamstud-20230928.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-north-american-studies-fponoamstud-20230928.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Philosophie FPOPhilo 20100608 i.d.F. 20190520.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-philosophie-fpophilo-20100608-idf-20190520.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-philosophie-fpophilo-20100608-idf-20190520.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Philosophie FPOPhilo 20190520 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-philosophie-fpophilo-20190520-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-philosophie-fpophilo-20190520-aes.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Philosophie FPOPhilo 20240904.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-philosophie-fpophilo-20240904.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-philosophie-fpophilo-20240904.md)

**Pflichtmodule (1):**
- Masterarbeit

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

**Pflichtmodule (7):**
- Kernmodul 1: Rahmenbedingungen
- Hauptseminar I
- Hauptseminar II
- Kernmodul 2: Praktiken
- Projekt
- Projektarbeit
- Masterarbeit

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

**Pflichtmodule (3):**
- MA-BM1 Politik & Gesellschaft Japans
- MA-BM2 Medien in Japan
- MA-BM3 Digitale Methoden

### Modulstudien Digital Humanities POM-DH 20210729 i.d.F. 20220808.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/modulstudien-digital-humanities-pom-dh-20210729-idf-20220808.md`](../pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/modulstudien-digital-humanities-pom-dh-20210729-idf-20220808.md)

**Pflichtmodule (7):**
- Grundlagen der Informatik (GdI-Kompakt)
- Bereich DH Schwerpunkt
- DH-Modul 1: Schwerpunkt Sprache und Text
- DH-Modul 2: Schwerpunkt Gesellschaft und Raum
- DH-Modul 3: Schwerpunkt Bild und Medien
- Theoretische Informatik für Wirtschaftsinformatik und Lehramts- studierende
- Grundlagen der Computerlinguistik II (statistischeVerfahren)

### Modulstudien Digital Humanities POM-DH 20210729.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/modulstudien-digital-humanities-pom-dh-20210729.md`](../pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/modulstudien-digital-humanities-pom-dh-20210729.md)

**Pflichtmodule (6):**
- Grundlagen der Informatik (GdI-Kompakt)
- Bereich DH Schwerpunkt
- DH-Modul 1: Schwerpunkt Sprache und Text
- DH-Modul 2: Schwerpunkt Gesellschaft und Raum
- DH-Modul 3: Schwerpunkt Bild und Medien
- Theoretische Informatik für Wirtschaftsinformatik und Lehramts- studierende

### Modulstudien Digital Humanities POM-DH 20250411.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/modulstudien-digital-humanities-pom-dh-20250411.md`](../pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/modulstudien-digital-humanities-pom-dh-20250411.md)

**Pflichtmodule (8):**
- Grundlagen der Informatik (GdI-Kompakt)
- Einführung in die Informatik für DH
- Bereich DH Schwerpunkt (max. 5 ECTS-Punkte)
- DH-Modul 1: Schwerpunkt Sprache undText
- DH-Modul 2: Schwerpunkt Gesellschaft und Daten
- DH-Modul 3: Schwerpunkt Bild und Medien
- Grundlagen der Informatik (GdI-Kompakt) 7
- Grundlagen der Computerlinguistik II (statistische Verfahren)

### PO ZS Geow im LA 20250320 .pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/po-zs-geow-im-la-20250320.md`](../pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/po-zs-geow-im-la-20250320.md)

**Pflichtmodule (4):**
- Grundlagen der Geowissenschaften I
- Rohstoffe und Nachhaltigkeit
- Dynamik des Systems Erde
- Kompetenzseminar zum Klimawandel

### PO Zusatzstudien Gender 20260305.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/po-zusatzstudien-gender-20260305.md`](../pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/po-zusatzstudien-gender-20260305.md)

**Pflichtmodule (2):**
- Basismodul: Was ist Gender?
- Gender in Natur- und Technik- wissenschaften

### 7. Dezember 2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/2aenderungssatzung-ma-20medienethikreligion.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/2aenderungssatzung-ma-20medienethikreligion.md)

**Pflichtmodule (3):**
- Grundlagen der Kommunikationswissenschaft
- SEM Methoden empirische Kommunikationsforschung
- Oder:Vertiefung Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach)

### 13. November 2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/3aes-ma-medien-ethik-religion.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/3aes-ma-medien-ethik-religion.md)

**Pflichtmodule (8):**
- Grundlagen der Kommunikations‐ oder Medienwissenschaft (Importmodul)
- SEM Methoden empirische Kommuni‐ kationsforschung oder Grundlagen der Medienwissenschaft
- _Oder_: Vertiefung der Kommunikations‐ oder Medienwissenschaft (je nach bisherigem Studienfach1) (Importmodul)
- Medienethik
- SEM Grundzüge der Medienethik
- Medienkunde, Journalismus und PR/Öffentlichkeitsarbeit
- SEM Grundfragen der Journalistik und Einführung in journalistische Darstel‐ lungsformen
- SEM Grundlagen der PR‐Theorie und Projekt Öffentlichkeitsarbeit

### Evangelische Theologie StuPO EvTheol 20150811 i.d.F. 20200916.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20200916.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20200916.md)

**Pflichtmodule (26):**
- Basismodule (Pflichtbereich)
- Propädeuticum
- Propäd – Grundlagen des Theologiestudiums / Pro- pädeuticum
- Fächergruppe AT/NT:Es muss ein Basismodul AT und ein Basismodul NT absolviert werden. Dabei muss mindestens in einem der beiden Module die Leistungsvariante A (12 ECTS- Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- AT1-A – Basismodul
- PS Einführung in die exegetischen Methoden AT
- Altes Testament
- Modulprüfung
- AT1-B – Basismodul Altes Testament
- V/Ü weitere Lehrveranstaltung
- NT1-A – Basismodul
- PS Einführung in die exegetischen Methoden NT
- Neues Testament
- NT1-B – Basismodul Neues Testament
- Fächergruppe ST/KG:Es muss ein Basismodul KG und ein Basismodul ST absolviert werden. Dabei muss mindestens in einem der beiden Module die Leistungsvariante A (12 ECTS- Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- KG1-A – Basismodul
- V KGimÜberblick 1,2, 3,4oder54
- Kirchengeschichte4
- KG1-B – Basismodul Kirchengeschichte4
- PSEinführungindieMethodender KG
- ST1-A – Basismodul Systematische Theologie
- PS Einführung in die Methoden der Systemati- h Thli
- scen eooge
- Ü Übung
- ST1-B – Basismodul Systematische Theologie
- PS Einführung in die Methoden der Systemati- schen Theologie

### Evangelische Theologie StuPO EvTheol 20150811 i.d.F. 20230314.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20230314.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20230314.md)

**Pflichtmodule (27):**
- Basismodule (Pflichtbereich)
- Propädeuticum
- Propäd – Grundlagen des Theologiestudiums / Pro- pädeuticum
- Fächergruppe AT/NT:Es muss ein Basismodul AT und ein Basismodul NT absolviert werden. Dabei muss mindestens in einem der beiden Module die Leistungsvariante A (12 ECTS- Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- AT1-A – Basismodul
- PS Einführung in die exegetischen Methoden AT
- Altes Testament
- Modulprüfung
- AT1-B – Basismodul Altes Testament
- V/Ü weitere Lehrveranstaltung
- NT1-A – Basismodul
- PS Einführung in die exegetischen Methoden NT
- Neues Testament
- NT1-B – Basismodul Neues Testament
- Ü Übung zum Proseminar
- Fächergruppe ST/KG:Es muss ein Basismodul KG und ein Basismodul ST absolviert werden. Dabei muss mindestens in einem der beiden Module die Leistungsvariante A (12 ECTS- Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- KG1-A – Basismodul
- V KGimÜberblick 1,2, 3,4oder54
- Kirchengeschichte4
- KG1-B – Basismodul Kirchengeschichte4
- PSEinführungindieMethodender KG
- ST1-A – Basismodul Systematische Theologie
- PS Einführung in die Methoden der Systemati- h Thli
- scen eooge
- Ü Übung
- ST1-B – Basismodul Systematische Theologie
- PS Einführung in die Methoden der Systemati- schen Theologie

### Evangelische Theologie StuPO EvTheol 20200916 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20200916-aes.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20200916-aes.md)

**Pflichtmodule (25):**
- Basismodule (Pflichtbereich)
- Propädeuticum
- Propäd – Grundlagen des Theologiestudiums / Pro- pädeuticum
- Fächergruppe AT/NT:Es muss ein Basismodul AT und ein Basismodul NT absolviert werden. Dabei muss mindestens in einem Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- AT1-A – Basismodul
- PS Einführung in die exegetischen Methoden AT
- Altes Testament
- Modulprüfung
- AT1-B – Basismodul Altes Testament
- V/Ü weitere Lehrveranstaltung
- NT1-A – Basismodul
- PS Einführung in die exegetischen Methoden NT
- Neues Testament
- NT1-B – Basismodul Neues Testament
- Fächergruppe ST/KG:Es muss ein Basismodul KG und ein Basismodul ST absolviert werden. Dabei muss mindestens in einem Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- KG1-A – Basismodul
- V KGimÜberblick 1,2, 3,4oder54
- Kirchengeschichte4
- KG1-B – Basismodul Kirchengeschichte4
- PSEinführungindieMethodender KG
- ST1-A – Basismodul Systematische Theologie
- PS Einführung in die Methoden der Systemati- hThli
- sceneooge
- Ü Übung
- ST1-B–Basismodul

### MA Christliche Medienkommunikation FPO C-M-K 20150611 i.d.F. 20180711.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20150611-idf-20180711.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20150611-idf-20180711.md)

**Pflichtmodule (2):**
- Masterarbeit
- Kolloquium zur Masterarbeit

### MA Christliche Medienkommunikation FPO C-M-K 20150611 i.d.F. 20191212.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20150611-idf-20191212.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20150611-idf-20191212.md)

**Pflichtmodule (2):**
- Masterarbeit
- Kolloquium zur Masterarbeit

### MA Christliche Medienkommunikation FPO C-M-K 20180711 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20180711-aes.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20180711-aes.md)

**Pflichtmodule (2):**
- Masterarbeit
- Kolloquium zur Masterarbeit

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20180711.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20180711.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20180711.md)

**Pflichtmodule (19):**
- Grundlagen Kommunikationswissenschaft
- Grundlagen der KommunikationswissenschaftI
- Grundlagen der Kommunikationswissenschaft II
- Vertiefung Kommunikationswissenschaft
- Vertiefung der KommunikationswissenschaftI
- Vertiefung der Kommunikationswissenschaft II
- Medienwissenschaft
- Dimensionen des Medialen und Visuellen
- Medienethik
- Medienkunde/Journalismus
- Mediensysteme, Journalismus und Öffentlichkeitsarbeit
- SEM Einführung in die Journalistik, Recherche und journalistischeDarstellungsformen
- SEMÖffentlichkeitsarbeit (Theorie undPraxis)
- SEM Medienrecht
- Praxismodul
- Praxisfeld Medien
- SEM Praxisfeld Medien II
- SEM Praxisfeld Medien III
- Masterarbeit

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20191212.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20191212.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20191212.md)

**Pflichtmodule (20):**
- Grundlagen Kommunikationswissenschaft
- Grundlagen der KommunikationswissenschaftI
- Grundlagen der Kommunikationswissenschaft II
- Vertiefung Kommunikationswissenschaft
- Vertiefung der KommunikationswissenschaftI
- Vertiefung der Kommunikationswissenschaft II
- Medienwissenschaft
- Dimensionen des Medialen und Visuellen
- Medienethik
- Medienkunde/Journalismus
- Mediensysteme, Journalismus und Öffentlichkeitsarbeit
- SEM Einführung in die Journalistik, Recherche und journalistischeDarstellungsformen
- SEMÖffentlichkeitsarbeit (Theorie undPraxis)
- SEM Medienrecht
- Praxismodul
- Praxisfeld Medien
- SEM Praxisfeld Medien II
- SEM Praxisfeld Medien III
- Masterarbeit
- Kolloquium zur Masterarbeit

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20200909.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20200909.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20200909.md)

**Pflichtmodule (20):**
- Grundlagen der Kommunikationswissenschaft
- Grundlagen der Kommunikations- wissenschaft
- Grundzüge der Theologie(Es istgemäß desgewählten Schwerpunkts eines der beiden Module
- Grundzüge der Theologie für Nicht- Theologen (ChristentumundMedien)
- Grundzüge der Theologie für Nicht- Theologen (IslamundMedien)
- Medienethik
- Mediensysteme/Journalismus(Es sind alle Module zu belegen)
- Mediensysteme, Journalismus und Öffentlichkeitsarbeit
- SEM Einführung in die Journalistik, Recherche und journalistischeDarstellungsformen
- SEMÖffentlichkeitsarbeit (Theorie undPraxis)
- SEM Medienrecht
- Praxismodul
- Praxisfeld Medien
- SEM PraxisfeldMedien II
- SEM PraxisfeldMedien III
- Masterarbeit
- Kolloquium zur Masterarbeit
- Grundzüge der Theologie(Es ist gemäß des gewählten Schwerpunkts eines der beiden Module zu belegen)
- SEM Einführung in die Journalistik, Recherche und journalistische Dar- stellungsformen
- SEM Öffentlichkeitsarbeit (Theorie undPraxis)

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20230731.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20230731.md)

**Pflichtmodule (20):**
- Grundlagen der Kommunikationswissenschaft
- Grundlagen der Kommunikations- wissenschaft
- Grundzüge der Theologie(Es istgemäß desgewählten Schwerpunkts eines der beiden Module
- Grundzüge der Theologie für Nicht- Theologen (Christentum und Medien)
- Grundzüge der Theologie für Nicht- Theologen (Islam und Medien)
- Medienethik
- Mediensysteme/Journalismus(Es sind alle Module zu belegen)
- Mediensysteme, Journalismus und Öffentlichkeitsarbeit
- SEM Einführung in die Journalistik, Recherche und journalistische Darstellungsformen
- SEM Öffentlichkeitsarbeit (Theorie und Praxis)
- SEM Medienrecht
- Praxismodul
- Praxisfeld Medien
- SEM Praxisfeld Medien II
- SEM Praxisfeld Medien III
- Masterarbeit
- Kolloquium zur Masterarbeit
- Grundzüge der Theologie(Es ist gemäß des gewählten Schwerpunkts eines der beiden Module zu belegen)
- Mediensysteme/Journalismus
- SEM Einführung in die Journalistik, Recherche und journalistische Dar- stellungsformen

### MA Medien-Ethik-Religion FPO M-E-R 20180711 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20180711-aes.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20180711-aes.md)

**Pflichtmodule (19):**
- Grundlagen Kommunikationswissenschaft
- Grundlagen der KommunikationswissenschaftI
- Grundlagen der Kommunikationswissenschaft II
- Vertiefung Kommunikationswissenschaft
- Vertiefung der KommunikationswissenschaftI
- Vertiefung der Kommunikationswissenschaft II
- Medienwissenschaft
- Dimensionen des Medialen und Visuellen
- Medienethik
- Medienkunde/Journalismus
- Mediensysteme, Journalismus und Öffentlichkeitsarbeit
- SEM Einführung in die Journalistik, Recherche und journalistischeDarstellungsformen
- SEMÖffentlichkeitsarbeit (Theorie undPraxis)
- SEM Medienrecht
- Praxismodul
- Praxisfeld Medien
- SEM Praxisfeld Medien II
- SEM Praxisfeld Medien III
- Masterarbeit

### MA Medien-Ethik-Religion FPO M-E-R 20200909 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20200909-aes.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20200909-aes.md)

**Pflichtmodule (20):**
- Grundlagen der Kommunikationswissenschaft
- Grundlagen der Kommunikations- wissenschaft
- Grundzüge der Theologie(Es istgemäß desgewählten Schwerpunkts eines der beiden Module
- Grundzüge der Theologie für Nicht- Theologen (ChristentumundMedien)
- Grundzüge der Theologie für Nicht- Theologen (IslamundMedien)
- Medienethik
- Mediensysteme/Journalismus(Es sind alle Module zu belegen)
- Mediensysteme, Journalismus und Öffentlichkeitsarbeit
- SEM Einführung in die Journalistik, Recherche und journalistischeDarstellungsformen
- SEMÖffentlichkeitsarbeit (Theorie undPraxis)
- SEM Medienrecht
- Praxismodul
- Praxisfeld Medien
- SEM PraxisfeldMedien II
- SEM PraxisfeldMedien III
- Masterarbeit
- Kolloquium zur Masterarbeit
- Grundzüge der Theologie(Es ist gemäß des gewählten Schwerpunkts eines der
- SEM Einführung in die Journalistik, Recherche und journalistische Dar- stellungsformen
- SEM Öffentlichkeitsarbeit (Theorie undPraxis)

### MA Medien-Ethik-Religion FPO M-E-R 20240904.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20240904.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20240904.md)

**Pflichtmodule (22):**
- Grundlagen – Methoden - Kate- gorien
- Grundzüge der Theologie(Es istgemäß desgewählten Schwerpunkts eines der beiden Module
- Grundlagen im Schwerpunkt Religion (Christentum und Me- dien): Grundzüge der Theologie und Kirchenkunde für Nichttheolo- gen
- Grundlagen im Schwerpunkt Religion (Islam und Medien): Grundzüge des Islam
- Medienethik
- Grundlagen: Medienethik
- Mediensysteme/Journalismus(Es sind alle Module zu belegen)
- Grundlagen Medienpraxis: Journalismus, Öffentlichkeitsar- beit, Social Media
- SEM Einführung in die Journalistik, Recher- che und journalistische Darstellungsformen
- SEM Öffentlichkeitsarbeit (Theorie und Pra- xis)
- SEM Medienrecht
- Praxismodul2
- Vertiefung Medienpraxis: Pra- xisfeld (digitale) Medien
- SEM Praxisfeld (digitale) Medien II
- SEM Praxisfeld (digitale) Medien III
- max. 42
- Grundzüge der Theologie(Es ist gemäß des gewählten Schwerpunkts eines der beiden Module zu belegen)
- Grundlagen im Schwerpunkt Religion (Christentum und Me- dien): Grundzüge der Theolo- gie und Kirchenkunde für Nicht- theologen
- Mediensysteme/Journalismus
- SEM Einführung in die Journa- listik, Recherche und journalisti- sche Darstellungsformen
- SEM Öffentlichkeitsarbeit (Theorie und Praxis)
- Praxismodul

### PDF vom 09.12.2008

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-20ma-medien-ethik-relig.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-20ma-medien-ethik-relig.md)

**Pflichtmodule (23):**
- Grundlagen der Kommunikations- wissenschaft (Import)
- Medienethik und Medienrecht
- Einführung Medienethik
- Theorie und Praxis des Journalismus
- Theorie und Praxis des Radiojour- nalismus
- Theorie und Praxis des Fernseh- journalismus
- Öffentlichkeitsarbeit und Präsentation
- Praxismodul
- Grundkurs Medien (3 SWS-Import)
- Medienkunde
- (ggf. Import)
- Medienkunde Elektronische Medien
- Grundlagen der Medienkunde (ggf. Import)
- Vertiefung journa- listische Theorie und Praxis
- Vertiefung journalistischer Formen (u.a. Rezension, Intensivkurs Repor- tage) oder Vertiefung journalisti- scher Gattungen (u.a. Musikjourna- lismus, Medizinjournalismus, Wis- senschaftsjournalismus) in den Printmedien und in den elektroni- schen Medien(incl. Internet)
- Vertiefung von Sendeformaten im Radio und Fernsehen oder Spre- cherziehung / Moderation
- Einführung theolo- gische Grundlagen
- VL oder Seminar: Grundzüge der Dogmatik oder Ethik im Überblick
- VL oder Seminar: Einführung in die Religionswissenschaft oder VL Grundzüge einer nichtchristlichen Religion
- Oder (je nach vorherigem Stu- dienfach):
- Vertiefung theolo- gische Grundlagen
- Dogmatische oder ethische Frage- stellung nach Wahl
- Religionswissenschaftliche Frage- stellung nach Wahl

### PDF vom 11.06.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-christliche-medienkommunikation.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-christliche-medienkommunikation.md)

**Pflichtmodule (2):**
- Masterarbeit
- Kolloquium zur Masterarbeit

### PDF vom 09.12.2008 i.d.F. 05.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-aug2015.md)

**Pflichtmodule (5):**
- Masterarbeit (Christentum und Medien)
- Kolloquium zur Masterarbeit
- Masterarbeit
- (Islam und Medien)
- Masterarbeit (Islam und Medien)

### PDF vom 09.12.2008 i.d.F. 07.12.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-dez2010.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-dez2010.md)

**Pflichtmodule (9):**
- Grundlagen der Kommunikationswis- senschaft
- SEM Methoden empirische Kom- munikationsforschung
- Oder:Vertiefung Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach)
- Medienethik
- SEM Einführung Medienethik
- Medienkunde und Journalistik
- SEM Medienkunde elektronische Medien incl. Medienrecht
- SEM Grundfragen der Journalistik und Einführung in die journalisti- schen Darstellungsformen
- Praxismodul I

### PDF vom 09.12.2008 i.d.F. 08.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-juli2014.md)

**Pflichtmodule (14):**
- Grundlagen der Kommunikations- oder Medienwissenschaft (Importmodul)
- SEM Methoden empirische Kommunika- tionsforschung oder Grundlagen der Medienwissenschaft
- Oder: Vertiefung der Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach1) (Importmodul)
- Medienethik
- SEMGrundzüge der Medienethik
- Einführung theologische und religi- onswissenschaft-liche Grundlagen
- VL oder SEM Einführung Altes Testa- ment2
- VL oder SEM Einführung Neues Testa- ment2
- VL oder SEM Einführung Kirchenge- schichte2
- VL oder SEM EinführungSystematik~~2~~
- VL oder SEM Einführung Praktische Theologie2
- VL oder SEM Einführung Religionswis- senschaft2
- Oder: Vertiefungsmodul Theologie3 (Importmodul)
- Praxismodul I

### PDF vom 09.12.2008 i.d.F. 13.11.2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-nov2013.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-nov2013.md)

**Pflichtmodule (8):**
- Grundlagen der Kommunikations‐ oder Medienwissenschaft (Importmodul)
- SEM Methoden empirische Kommunikationsforschung oder Grundlagen der Medienwissenschaft
- _Oder_: Vertiefung der Kommunikations‐ oder Medienwissenschaft (je nach bisherigem Studienfach1) (Importmodul)
- Medienethik
- SEM Grundzüge der Medienethik
- Medienkunde, Journalismus und PR/Öffentlichkeitsarbeit
- SEM Grundfragen der Journalistik und Einführung in journalistische Darstellungsformen
- SEM Grundlagen der PR‐Theorie und

### PDF vom 09.12.2008 i.d.F. 24.11.2009

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/proma-medienethikrelig.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/proma-medienethikrelig.md)

**Pflichtmodule (10):**
- Grundlagen der Kommunikations- wissenschaft
- Medienkunde Zeitung
- Medienkunde elektronische Medien
- Oder:Vertiefung Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach)
- Medienethik und Medienrecht
- Einführung Medienrecht
- Theorie und Praxis des Journalis- mus
- Theorie und Praxis des Radiojour- nalismus (Grundkurs)
- Theorie und Praxis des Fernseh- journalismus (Projekt)
- Praxismodul I

### PDF vom 11.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/stpo-evangelische-theologie-neu.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/stpo-evangelische-theologie-neu.md)

**Pflichtmodule (19):**
- Grundlagen des Theolo- giestudiums / Propädeuti- cum
- Basismodul Altes Testament
- PS Einführung in die exegetischen Methoden AT
- V/Ü weitere Lehrveranstaltung
- Modulprüfung
- Basismodul Neues Testament
- PS Einführung in die exegetischen Methoden NT
- Kirchengeschichte
- Basismodul Systematische Theologie
- PS Einführung in die Methoden der Systemati- schen Theologie
- Ü Übung
- Basismodul Praktische Theologie
- PS Homiletik / Liturgik / Poimenik / Publizistik
- PS Religions- u Gemeindepädagogik/Diakonik/ Gemeindeaufbau /Pastoraltheologie
- Basismodul Theoriebegleitetes Prakti- kum
- Interdisziplinäres Basismodul
- V/S/Ü Weitere interdisziplinäre Lehrveranstal- tung (2SWS)
- Basismodul Religionswissenschaft
- PS Einführung in die Methoden der Religionswissenschaft

### PDF vom 27. Juli 2012

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/stuo-magister-20theologiae.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/stuo-magister-20theologiae.md)

**Pflichtmodule (26):**
- Grundlagen des Theologie- studiums/ Propädeuticum
- Basismodul Altes Testa- ment
- PS Einführung in die exegetischen Methoden AT (2 SWS)
- V/Ü weitere Lehrveranstaltung (2 SWS)
- Proseminararbeit oder Modulprü- fung
- Veranstaltung
- Basismodul Neues Testa- ment
- PS Einführung in die exegetischen Methoden NT (2 SWS)
- Kirchen- geschichte
- PS Einführung in die Methoden der KG (2 SWS)
- Basismodul Systematische Theologie
- PS Einführung in die Methoden der Systematischen Theologie (2 SWS)
- Ü Übung zur Vorlesung „Grund- züge der Dogmatik“(2SWS)
- Basismodul Praktische Theologie
- PS Homiletik/Liturgik/Poimenik/ Publizistik(2SWS)
- PS Religions- u Gemeindepäda- gogik/Diakonik/ Gemeindeaufbau/Pastoral- theologie (2SWS)
- schriftliche Ausarbeitung zu einem der Proseminare
- Basismodul Gemeinde- praktikum
- Inter- disziplinäres Basismodul
- Seminararbeit oder Prüfung zum interdisziplinären Seminar
- V/S/Ü Weitere interdisziplinäre Lehrveranstaltung (2 SWS)
- Prüfung zur Lehrveranstaltung
- Basismodul Religions- wissenschaft
- PS Einführung in die Methoden der Religionswissenschaft (2 SWS)
- V/Ü weitere LV (2 SWS)
- Proseminararbeit oder mündliche Modulprüfung

### PDF vom 25.09.1980 i.d.F. 28.12.2004

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/zwischenpruefungso.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/zwischenpruefungso.md)

**Pflichtmodule (14):**
- Basismodul 1: Sprachwissen- schaft
- Basismodul 2: Literaturwissen- schaft
- Basismodul 3: Sprachpraktische Grundlagen
- Basismodul 4: Sprachproduktion
- Basismodul 5: Landeskunde
- Basismodul 1
- _Linguistik_
- Basismodul 2
- _Literatur- und_
- _Kulturwissenschaft_
- Literaturwiss.
- oder
- Kulturwissenschaft
- Dauer der schriftlichen Prüfung

### 12. Juni 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/1aesa-wtb-organisations-personalentw.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/1aesa-wtb-organisations-personalentw.md)

**Pflichtmodule (23):**
- Grundlagen der Organisations- und Personalentwicklung
- Strategie und Verantwortung
- Organisationsforschung
- Teambuilding
- Grundlagen Organisation
- Konzepte der Organisationsentwicklung
- Konzepte der Organisationsentwicklung in der Praxis
- Unternehmenskultur und Lernkultur
- Umsetzung von Organisationsentwicklungsprozessen
- Vielfalt managen (e-learning)
- Projektmanagement
- Moderation und Präsentation
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Innovative Arbeitsorganisation
- Betriebliches Bildungsmanagement
- Umsetzung von Personalentwicklung
- Kompetenzmessung
- Neue Lernformen im Betrieb
- Management und Führung
- Instrumente der Mitarbeiterführung
- Kommunikation und Gesprächsführung
- Personalmanagement

### 11. August 2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/2aes-20wtb-ma-20multimediadidaktik.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/2aes-20wtb-ma-20multimediadidaktik.md)

**Pflichtmodule (3):**
- Hausaufgabe, Referat (einschl. Präsentation) Hausaufgabe Referat (einschl. Präsentation)
- mündl. Prüfung Referat (einschl. Präsentation)
- mündl. Prüfung

### MA EdT 20190828.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/ma-edt-20190828.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/ma-edt-20190828.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA EdT 20240926 i.d.F. 20260213.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/ma-edt-20240926-idf-20260213.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/ma-edt-20240926-idf-20260213.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA EdT 20240926.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/ma-edt-20240926.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/ma-edt-20240926.md)

**Pflichtmodule (1):**
- Masterarbeit

### PO MA OEPE 20170307 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20170307-idf-20180730.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20170307-idf-20180730.md)

**Pflichtmodule (27):**
- Grundlagen der Organisations- und Personalentwicklung
- Strategie und Verantwortung
- Organisationsforschung
- Teambuilding
- Grundlagen Organisation
- Konzepte der Organisations- entwicklung
- Konzepte der Organisationsentwicklung in der Praxis
- Unternehmenskultur und Lernkultur
- Umsetzung von Organisations- entwicklungsprozessen
- Vielfalt managen(e-learning)
- Projektmanagement
- Moderation und Präsentation
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Innovative Arbeitsorganisation
- Betriebliches Bildungsmanagement
- Umsetzung von Personalentwicklung
- Kompetenzmessung
- Neue Lernformen im Betrieb
- Management und Führung
- Instrumente der Mitarbeiterführung
- Kommunikation und Gesprächsführung
- Personalmanagement
- Personalmarketing
- Arbeitsrecht
- VertiefungOrganisations- und Personalentwicklung
- Praktische Vertiefung

### PO MA OEPE 20170307 i.d.F. 20220629.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20170307-idf-20220629.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20170307-idf-20220629.md)

**Pflichtmodule (25):**
- Grundlagen der Organisations- und Personalentwicklung
- Strategie und Verantwortung
- Organisationsforschung
- Teambuilding
- Grundlagen Organisation
- Konzepte der Organisations- entwicklung
- Konzepte der Organisationsentwicklung in der Praxis
- Unternehmenskultur und Lernkultur
- Umsetzung von Organisations- entwicklungsprozessen
- Vielfalt managen
- Projektmanagement
- Moderation und Präsentation
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Innovative Arbeitsorganisation
- Betriebliches Bildungsmanagement
- Umsetzung von Personalentwicklung
- Kompetenzmessung
- Neue Lernformen im Betrieb
- Management und Führung
- Instrumente der Mitarbeiterführung
- Kommunikation und Gesprächsführung
- Personalmanagement
- Personalmarketing
- Arbeitsrecht

### PO MA OEPE 20170307 i.d.F. 20250711.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20170307-idf-20250711.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20170307-idf-20250711.md)

**Pflichtmodule (23):**
- Grundlagen der Organisations- und Personalentwicklung
- Strategie und Verantwortung
- Organisationsforschung
- Teambuilding
- Grundlagen Organisation
- Konzepte der Organisations- entwicklung
- Konzepte der Organisationsentwicklung in der Praxis
- Unternehmenskultur und Lernkultur
- Umsetzung von Organisations- entwicklungsprozessen
- Vielfalt managen
- Projektmanagement
- Moderation und Präsentation
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Innovative Arbeitsorganisation
- Betriebliches Bildungsmanagement
- Umsetzung von Personalentwicklung
- Kompetenzmessung
- Neue Lernformen im Betrieb
- Management und Führung
- Instrumente der Mitarbeiterführung
- Kommunikation und Gesprächsführung
- Personalmanagement

### PO MA OEPE 20220629 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20220629-aes.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20220629-aes.md)

**Pflichtmodule (24):**
- Grundlagen der Organisations- und Personalentwicklung
- Strategie und Verantwortung
- Organisationsforschung
- Teambuilding
- Grundlagen Organisation
- Konzepte der Organisations- entwicklung
- Konzepte der Organisationsentwicklung in der Praxis
- Unternehmenskultur und Lernkultur
- Umsetzung von Organisations- entwicklungsprozessen
- Vielfalt managen
- Projektmanagement
- Moderation und Präsentation
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Innovative Arbeitsorganisation
- Betriebliches Bildungsmanagement
- Umsetzung von Personalentwicklung
- Kompetenzmessung
- Neue Lernformen im Betrieb
- Management und Führung
- Instrumente der Mitarbeiterführung
- Kommunikation und Gesprächsführung
- Personalmanagement
- Personalmarketing

### PDF vom 07.03.2017 i.d.F. 12.06.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-organisationpersonalentw-weiterbld-ma-juni2017.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-organisationpersonalentw-weiterbld-ma-juni2017.md)

**Pflichtmodule (27):**
- Grundlagen der Organisations- und Personalentwicklung
- Strategie und Verantwortung
- Organisationsforschung
- Teambuilding
- Grundlagen Organisation
- Konzepte der Organisationsentwicklung
- Konzepte der Organisationsentwicklung in der Praxis
- Unternehmenskultur und Lernkultur
- Umsetzung von Organisationsentwick- lungsprozessen
- Vielfalt managen(e-learning)
- Projektmanagement
- Moderation und Präsentation
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Innovative Arbeitsorganisation
- Betriebliches Bildungsmanagement
- Umsetzung von Personalentwicklung
- Kompetenzmessung
- Neue Lernformen im Betrieb
- Management und Führung
- Instrumente der Mitarbeiterführung
- Kommunikation und Gesprächsführung
- Personalmanagement
- Personalmarketing
- Arbeitsrecht
- VertiefungOrganisations- und Personalentwicklung
- Praktische Vertiefung

### PDF vom 07.03.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-organisationpersonalentw-weiterbld-ma.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-organisationpersonalentw-weiterbld-ma.md)

**Pflichtmodule (26):**
- Grundlagen der Organisations- und Personalentwicklung
- Strategie und Verantwortung
- Organisationsforschung
- Teambuilding
- Qualifikationsplanung und Personal- entwicklung
- Konzepte der Personalentwicklung
- Grundlagen Organisation
- Konzepte der Organisationsentwicklung
- Unternehmenskultur und Lernkultur
- Konzepte der Organisationsentwicklung in der Praxis
- Umsetzung von Organisationsentwick- lungsprozessen
- Vielfalt managen (e-learning)
- Projektmanagement
- Moderation und Präsentation
- Grundlage Personal
- Methoden und Instrumente der Personalentwicklung
- Instrumente der Personalentwicklung
- Neue Lernformen im Betrieb
- Personalmanagement und Arbeitsrecht
- Personalmarketing
- Arbeitsrecht
- Management und Führung
- Instrumente der Mitarbeiterführung
- Kommunikation und Gesprächsführung
- Bildungsmanagement
- Betriebliches Bildungsmanagement

### PDF vom 20.10.2003

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/sto-sportwissenschaft.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/sto-sportwissenschaft.md)

**Pflichtmodule (18):**
- Einführung in das Gesundheitswesen
- Gerontologische, psychogerontologische und geriatrische
- Kommunikationspsychologische Grundlagen
- Angewandte Methodenlehre
- Wissenschaftliches Projekt
- Bewegungswissenschaft incl. Biomechanik
- Sportdidaktik/Sportpädagogik
- Sportmedizin
- Sportökonomie
- Sportpsychologie
- Sportsoziologie
- Trainingswissenschaft
- Sport und Gesundheit (Gymnastik und Körperbildung)
- Lehrpraktisches Handeln
- Herz-Kreislauf-Bereich
- Neurologischer Bereich
- Orthopädischer Bereich
- Stoffwechsel-Bereich

### PDF vom 25.09.1980 i.d.F. 28.12.2004

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/zwischenpruefungso.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/zwischenpruefungso.md)

**Pflichtmodule (14):**
- Basismodul 1: Sprachwissen- schaft
- Basismodul 2: Literaturwissen- schaft
- Basismodul 3: Sprachpraktische Grundlagen
- Basismodul 4: Sprachproduktion
- Basismodul 5: Landeskunde
- Basismodul 1
- _Linguistik_
- Basismodul 2
- _Literatur- und_
- _Kulturwissenschaft_
- Literaturwiss.
- oder
- Kulturwissenschaft
- Dauer der schriftlichen Prüfung

### 2. Juli 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/10aes-2fachba-paedagogik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/10aes-2fachba-paedagogik.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### 2. Juni 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/11aes-2fach-ba-politikwissenschaft.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/11aes-2fach-ba-politikwissenschaft.md)

**Pflichtmodule (8):**
- Politische Systeme I
- Politische Systeme II
- Außereuropäische Regionen I
- Außereuropäische Regionen II
- Internationale Beziehungen I
- Internationale Beziehungen II
- Politische Theorie & Ideengeschichte I
- Politische Theorie & Ideengeschichte II

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/11aesa-2fachba-kunstgeschichte.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/11aesa-2fachba-kunstgeschichte.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### 28. Februar 2008

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/1aesa-kunstgesch.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/1aesa-kunstgesch.md)

**Pflichtmodule (1):**
- Protokoll oder mündlicher Vortrag und Hausarbeit

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20140718 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20180730.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20180730.md)

**Pflichtmodule (13):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie – Ältere Urgeschichte2
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Übung zur prähistorischen Kulturentwicklung Europas
- Prähistorische Archäologie – Jüngere Urgeschichte2
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Klassische Archäologie – Griechische Archäologie2
- Klassische Archäologie: Griechische Archäologie I A
- Bachelorarbeit und –prüfung
- Bachelorarbeit5
- Bachelorarbeit

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20140718 i.d.F. 20190220.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20190220.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20190220.md)

**Pflichtmodule (13):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie – Ältere Urgeschichte2
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Übung zur prähistorischen Kultur- entwicklung Europas
- Prähistorische Archäologie – Jüngere Urgeschichte2
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Klassische Archäologie – Griechische Archäologie2
- Klassische Archäologie: Griechische Archäologie I A
- Bachelorarbeit und -prüfung
- Bachelorarbeit5
- Bachelorarbeit

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20180730 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20180730-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20180730-aes.md)

**Pflichtmodule (11):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie – Ältere Urgeschichte2
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Übung zur prähistorischen Kulturentwicklung Europas
- Prähistorische Archäologie – Jüngere Urgeschichte2
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Bachelorarbeit und -prüfung
- Bachelorarbeit5
- Bachelorarbeit

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20190220 ÄS zu 2ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20190220-aes-zu-2aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20190220-aes-zu-2aes.md)

**Pflichtmodule (21):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie – Ältere Urgeschichte2
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Übung zur prähistorischen Kulturentwicklung Europas
- Prähistorische Archäologie – Jüngere Urgeschichte2
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Klassische Archäologie – Griechische Archäologie2
- Klassische Archäologie: Griechische Archäologie I A
- Klassische Archäologie: Griechische Archäologie I B
- Übung zur griechischen Kulturgeschichte
- Klassische Archäologie – Römische Archäologie2
- Klassische Archäologie: Römische Archäologie I A
- Klassische Archäologie: Italisch-römische Archäologie I B
- Übung zur römischen Kulturgeschichte
- Christliche Archäologie – Kulturgeschichte2
- Christliche Archäologie: Kulturgeschichte I A
- Bachelorarbeit und -prüfung
- Bachelorarbeit5
- Bachelorarbeit

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20240430.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20240430.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20240430.md)

**Pflichtmodule (10):**
- Basismodule: Kulturentwicklung und Kulturgeschichte2
- Prähistorische Archäologie – Ältere Urgeschichte
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Übung zur prähistorischen Kulturentwicklung Europas
- Prähistorische Archäologie – Jüngere Urgeschichte
- Bachelorarbeit im Erstfach (Archäologische Wissenschaften)
- Bachelorarbeit
- Basismodule: Kulturentwicklung und Kulturgeschichte3
- Bachelorarbeit im Erstfach

### 2-Fach-BA Computerlinguistik FPO CompLing 20071005 i.d.F. 20220411.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-computerlinguistik-fpo-compling-20071005-idf-20220411.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-computerlinguistik-fpo-compling-20071005-idf-20220411.md)

**Pflichtmodule (14):**
- Grundlagen der Computerlinguistik I (traditionelle Verfahren)
- Programmierung und Infrastrukturen I
- Grundlagen der Computerlinguistik II (statistische Verfahren)
- ÜbungCL 2
- Programmierung und Infrastrukturen II
- Grundlagen der Informatik (GdI)
- Grundlagen der Computerlinguistik III (Deep Learning)
- Proseminar Computerlinguistik
- Basismodul II: Linguistics (A)
- Grundlagen der Germanistischen Linguistik 1 (LingBM 1)
- Bachelorarbeit im Erstfach (Computerlinguistik)
- Bachelorarbeit
- Grundlagen der Computerlinguistik II (statistischeVerfahren)
- Bachelorarbeit im Erstfach

### 2 Fach BA Digitale Geistes- und Sozialwissenschaften 20180829 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-digitale-geistes-und-sozialwissenschaften-20180829-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-digitale-geistes-und-sozialwissenschaften-20180829-aes.md)

**Pflichtmodule (13):**
- Grundlagen der Informatik
- Konzeptionelle Modellierung
- Mathematik für Naturwissen- schaftler
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende2
- Theoretische Informatik für Wirt- hfifikLh
- scatsnormat und eramt
- Theoretische Informatik für Wirt- schaftsinformatik und Lehramt
- Grundlagen der Logik in der Informatik2
- Mathematische Modell- bildung und Statistik für Naturwissenschaftler
- DH-Modul 1: Schwerpunkt Sprache und Text
- DH-Modul 2: Schwerpunkt Gesellschaft und Raum
- DH-Modul 3: Schwerpunkt Bild und Medien
- Praxis-/Projektmodul

### 2-Fach-BA English and American Studies 20071004 i.d.F. 20200124.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20071004-idf-20200124.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20071004-idf-20200124.md)

**Pflichtmodule (19):**
- Basismodule: 35 ECTS-Punkte
- Basismodul I _Language_
- GLC (II)
- Basismodul II _Linguistics_(A)
- Basismodul III3 _Linguistics_(B)
- Aufbauseminar
- Basismodul IV _Literature_(A)
- Basismodul V _Literature_(B)
- Basismodul VI _Culture_(A)
- Basismodul VII _Culture_ (B)
- Studienrichtung_American Studies_: 45 ECTS-Punkte (vgl. § 4a)**
- Zwischenmodul I _Culture_
- Import-Kombi-Modul _Politics & Culture_
- Mittelseminar_Politics & Culture_
- Bachelorarbeit im Erstfach (_English and American Studies_) **
- Bachelorarbeit10
- Basismodul III4 _Linguistics_(B)
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA English and American Studies 20200124 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20200124-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20200124-aes.md)

**Pflichtmodule (20):**
- Basismodule: 35 ECTS-Punkte
- Basismodul I _Language_
- GLC (II)
- Basismodul II _Linguistics_(A)
- Basismodul III3 _Linguistics_(B)
- Aufbauseminar
- Basismodul IV _Literature_(A)
- Basismodul V _Literature_(B)
- Basismodul VI _Culture_(A)
- Basismodul VII _Culture_ (B)
- Studienrichtung_American Studies_: 45 ECTS-Punkte (vgl.**
- Zwischenmodul I _Culture_
- Import-Kombi-Modul _Politics & Culture_
- Mittelseminar_Politics & Culture_
- Bachelorarbeit im Erstfach (_English and American Studies_) **
- Bachelorarbeit10
- Basismodul III4 _Linguistics_(B)
- Studienrichtung_American Studies_: 35 ECTS-Punkte (vgl.**
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA English and American Studies 20250930.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20250930.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20250930.md)

**Pflichtmodule (20):**
- Basismodule: 35 ECTS-Punkte
- Basismodul I Language
- GLC (II)
- Basismodul II Linguistics (A)
- Basismodul III3 Linguistics (B)
- Aufbauseminar
- Basismodul IV Literature (A)
- Basismodul V Literature (B)
- Basismodul VI Culture (A)
- Basismodul VII Culture (B)
- Studienrichtung American Studies: 45 ECTS-Punkte (vgl.§ 5)
- Zwischenmodul I Culture
- Import-Kombi-Modul Politics & Culture
- Mittelseminar Politics & Culture
- Bachelorarbeit im Erstfach (English and American Studies)
- Bachelorarbeit10
- Basismodul III4 Linguistics (B)
- Studienrichtung American Studies: 35 ECTS-Punkte (vgl. § 4a)
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA FPO BA SKAND 20071004 i.d.F. 20190520.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20190520.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20190520.md)

**Pflichtmodule (12):**
- Basismodule: Es müssen alle Basismodule belegt werden (40 ECTS).
- Literaturwissenschaft 1
- Literaturwissenschaft 2
- Literaturwissenschaft 3
- Nordische Kulturgeschichte 1
- Nordische Kulturgeschichte 2
- Nordische Erstsprache 1
- Nordische Erstsprache 2
- Sprachanalyse
- Bachelorarbeit (nur im Erstfach): 10 ECTS
- Abschlussmodul Bachelorarbeit
- Bachelorarbeit

### 2-Fach-BA FPO BA SKAND 20071004 i.d.F. 20211201.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20211201.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20211201.md)

**Pflichtmodule (13):**
- Basismodule: Es müssen alle Basismodule belegt werden (40 ECTS).
- Literaturwissenschaft 1
- Literaturwissenschaft 2
- Literaturwissenschaft 3
- Nordische Kulturgeschichte 1
- Nordische Kulturgeschichte 2
- Nordische Erstsprache 1
- Nordische Erstsprache 2
- Sprachanalyse
- Bachelorarbeit im Erstfach (Skandinavistik)
- Abschlussmodul Bachelorarbeit
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA FPO BA SKAND 20250731.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20250731.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20250731.md)

**Pflichtmodule (15):**
- Basismodule(40 ECTS-Punkte)
- Literaturgeschichte 1
- Literaturgeschichte 2
- Literaturwissenschaft
- Nordische Kulturgeschichte 1
- Nordische Kulturgeschichte 2
- Nordische Erstsprache 1
- Nordische Erstsprache 24
- Sprachanalyse
- Bachelorarbeit im Erstfach (Skandinavistik)
- Abschlussmodul Bachelorarbeit
- Bachelorarbeit
- Basismodule (40 ECTS-Punkte)
- Nordische Erstsprache 25
- Bachelorarbeit im Erstfach

### 2-Fach-BA Frankoromanistik 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-20210624-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-20210624-aes.md)

**Pflichtmodule (9):**
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Französische Sprachpraxis 32
- Traduction version
- Communication orale et civilisation
- Bachelorarbeit im Erstfach (Frankoromanistik)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA Frankoromanistik FPO BA Frankorom 20071004 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-fpo-ba-frankorom-20071004-idf-20210624.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-fpo-ba-frankorom-20071004-idf-20210624.md)

**Pflichtmodule (9):**
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Französische Sprachpraxis 32
- Traduction version
- Communication orale et civilisation
- Bachelorarbeit im Erstfach (Frankoromanistik)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA Germanistik FPO BA Germ 20071004 i.d.F. 20220914.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-ba-germ-20071004-idf-20220914.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-ba-germ-20071004-idf-20220914.md)

**Pflichtmodule (16):**
- Ling BM-1 Grundlagen der germanistischen Linguistik
- Lit BM Grundlagen des wissenschaftlichen Arbeitens in der Literaturwissen- schaft
- NdL BM-1 Grundlagen der Neueren deutschen Literaturwissenschaft 1
- Ling BM-2 Grundlagen der historischen Linguistik
- Geschichte der deutschen Sprache
- Med BM Grundlagen der Germanistischen Mediävistik
- NdL BM-2 Grundlagen der Neueren deutschen Literaturwissenschaft2
- Bachelorarbeit im Erstfach (Germanistik)
- Abschlussmodule5
- Ling Finit Abschlussmodul Bachelorarbeit Linguistik
- Bachelorarbeit
- NdL Finit Abschlussmodul Bachelorarbeit Neuere deutsche Literaturwissen- schaft
- NdL BM-1 Grundlagen der Neueren deutschen Literaturwissenschaft1
- Geschichte derdeutschenSprache
- NdL BM-2 Grundlagen der Neueren deutschen Literaturwissenschaft 2
- Bachelorarbeit im Erstfach

### 2-Fach-BA Germanistik FPO BA Germ 20260115.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-ba-germ-20260115.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-ba-germ-20260115.md)

**Pflichtmodule (17):**
- Ling BM-1 Grundlagen der germanistischen Linguistik
- Lit BM Grundlagen des wissenschaftlichen Arbeitens in der Literaturwissen- schaft
- NdL BM-1 Grundlagen der Neueren deutschen Literaturwissenschaft 1
- Ling BM-2 Grundlagen der historischen Linguistik
- Geschichte der deutschen Sprache
- Med BM Grundlagen der Germanistischen Mediävistik
- NdL BM-2 Grundlagen der Neueren deutschen Literaturwissenschaft2
- Bachelorarbeit im Erstfach(Germanistik)
- Abschlussmodule5
- Ling Finit Abschlussmodul Bachelorarbeit
- Lit BM Grundlagen des wissenschaftli- chen Arbeitens in der Literatur- wissenschaft
- Einführung in die historische Liitik
- ngus
- Geschichte der deutschen Spra- che
- NdL BM-2 Grundlagen der Neueren deutschen Literaturwissenschaft 2
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA Germanistik FPO Germanistik Zwei-Fach 20190708 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-germanistik-zwei-fach-20190708-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-germanistik-zwei-fach-20190708-aes.md)

**Pflichtmodule (13):**
- Grundlagen der Germanistischen Linguistik 1(LingBM 1)
- Grundlagen der Germanistischen Linguistik 2(LingBM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft2(NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1(MedBM 1)
- Grundlagen der Germanistischen Mediävistik 2(MedBM 2)
- Bachelorarbeit im Erstfach (Germanistik)
- Abschlussmodule
- Abschlussmodul Bachelorarbeit Linguistik (Ling Finit)
- Bachelorarbeit
- Abschlussmodul Bachelorarbeit Neuere deutsche Literaturwissen- schaft(NdL Finit)
- Abschlussmodul Bachelorarbeit Mediävistik(MedFinit)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)

### 2-Fach-BA Germanistik FPO Germanistik Zwei-Fach 20220914 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-germanistik-zwei-fach-20220914-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-germanistik-zwei-fach-20220914-aes.md)

**Pflichtmodule (18):**
- Ling BM-1 Grundlagen der germanistischen Linguistik
- Lit BM Grundlagen des wissenschaftli- chen Arbeitens in der Literaturwis- senschaft
- NdL BM-1 Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- Ling BM-2 Grundlagen der historischen Linguistik
- Geschichte der deutschen Sprache
- Med BM Grundlagen der Germanistischen Mediävistik
- NdL BM-2 Grundlagen der Neueren deut- schen Literaturwissenschaft2
- Bachelorarbeit im Erstfach (Germanistik)
- Abschlussmodule5
- Ling Finit Abschlussmodul Bachelorarbeit Linguistik
- Bachelorarbeit
- NdL Finit Abschlussmodul Bachelorarbeit Neuere deutsche Literaturwissen- schaft
- Med Finit Abschlussmodul Bachelorarbeit Mediävistik
- Lit BM Grundlagen des wissenschaftli- chen Arbeitens in der Literatur- wissenschaft
- Einführung in die historische Liiik
- ngust
- NdL BM-2 Grundlagen der Neueren deut- schen Literaturwissenschaft 2
- Bachelorarbeit im Erstfach

### 2-Fach-BA Iberoromanistik 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-20210624-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-20210624-aes.md)

**Pflichtmodule (8):**
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Spanische Sprachpraxis 32
- Gramática y estilísticaI
- Bachelorarbeit im Erstfach (Iberomanistik)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA Iberoromanistik FPO BA Iberorom 20071004 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-fpo-ba-iberorom-20071004-idf-20210624.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-fpo-ba-iberorom-20071004-idf-20210624.md)

**Pflichtmodule (8):**
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Spanische Sprachpraxis 32
- Gramática y estilísticaI
- Bachelorarbeit im Erstfach (Iberomanistik)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA  Islamisch Religiöse Studien BA IRS Zwei-Fach 20140718 i.d.F. 20200909.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-islamisch-religioese-studien-ba-irs-zwei-fach-20140718-idf-20200909.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-islamisch-religioese-studien-ba-irs-zwei-fach-20140718-idf-20200909.md)

**Pflichtmodule (2):**
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA Islamisch-Religiöse Studien BA IRS Zwei-Fach 20200909 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-islamisch-religioese-studien-ba-irs-zwei-fach-20200909-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-islamisch-religioese-studien-ba-irs-zwei-fach-20200909-aes.md)

**Pflichtmodule (2):**
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA Italoromanistik 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-italoromanistik-20210624-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-italoromanistik-20210624-aes.md)

**Pflichtmodule (12):**
- Basismodul Italienische Sprachpraxis 1
- Mündliche Sprachkompetenz I (Comprensione e produzione oraleI)
- Basismodul Italienische Sprachpraxis 22
- Fonetica pratica
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft
- Bachelorarbeit im Erstfach (Italoromanistik)
- Bachelorarbeit
- Mündliche Sprachkompetenz I (Comprensione e produzione orale I)
- Basismodul Italienische Sprachpraxis 23
- Bachelorarbeit im Erstfach

### 2-Fach-BA Italoromanistik FPO BA Italorom 20071004 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-italoromanistik-fpo-ba-italorom-20071004-idf-20210624.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-italoromanistik-fpo-ba-italorom-20071004-idf-20210624.md)

**Pflichtmodule (13):**
- Basismodul Italienische Sprachpraxis 1
- Mündliche Sprachkompetenz I (Comprensione e produzione orale I)
- Basismodul Italienische Sprachpraxis 22
- Fonetica pratica
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft
- Bachelorarbeit im Erstfach (Italoromanistik)
- Bachelorarbeit
- Mündliche Sprachkompetenz I (Comprensione e produzione oraleI)
- Basismodul Italienische Sprachpraxis 23
- Bachelorarbeit im Erstfach
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:

### 2-Fach-BA Japanologie FPO BA Japanologie 20071004 i.d.F. 20210729.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20071004-idf-20210729.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20071004-idf-20210729.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach(Japanologie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Japanologie FPO BA-Japanologie 20210729 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20210729-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20210729-aes.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach(Japanologie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Japanologie FPO BA Japanologie 20230615.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20230615.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-japanologie-fpo-ba-japanologie-20230615.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach (Japanologie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Kulturgeographie FPO Kulturgeo Zwei-Fach 20071005 i.d.F. 20200827.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20071005-idf-20200827.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20071005-idf-20200827.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach
- GZB 14: Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit

### 2-Fach-BA Kulturgeographie FPO Kulturgeo Zwei-Fach 20071005 i.d.F. 20221011.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20071005-idf-20221011.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20071005-idf-20221011.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach
- GZB 14: Bachelorarbeit
- Bachelorarbeit

### 2-Fach-BA Kulturgeographie FPO Kulturgeo Zwei-Fach 20200827 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20200827-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20200827-aes.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach
- GZB 14: Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit

### 2-Fach-BA Kulturgeographie FPO Kulturgeo Zwei-Fach 20221011 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20221011-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20221011-aes.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach
- GZB 14: Bachelorarbeit
- Bachelorarbeit

### 2-Fach-BA Kulturgeographie FPO Kulturgeo  Zwei-Fach 20230928.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20230928.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kulturgeographie-fpo-kulturgeo-zwei-fach-20230928.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach
- GZB 14: Bachelorarbeit
- Bachelorarbeit

### 2-Fach-BA Kunstgeschichte FPO BA KuGe 20071005 i.d.F. 20200813.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20071005-idf-20200813.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20071005-idf-20200813.md)

**Pflichtmodule (23):**
- Einführung in die Kunstgeschichte2
- Beschreiben und vergleichendes Sehen2
- Propädeutik – Ikonographie2
- Propädeutik – Quellenkunde und Kunsttheorie2
- Geschichte der Bildenden Kunst des Mittelalters – Einführung3
- Geschichte der Bildenden Kunst des Mittelalters – Spezialisierung
- Geschichte der Bildenden Kunst von der Renaissance biszurGegenwart– Einführung3
- Geschichte der Bildenden Kunst von der Renaissance bis zur Gegenwart – Spezialisierung
- Geschichte der Architektur – Einführung3
- Geschichte der Architektur – Spezialisierung
- Vertiefung im Bereich der Bildenden Kunst und der Architektur4
- Spezialisierung im Bereich der Bildenden Kunst und der Architektur5
- Grundlagen der Graphischen Künste
- Grundlagen der angewandten Künste
- Grundlagen der Denkmalpflege
- Digitales Lernen und Lehren
- Berufsorientierung Kunstgeschichte
- Kunstgeschichte Italiens I
- Kunstgeschichte Italiens II
- Bachelorarbeit im Erstfach (Kunstgeschichte)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA Kunstgeschichte FPO BA KuGe 20071005 i.d.F. 20230323.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20071005-idf-20230323.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20071005-idf-20230323.md)

**Pflichtmodule (20):**
- Einführungin die Kunstgeschichte2
- Beschreiben und vergleichendes Sehen2
- Propädeutik – Ikonographie2
- Propädeutik – Quellenkunde und Kunsttheorie 2
- Geschichte der Bildenden Kunst des Mittelal- ters–Einführung3
- Geschichte der Bildenden Kunst des Mittelal- ters – Spezialisierung
- Geschichte der Bildenden Kunst von der Re- naissance bis zur Gegenwart–Einführung3
- Geschichte der Bildenden Kunst von der Re- naissance bis zur Gegenwart – Spezialisie- rung
- Geschichte der Architektur – Einführung 3
- Geschichte der Architektur – Spezialisierung
- Vertiefung im Bereich der Bildenden Kunst und der Architektur4
- Spezialisierung im Bereich der Bildenden Kunst und der Architektur5
- Grundlagen der Graphischen Künste
- Grundlagen der angewandten Künste
- Grundlagen der Denkmalpflege
- Digitales Lernen und Lehren
- Bachelorarbeit im Erstfach(Kunstgeschichte)
- Bachelorarbeit
- Bachelorarbeit im Erstfach
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:

### 2-Fach-BA Kunstgeschichte FPO BA KuGe 20200813 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20200813-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20200813-aes.md)

**Pflichtmodule (23):**
- Einführung in die Kunstgeschichte2
- Beschreiben und vergleichendes Sehen2
- Propädeutik – Ikonographie2
- Propädeutik – Quellenkunde und Kunsttheorie2
- Geschichte der Bildenden Kunst des Mittelalters – Einführung3
- Geschichte der Bildenden Kunst des Mittelalters – Spezialisierung
- Geschichte der Bildenden Kunst von der Renaissance biszurGegenwart– Einführung3
- Geschichte der Bildenden Kunst von der Renaissance bis zur Gegenwart – Spezialisierung
- Geschichte der Architektur – Einführung3
- Geschichte der Architektur – Spezialisierung
- Vertiefung im Bereich der Bildenden Kunst und der Architektur4
- Spezialisierung im Bereich der Bildenden Kunst und der Architektur5
- Grundlagen der Graphischen Künste
- Grundlagen der angewandten Künste
- Grundlagen der Denkmalpflege
- Digitales Lernen und Lehren
- Berufsorientierung Kunstgeschichte
- Kunstgeschichte Italiens I
- Kunstgeschichte Italiens II
- Bachelorarbeit im Erstfach (Kunstgeschichte)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA Kunstgeschichte FPO BA KuGe 20230323 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20230323-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-kunstgeschichte-fpo-ba-kuge-20230323-aes.md)

**Pflichtmodule (19):**
- Einführungin die Kunstgeschichte2
- Beschreiben und vergleichendes Sehen2
- Propädeutik – Ikonographie2
- Propädeutik – Quellenkunde und Kunsttheorie 2
- Geschichte der Bildenden Kunst des Mittelal- ters–Einführung3
- Geschichte der Bildenden Kunst des Mittelal- ters – Spezialisierung
- Geschichte der Bildenden Kunst von der Re- naissance biszurGegenwart– Einführung 3
- Geschichte der Bildenden Kunst von der Re- naissance bis zur Gegenwart – Spezialisie- rung
- Geschichte der Architektur – Einführung 3
- Geschichte der Architektur – Spezialisierung
- Vertiefung im Bereich der Bildenden Kunst und der Architektur4
- Spezialisierung im Bereich der Bildenden Kunst und der Architektur5
- Grundlagen der Graphischen Künste
- Grundlagen der angewandten Künste
- Grundlagen der Denkmalpflege
- Digitales Lernen und Lehren
- Bachelorarbeit im Erstfach(Kunstgeschichte)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Lateinische Philologie 20071004 i.d.F. 20180928.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-lateinische-philologie-20071004-idf-20180928.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-lateinische-philologie-20071004-idf-20180928.md)

**Pflichtmodule (6):**
- Basismodul 1: Einführung in die Sprache und Literatur deslateinischen Europas
- Basismodul 2: Einführungindielateinische Schrift
- Einführung in die Indogermanistik9
- vgl.: FPO B.A. Indogermanistik und Indoiranistik
- Einführung in das Germanische10
- Bachelorarbeit

### 2 Fach-BA Lateinische Philologie 20180928 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-lateinische-philologie-20180928-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-lateinische-philologie-20180928-aes.md)

**Pflichtmodule (5):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Basismodul 2: Einführung in die lateinische Schrift
- Einführung in die Indogermanistik9
- Einführung in das Germanische10
- Bachelorarbeit

### 2-Fach-BA Lateinische Philologie 20260305.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-lateinische-philologie-20260305.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-lateinische-philologie-20260305.md)

**Pflichtmodule (8):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Basismodul 2: Einführung in die lateinische Schrift
- Einführung in die Indoger- manistik7
- Einführung in das Germani- sche8
- Sanskrit I8
- Bachelorarbeit im Erstfach (Lateinische Philologie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Linguistische Informatik FPO LingInf 20220411 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-linguistische-informatik-fpo-linginf-20220411-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-linguistische-informatik-fpo-linginf-20220411-aes.md)

**Pflichtmodule (14):**
- Grundlagen der Computerlinguistik I (traditionelle Verfahren)
- Programmierung und Infrastrukturen I
- Grundlagen der Computerlinguistik II (statistische Verfahren)
- ÜbungCL 2
- Programmierung und Infrastrukturen II
- Grundlagen der Informatik (GdI)
- Grundlagen der Computerlinguistik III (Deep Learning)
- Proseminar Computerlinguistik
- Basismodul II: Linguistics (A)
- Grundlagen der Germanistischen Linguistik 1 (LingBM 1)
- Bachelorarbeit im Erstfach (Computerlinguistik)
- Bachelorarbeit
- Grundlagen der Computerlinguistik II (statistischeVerfahren)
- Bachelorarbeit im Erstfach

### 2-Fach-BA Mittel- und Neulatein FPO Mittellatein Zwei-Fach 20071005 i.d.F. 20190614.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20071005-idf-20190614.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20071005-idf-20190614.md)

**Pflichtmodule (14):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Übersetzung ausgewählter Texte
- Tutorium
- Basismodul 2: Einführung in die lateinische Schrift (Paläographie)
- Exkursion
- Basismodul 3A: Das Klassische Erbe A2 (gemäß§4a)
- Basismodul 3B: Das Klassische Erbe B2
- Das Klassische Erbe
- Basismodul 4: Europäische Mediävistik I (gemäß§4a)
- Basismodul 5: Europäische Mediävistik II (gemäß§4a)
- Bachelorarbeit im Erstfach (Mittellatein und Neulatein)
- Bachelorarbeit
- Basismodul 3A: Das Klassische Erbe A3 (gemäß§4a)
- Basismodul 3B: Das Klassische Erbe B3

### 2-Fach-BA Mittel-und Neulatein FPO Mittellatein Zwei-Fach 20190614 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20190614-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20190614-aes.md)

**Pflichtmodule (10):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Übersetzung ausgewählter Texte
- Tutorium
- Basismodul 2: Einführung in die lateinische Schrift (Paläographie)
- Exkursion
- Basismodul 3B: Das Klassische Erbe B2
- DasKlassischeErbe
- Bachelorarbeit im Erstfach (Mittellatein und Neulatein)
- Bachelorarbeit
- Basismodul 3B: Das Klassische Erbe B3

### 2-Fach-BA Mittel- und Neulatein FPO Mittellatein Zwei-Fach 20240430.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20240430.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20240430.md)

**Pflichtmodule (14):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Übersetzung ausgewählter Texte
- Tutorium oder Übung
- Basismodul 2: Einführung in die lateinische Schrift (Paläographie)
- Exkursion
- Basismodul 3A: Das Klassische Erbe A2 (gemäß§5)
- Basismodul 3B: Das Klassische Erbe B2
- Das Klassische Erbe
- Basismodul 4: Europäische Mediävistik I (gemäß§5)
- Basismodul 5: Europäische Mediävistik II (gemäß§5)
- Bachelorarbeit im Erstfach (Mittellatein und Neulatein)
- Bachelorarbeit
- Basismodul 3A: Das Klassische Erbe A3 (gemäß§5)
- Basismodul 3B: Das Klassische Erbe B3

### 2-Fach-BA Ökonomie FPO Ökon Zwei-Fach 20071005 i.d.F. 20210225.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20071005-idf-20210225.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20071005-idf-20210225.md)

**Pflichtmodule (10):**
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Wirtschaftsprivatrecht
- Vertiefung Wirtschaftswissenschaften I
- Vertiefung Wirtschaftswissenschaften II
- Vertiefung Wirtschaftswissenschaften III
- Zweitfach (Kombinationsmöglichkeiten gemäß Anlage 3 der ABMStPO/Phil)
- Module des Zweitfachs3
- Bachelorarbeit im Erstfach (Ökonomie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Ökonomie FPO Ökon Zwei-Fach 20190916 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20190916-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-oekonomie-fpo-oekon-zwei-fach-20190916-aes.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach (Ökonomie)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA Orientalistik FPO Orient 20071005 i.d.F. 20210225.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-orientalistik-fpo-orient-20071005-idf-20210225.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-orientalistik-fpo-orient-20071005-idf-20210225.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach(Orientalistik)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Orientalistik FPO Orient 20210225 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-orientalistik-fpo-orient-20210225-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-orientalistik-fpo-orient-20210225-aes.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach(Orientalistik)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Pädagogik 20210225 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-paedagogik-20210225-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-paedagogik-20210225-aes.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach (Pädagogik)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA Pädagogik FPO Päd-Zwei-Fach 20071005 i.d.F. 20210225.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-paedagogik-fpo-paed-zwei-fach-20071005-idf-20210225.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-paedagogik-fpo-paed-zwei-fach-20071005-idf-20210225.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach (Pädagogik)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA Pädagogik FPO Päd-Zwei-Fach 20250522.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-paedagogik-fpo-paed-zwei-fach-20250522.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-paedagogik-fpo-paed-zwei-fach-20250522.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach(Pädagogik)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Philosophie FPO B.A. Philosophie 20210122 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-philosophie-fpo-b-a-philosophie-20210122-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-philosophie-fpo-b-a-philosophie-20210122-aes.md)

**Pflichtmodule (13):**
- Grundkurs Praktische Philosophie
- Grundkurs Theoretische Philosophie
- Basismodul Philosophie
- Textseminar (Mittelseminar)
- Basismodul Praktische Philosophie
- Basismodul Theoretische Philosophie
- Philosophiegeschichte3
- Philosophie systematisch4
- Bachelorarbeit im Erstfach (Philosophie)
- Bachelorarbeit
- Philosophiegeschichte4
- Philosophie systematisch5
- Bachelorarbeit im Erstfach

### 2-Fach BA Philosophie FPO B.A. Philosophie Zwei-Fach 20071005 i.d.F. 20210122.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-philosophie-fpo-b-a-philosophie-zwei-fach-20071005-idf-20210122.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-philosophie-fpo-b-a-philosophie-zwei-fach-20071005-idf-20210122.md)

**Pflichtmodule (13):**
- Grundkurs Praktische Philosophie
- Grundkurs Theoretische Philosophie
- Basismodul Philosophie
- Textseminar (Mittelseminar)
- Basismodul Praktische Philosophie
- Basismodul Theoretische Philosophie
- Philosophiegeschichte3
- Philosophie systematisch4
- Bachelorarbeit im Erstfach (Philosophie)
- Bachelorarbeit
- Philosophiegeschichte4
- Philosophie systematisch5
- Bachelorarbeit im Erstfach

### 2-Fach-BA Politikwissenschaft 20071005 i.d.F. 20210122.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-20071005-idf-20210122.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-20071005-idf-20210122.md)

**Pflichtmodule (11):**
- Politische Systeme I
- Politische Systeme II
- Außereuropäische Regionen I
- Außereuropäische Regionen II
- Internationale Beziehungen I
- Internationale Beziehungen II
- Politische Theorie & Ideengeschichte I
- Politische Theorie & Ideengeschichte II
- Bachelorarbeit im Erstfach (Politikwissenschaft)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Politikwissenschaft 20260305.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-20260305.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-20260305.md)

**Pflichtmodule (9):**
- Politische Systeme I
- Politische Systeme II
- Internationale Beziehungen I
- Internationale Beziehungen II
- Politische Theorie & Ideengeschichte I
- Politische Theorie & Ideengeschichte II
- Bachelorarbeit im Erstfach (Politikwissenschaft)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Politikwissenschaft FPO B.A. Politik 20210122 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-fpo-b-a-politik-20210122-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-politikwissenschaft-fpo-b-a-politik-20210122-aes.md)

**Pflichtmodule (11):**
- Politische Systeme I
- Politische Systeme II
- Außereuropäische Regionen I
- Außereuropäische Regionen II
- Internationale Beziehungen I
- Internationale Beziehungen II
- Politische Theorie & Ideengeschichte I
- Politische Theorie & Ideengeschichte II
- Bachelorarbeit im Erstfach (Politikwissenschaft)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Skandinavistik FPO BA SKAND 20190520 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-skandinavistik-fpo-ba-skand-20190520-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-skandinavistik-fpo-ba-skand-20190520-aes.md)

**Pflichtmodule (12):**
- Basismodule: Es müssen alle Basismodule belegt werden (40 ECTS).
- Literaturwissenschaft 1
- Literaturwissenschaft 2
- Literaturwissenschaft 3
- Nordische Kulturgeschichte 1
- Nordische Kulturgeschichte 2
- Nordische Erstsprache 1
- Nordische Erstsprache 2
- Sprachanalyse
- Bachelorarbeit (nur im Erstfach): 10 ECTS
- Abschlussmodul Bachelorarbeit
- Bachelorarbeit

### 2-Fach-BA Skandinavistik FPO BA SKAND 20211201 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-skandinavistik-fpo-ba-skand-20211201-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-skandinavistik-fpo-ba-skand-20211201-aes.md)

**Pflichtmodule (13):**
- Basismodule: Es müssen alle Basismodule belegt werden (40 ECTS).
- Literaturwissenschaft 1
- Literaturwissenschaft 2
- Literaturwissenschaft 3
- Nordische Kulturgeschichte 1
- Nordische Kulturgeschichte 2
- Nordische Erstsprache 1
- Nordische Erstsprache 2
- Sprachanalyse
- Bachelorarbeit im Erstfach (Skandinavistik)
- Abschlussmodul Bachelorarbeit
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20071005 i.d.F. 20190806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20190806.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20190806.md)

**Pflichtmodule (20):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Einführung in die sozio- logische Methodenlehre (SozM-E)
- V Einführung in die Methoden der iih Silfh
- emprscenozaorscung
- Ü Methoden der empirischen Sozialforschung
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Qualifikationsprofil II (SozQ-II), vgl. § 5
- Bachelorarbeit im Erstfach (Soziologie)
- Bachelorarbeit
- Einführung Soziologische Theorien(SozT-E)
- Einführung in die soziologische Methoden- lehre (SozM-E)
- Methoden der empiri-
- schenSozialforschung
- Ü Methoden der empiri- schen Sozialforschung
- Bachelorarbeit im Erstfach

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20071005 i.d.F. 20200818.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20200818.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20200818.md)

**Pflichtmodule (19):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Einführung in die sozio- logische Methodenlehre (SozM-E)
- der empirischen
- Sozialforschung
- Ü Methoden der empirischen Sozialforschung
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Qualifikationsprofil II (SozQ-II), vgl. § 5
- Bachelorarbeit im Erstfach (Soziologie)
- Bachelorarbeit
- Einführung in die soziologische Methoden- lehre (SozM-E)
- Methoden der empiri-
- schenSozialforschung
- Ü Methoden der empiri- schen Sozialforschung
- Bachelorarbeit im Erstfach

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20190806 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20190806-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20190806-aes.md)

**Pflichtmodule (20):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Einführung in die soziolo- gische Methodenlehre (SozM-E)
- V Einführung in die Methoden der
- empirischenSozialforschung
- Ü Methoden der empirischen Sozialforschung
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Qualifikationsprofil II (SozQ-II), vgl. § 5
- Bachelorarbeit im Erstfach (Soziologie)
- Bachelorarbeit
- Einführung in die soziologische Metho- denlehre (SozM-E)
- Methoden der empiri-
- schen Sozialforschung
- Ü Methoden der empiri- schen Sozialforschung
- Qualifikationsprofil II
- Bachelorarbeit im Erstfach

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20200818 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20200818-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20200818-aes.md)

**Pflichtmodule (19):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Einführung in die sozio- logische Methodenlehre (SozM-E)
- der empirischen Sozialfor-
- schung
- Ü Methoden der empirischen Sozialforschung
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Qualifikationsprofil II (SozQ-II), vgl. § 5
- Bachelorarbeit im Erstfach (Soziologie)
- Bachelorarbeit
- Einführung in die soziologische Methoden- lehre (SozM-E)
- Methoden der empiri-
- schen Sozialforschung
- Ü Methoden der empiri- schen Sozialforschung
- Bachelorarbeit im Erstfach

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20230822.md)

**Pflichtmodule (13):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Einführung in die sozio- logische Methodenlehre (SozM-E)
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Qualifikationsprofil II (SozQ-II), vgl. § 5
- Bachelorarbeit im Erstfach (Soziologie)
- Bachelorarbeit
- Einführung in die soziologische Methoden- lehre (SozM-E)
- Bachelorarbeit im Erstfach

### 2-Fach-BA Theater- und Medienwissenschaft FPO B.A. Theatermedien 20071004 i.d.F. 20190815.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20071004-idf-20190815.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20071004-idf-20190815.md)

**Pflichtmodule (11):**
- Basismodul Medienwissenschaft
- Basisseminar Analyse
- Basismodul Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Technik
- Bachelorarbeit im Erstfach (Theater- und Medienwissenschaft)
- Bachelorarbeit
- Forschungsfragen
- Bachelorarbeit im Erstfach

### 2-Fach-BA Theater- und Medienwissenschaft FPO B.A. Theatermedien 20071004 i.d.F. 20220512.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20071004-idf-20220512.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20071004-idf-20220512.md)

**Pflichtmodule (11):**
- Basismodul Medienwissenschaft
- Basisseminar Analyse
- Basismodul Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Technik
- Bachelorarbeit im Erstfach (Theater- und Medienwissenschaft)
- Bachelorarbeit
- Forschungsfragen
- Bachelorarbeit im Erstfach

### 2-Fach-BA Theater- und Medienwissenschaft FPO B.A. Theatermedien 20190815 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20190815-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20190815-aes.md)

**Pflichtmodule (12):**
- Basismodul Medienwissenschaft
- Basisseminar Analyse
- Basismodul Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Technik
- Bachelorarbeit im Erstfach (Theater- und Medienwissenschaft)
- Bachelorarbeit
- Forschungsfragen
- Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 17. Februar 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2aes-2fachba-oeffentlichesrecht.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2aes-2fachba-oeffentlichesrecht.md)

**Pflichtmodule (13):**
- Grundlagen-modul
- Staats- organisationsrecht
- Grundrechte
- Allgemeine Grundlagen des Verwaltungsrechts
- Allgemeines Verwaltungsrecht
- Europa- und
- Völkerrecht I
- Verwaltungs-recht I
- Verwaltungsprozes srecht
- Europa- und Völkerecht II
- Völkerrecht II
- Verwaltungs-recht II
- Umweltrecht I

### 2Fach Geschichte 20071004 i.d.F. 20180911.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fach-geschichte-20071004-idf-20180911.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fach-geschichte-20071004-idf-20180911.md)

**Pflichtmodule (7):**
- Basismodul I3
- Basismodul II3
- Basismodul III3
- Methodische und Theoretische
- Methodische Grundlagen
- Theoretische Grundlagen
- Bachelorarbeit

### 2Fach Geschichte 20180911 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fach-geschichte-20180911-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fach-geschichte-20180911-aes.md)

**Pflichtmodule (7):**
- Basismodul I3
- Basismodul II3
- Basismodul III3
- Methodische und Theoretische Grundlagen
- Methodische Grundlagen
- Theoretische Grundlagen
- Bachelorarbeit

### PDF vom 18.07.2014 i.d.F. 11.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fachba-archaeologischewissenschaften-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fachba-archaeologischewissenschaften-aug2015.md)

**Pflichtmodule (11):**
- Basismodule: Kulturentwicklung und Kulturgeschichte~~3)~~
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I3)
- Proseminar zur prähistori-
- schen Kulturentwicklung
- Europas
- Übung zur prähistorischen Kulturentwicklung Europas
- Prähistorische Archäologie: Jüngere Urgeschichte I3)
- Proseminar zur prähistori- schen Kulturentwicklung Europas
- Bachelorarbeit und -prüfung
- Bachelorarbeit6)

### PDF vom 18.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fachba-archaeologischewissenschaften.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fachba-archaeologischewissenschaften.md)

**Pflichtmodule (11):**
- Basismodule: Kulturentwicklung und Kulturgeschichte3)
- PrähistorischeArchäologie
- Prähistorische Archäologie: Ältere Urgeschichte I3)
- Proseminar zur prähistori-
- schen Kulturentwicklung
- Europas
- Übung zur prähistorischen Kulturentwicklung Europas
- Prähistorische Archäologie: Jüngere Urgeschichte I3)
- Proseminar zur prähistori- schen Kulturentwicklung Europas
- Bachelorarbeit und -prüfung
- Bachelorarbeit6)

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

**Pflichtmodule (17):**
- Grundlagen Japanologie 1
- EinführungStudium
- Grundlagen Japanologie 2
- Japanisch 3
- Sprachkurs
- Japanisch 4
- LektüreModerneProsa
- Grundlagen Japanologie 31
- Arbeitsmittel
- Grundlagen Japanologie 41
- Japanische Literatur und Film
- Aktuelle Publikationen
- Hauptseminar Literatur/Film
- Japanisch 5
- Zeitungslektüre
- Japanisches Theater1
- Hauptseminar Theater

### 11. August 2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/5aes-englischamerican.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/5aes-englischamerican.md)

**Pflichtmodule (4):**
- (101) Basismodul I Language
- (102) Basismodul II Linguistics
- (103) Basismodul III Literature
- (104) Basismodul IV Culture

### 9. Mai 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-indogermindoiran.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-indogermindoiran.md)

**Pflichtmodule (5):**
- EinführungindieIndogermanistik
- Einführungindas Germanische
- SanskritI
- SanskritII
- Bachelorarbeit

### 25. Juni 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-nordphilologie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-nordphilologie.md)

**Pflichtmodule (10):**
- Basismodule:
- Nordistische Linguistik 12
- Nordistische Linguistik 22
- Einführungsseminar 2
- Nordistische Literatur- und Kulturwissenschaft 12
- Nordistische Literatur- und Kulturwissenschaft22
- Altnordisch 12
- Altnordisch 22
- Nordische Erstsprache 12
- Nordische Erstsprache 22

### 15. Juli 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-theater-und-medien.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-theater-und-medien.md)

**Pflichtmodule (10):**
- Basisseminar Theo/Histo
- Medienwissenschaft
- Basismodul Theaterwissenschaft
- Basisseminar Analyse
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Theorien der Praxis
- Bachelorarbeit
- Oberseminar Forschungsfragen (fakultativ)

### 11. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fach-ba-linginformatik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fach-ba-linginformatik.md)

**Pflichtmodule (10):**
- Grundlagen der Computerlinguistik I
- ÜbungCL 1
- Arbeitstechniken
- Grundlagen der Informatik (Importmodul)
- Grundlagen der Computerlinguistik II
- Programmierung I
- Programmierung II
- Proseminar Computerlinguistik
- Werkzeuge und Infrastrukturen
- Konzeptionelle Modellierung (Importmodul)

### 7. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fachba-germanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fachba-germanistik.md)

**Pflichtmodule (4):**
- Grundlagen der Germanistischen Linguistik (Ling1)
- Alternative für ausländische Studierende: Grundlagen der Germanistischen Linguistik (DaF) (Ling1a)
- Grundlagen der Germanistischen Mediävistik (Med 1)
- Grundlagen der Neueren deutschen Literatur (NdL 1)

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aesa-2fachba-nordphilologie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aesa-2fachba-nordphilologie.md)

**Pflichtmodule (12):**
- Basismodule: Es müssen alle Basismodule belegt werden (40 ECTS).
- Nordistische Literaturwissenschaft 1
- Nordistische Literaturwissenschaft 2
- Nordistische Literaturwissenschaft 3
- Nordische Kulturgeschichte 1
- Nordische Kulturgeschichte 2
- Nordische Erstsprache 1
- Nordische Erstsprache 2
- Seminar Sprachanalyse
- Bachelorarbeit (nur im Erstfach): 10
- Abschlussmodul Bachelorarbeit
- Bachelorarbeit

### 10. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-frankoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-frankoromanistik.md)

**Pflichtmodule (8):**
- Basismodul Französische Sprachpraxis 1
- Vocabulaire, idiomatique et civilisation I
- Communication orale
- Basismodul Französische Sprachpraxis 2
- Grammaire cours élémentaire II (groupe verbal)
- Phonétique pratique, orthophonie et intonation
- Basismodul Einführung in die Frankoromanistik
- Basisseminar französische Literaturwissenschaft

### 10. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-iberoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-iberoromanistik.md)

**Pflichtmodule (6):**
- Basismodul Spanische Sprachpraxis 1
- Cultura y comunicación oral
- BasismodulSpanische Sprachpraxis 2
- Fonética práctica
- Basismodul Einführung in die Iberoromanistik
- Basisseminar Spanische Literaturwissenschaft Phonetik und Phonologie des

### 10. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-italoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-italoromanistik.md)

**Pflichtmodule (7):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I
- Basismodul Italienische Sprachpraxis 2
- Fonetica pratica
- Tecniche di lettura
- Basismodul Einführung in die Italoromanistik
- Basisseminar ItalienischeLiteraturwissenschaft

### 2. Juni 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-philosophie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-philosophie.md)

**Pflichtmodule (11):**
- Grundkurs PraktischePhilosophie
- Grundkurs Theoretische Philosophie
- Basismodul Philosophie
- Textseminar (Mittelseminar)
- Basismodul Praktische Philosophie
- Historisch-systematische Ein- füh Pi
- rung (rosemnar)
- Basismodul Theoretische Philosophie
- Philosophiegeschichte2
- Philosophie systematisch3
- Bachelorarbeit

### 5. August 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fachba-germanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fachba-germanistik.md)

**Pflichtmodule (8):**
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Analyseseminar 1
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
- Analyseseminar 2
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1 (MedBM 1)
- Grundlagen der Germanistischen Mediävistik 2 (Med BM 2)

### 3. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fachba-mittelneulatein.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fachba-mittelneulatein.md)

**Pflichtmodule (11):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Übersetzungausgewählter Texte
- Tutorium
- Basismodul 2: Einführung in die lateinische Schrift (Paläographie)
- Exkursion
- Basismodul 3A: Das Klassische Erbe A2
- Basismodul 3B:
- Das Klassische Erbe B2
- Basismodul 4: Europäische Mediävistik I
- Basismodul 5: Europäische Mediävistik
- Bachelorarbeit

### 12. Juni 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aesa-2fba-sinologie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aesa-2fba-sinologie.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### 2. Juni 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aes-2fach-ba-informatik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aes-2fach-ba-informatik.md)

**Pflichtmodule (12):**
- Grundlagen der Informatik
- Konzeptionelle Mo- dellierung
- Konzeptionelle Modellie- rung
- Mathematik
- Theoretische Infor- matik
- Theoretische Informatik für Wirtschaftsinformatik und Lehramt
- Grundlagen der Logik in der Infor- matik
- Grundlagen der Logik und Logikprogrammierung
- Mathematische Modellbildung und Statistik
- Mathematische Modellbil- dung und Statistik für Na- turwissenschaftler
- Kernmodul 1: Ein- führung in die Digi- talen Geistes- und Sozialwissenschaf- ten
- Einführung in die Digitalen Geistes- und Sozialwissen- schaften

### 22. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aes-2fachba-soziologie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aes-2fachba-soziologie.md)

**Pflichtmodule (13):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Statistische Analyseverfahren I (SozS-I)
- Ü Statistische Analyseverfahren I
- Statistische Analyseverfahren II (SozS-II)
- V Statistische Analyse- fhII
- veraren
- Ü Statistische Analyse- verfahren II
- Qualifikationsprofil I (SozQ-I)
- Qualifikationsprofil II (SozQ-II)

### 28. Juli 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-frankoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-frankoromanistik.md)

**Pflichtmodule (8):**
- Basismodul Französische Sprachpraxis 1
- Communication orale
- Basismodul Französische Sprachpraxis 2
- Parcours grammatical II
- Phonétique pratique, orthophonie et intonation
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Bachelorarbeit

### 28. Juli 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-iberoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-iberoromanistik.md)

**Pflichtmodule (7):**
- Basismodul Spanische Sprachpraxis 1
- Culturaycomunicación oral
- Basismodul Spanische Sprachpraxis 2
- Fonética práctica
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Bachelorarbeit

### 28. Juli 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-italoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-italoromanistik.md)

**Pflichtmodule (7):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I
- Basismodul Italienische Sprachpraxis 2
- Fonetica pratica
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft

### PDF vom 05.10.2007

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20buchwiss.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20buchwiss.md)

**Pflichtmodule (2):**
- Typografische Grundlagen
- Bachelorarbeit

### PDF vom 04.10.2007

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20frankorom.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-20frankorom.md)

**Pflichtmodule (4):**
- Einführung in die romanistische Sprachwissenschaft
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

### PDF vom 05.10.2007 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-ba-kunstgesch-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-ba-kunstgesch-aug2017.md)

**Pflichtmodule (1):**
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

**Pflichtmodule (10):**
- Basisseminar Theo/Histo
- Medienwissenschaft
- Basismodul Theaterwissenschaft
- Basisseminar Analyse
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Theoriender Praxis
- Bachelorarbeit
- Oberseminar Forschungs- fragen (fakultativ)

### PDF vom 04.10.2007 i.d.F. 10.06.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankorom-10juni2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankorom-10juni2014.md)

**Pflichtmodule (9):**
- Basismodul Französische Sprachpraxis 1
- Vocabulaire, idiomatique et civilisation I
- Communication orale
- Basismodul Französische Sprachpraxis 2
- Grammaire cours élémentaire II (groupe verbal)
- Phonétique pratique, orthophonie et intonation
- Basismodul Einführung in die Frankoromanistik
- Basisseminar französische Literaturwis- senschaft
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F: 28.07.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankoromjuli2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankoromjuli2017.md)

**Pflichtmodule (8):**
- Basismodul Französische Sprachpraxis 1
- Communication orale
- Basismodul Französische Sprachpraxis 2
- Parcours grammatical II
- Phonétique pratique, orthophonie et intonation
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 05.08.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-aug2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-aug2016.md)

**Pflichtmodule (8):**
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Analyseseminar 1
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
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

### PDF vom 04.10.2007 i.d.F. 07.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-juli-2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-juli-2014.md)

**Pflichtmodule (4):**
- Grundlagen der Germanistischen Linguistik (Ling1)
- Alternative für ausländische Studierende: Grundlagen der Germanistischen Linguistik (DaF) (Ling1a)
- Grundlagen der Germanistischen Mediävistik (Med 1)
- Grundlagen der Neueren deutschen Literatur (NdL 1)

### PDF vom 04.10.2007 i.d.F. 08.03.2011

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-maerz2011.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-maerz2011.md)

**Pflichtmodule (14):**
- Basismodul: Grundlagen der Germanistischen Linguistik
- Einführungskurs: Einführung in die GermanistischeLinguistik
- Für ausländische Studierende
- Basismodul: Grundlagen der Germanistischen Linguistik (DaF)
- Basismodul: Grundlagen der Germanistischen Mediävistik
- Einführungskurs: Einführung in die Germanistische Mediävistik
- Basismodul: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die Neuere deutsche Literatur- wissenschaft
- Basismodul Ling 1: Grundlagen der Germa- nistischen Linguistik
- Kurs: Einführung in die Germanistische Linguistik
- Für ausländische Studierende Basismodul Ling 1a: Grundlagen der Germa- nistischen Linguistik (DaF)
- Basismodul Med 1: Grundlagen der Germa- nistischen Mediävistik
- Basismodul NdL 1: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die neuere Deutsche Literaturwissenschaft

### PDF vom 04.10.2007 i.d.F. 04.05.2012

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-mai2012.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-mai2012.md)

**Pflichtmodule (14):**
- Basismodul: Grundlagen der Germanistischen Linguistik
- Einführungskurs: Einführung in die GermanistischeLinguistik
- Für ausländische Studierende
- Basismodul: Grundlagen der Germanistischen Linguistik (DaF)
- Basismodul: Grundlagen der Germanistischen Mediävistik
- Einführungskurs: Einführung in die Germanistische Mediävistik
- Basismodul: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die Neuere deutsche Literatur- wissenschaft
- Basismodul Ling 1: Grundlagen der Germa- nistischen Linguistik
- Kurs: Einführung in die Germanistische Linguistik
- Für ausländische Studierende Basismodul Ling 1a: Grundlagen der Germa- nistischen Linguistik (DaF)
- Basismodul Med 1: Grundlagen der Germa- nistischen Mediävistik
- Basismodul NdL 1: Grundlagen der Neueren deutschen Literatur
- Einführungskurs: Einführung in die neuere Deutsche Literaturwissenschaft

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

**Pflichtmodule (2):**
- Mind. 20 ECTS- Punkte
- Mind. 40 ECTS- Punkte

### PDF vom 04.10.2007 i.d.F. 05.11.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-geschichte.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-geschichte.md)

**Pflichtmodule (2):**
- Mind. 20 ECTS- Punkte
- Mind. 40 ECTS- Punkte

### PDF vom 05.10.2007 i.d.F. 04.02.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-griechphil-feb2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-griechphil-feb2015.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 10.06.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-iberorom-10juni2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-iberorom-10juni2014.md)

**Pflichtmodule (7):**
- Basismodul Spanische Sprachpraxis 1
- Culturaycomunicación oral
- BasismodulSpanische Sprachpraxis 2
- Fonética práctica
- Basismodul Einführung in die Iberoromanistik
- Basisseminar Spanische Literaturwissen- schaft
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 28.07.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-iberoromjuli2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-iberoromjuli2017.md)

**Pflichtmodule (7):**
- Basismodul Spanische Sprachpraxis 1
- Culturaycomunicación oral
- Basismodul Spanische Sprachpraxis 2
- Fonética práctica
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

**Pflichtmodule (15):**
- Grundlagen der Informatik
- Konzeptionelle Modellierung
- KonzeptionelleModellierung
- Mathematik
- Theoretische Informatik
- Theoretische Informatik für Wirtschaftsinformatik und Lehramt
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik und Logikprogrammierung
- Mathematische Modellbildung und Statistik
- Mathematische Modellbil- dung und Statistik für Natur- wissenschaftler
- Kernmodul 1: Einführung in die Digitalen Geistes- und Sozial- wissenschaften
- Einführung in die Digitalen Geistes- und Sozialwissen- schaften
- Kernmodul 2: Nutzung digitaler Daten in den Geistes- und So- zialwissenschaften
- Kernmodul 3: Wissenschaft und Gesellschaft im digitalen Zeitalter
- Praxismodul

### PDF vom 04.10.2007 i.d.F. 10.06.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italorom-10juni2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italorom-10juni2014.md)

**Pflichtmodule (7):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I
- Basismodul Italienische Sprachpraxis 2
- Fonetica pratica
- Tecniche di lettura
- Basismodul Einführung in die Italoromanistik
- Basisseminar ItalienischeLiteraturwissen- schaft

### PDF vom 04.10.2007 i.d.F. 28.07.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italoromjuli2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italoromjuli2017.md)

**Pflichtmodule (8):**
- Basismodul Italienische Sprachpraxis 1
- Comprensione e produzione orale I
- Basismodul Italienische Sprachpraxis 2
- Fonetica pratica
- Tecniche di lettura
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-japan-februar2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-japan-februar2014.md)

**Pflichtmodule (21):**
- Grundlagen Japanologie 1
- EinführungStudium
- Grundlagen Japanologie 2
- Japanisch 3
- Sprachkurs
- Japanisch 4
- Lektüre Moderne Prosa
- Grundlagen Japanologie 31
- Arbeitsmittel
- Grundlagen Japanologie 41
- Japanische Literatur und Film
- Aktuelle Publikationen
- Hauptseminar Literatur/Film
- Japanisch 5
- Zeitungslektüre
- Japanisches Theater1
- Hauptseminar Theater
- Japanologie 1
- Oberseminar Wihftlih Päti
- ssenscaces rseneren
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 07.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-japan-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-japan-juli2014.md)

**Pflichtmodule (21):**
- Grundlagen Japanologie 1
- EinführungStudium
- Grundlagen Japanologie 2
- Japanisch 3
- Sprachkurs
- Japanisch 4
- Lektüre Moderne Prosa
- Grundlagen Japanologie 31
- Arbeitsmittel
- Grundlagen Japanologie 41
- Japanische Literatur und Film
- Aktuelle Publikationen
- Hauptseminar Literatur/Film
- Japanisch 5
- Zeitungslektüre
- Japanisches Theater1
- Hauptseminar Theater
- Japanologie 1
- Oberseminar Wihftlih Päti
- ssenscaces rseneren
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 03.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-mittellatein-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-mittellatein-aug2015.md)

**Pflichtmodule (11):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Übersetzungausgewählter Texte
- Tutorium
- Basismodul 2: Einführung in die lateinische Schrift (Paläographie)
- Exkursion
- Basismodul 3A: Das Klassische Erbe A2
- Basismodul 3B:
- Das Klassische Erbe B2
- Basismodul 4: Europäische Mediävistik I
- Basismodul 5: Europäische Mediävistik
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-mittellatein-februar2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-mittellatein-februar2014.md)

**Pflichtmodule (17):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Proseminar Einführungin das lateinische Europa
- Übersetzungausgewählter Texte
- Tutorium
- Basismodul 2: Einführung in die lateinische Schrift
- Proseminar Schrift und Kultur
- Bibliotheksexkursion mit Selbststudiumseinheit
- Basismodul 3A: Das klassische Erbe oder
- Das klassische Erbe(Klassisches Latein)
- Basismodul 3B: Das klassische Erbe
- Proseminar Das klassische Erbe
- Übungoder VorlesungDas klassische Erbe
- Basismodul 4: Europäische Mediävistik I
- aus einem der Fächer: Anglistik, Germanistik und Kompa- ratistikoder Romanistik
- Basismodul 5: Europäische Mediävistik II
- aus einem der Fächer: Buchwissenschaft, Geschichte, Kunstgeschichte, Philosophie
- Bachelorarbeit(MLat 8)

### PDF vom 05.10.2007 i.d.F. 25.06.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-nordphil-juni2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-nordphil-juni2015.md)

**Pflichtmodule (12):**
- Basismodule:
- Nordistische Linguistik 12
- Nordistische Linguistik 22
- Einführungsseminar 2
- Nordistische Literatur- und Kulturwissenschaft 12
- Nordistische Literatur- und Kulturwissenschaft22
- Altnordisch 12
- Altnordisch 22
- Nordische Erstsprache 12
- Nordische Erstsprache 22
- Bachelorarbeit (nur im Erstfach)
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-nordphilaug2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-nordphilaug2017.md)

**Pflichtmodule (12):**
- Basismodule: Es müssen alle Basismodule belegt werden (40 ECTS).
- Nordistische Literaturwissenschaft 1
- Nordistische Literaturwissenschaft 2
- Nordistische Literaturwissenschaft 3
- Nordische Kulturgeschichte 1
- Nordische Kulturgeschichte 2
- Nordische Erstsprache 1
- Nordische Erstsprache 2
- Seminar Sprachanalyse
- Bachelorarbeit (nur im Erstfach): 10 ECTS
- Abschlussmodul Bachelorarbeit
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-orient-feb2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-orient-feb2014.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 21.05.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-orient-mai2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-orient-mai2015.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 02.06.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-philosophie-juni2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-philosophie-juni2016.md)

**Pflichtmodule (12):**
- Grundkurs PraktischePhilosophie
- Grundkurs TheoretischePhilosophie
- Basismodul Philosophie
- Textseminar (Mittelseminar)
- Basismodul Praktische Philosophie
- Historisch-systematische Eifüh Pi
- nrung (rosemnar)
- Basismodul Theoretische Philosophie
- Philosophiegeschichte2
- Philosophie systematisch3
- Bachelorarbeit
- umme:

### PDF vom 05.10.2007 i.d.F. 02.06.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-politik-juni2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-politik-juni2016.md)

**Pflichtmodule (9):**
- Politische Systeme I
- Politische Systeme II
- Außereuropäische Regionen I
- Außereuropäische Regionen II
- Internationale Beziehungen I
- Internationale Beziehungen II
- Politische Theorie & Ideengeschichte I
- Politische Theorie & Ideengeschichte II
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-februar2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-februar2014.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 22.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-juli2014.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 29.07.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-juli2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-juli2016.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 12.06.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-juni2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-sinologie-juni2017.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 22.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-soziol-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-soziol-juli2014.md)

**Pflichtmodule (12):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien(SozT-V)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Statistische Analyseverfahren I (SozS-I)
- Ü Statistische Analyseverfahren I
- Statistische Analyseverfahren II (SozS-II)
- V Statistische Analyse-verfahren II
- Ü Statistische Analyse-verfahren II
- Qualifikationsprofil I (SozQ-I)
- Qualifikationsprofil II (SozQ-II)

### PDF vom 05.10.2007 i.d.F. 02.07.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-soziol-juli2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-soziol-juli2015.md)

**Pflichtmodule (13):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien(SozT-V)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Statistische Analyseverfahren I (SozS-I)
- Ü Statistische Analyseverfahren I
- Statistische Analyseverfahren II (SozS-II)
- V Statistische Analyse-verfahren II
- Ü Statistische Analyse-verfahren II
- Qualifikationsprofil I (SozQ-I)
- Qualifikationsprofil II (SozQ-II)
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-theater-februar2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-theater-februar2014.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- Verfassender Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 15.07.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-theater-juli2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-theater-juli2016.md)

**Pflichtmodule (10):**
- Basisseminar Theo/Histo
- Medienwissenschaft
- Basismodul Theaterwissenschaft
- Basisseminar Analyse
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Theorien der Praxis
- Bachelorarbeit
- Oberseminar Forschungsfragen (fakultativ)

### PDF vom 05.10.2007 i.d.F. 11.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-aug2015.md)

**Pflichtmodule (10):**
- Grundlagen der Computerlinguistik I
- ÜbungCL 1
- Arbeitstechniken
- Grundlagen der Informatik (Importmodul)
- Grundlagen der Computerlinguistik II
- Programmierung I
- Programmierung II
- Proseminar Computerlinguistik
- Werkzeuge und Infrastrukturen
- Konzeptionelle Modellierung (Importmodul)

### PDF vom 05.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-februar2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-februar2014.md)

**Pflichtmodule (26):**
- Grundlagen der Computerlinguistik I
- Computerlinguistik I: Sprachtheorie
- Übung zur Vorlesung Grundlagen der Computerlinguis- tik I: Sprachtheorie
- Computerlinguistik II: Formale Sprachen
- Übung zur Vorlesung Grundlagen der Computerlinguis- tik II: Formale Sprachen
- Werkzeuge und Arbeitstechniken
- Werkzeuge und Arbeitstechniken der Computerlinguis- tik
- Einführungin die Grammatikentwicklung
- Grundlagen der Computerlinguistik II
- Computerlinguistik III: Morphologie und Syntax
- Übung zur Vorlesung Grundlagen der Computerlinguis- tik III: Morphologie und Syntax
- Computerlinguistik IV: Semantik und Pragmatik
- Übung zur Vorlesung Grundlagen der Computerlinguis- tik IV: Semantik und Pragmatik
- Grundlagen der Informatik
- Rechnerübungzu Grundlagen der Informatik
- Tafelübungzu Grundlagen der Informatik
- Konzeptionelle Modellierung
- Übungzu Konzeptionelle Modellierung
- Datenbanksysteme
- VorlesungDatenbanksysteme
- Übungzu VorlesungDatenbanksysteme
- Maschinelle Sprachverarbeitung
- Programmierung
- Grundkurs Programmierung
- Aufbaukurs Programmierung
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 22.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-juli2014.md)

**Pflichtmodule (8):**
- Grundlagen der Computerlinguistik I
- ÜbungCL 1
- Arbeitstechniken
- Grundlagen der Informatik (Importmodul)
- Grundlagen der Computerlinguistik II
- Programmierung
- Aufbauseminar Programmierung
- Bachelorarbeit*

### FPO 2-Fach BA DGSW 20080722 i.d.F. 20180829.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-2-fach-ba-dgsw-20080722-idf-20180829.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-2-fach-ba-dgsw-20080722-idf-20180829.md)

**Pflichtmodule (13):**
- Grundlagen der Informatik
- Konzeptionelle Modellierung
- Mathematik für Naturwissen- schaftler
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende2
- Theoretische Informatik für Wirt-
- schaftsinformatik und Lehramt
- Theoretische Informatik für Wirt- schaftsinformatik und Lehramt
- Grundlagen der Logik in der Informatik2
- Mathematische Modell- bildung und Statistik für Naturwissenschaftler
- DH-Modul 1: Schwerpunkt Sprache und Text
- DH-Modul 2: Schwerpunkt Gesellschaft und Raum
- DH-Modul 3: Schwerpunkt Bild und Medien
- Praxis-/Projektmodul

### FPO 2-Fach BA DGSW 20250411.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-2-fach-ba-dgsw-20250411.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-2-fach-ba-dgsw-20250411.md)

**Pflichtmodule (8):**
- Grundlagen der Informatik (GdI)
- Einführung in die Informa- tik für DH
- Grundlagen der Logik in der Informatik
- Theoretische Informatik für DH
- Bachelorarbeit im Erstfach (Digitale Geistes- und Sozialwissenschaften)
- Bachelorarbeit
- Einführung in die Informatik für DH
- Bachelorarbeit im Erstfach

### FPO BA Sino Zwei-Fach 20071005 i.d.F. 20190828.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-20071005-idf-20190828.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-20071005-idf-20190828.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach (Sinologie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### FPO BA Sino Zwei-Fach 20230615 i.d.F. 20260331.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-20230615-idf-20260331.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-20230615-idf-20260331.md)

**Pflichtmodule (2):**
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### FPO BA Sino Zwei-Fach 20230615.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-20230615.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-20230615.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach (Sinologie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### FPO BA Sino Zwei-Fach ÄS 20190828.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-aes-20190828.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-aes-20190828.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach (Sinologie)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### FPO BA Sino Zwei-Fach ÄS 20260331.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-aes-20260331.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-ba-sino-zwei-fach-aes-20260331.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### FPO Griechisch Zwei-Fach 20071005 i.d.F. 20200806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20071005-idf-20200806.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20071005-idf-20200806.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach (Mittellatein und Neulatein)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### FPO Griechisch Zwei-Fach 20200806 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20200806-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20200806-aes.md)

**Pflichtmodule (4):**
- Bachelorarbeit im Erstfach (Mittellatein und Neulatein)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### FPO Griechisch Zwei-Fach 20250131.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20250131.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-griechisch-zwei-fach-20250131.md)

**Pflichtmodule (3):**
- Bachelorarbeit im Erstfach(Mittellatein und Neulatein)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### Indogermanistik und Indoiranistik Zwei-Fach FPO Indo 20250131.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/indogermanistik-und-indoiranistik-zwei-fach-fpo-indo-20250131.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/indogermanistik-und-indoiranistik-zwei-fach-fpo-indo-20250131.md)

**Pflichtmodule (7):**
- Einführung in die Indogermanistik
- Einführung in das Germanische
- Sanskrit I
- Sanskrit II
- Bachelorarbeit im Erstfach (Indogermanistik und Indoiranistik)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

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

### 26. Juni 2007

PO-Quelle: [`pruefungsordnungen/rw/wiso/1aesa-ba-wiwi.md`](../pruefungsordnungen/rw/wiso/1aesa-ba-wiwi.md)

**Pflichtmodule (1):**
- zialök.

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

**Pflichtmodule (27):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissen- schaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik: Analysis und Lineare Algebra
- Statistik
- BWL/VWL
- Absatz
- Mikroökonomie
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Kernbereich des Schwerpunkts International
- Europäisches und internationales Recht
- Internationale Kommunikation
- Global governance
- International business relations
- Globalisierung und Internationalisierung
- Sprachen 1.2
- Sprachen 2.1
- Sprachen 2.2

### BA Sozialökonomik FPO BA SozÖk 20170810 i.d.F. 20190220.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20190220.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20190220.md)

**Pflichtmodule (27):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissen- schaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik: Analysis und Lineare Algebra
- Statistik
- BWL/VWL
- Absatz
- Mikroökonomie
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Kernbereich des Schwerpunkts International
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

**Pflichtmodule (27):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissen- schaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik: Analysis und Lineare Algebra
- Statistik
- BWL/VWL
- Absatz
- Mikroökonomie
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Kernbereich des Schwerpunkts International
- Europäisches und internationales Recht
- Internationale Kommunikation
- Global governance
- International business relations
- Globalisierung und Internationalisierung
- Sprachen 1.2
- Sprachen 2.1
- Sprachen 2.2

### BA Sozialökonomik FPO BA SozÖk 20170810 i.d.F. 20200902.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20200902.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20170810-idf-20200902.md)

**Pflichtmodule (27):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissen- schaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik
- Data Science: Datenauswertung
- Data Science: Statistik
- BWL/VWL
- Absatz
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Kernbereich des Schwerpunkts International
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

**Pflichtmodule (32):**
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Kernbereich des Schwerpunkts Verhaltenswissenschaften
- Empirische Methoden und Statistik
- Personal und Organisation I
- Digital Technologies & Society
- Sozialpolitische Grundlagen
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissen- schaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik
- Data Science: Datenauswertung
- Data Science: Statistik
- BWL/VWL
- Absatz
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

**Pflichtmodule (32):**
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Kernbereich des Schwerpunkts Verhaltenswissenschaften
- Empirische Methoden und Statistik
- Personal und Organisation I
- VP5)
- Digital Technologies & Society
- Sozialpolitische Grundlagen
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaf- ten
- Internationale Politik I
- International Politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswis- senschaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik
- Data Science: Datenauswertung
- Data Science: Statistik
- BWL/VWL
- Marketing
- Kernbereich des Schwerpunkts International
- Europäisches und internationales Recht
- Hot Topics in International Communi- cation Research
- Global governance
- International business relations
- Sprachen 1.2
- Sprachen 2.1
- Sprachen 2.2

### BA Sozialökonomik FPO BA SozÖk 20240807.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20240807.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-sozialoekonomik-fpo-ba-sozoek-20240807.md)

**Pflichtmodule (18):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik: Die Europäische In- tegration
- International Politics: Global Sustainabi- lity
- Unternehmer und Unternehmen
- Soziologie II
- Medien und Kommunikation
- Sozialpsychologie
- VP5)
- Digitale Sozialwissenschaften
- Methodische Grundlagen der Wirtschaftswissenschaften
- Social Data Science I: Forschungsde- signs
- Social Data Science II: Datenanalyse
- Social Data Science III: Vertiefte Methoden
- Mathematik
- Data Science: Datenauswertung
- Grundlagen des öffentlichen Rechts und des Zivilrechts

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20190222.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20190222.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20190222.md)

**Pflichtmodule (13):**
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Wirtschaftsprivatrecht
- Kernbereich des Schwerpunkts BWL
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Kernbereich des Schwerpunkts VWL
- Kernbereich des Schwerpunkts WI
- Kernbereich des Schwerpunkts WiPäd I
- Grundlagen der Wirtschafts- und Betriebs- pädagogik
- Betriebliche Aus- und Weiterbildung
- Präsentations- und Moderationstechniken
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Kernbereich des Schwerpunkts WiPäd II

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20190731.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20190731.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20190731.md)

**Pflichtmodule (13):**
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Wirtschaftsprivatrecht
- Kernbereich des Schwerpunkts BWL
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Kernbereich des Schwerpunkts VWL
- Kernbereich des Schwerpunkts WI
- Kernbereich des Schwerpunkts WiPäd I
- Grundlagen der Wirtschafts- und Betriebs- pädagogik
- Betriebliche Aus- und Weiterbildung
- Präsentations- und Moderationstechniken
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Kernbereich des Schwerpunkts WiPäd II

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20200902.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20200902.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20200902.md)

**Pflichtmodule (46):**
- Übersicht/Welt des Unternehmens
- Unternehmensplanspiel
- Unternehmen, Märkte, Volkswirtschaften
- Unternehmer und Unternehmen
- Data Science
- Data Science: Machine Learning und Data Driven Business
- Data Science: Datenauswertung
- Data Science: Statistik
- Data Science: Datenmanagement und -analyse
- Data Science: Ökonometrie
- BWL/Unternehmen und ihr Geschäft
- Absatz
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- VWL/Unternehmen und ihr Umfeld
- Makroökonomie
- Mikroökonomie
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
- IT-Management
- Methodische Grundlagen der Wirtschaftswissenschaften
- Kernbereich des Schwerpunkts WiPäd I
- Grundlagen der Wirtschafts- und Betriebs- pädagogik
- Betriebliche Aus- und Weiterbildung
- Präsentations- und Moderationstechniken
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Kernbereich des Schwerpunkts WiPäd II

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20210122.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20210122.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20210122.md)

**Pflichtmodule (46):**
- Übersicht/Welt des Unternehmens
- Unternehmensplanspiel
- Unternehmen, Märkte, Volkswirtschaften
- Unternehmer und Unternehmen
- Data Science
- Data Science: Machine Learning und Data Driven Business
- Data Science: Datenauswertung
- Data Science: Statistik
- Data Science: Datenmanagement und -analyse
- Data Science: Ökonometrie
- BWL/Unternehmen und ihr Geschäft
- Absatz
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- VWL/Unternehmen und ihr Umfeld
- Makroökonomie
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
- IT-Management
- Methodische Grundlagen der Wirtschaftswissenschaften
- Mikroökonomie
- Kernbereich des Schwerpunkts WiPäd I
- Grundlagen der Wirtschafts- und Betriebs- pädagogik
- Betriebliche Aus- und Weiterbildung
- Präsentations- und Moderationstechniken
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Kernbereich des Schwerpunkts WiPäd II

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20210806.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20210806.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20210806.md)

**Pflichtmodule (45):**
- Übersicht/Welt des Unternehmens
- Unternehmensplanspiel
- Unternehmen, Märkte, Volkswirtschaften
- Unternehmer und Unternehmen
- Data Science
- Data Science: Machine Learning und Data Driven Business
- Data Science: Datenauswertung
- Data Science: Statistik
- Data Science: Datenmanagement und -analyse
- Data Science: Ökonometrie
- BWL/Unternehmen und ihr Geschäft
- Absatz
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- VWL/Unternehmen und ihr Umfeld
- Makroökonomie
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
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Kernbereich des Schwerpunkts VWL
- Internationale Wirtschaft
- Ökonomie des öffentlichen Sektors
- Arbeitsmarktpolitik
- Wettbewerbstheorie und -politik
- Kernbereich des Schwerpunkts WI
- Innovation strategy
- E-Business-Management
- IT-Management
- Methodische Grundlagen der Wirtschaftswissenschaften
- Kernbereich des Schwerpunkts WiPäd I
- Grundlagen der Wirtschafts- und Betriebs- pädagogik
- Betriebliche Aus- und Weiterbildung
- Präsentations- und Moderationstechniken
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Kernbereich des Schwerpunkts WiPäd II

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20220727.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20220727.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20220727.md)

**Pflichtmodule (18):**
- Übersicht/Welt des Unternehmens
- Perspektiven der Wirtschaftswissenschaften
- Unternehmen, Märkte, Volkswirtschaften
- Unternehmer und Unternehmen
- Data Science
- Data Science: Machine Learning und Data Driven Business
- Data Science: Datenauswertung
- Data Science: Statistik
- Data Science: Datenmanagement und -analyse
- Data Science: Ökonometrie3)
- BWL/Unternehmen und ihr Geschäft
- Marketing3)
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- VWL/Unternehmen und ihr Umfeld
- Makroökonomie3)
- Mikroökonomie
- Grundlagen des öffentlichen Rechts und desZivilrechts

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20230323.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20230323.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20230323.md)

**Pflichtmodule (18):**
- Übersicht/Welt des Unternehmens
- Perspektiven der Wirtschaftswissenschaften (GOP)
- Unternehmen, Märkte, Volkswirtschaften (GOP)
- Unternehmer und Unternehmen (GOP)
- Data Science
- Data Science: Machine Learning und Data Driven Business (GOP)
- Data Science: Datenauswertung (GOP)
- Data Science: Statistik (GOP)
- Data Science: Datenmanagement und –analyse (GOP)
- Data Science: Ökonometrie3)
- BWL/Unternehmen und ihr Geschäft
- Marketing3)
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- VWL/Unternehmen und ihr Umfeld
- Makroökonomie3)
- Mikroökonomie (GOP)
- Grundlagen des öffentlichen Rechts und desZivilrechts

### BA Wirtschaftswissenschaften FPO BA WiWi 20200902 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20200902-aes.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20200902-aes.md)

**Pflichtmodule (45):**
- Übersicht/Welt des Unternehmens
- Unternehmensplanspiel
- Unternehmen, Märkte, Volkswirtschaften
- Unternehmer und Unternehmen
- Data Science
- Data Science: Machine Learning und Data Driven Business
- Data Science: Datenauswertung
- Data Science: Statistik
- Data Science: Datenmanagement und -analyse
- Data Science: Ökonometrie
- BWL/Unternehmen und ihr Geschäft
- Absatz
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- VWL/Unternehmen und ihr Umfeld
- Makroökonomie
- Grundlagen des öffentlichen Rechts und des Zivilrechts
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
- Kernbereich des Schwerpunkts VWL
- Internationale Wirtschaft
- Ökonomie des öffentlichen Sektors
- Arbeitsmarktpolitik
- Wettbewerbstheorie und -politik
- Kernbereich des Schwerpunkts WI
- Innovation strategy
- E-Business-Management
- IT-Management
- Methodische Grundlagen der Wirtschaftswissenschaften
- Kernbereich des Schwerpunkts WiPäd I
- Grundlagen der Wirtschafts- und Betriebs- pädagogik
- Betriebliche Aus- und Weiterbildung
- Präsentations- und Moderationstechniken
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Kernbereich des Schwerpunkts WiPäd II
- Grundlagen der Wirtschafts- und Betriebs-

### BA Wirtschaftswissenschaften FPO BA WiWi 20220727 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20220727-aes.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20220727-aes.md)

**Pflichtmodule (16):**
- Übersicht/Welt des Unternehmens
- Perspektiven der Wirtschaftswissenschaften
- Unternehmen, Märkte, Volkswirtschaften
- Unternehmer und Unternehmen
- Data Science
- Data Science: Machine Learning und Data Driven Business
- Data Science: Datenauswertung
- Data Science: Statistik
- Data Science: Datenmanagement und -analyse
- Data Science: Ökonometrie3)
- BWL/Unternehmen und ihr Geschäft
- Marketing3)
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- VWL/Unternehmen und ihr Umfeld
- Grundlagen des öffentlichen Rechts und desZivilrechts

### BA Wirtschaftswissenschaften FPO BA WiWi 20240807 i.d.F. 20250616.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20240807-idf-20250616.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20240807-idf-20250616.md)

**Pflichtmodule (17):**
- Übersicht/Welt des Unternehmens
- Perspektiven der Wirtschaftswissenschaften (GOP)
- Unternehmen, Märkte, Volkswirtschaften (GOP)
- Unternehmer und Unternehmen (GOP)
- Data Science
- Data Science: Machine Learning und Data Driven Business (GOP)
- Data Science: Datenauswertung (GOP)
- Data Science: Statistik (GOP)
- Data Science: Datenmanagement und – analyse (GOP)
- Data Science: Ökonometrie3)
- BWL/Unternehmen und ihr Geschäft
- Marketing3)
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- VWL/Unternehmen und ihr Umfeld
- Makroökonomie3)
- Grundlagen des öffentlichen Rechts und des Zivilrechts

### BA Wirtschaftswissenschaften FPO BA WiWi 20240807.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20240807.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20240807.md)

**Pflichtmodule (17):**
- Übersicht/Welt des Unternehmens
- Perspektiven der Wirtschaftswissenschaften (GOP)
- Unternehmen, Märkte, Volkswirtschaften (GOP)
- Unternehmer und Unternehmen (GOP)
- Data Science
- Data Science: Machine Learning und Data Driven Business (GOP)
- Data Science: Datenauswertung (GOP)
- Data Science: Statistik (GOP)
- Data Science: Datenmanagement und – analyse (GOP)
- Data Science: Ökonometrie3)
- BWL/Unternehmen und ihr Geschäft
- Marketing3)
- Jahresabschluss
- Produktion, Logistik, Beschaffung
- VWL/Unternehmen und ihr Umfeld
- Makroökonomie3)
- Grundlagen des öffentlichen Rechts und des Zivilrechts

### BSc Wirtschaftsinformatik FPO BA WInf 20170810 i.d.F. 20180615.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20180615.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20180615.md)

**Pflichtmodule (17):**
- Übersicht/Welt des Unternehmens
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

**Pflichtmodule (17):**
- Übersicht/Welt des Unternehmens
- Buchführung (GOP)
- Wirtschaftsinformatik
- Business & Information Systems Engineering (GOP)
- Mathematik
- Mathematik: Analysis und Lineare Algebra (GOP)
- Mathematik: Finanzmathematik (GOP)
- Informatik
- Algorithmen und Datenstrukturen (für Medizin- technik) (GOP)
- Theoretische Informatik für Wirtschaftsinformatik
- Grundlagen der Logik in der Informatik
- Unternehmer und Unternehmen
- Absatz
- Produktion, Logistik, Beschaffung
- Data & knowledge
- Digital business
- Architectures & development

### BSc Wirtschaftsinformatik FPO BA WInf 20170810 i.d.F. 20200902.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20200902.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20200902.md)

**Pflichtmodule (21):**
- Pflichtbereich Wirtschaftswissenschaften
- Unternehmer und Unternehmen (GOP)
- Absatz
- Produktion, Logistik, Beschaffung
- Pflichtbereich Informatik
- Algorithmen & Datenstrukturen (für Medizintechnik) (AuD-MT-V) (GOP)
- Algorithmen & Datenstrukturen (für Medizintechnik) (AuD-MT-UE) (GOP)
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
- Bachelor- arbeit
- mind. 128

### BSc Wirtschaftsinformatik FPO BA WInf 20170810 i.d.F. 20210222.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210222.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210222.md)

**Pflichtmodule (21):**
- Pflichtbereich Wirtschaftswissenschaften
- Unternehmer und Unternehmen (GOP)
- Absatz
- Produktion, Logistik, Beschaffung
- Pflichtbereich Informatik
- Algorithmen & Datenstrukturen (für Medizintechnik) (AuD-MT-V) (GOP)
- Algorithmen & Datenstrukturen (für Medizintechnik) (AuD-MT-UE) (GOP)
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
- Bachelor- arbeit
- mind. 128

### BSc Wirtschaftsinformatik FPO BA WInf 20170810 i.d.F. 20210806.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210806.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210806.md)

**Pflichtmodule (21):**
- Pflichtbereich Wirtschaftswissenschaften
- Unternehmer und Unternehmen (GOP)
- Absatz
- Produktion, Logistik, Beschaffung
- Pflichtbereich Informatik
- Algorithmen & Datenstrukturen (für Medizintechnik) (AuD-MT-V) (GOP)
- Algorithmen & Datenstrukturen (für Medizintechnik) (AuD-MT-UE) (GOP)
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
- Bachelor- arbeit
- mind. 128

### BSc Wirtschaftsinformatik FPO BA WInf 20200902 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20200902-aes.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20200902-aes.md)

**Pflichtmodule (12):**
- Pflichtbereich Wirtschaftswissenschaften
- Unternehmer und Unternehmen (GOP)
- Absatz
- Produktion, Logistik, Beschaffung
- Pflichtbereich Informatik
- Algorithmen & Datenstrukturen (für Medizintechnik) (AuD-MT-V) (GOP)
- Algorithmen & Datenstrukturen (für Medizintechnik) (AuD-MT-UE) (GOP)
- Konzeptionelle Modellierung
- Grundlagen der Logik in der Informatik
- Softwareentwicklung in Großprojekten
- Theoretische Informatik für Wirtschaftsinformatik
- mind. 61 mind. 58 mind. 9 180

### BSc Wirtschaftsinformatik FPO BA WInf 20210806 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20210806-aes.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20210806-aes.md)

**Pflichtmodule (22):**
- Pflichtbereich Wirtschaftswissenschaften
- Unternehmer und Unternehmen (GOP)
- Absatz
- Produktion, Logistik, Beschaffung
- Pflichtbereich Informatik
- Algorithmen & Datenstrukturen (für Medizintechnik) (AuD-MT-V) (GOP)
- Algorithmen & Datenstrukturen (für Medizintechnik) (AuD-MT-UE) (GOP)
- Konzeptionelle Modellierung
- Grundlagen der Logik in der Informatik
- Softwareentwicklung in Großprojekten
- Theoretische Informatik für Wirtschaftsinformatik
- Pflichtbereich Wirtschaftsinformatik
- WIN-Projektwoche
- Business and Information Systems Engineering (GOP)
- Data Science: Machine Learning und Data Driven Business
- Data Science: Datenmanagement und -analyse für Wirtschaftsinformatik (GOP)
- Business Process Management (GOP)
- Managing Projects Successfully
- Pflichtbereich Methodische Grundlagen
- Data Science: Datenauswertung
- Data Science: Statistik
- Bachelorarbeit

### BSc Wirtschaftsinformatik FPO BA WInf 20230822 i.d.F. 20250616.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20230822-idf-20250616.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20230822-idf-20250616.md)

**Pflichtmodule (18):**
- Pflichtbereich Wirtschaftswissenschaften
- Unternehmer und Unternehmen (GOP)
- Marketing
- Produktion, Logistik, Beschaffung
- Pflichtbereich Informatik
- Algorithmen und Datenstrukturen für MT - Vorlesung (GOP)
- Algorithmen und Datenstrukturen für MT - Übung (GOP)
- Einführung in Datenbanken für Wirtschaftsinfor- matik
- Grundlagen der Logik in der Informatik
- Einführung in das Software Engineering
- Theoretische Informatik für Wirtschaftsinformatik
- Pflichtbereich Wirtschaftsinformatik
- WIN-Projektwoche
- Pflichtbereich Methodische Grundlagen
- Data Science: Datenauswertung
- Data Science: Statistik
- Bachelorarbeit
- Modul Bachelorarbeit

### BSc Wirtschaftsinformatik FPO BA WInf 20230822.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20230822.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20230822.md)

**Pflichtmodule (21):**
- Pflichtbereich Wirtschaftswissenschaften
- Unternehmer und Unternehmen (GOP)
- Marketing
- Produktion, Logistik, Beschaffung
- Pflichtbereich Informatik
- Algorithmen und Datenstrukturen für MT - Vorlesung (GOP)
- Algorithmen und Datenstrukturen für MT - Übung (GOP)
- Einführung in Datenbanken für Wirtschaftsinfor- matik
- Grundlagen der Logik in der Informatik
- Einführung in das Software Engineering
- Theoretische Informatik für Wirtschaftsinformatik
- Pflichtbereich Wirtschaftsinformatik
- WIN-Projektwoche
- Business and Information Systems Engineering (GOP)
- Pflichtbereich Methodische Grundlagen
- Data Science: Datenauswertung
- Data Science: Statistik
- Bachelorarbeit
- Modul Bachelorarbeit
- Bachelor- arbeit
- mind. 128

### PDF vom 10.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-ibs-aug2017.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-ibs-aug2017.md)

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
- Internationale Politik I
- International politics II
- Kernbereich des Schwerpunkts IBS
- Internationale Wirtschaft
- Europäisches und internationales Recht
- Sprachen IBS 2
- Internationale Unternehmensführung

### PDF vom 10.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-sozoek-aug2017.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-sozoek-aug2017.md)

**Pflichtmodule (17):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissen- schaften
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik: Analysis und Lineare Algebra
- Statistik
- BWL/VWL
- Absatz
- Mikroökonomie

### PDF vom 10.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-wirtschaftsinformatik.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-wirtschaftsinformatik.md)

**Pflichtmodule (16):**
- Übersicht/Welt des Unternehmens
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
- Innovation strategy
- E-Business-Management

### PDF vom 10.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-wiwiaug2017.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/fpo-ba-wiwiaug2017.md)

**Pflichtmodule (28):**
- Übersicht/Welt des Unternehmens
- Unternehmensplanspiel
- Unternehmen, Märkte, Volkswirtschaften
- Unternehmer und Unternehmen
- Methodische Grundlagen der Wirtschaftswissenschaften
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
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Wirtschaftsprivatrecht
- Kernbereich des Schwerpunkts WiPäd I
- Grundlagen der Wirtschafts- und Betriebspä- dagogik
- Berufliche Weiterbildung
- Präsentations- und Moderationstechniken
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Kernbereich des Schwerpunkts WiPäd II
- Grundlagen der Wirtschafts- und Betriebs- pädagogik

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/1aesa-fpomigg.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/1aesa-fpomigg.md)

**Pflichtmodule (1):**
- min. 51

### 18. Januar 2016

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/5aes-ma-iis.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/5aes-ma-iis.md)

**Pflichtmodule (1):**
- WI+INF

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/5aesa-fpowipaed.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/5aesa-fpowipaed.md)

**Pflichtmodule (3):**
- Masterarbeit
- Mindestens 41 SWS
- Mindestens 33 SWS

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-fpomanagement.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-fpomanagement.md)

**Pflichtmodule (1):**
- Mindestens 25 SWS

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-fpomscaup.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/6aesa-fpomscaup.md)

**Pflichtmodule (1):**
- mind. 73

### 10. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/7aesa-ma-fpoeco.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/7aesa-ma-fpoeco.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

### 18. August 2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/8aesa-fpomarketing.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/8aesa-fpomarketing.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 02.09.2009

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuo-pro-20ma-marketing.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuo-pro-20ma-marketing.md)

**Pflichtmodule (1):**
- VL+ÜB

### PDF vom 15.05.2015 i.d.F. 18.09.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuo-pro-ma-gesundheitsmanagement-oekonomieaug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuo-pro-ma-gesundheitsmanagement-oekonomieaug2017.md)

**Pflichtmodule (1):**
- mind. 51

### PDF vom 08.07.2010 i.d.F. 17.01.2011

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-20ma-internationalewirtschaftsinformatik-iis-17jan2011.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-20ma-internationalewirtschaftsinformatik-iis-17jan2011.md)

**Pflichtmodule (1):**
- WI+I

### PDF vom 08.07.2010

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-20ma-internationalewirtschaftsinformatik-iis.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-20ma-internationalewirtschaftsinformatik-iis.md)

**Pflichtmodule (1):**
- WI+I

### PDF vom 20.07.2009 i.d.F. 10.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-economicsaug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-economicsaug2017.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

### PDF vom 08.07.2010 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-iis-aug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-iis-aug2017.md)

**Pflichtmodule (2):**
- Masterarbeit (30 ECTS)
- Masterarbeit

### PDF vom 08.07.2010 i.d.F. 15.02.2013

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-internationalewirtschaftsinformatik-iis-feb2013.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-internationalewirtschaftsinformatik-iis-feb2013.md)

**Pflichtmodule (1):**
- WI+I

### PDF vom 08.07.2010 i.d.F. 18.02.2014

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-internationalewirtschaftsinformatik-iis-feb2014.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-internationalewirtschaftsinformatik-iis-feb2014.md)

**Pflichtmodule (1):**
- WI+I

### PDF vom 08.07.2010 i.d.F. 18.01.2016

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-internationalewirtschaftsinformatik-iis-jan2016.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fachstuopro-ma-internationalewirtschaftsinformatik-iis-jan2016.md)

**Pflichtmodule (1):**
- WI+INF

### PDF vom 17.07.2009 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpo-ma-arb-marktpersonalaug2017.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpo-ma-arb-marktpersonalaug2017.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

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
- Masterarbeit

### FPOAuP 20090717 i.d.F. 20191203.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20191203.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20191203.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

### FPOAuP 20090717 i.d.F. 20200221.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200221.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200221.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

### FPOAuP 20090717 i.d.F. 20200731.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200731.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200731.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

### FPOAuP 20090717 i.d.F. 20210726.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20210726.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20210726.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

### FPOAuP 20090717 i.d.F. 20250227.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20250227.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20250227.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

### FPOECO 20090720 i.d.F. 20191129.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20191129.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20191129.md)

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

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

**Pflichtmodule (2):**
- Masterarbeit
- Seminar zur Masterarbeit

### FPOManagement 20090724 i.d.F. 20190205.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20190205.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20190205.md)

**Pflichtmodule (12):**
- Pflichtbereich I
- Business strategy
- Produktions- und Supply chain management
- Personalmanagement
- Finanzielle Grundlagen des Managements
- Technology and innovation management
- Pflichtbereich II
- Angewandte Managementmethoden
- Fallstudien und Projekte im Management
- Teamfähigkeit, Präsentations- und Verhandlungstechniken
- Fortgeschrittene Methoden der Managementforschung
- Masterarbeit

### FPOManagement 20090724 i.d.F. 20191203.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20191203.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20191203.md)

**Pflichtmodule (12):**
- Pflichtbereich I
- Business strategy
- Produktions- und Supply chain management
- Personalmanagement
- Finanzielle Grundlagen des Managements
- Technology and innovation management
- Pflichtbereich II
- Angewandte Managementmethoden
- Fallstudien und Projekte im Management
- Teamfähigkeit, Präsentations- und Verhandlungstechniken
- Fortgeschrittene Methoden der Managementforschung
- Masterarbeit

### FPOManagement 20090724 i.d.F. 20210812.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20210812.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20210812.md)

**Pflichtmodule (12):**
- Pflichtbereich I
- Business strategy
- Produktions- und Supply chain management
- Personalmanagement
- Finanzielle Grundlagen des Managements
- Technology and innovation management
- Pflichtbereich II
- Angewandte Managementmethoden
- Fallstudien und Projekte im Management
- Teamfähigkeit, Präsentations- und Verhandlungstechniken
- Fortgeschrittene Methoden der Managementforschung
- Masterarbeit

### FPOManagement 20090724 i.d.F. 20230323.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20230323.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20090724-idf-20230323.md)

**Pflichtmodule (1):**
- Mind. 40 SWS4

### FPOManagement 20240229 i.d.F. 20260305.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20240229-idf-20260305.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20240229-idf-20260305.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOManagement 20240229.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20240229.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-20240229.md)

**Pflichtmodule (2):**
- Mind. 40 SWS4
- Mind. 20 SWS4

### FPOManagement ÄSa 20260305.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-aesa-20260305.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomanagement-aesa-20260305.md)

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

### FPOMiGG 20240229 i.d.F. 20250227.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomigg-20240229-idf-20250227.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpomigg-20240229-idf-20250227.md)

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

**Pflichtmodule (3):**
- Masterarbeit
- Seminar zur Masterarbeit
- Masterareit

### FPOSozialökonomik 20090902 i.d.F. 20220727.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20090902-idf-20220727.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20090902-idf-20220727.md)

**Pflichtmodule (3):**
- Masterarbeit
- Seminar zur Masterarbeit
- asterarbet

### FPOSozialökonomik 20240807 i.d.F. 20241122.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20240807-idf-20241122.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20240807-idf-20241122.md)

**Pflichtmodule (3):**
- Masterarbeit
- Seminar zur Masterarbeit
- asterarbet

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

### MA FPOWiPäd 20230615 i.d.F. 20260213.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/ma-fpowipaed-20230615-idf-20260213.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/ma-fpowipaed-20230615-idf-20260213.md)

**Pflichtmodule (3):**
- Masterarbeit
- S SWS d ECTSPk
- umme un -unte

### MSc Finance Auditing Controlling Taxation FPOFACT 20090720 i.d.F. 20191120.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20090720-idf-20191120.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-finance-auditing-controlling-taxation-fpofact-20090720-idf-20191120.md)

**Pflichtmodule (7):**
- Controlling of business systems
- Kapitalmarktorientierte Unternehmens- steuerung
- Versicherungs- und Risikotheorie
- Steuerliche Gewinnermittlung
- Unternehmenssteuerrecht
- Konzernrechnungslegung
- Masterarbeit

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

**Pflichtmodule (3):**
- Masterarbeit
- S SWS d ECTSPk
- umme un -unte

### MSc Marketing FPOMarketing 20090902 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-marketing-fpomarketing-20090902-idf-20180730.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-marketing-fpomarketing-20090902-idf-20180730.md)

**Pflichtmodule (1):**
- Masterarbeit

### MSc Marketing FPOMarketing 20090902 i.d.F. 20191129.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-marketing-fpomarketing-20090902-idf-20191129.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/msc-marketing-fpomarketing-20090902-idf-20191129.md)

**Pflichtmodule (1):**
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

**Pflichtmodule (8):**
- Controlling of business systems
- Kapitalmarktorientierte Unternehmensbesteuerung
- Versicherungs- und Risikotheo- rie
- Steuerliche Gewinnermittlung
- Unternehmenssteuerrecht
- Konzernrechnungslegung
- Masterarbeit
- Versicherungs- und Risikotheorie

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
- Seminar zur Masterarbeit
- Masterareit

### Modulstudien Berufspädagogik POMBPäd 20240807.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/modul-und-zusatzstudien/modulstudien-berufspaedagogik-pombpaed-20240807.md`](../pruefungsordnungen/rw/wiso/modul-und-zusatzstudien/modulstudien-berufspaedagogik-pombpaed-20240807.md)

**Pflichtmodule (7):**
- (2) Grundlagen der Wirtschafts- und Betriebspädagogik
- Schulorganisation und Bildungssystem
- Betriebliche Aus- und Weiterbildung
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Berufspädagogische Vertiefung
- Unterrichtsfach (Zweitfach) inkl. Fachdidaktik

### PDF vom 01.08.2006 i.d.F. 24.02.2010

PO-Quelle: [`pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-neu.md`](../pruefungsordnungen/rw/wiso/po-bachelorstudiengaenge-neu.md)

**Pflichtmodule (2):**
- VWL: Makroökonomie VWL: Mikroökonomie für Sozialökonomie VWL: Wirtschaft und Staat
- VWL: Makroökonomie VWL: Mikroökonomie für Sozialökonom ie VWL: Wirtschaft und Staat

### 6. Juni 2014

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/3aes-wtb-ma-healthbusinessadmin.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/3aes-wtb-ma-healthbusinessadmin.md)

**Pflichtmodule (1):**
- oder

### berufsbegl. WTB MA Health Business Administration PO MHBA 20180706.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20180706.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20180706.md)

**Pflichtmodule (6):**
- Grundlagen des Gesundheits- wesens I: Kostenträger
- oder
- Modul 4: (Pflichtmodul)
- Grundlagen des Gesundheits- wesens II: Leistungserbringer
- Modul 5: (Wahlpflichtmodul)
- Ambulante Versorgung

### berufsbegl. WTB MA Health Business Administration PO MHBA 20231207 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20231207-idf-20240926.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20231207-idf-20240926.md)

**Pflichtmodule (3):**
- Grundlagen des Gesundheitswesens I: Kostenträger
- oder
- Fernstudium

### berufsbegl. WTB MA Health Business Administration PO MHBA 20231207.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20231207.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-ma-health-business-administration-po-mhba-20231207.md)

**Pflichtmodule (3):**
- Grundlagen des Gesundheitswesens I: Kostenträger
- oder
- Fernstudium

### berufsbegl WTB MBA Business Management PO MBA 20200902.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-mba-business-management-po-mba-20200902.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-mba-business-management-po-mba-20200902.md)

**Pflichtmodule (1):**
- ETPk

### berufsbegl WTB MBA Business Management und MBA Global Business Management PO MBA BM-GBM 20230615 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-mba-business-management-und-mba-global-business-management-po-mba-bm-gbm-20230615-idf.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/berufsbegl-wtb-mba-business-management-und-mba-global-business-management-po-mba-bm-gbm-20230615-idf.md)

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

**Pflichtmodule (4):**
- Grundlagen des Gesund- heitswesens I: Kostenträger
- Modul 4: (Pflichtmodul)
- Grundlagen des Gesund- heitswesens II: Leistungserbringer
- Modul 5: (Wahlpflichtmodul)

### PDF vom 13.11.2013

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/pro-wtb-mba-neu.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/pro-wtb-mba-neu.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 18.02.2014 i.d.F. 22.07.2015

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/wtb-pro-marketing-management-juli2015.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/wtb-pro-marketing-management-juli2015.md)

**Pflichtmodule (2):**
- Masterarbeit
- Berufspraxis

### PDF vom 18.02.2014

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/wtb-pro-marketing-management.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/wtb-pro-marketing-management.md)

**Pflichtmodule (2):**
- Pflichtmodul:
- Marketing- und Vertriebs- Strategie

### BSc Artificial Intelligence FPOBScAI 20240328 i.d.F. 20250616.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/artificial-intelligence-in-biomedical-engineering/bsc-artificial-intelligence-fpobscai-20240328-idf-20250616.md`](../pruefungsordnungen/technische-fakultaet/artificial-intelligence-in-biomedical-engineering/bsc-artificial-intelligence-fpobscai-20240328-idf-20250616.md)

**Pflichtmodule (13):**
- Algorithms, programming, and data representation
- Data Engineering
- Applied Programming
- Computational Complexity
- Einführung in das Software Engineering
- Mathematics for Data Science 1
- Mathematics for Data Science 2
- Probability and Stochastic Processes
- Artificial Intelligence Perspectives
- Artificial Intelligence Fundamentals 1
- Logic and Symbolic Artificial Intelligence
- Artificial Intelligence Fundamentals 2
- Ethics and Philosophy of AI (Hauptseminar)

### BSc Artificial Intelligence FPOBScAI 20240328.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/artificial-intelligence-in-biomedical-engineering/bsc-artificial-intelligence-fpobscai-20240328.md`](../pruefungsordnungen/technische-fakultaet/artificial-intelligence-in-biomedical-engineering/bsc-artificial-intelligence-fpobscai-20240328.md)

**Pflichtmodule (14):**
- Algorithms, programming, and data representation
- Data Engineering
- Applied Programming
- Computational Complexity
- Einführung in das Software Engineering
- Mathematics for Data Science 1
- Mathematics for Data Science 2
- Probability and Stochastic Processes
- Artificial Intelligence Perspectives
- Artificial Intelligence Fundamentals 1
- Logic and Symbolic Artificial Intelligence
- Artificial Intelligence Fundamentals 2
- Ethics and Philosophy of AI (Hauptseminar)
- Artificial Intelligence Fundamentals2

### 3. Juli 2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/3aes-ba-ma-chemicaleng-nct.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/3aes-ba-ma-chemicaleng-nct.md)

**Pflichtmodule (3):**
- Masterarbeit mit Referat
- Umfang ca. 900
- Masterarbeit mit Reerat

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

**Pflichtmodule (30):**
- rungsprüfung (GOP)
- Mathematik für CBI 1
- Allgemeine und Anorganische Chemie
- Experimentalphysik
- Konstruktionslehre
- Messtechnik: Sensorik und Messver- fahren
- Chemische und Biologische Prozess- technik
- Wahlmodul aus dem Angebot der FAU
- Mathematik für CBI 2
- Physikalische Chemie
- Mathematik für CBI 3
- Organische Chemie
- Technische Thermodynamik
- Mikrobiologie
- Biochemie
- Reaktionstechnik
- Strömungsmechanik
- Wissenschaftliches Rechnen
- Wärme- und Stoffübertragung
- Chemische Thermodynamik
- Wahlpflichtmodul 1
- Wahlpflichtmodul 2
- Mechanische Verfahrenstechnik
- Thermische Verfahrenstechnik
- Bioreaktions- und Bioverfahrenstechnik
- Praktikum CBI 1
- Praktikum CBI 2
- Prozessmaschinen und Anlagenbau
- Bachelorarbeit
- Hauptseminar

### BSc MSc Chemical Engineering FPOCEN 20230426 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/bsc-msc-chemical-engineering-fpocen-20230426-aes.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/bsc-msc-chemical-engineering-fpocen-20230426-aes.md)

**Pflichtmodule (2):**
- (GOP)
- Masterarbeit mit Hauptseminar

### BSc-MSc Energietechnik FPOET 20220411 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/bsc-msc-energietechnik-fpoet-20220411-aes.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/bsc-msc-energietechnik-fpoet-20220411-aes.md)

**Pflichtmodule (1):**
- Referat

### FPO-BA-MA ChemEngin-NachhaltigeChemTechn 20110607 i.d.F. 20230426.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-20110607-idf-20230426.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-20110607-idf-20230426.md)

**Pflichtmodule (2):**
- Masterarbeit mit Hauptse- minar
- Masterarbeit mit Hauptseminar

### PDF vom 07.06.2011 i.d.F. 26.01.2016

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-jan2016.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-jan2016.md)

**Pflichtmodule (3):**
- Masterarbeit mit Referat
- Umfang ca.
- Masterarbeit mit Reerat

### PDF vom 07.06.2011 i.d.F. 03.07.2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-juli2015.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-juli2015.md)

**Pflichtmodule (3):**
- Masterarbeit mit Referat
- Umfang ca.
- Masterarbeit mit Reerat

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
- SWS (semester hours)

### BSc-MSc Autonomy Technologies FPO AT 20230426 i.d.F. 20240430 en.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20240430-en.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20240430-en.md)

**Pflichtmodule (1):**
- SWS (semester hours)

### BSc-MSc Autonomy Technologies FPO AT 20230426 i.d.F. 20240430.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20240430.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20240430.md)

**Pflichtmodule (16):**
- Human-centered Mechatronics and Robotics
- Robot Mechanisms and User Interfaces
- Human Computer Interaction
- Intent Detection and Feedback
- Digital Communications
- Information Theoryand Coding
- MIMO Communication Systems
- Machine Learningin Communications
- Robotics I
- Nonlinear Control Systems
- Numerical optimization and modelpredictive control
- Introduction to DeepLearning
- Radar,RFID and Wireless Sensor Systems
- Statistical Signal Processing
- Image,Video,and Multidimensional Signal Processing
- Machine Learningin Signal Processing

### BSc-MSc Autonomy Technologies FPO AT 20230426 i.d.F. 20241219 en.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20241219-en.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20241219-en.md)

**Pflichtmodule (1):**
- SWS (semester hours)

### BSc-MSc Autonomy Technologies FPO AT 20230426 i.d.F. 20241219.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20241219.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426-idf-20241219.md)

**Pflichtmodule (16):**
- Human-centered Mechatronics and Robotics
- Robot Mechanisms and User Interfaces
- Human Computer Interaction
- Intent Detection and Feedback
- Digital Communications
- Information Theoryand Coding
- MIMO Communication Systems
- Machine Learningin Communications
- Robotics I
- Nonlinear Control Systems
- Numerical optimization and modelpredictive control
- Introduction to DeepLearning
- Radar,RFID and Wireless Sensor Systems
- Statistical Signal Processing
- Image,Video,and Multidimensional Signal Processing
- Machine Learningin Signal Processing

### BSc-MSc Autonomy Technologies FPO AT 20230426.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/bsc-msc-autonomy-technologies-fpo-at-20230426.md)

**Pflichtmodule (16):**
- Human-centered Mechatronics and Robotics
- Robot Mechanisms and User Interfaces
- Human Computer Interaction
- Intent Detection and Feedback
- Digital Communications
- Information Theoryand Coding
- MIMO Communication Systems
- Machine Learningin Communications
- Robotics I
- Nonlinear Control Systems
- Numerical optimization and modelpredictive control
- Introduction to DeepLearning
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

### FPOCME 20250320.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/fpocme-20250320.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/fpocme-20250320.md)

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

### 24. Juli 2014

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/6aes-ba-ma-computengineering.md`](../pruefungsordnungen/technische-fakultaet/informatik/6aes-ba-ma-computengineering.md)

**Pflichtmodule (2):**
- Masterarbeit
- SummeECTS

### 7. Oktober 2013

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/7aes-ba-ma-informatik.md`](../pruefungsordnungen/technische-fakultaet/informatik/7aes-ba-ma-informatik.md)

**Pflichtmodule (17):**
- (4) Grundlagen der Technischen Informatik
- (2) Parallele und funktionale Programmierung
- Grundlagen der Rechnerarchitektur und -organisation
- (2) Grundlagen der Schaltungstechnik
- (4) Systemprogrammierung
- (2) Grundlagen der Logik und Logikprogrammierung
- (2) Softwareentwicklungin Großprojekten
- (4) Berechenbarkeit und Formale Sprachen
- (4) Theorie der Programmierung
- (2) Rechnerkommunikation
- (4) Algorithmik kontinuierlicher Systeme
- (2) Implementierungvon Datenbanksystemen
- Seminar (Schlüsselqualifikation)
- (4) Mathematik für INF 11)
- (4) Mathematik für INF 21)
- (4) Mathematik für INF 31)
- (4) Mathematik für INF 41)

### 4. August 2014

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/8aes-ba-ma-informatik.md`](../pruefungsordnungen/technische-fakultaet/informatik/8aes-ba-ma-informatik.md)

**Pflichtmodule (22):**
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
- Mathematik für INF 11)
- Mathematik für INF 21)
- Mathematik für INF 31)
- Mathematik für INF 41)
- Bachelorarbeit
- chelorarbeit
- PfP: PL (K, 90 min.) und SL
- m, zusätzlich K, 60 min., wenn „Data Warehousing“ gewähltwird
- PfP: PL (K, 90 min.) und SL (ÜbL)

### BA-MA-Medizintechnik FPOMT 20090915 i.d.F. 20180828 en.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20180828-en.md`](../pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20180828-en.md)

**Pflichtmodule (4):**
- ECTS credits
- Foundations of anatomy and physiology for non-medical stu- dents
- Medical engineering I (bio- materials)
- Material surfaces in medicine

### BA-MA-Medizintechnik FPOMT 20090915 i.d.F. 20180828.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20180828.md`](../pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20180828.md)

**Pflichtmodule (10):**
- Grundlagen der Anatomie und Physiologie für Nichtmediziner
- Pattern Recognition
- Pattern Analysis
- Signale und Systeme II
- Passive Bauelemente und deren HF-Verhalten
- Schaltungstechnik
- Regelungstechnik A (Grundlagen)
- Medizinelektronik
- Medizintechnik I (Biomaterialien)
- Werkstoffoberflächen in der Medizin/Material Surfaces in Medicine

### BA-MA-Medizintechnik FPOMT 20090915 i.d.F. 20190710 en.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20190710-en.md`](../pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20190710-en.md)

**Pflichtmodule (6):**
- Foundations of anatomy and physiology for non-medical stu- dents
- ECTS credits
- Pattern recognition
- Pattern analysis
- Medical engineering I (bio- materials)
- Material surfaces in medicine

### BA-MA-Medizintechnik FPOMT 20090915 i.d.F. 20190710.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20190710.md`](../pruefungsordnungen/technische-fakultaet/informatik/ba-ma-medizintechnik-fpomt-20090915-idf-20190710.md)

**Pflichtmodule (11):**
- Grundlagen der Anatomie und Physiologie für Nichtmediziner
- Pattern Recognition
- Pattern Analysis
- Obligatorisch nachzuweisende Module
- Signale und Systeme II
- Passive Bauelemente und deren HF-Verhalten
- Schaltungstechnik
- Regelungstechnik A (Grundlagen)
- Medizinelektronik
- Medizintechnik I (Biomaterialien)
- Werkstoffoberflächen in der Medizin/Material Surfaces in Medicine

### berufsbegl BSc Informatik-IT-Sicherheit BPOITS 20150116 i.d.F. 20190815.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/berufsbegl-bsc-informatik-it-sicherheit-bpoits-20150116-idf-20190815.md`](../pruefungsordnungen/technische-fakultaet/informatik/berufsbegl-bsc-informatik-it-sicherheit-bpoits-20150116-idf-20190815.md)

**Pflichtmodule (23):**
- Grundlagen der Programmierung
- Programmierkonzepte
- Mathematik 1
- Konzeptionelle Modellierung
- Mathematik 2
- Mathematik 2b
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
- Kolloquium

### BSc-MSc Computational Engineering 20070919 i.d.F. 20180116.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180116.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180116.md)

**Pflichtmodule (27):**
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
- (5) Statik,Elastostatik und Festigkeitslehre
- (3) Dynamik starrer Körper
- (3) Technische Thermodynamik I
- (3) Technische Thermodynamik II
- (2) Strömungsmechanik I
- (3) Wärme- und Stoffübertragung
- Masterarbeit
- SummeECTS

### BSc-MSc Computational Engineering 20070919 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180730.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180730.md)

**Pflichtmodule (27):**
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
- (5) Statik,Elastostatik und Festigkeitslehre
- (3) Dynamik starrer Körper
- (4) Experimentalphysik 3: Optik und Quanteneffekte
- (2) Moderne Optik I: Fortgeschrittene Optik
- (2) Photonik 1
- (2) Photonik 2
- Masterarbeit
- SummeECTS

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

### BSc-MSc Computational Engineering FPOCE 20070919 i.d.F. 20220421.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20070919-idf-20220421.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20070919-idf-20220421.md)

**Pflichtmodule (46):**
- Grundlagen der Programmierung (GOP)
- Grundlagen der Logik in der Informatik
- Einführungin die Algorithmik(GOP)
- (4) Computational Engineering1(GOP)
- (2) Systemprogrammierung
- (2) Simulation und Modellierung1
- (2) Simulation und wissenschaftliches Rechnen 1
- (2) Simulation und wissenschaftliches Rechnen 2
- Mathematik
- (4) Mathematik für CE 11) (GOP)
- (6) Mathematik für CE 21) (GOP)
- (2) Mathematik für CE 31)
- (2) Mathematik für CE 41)
- (2) Numerik I für Ingenieure
- (2) Numerik II für Ingenieure
- Technisches Anwendungsfach (TAF), mind. 35 ECTS-Punkte2)
- (4) Experimentalphysik für Naturwissenschaftler I(GOP)
- (4) Experimentalphysik für Naturwissenschaftler II(GOP)
- (2) Computational Engineering2(GOP)
- (8) TAF – Module3)
- (10) Technische Wahlmodule, max. 17,5 ECTS- Punkte4)
- Bachelorarbeit
- Technisches Anwendungsfach
- Einführungin die Regelungstechnik1
- Regelungstechnisches Praktikum für CE
- Regelungstechnik B(Zustandsraummethoden)
- (2) Digitale Regelung
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
- (5) Statik,Elastostatik und Festigkeitslehre
- (3) Dynamik starrer Körper
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

### BSc-MSc Computational Engineering FPOCE 20250604.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20250604.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20250604.md)

**Pflichtmodule (46):**
- Grundlagen der Programmierung (GOP)
- Grundlagen der Logik in der Informatik
- Einführungin die Algorithmik(GOP)
- (4) Computational Engineering1(GOP)
- (2) Systemprogrammierung
- (2) Simulation und Modellierung1
- (2) Simulation und wissenschaftliches Rechnen 1
- (2) Simulation und wissenschaftliches Rechnen 2
- Mathematik
- (4) Mathematik für CE 11) (GOP)
- (6) Mathematik für CE 21) (GOP)
- (2) Mathematik für CE 31)
- (2) Mathematik für CE 41)
- (2) Numerik I für Ingenieure
- (2) Numerik II für Ingenieure
- Technisches Anwendungsfach (TAF), mind. 35 ECTS-Punkte2
- (4) Experimentalphysik für Naturwissenschaftler I(GOP)
- (4) Experimentalphysik für Naturwissenschaftler II(GOP)
- (2) Computational Engineering2(GOP)
- (8) TAF – Module3)
- (10) Technische Wahlmodule, max. 17,5 ECTS-Punkte4)
- Bachelorarbeit
- Technisches Anwendungsfach
- Einführungin die Regelungstechnik1
- Regelungstechnisches Praktikum für CE
- Regelungstechnik B(Zustandsraummethoden)
- (2) Digitale Regelung
- Grundlagen der Elektrotechnik I
- Grundlagen der Elektrotechnik III
- Sensorik
- (2) Einführung in die Grundlagen der Elektrotechnik für CE- Studierende
- Signale und Systeme I
- Signale und Systeme II
- (3) Information Theory and Coding/Informationstheorie und Codierung
- (3) Digitale Signalverarbeitung
- (3) Technische Thermodynamik I
- (3) Technische Thermodynamik II
- (2) Strömungsmechanik I
- (3) Wärme- und Stoffübertragung
- (5) Statik, Elastostatik und Festigkeitslehre
- (3) Dynamik starrer Körper
- (4) Experimentalphysik 3: Optik und Quanteneffekte
- (2) Moderne Optik I: Fortgeschrittene Optik
- (2) Photonik 1
- (2) Photonik 2
- Masterarbeit

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20180801.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20180801.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20180801.md)

**Pflichtmodule (24):**
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
- Mathematik für INF 11)
- Mathematik für INF 21)
- Mathematik für INF 31)
- Mathematik für INF 41)
- Bachelorarbeit
- chelorarbeit
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- m, zusätzlich K, 60 Min., wenn „Data Warehousing“ gewählt wird
- PL (K, 90 Min.) und SL (ÜbL)

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20190306.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20190306.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20190306.md)

**Pflichtmodule (23):**
- Grundlagen der Technischen Informatik
- Grundlagen der Technischen Informatik UE
- Parallele und funktionale Programmierung
- Parallele und funktionale ProgrammierungUE
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Rechnerarchitektur und -organisation UE
- Grundlagen der Schaltungs- technik
- Grundlagen der Schaltungstechnik UE
- Systemprogrammierung
- Systemprogrammierung UE
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik in der Informa- tik UE
- Softwareentwicklung in Großprojekten
- Softwareentwicklung in Großprojekten UE
- Berechenbarkeit und Formale Sprachen
- Berechenbarkeit und Formale Spra- chen UE
- Bachelorarbeit
- Masterarbeit
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- PL (K, 90 Min.) und SL (ÜbL)
- m, 30 Min. oder K, 90 Min. und SL(ÜbL)

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20191203.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20191203.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20191203.md)

**Pflichtmodule (23):**
- Grundlagen der Technischen Informatik
- Grundlagen der Technischen Informatik UE
- Parallele und funktionale Programmierung
- Parallele und funktionale ProgrammierungUE
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Rechnerarchitektur und -organisation UE
- Grundlagen der Schaltungs- technik
- Grundlagen der Schaltungstechnik UE
- Systemprogrammierung
- Systemprogrammierung UE
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik in der Informa- tik UE
- Softwareentwicklung in Großprojekten
- Softwareentwicklung in Großprojekten UE
- Berechenbarkeit und Formale Sprachen
- Berechenbarkeit und Formale Spra- chen UE
- Bachelorarbeit
- Masterarbeit
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- PL (K, 90 Min.) und SL (ÜbL)
- m, 30 Min. oder K, 90 Min. und SL(ÜbL)

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20200820.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20200820.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20200820.md)

**Pflichtmodule (29):**
- Grundlagen der Programmie- rung
- Grundlagen der Programmierung UE
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik in der Informatik UE
- Sichere Systeme
- Sichere Systeme UE
- Grundlagen der Technischen Informatik
- Grundlagen der Technischen Informatik UE
- Einführung in die Algorithmik
- Einführung in die Algorithmik UE
- Systemprogrammierung
- Systemprogrammierung UE
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Rechnerarchitektur und -organisation UE
- Rechnerkommunikation
- Rechnerkommunikation UE
- Parallele und funktionale Programmierung
- Parallele und funktionale ProgrammierungUE
- Softwareentwicklung in Großprojekten
- Softwareentwicklung in Großprojekten UE
- Berechenbarkeit und Formale Sprachen
- Berechenbarkeit und Formale Sprachen UE
- Bachelorarbeit
- Masterarbeit
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- PL (K, 90 Min.) und SL (ÜbL)
- m, 30 Min. oder K, 90 Min. und SL(ÜbL)

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20210701.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20210701.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20210701.md)

**Pflichtmodule (30):**
- Grundlagen der Programmie- rung
- Grundlagen der Programmierung UE
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik in der Informatik UE
- Sichere Systeme
- Sichere Systeme UE
- Grundlagen der Technischen Informatik
- Grundlagen der Technischen Informatik UE
- Einführung in die Algorithmik
- Einführung in die Algorithmik UE
- Systemprogrammierung
- Systemprogrammierung UE
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Rechnerarchitektur und -organisation UE
- Rechnerkommunikation
- Rechnerkommunikation UE
- Parallele und funktionale Programmierung
- Parallele und funktionale ProgrammierungUE
- Softwareentwicklung in Großprojekten
- Softwareentwicklung in Großprojekten UE
- Berechenbarkeit und Formale Sprachen
- Berechenbarkeit und Formale Sprachen UE
- Bachelorarbeit
- Masterarbeit
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- PL (K, 90 Min.) und SL (ÜbL)
- m, 30 Min. oder K, 90 Min. und SL(ÜbL)
- K, 60/90 Min. oder m, 30 Min.

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20220301.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20220301.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20220301.md)

**Pflichtmodule (33):**
- Grundlagen der Program- mierung
- Grundlagen der Programmierung UE
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik in der Informatik UE
- Sichere Systeme
- Sichere Systeme UE
- Grundlagen der Technischen Informatik
- Grundlagen der Technischen Informatik UE
- Einführung in die Algorithmik
- Einführung in die Algorithmik UE
- Systemprogrammierung
- Systemprogrammierung UE
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Rechnerarchitektur und -organisation UE
- Rechnerkommunikation
- Rechnerkommunikation UE
- Parallele und funktionale Programmierung
- Parallele und funktionale ProgrammierungUE
- Softwareentwicklung in Großprojekten
- Softwareentwicklung in Großprojek- ten UE
- Bachelorarbeit
- Masterarbeit
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

**Pflichtmodule (34):**
- Grundlagen der Programmie- rung
- Grundlagen der Programmierung UE
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik in der Informatik UE
- Sichere Systeme
- Sichere Systeme UE
- Grundlagen der Technischen Informatik
- Grundlagen der Technischen Informatik UE
- Einführung in die Algorithmik
- Einführung in die Algorithmik UE
- Systemprogrammierung
- Systemprogrammierung UE
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Rechnerarchitektur und -organisation UE
- Rechnerkommunikation
- Rechnerkommunikation UE
- Parallele und funktionale Programmierung
- Parallele und funktionale ProgrammierungUE
- Einführung in das Software Engineering
- Einführung in das Software Enginee- ringUE
- Bachelorarbeit
- Masterarbeit
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

**Pflichtmodule (33):**
- Grundlagen der Programmie- rung
- Grundlagen der Programmierung UE
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik in der InformatikUE
- Sichere Systeme
- Sichere Systeme UE
- Grundlagen der Technischen Informatik
- Grundlagen der Technischen InformatikUE
- Einführung in die Algorithmik
- Einführung in die Algorithmik UE
- Systemprogrammierung
- Systemprogrammierung UE
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Rechnerarchitektur und-organisationUE
- Rechnerkommunikation
- Rechnerkommunikation UE
- Parallele und funktionale Programmierung
- Parallele und funktionale Programmierung UE
- Einführung in das Software Engineering
- Bachelorarbeit
- Masterarbeit
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

**Pflichtmodule (37):**
- Grundlagen der Technischen Informatik
- Grundlagen der Technischen Informatik UE
- Parallele und funktionale Programmierung
- Parallele und funktionale ProgrammierungUE
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Rechnerarchitektur und -organisation UE
- Grundlagen der Schaltungs- technik
- Grundlagen der Schaltungstechnik UE
- Systemprogrammierung
- Systemprogrammie- rungUE
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik in der Informatik UE
- Softwareentwicklung in Großprojekten
- Softwareentwicklung in Großprojekten UE
- Berechenbarkeit und Formale Sprachen
- Berechenbarkeit und Formale Sprachen UE
- Theorie der Programmierung
- Theorie der Program- mierungUE
- Rechnerkommunikation
- Rechnerkommunika- tion UE
- Algorithmik kontinuierlicher Systeme
- Algorithmik kontinuier- licher Systeme UE
- Implementierung von Daten- banksystemen
- Implementierung von Datenbanksystemen UE
- Hauptseminar (Schlüssel- qualifikation)
- Mathematik für INF 12)
- Mhik f INF 1
- Mathematik für INF 22)
- Mathematik für INF 2 V
- Bachelorarbeit
- ECTS-Punkte:
- Masterarbeit
- K60 Min.
- PL (K, 90 Min.) und SL
- PL (K, 90 Min.)
- PL (K, 90 Min.) und SL (ÜbL)
- m, 30 Min. oder K, 90 Min. und SL(ÜbL)

### BSc-MSc Informatik FPOINF 20200820 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20200820-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20200820-aes.md)

**Pflichtmodule (23):**
- Grundlagen der Programmie- rung
- Grundlagen der Programmierung UE
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik in der Informatik UE
- Sichere Systeme
- Sichere Systeme UE
- Grundlagen der Technischen Informatik
- Grundlagen der Technischen Informatik UE
- Einführung in die Algorithmik
- Einführung in die Algorithmik UE
- Systemprogrammierung
- Systemprogrammierung UE
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Rechnerarchitektur und -organisation UE
- Rechnerkommunikation
- Rechnerkommunikation UE
- Parallele und funktionale Programmierung
- Parallele und funktionale ProgrammierungUE
- Softwareentwicklung in Großprojekten
- Softwareentwicklung in Großprojekten UE
- Berechenbarkeit und Formale Sprachen
- Bachelorarbeit
- Masterarbeit

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

### BSc-MSc Informatik FPOINF 20240328 iF 20250604.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328-if-20250604.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328-if-20250604.md)

**Pflichtmodule (31):**
- Grundlagen der Programmierung
- Grundlagen der Programmierung UE
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik in der InformatikUE
- Sichere Systeme
- Sichere Systeme UE
- Grundlagen der Technischen Informatik
- Grundlagen der Technischen InformatikUE
- Einführung in die Algorithmik
- Einführung in die Algorithmik UE
- Systemprogrammierung
- Systemprogrammierung UE
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Rechnerarchitektur und-organisationUE
- Rechnerkommunikation
- Rechnerkommunikation UE
- Parallele und funktionale Programmierung
- Parallele und funktionale ProgrammierungUE
- Bachelorarbeit
- Masterarbeit
- PL (K, 60 Min.)
- PL (K, 90 Min.) und SL(ÜbL)
- PL (K, 90 Min.)
- PL (m, 30 Min. oder K,90 Min.)
- PL (m, 30 Min. oder K, 90 Min.) und SL(ÜbL)
- PL (m, 30 Min.)
- PL (K, 90 Min. oder m,30 Min.)
- PL (K, 60/90 Min. oder m,30 Min.)
- PL (K, 60 Min.) und SL(ÜbL)
- PL (K, 90 Min oder m,30 Min.)
- PL (K, 90 Min)

### BSc-MSc Informatik FPOINF 20240328 iF 20260115.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328-if-20260115.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328-if-20260115.md)

**Pflichtmodule (13):**
- Masterarbeit
- S SWS d ECTSPk
- ummen un -unte:
- PL (K, 60 Min.)
- PL (K, 90 Min.)und SL(ÜbL)
- PL (K, 90 Min.)
- PL (m, 30 Min._oder_ K,90 Min.)
- PL (m, 30 Min._oder_ K, 90 Min.)und SL(ÜbL)
- PL (K, 120 Min._oder_m, 30 Min.)
- PL (K, 90 Min._oder_ m,30 Min.)
- PL (K, 60/90 Min._oder_ m,30 Min.)
- PL (K, 60 Min._oder_m, 30 Min.)und SL (ÜbL)
- PL (K, 90 Min)

### BSc-MSc Informatik FPOINF 20240328.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328.md)

**Pflichtmodule (31):**
- Grundlagen der Programmierung
- Grundlagen der Programmierung UE
- Grundlagen der Logik in der Informatik
- Grundlagen der Logik in der InformatikUE
- Sichere Systeme
- Sichere Systeme UE
- Grundlagen der Technischen Informatik
- Grundlagen der Technischen InformatikUE
- Einführung in die Algorithmik
- Einführung in die Algorithmik UE
- Systemprogrammierung
- Systemprogrammierung UE
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Rechnerarchitektur und-organisationUE
- Rechnerkommunikation
- Rechnerkommunikation UE
- Parallele und funktionale Programmierung
- Parallele und funktionale Programmierung UE
- Bachelorarbeit
- Masterarbeit
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

### BSc-MSc-Medizintechnik FPOMT 20090915 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20230731.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-medizintechnik-fpomt-20090915-idf-20230731.md)

**Pflichtmodule (13):**
- Bachelorarbeit
- Hauptseminar Bachelorarbeit
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

**Pflichtmodule (11):**
- Obligatorisch nachzuweisende Module
- Grundlagen der Anatomie und Physiologie für Nichtmediziner
- Pattern Recognition
- Pattern Analysis
- Signale und Systeme II
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
- Mathematik für CE 4~~1)~~ (5 ECTS) Numerik 2 (mind.5ECTS)
- Mathematik für CE 3~~1)~~ (5 ECTS) Numerik 1 (mind. 5 ECTS)
- Mathematik für CE 2~~1)~~ (10 ECTS)
- Mathematik für CE 1~~1)~~ (7.5 ECTS)
- Mathematik fest

### PDF vom 19.09.2007 i.d.F. 29.07.2013

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-juli2013.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-juli2013.md)

**Pflichtmodule (6):**
- Simulation und wissenschaftliches Rechnen 1 (7.5 ECTS) Simulation and Modeling 1 (5 ECTS)
- Mathematik für CE 4~~1)~~ (5 ECTS) Numerik 2 (mind.5ECTS)
- Mathematik für CE 3~~1)~~ (5 ECTS) Numerik 1 (mind. 5 ECTS)
- Mathematik für CE 2~~1)~~ (10 ECTS)
- Mathematik für CE 1~~1)~~ (7.5 ECTS)
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

**Pflichtmodule (3):**
- PfP: PL (K, 90 min.) und SL
- m, zusätzlich K, 60 min., wenn „Data Warehousing“ gewähltwird
- PfP: PL (K, 90 min.) und SL(ÜbL)

### PDF vom 21.09.2007 i.d.F. 31.07.2012

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-juli2012.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-juli2012.md)

**Pflichtmodule (1):**
- unbenoteter Schein

### PDF vom 21.09.2007 i.d.F. 11.06.2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-juni2015.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-juni2015.md)

**Pflichtmodule (3):**
- PfP: PL (K, 90 min.) und SL
- m, zusätzlich K, 60 min., wenn „Data Warehousing“ gewähltwird
- PfP: PL (K, 90 min.) und SL(ÜbL)

### PDF vom 21.09.2007 i.d.F. 08.10.2012

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-oktober2012.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-oktober2012.md)

**Pflichtmodule (1):**
- unbenoteter Schein

### PDF vom 21.09.2007 i.d.F. 07.10.2013

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-oktober2013.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik-oktober2013.md)

**Pflichtmodule (1):**
- unbenoteter Schein

### PDF vom 21.09.2007 i.d.F. 07.07.2010

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-informatik.md)

**Pflichtmodule (1):**
- unbenoteter Schein

### FPOAI 20201111 i.d.F. 20220726.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111-idf-20220726.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111-idf-20220726.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOAI 20201111 i.d.F. 20230323.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111-idf-20230323.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111-idf-20230323.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOAI 20201111.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpoai-20201111.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOMScAI 20240328 i.d.F. 20260213.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpomscai-20240328-idf-20260213.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpomscai-20240328-idf-20260213.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOMScAI 20240328.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpomscai-20240328.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpomscai-20240328.md)

**Pflichtmodule (1):**
- Masterarbeit

### 24. Juli 2014

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/maschinenbau/10aes-ba-ma-wing.md`](../pruefungsordnungen/technische-fakultaet/maschinenbau/10aes-ba-ma-wing.md)

**Pflichtmodule (15):**
- BWL für Ingenieure
- Statistik
- Buchführung
- Mathematik für WING 1~~1)~~ Übung
- EinführungindieIuK-Technik
- Mathematik für WING 2~~1)~~ Ü
- bung
- Praktikum Software für die Mathematik
- Elektronik und Schaltungstechnik
- Praktikum Elektronik und Schaltungstechnik
- Nachrichtentechnische Systeme
- Wahlpflichtmodul 2
- Technisches Wahlmodul
- Hochschulpraktikum
- Wirtschaftswissen- schaftlicher Bereich

### BA-MA FPOWING 20070925 i.d.F. 20180515.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20070925-idf-20180515.md`](../pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20070925-idf-20180515.md)

**Pflichtmodule (3):**
- BWL für Ingenieure
- Statistik
- Buchführung

### BA-MA FPOWING 20070925 i.d.F. 20190815.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20070925-idf-20190815.md`](../pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20070925-idf-20190815.md)

**Pflichtmodule (3):**
- BWL für Ingenieure
- Statistik
- Buchführung

### BA-MA FPOWING 20180515 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20180515-aes.md`](../pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20180515-aes.md)

**Pflichtmodule (19):**
- Mathematik für WING11)
- StatikundFestigkeitslehre
- Mathematik für WING21)
- Mathematik für WING 3 1)
- Dynamikstarrer Körper
- Technische Darstellungslehre I
- Technische DarstellungslehreII
- Grundlagen der Produktentwicklung
- Konstruktionstechnisches Praktikum
- Grundlagender Informatik
- Wirtschaftswissen-
- schaftlicher Bereich
- BWL für Ingenieure
- Statistik
- Buchführung
- Überfakultärer Bereich
- Bachelorarbeit
- GOP =Grundlagen-und Orientierungsprüfung
- K = Katalog von Modulen zur Zulassung für das Masterstudium

### PDF vom 25.09.2007 i.d.F. 24.07.2014

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/maschinenbau/fpo-ba-ma-wing-juli2014.md`](../pruefungsordnungen/technische-fakultaet/maschinenbau/fpo-ba-ma-wing-juli2014.md)

**Pflichtmodule (24):**
- Mathematik für WING 1~~1)~~
- Statik und Festigkeitslehre
- Mathematik für WING 2~~1)~~
- Dynamikstarrer Körper
- Technische Darstellungslehre I
- Technische Darstellungslehre II
- Grundlagen der Produktentwicklung
- Konstruktionsübung
- Grundlagender Informatik
- Wahlpflichtmodul 2
- Technisches Wahlmodul
- Hochschulpraktikum
- Wirtschaftswissenschaftlicher Bereich
- BWL für Ingenieure
- Statistik
- Buchführung
- Mathematik für WING1~~1)~~
- EinführungindieIuK-Technik
- Mathematik für WING 21)
- bung
- PraktikumSoftwarefürdieMathematik
- Elektronik und Schaltungstechnik
- Praktikum Elektronik und Schaltungstechnik
- Nachrichtentechnische Systeme

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

### BSc MSc FPOMWT 20070925 i.d.F. 20200306.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/bsc-msc-fpomwt-20070925-idf-20200306.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/bsc-msc-fpomwt-20070925-idf-20200306.md)

**Pflichtmodule (2):**
- Referat
- SWS und ETCS-Punkte:

### BSc-MSc FPOMWT 20200306 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/bsc-msc-fpomwt-20200306-aes.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/bsc-msc-fpomwt-20200306-aes.md)

**Pflichtmodule (2):**
- Hauptseminar Bachelorarbeit
- Referat

### Elite-MA Advanced Materials and Processes FPO MAP 20060515 i.d.F. 20190115.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-20060515-idf-20190115.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-20060515-idf-20190115.md)

**Pflichtmodule (1):**
- Masterarbeit

### Elite-MA Advanced Materials and Processes FPO MAP-M 20190115 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-m-20190115-aes.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-m-20190115-aes.md)

**Pflichtmodule (1):**
- Masterarbeit
