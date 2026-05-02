---
kind: "campo-pflichtmodule-aus-po"
po_files_with_pflicht_modules: 679
total_pflicht_modules: 5243
scraped_at: 2026-05-02T04:33:11+00:00
---

# Pflichtmodule — direkt aus PO-Anlagen extrahiert

Diese Datei sammelt strukturierte Pflichtmodul-Listen, die wir aus den *Studienverlaufsplan*- und *Curricular-Übersicht*-Tabellen der FAU-Prüfungsordnungen gelesen haben (Markdown-Tables, vom PyMuPDF4LLM-Konverter aus den PDF-Anlagen erzeugt). Pro PO wird die Sektion verfolgt — Module aus Sektionen *Grundlagen*, *Pflichtbereich*, *Basismodule*, *Kernbereich*, *Bachelorarbeit*, *Masterarbeit* gelten als Pflicht. *Wahlpflicht*, *Wahlbereich*, *Aufbaumodule*, *Vertiefungsmodule*, *Schwerpunkte* und *Schlüsselqualifikationen* werden ausgenommen.

## Vorbehalte

* **Vollständigkeit:** ~74 % der PO-Markdown-Dateien enthalten   überhaupt erkennbare Tabellen; davon haben wieder nur ~30 %   klare Pflicht-Section-Marker. Etwa die Hälfte aller POs liefert   hier deshalb noch kein Ergebnis — bei vielen ist die Anlage als   **Bild** im PDF eingebettet (typisches Beispiel: *Curricular-  Übersicht* als Diagramm) und entzieht sich der Text-Extraktion.
* **Modul-Name vs. Veranstaltungs-Titel:** ein Pflichtmodul   *Analysis I* erscheint in Campo als *Vorlesung Analysis I* +   *Übung Analysis I* + *Tafelübung Analysis I*. Hier wird nur das   Modul gelistet; das Cross-Mapping zu Campo-Veranstaltungen   übernimmt die Heuristik in `pflichtveranstaltungen.md` bzw.   ein RAG-Agent zur Anfragezeit.
* **Modul-Reihenfolge:** Module erscheinen in der Reihenfolge des   Studienverlaufsplans (typisch nach Fachsemester sortiert).

**Statistik:** 679 POs lieferten zusammen 5243 eindeutige Pflichtmodul-Einträge.

## Pro PO

### 30. September 2015

PO-Quelle: [`pruefungsordnungen/lehramt/7aes-lapo-allgemein.md`](../pruefungsordnungen/lehramt/7aes-lapo-allgemein.md)

**Pflichtmodule (5):**
- Pädagogik, Didaktik und Methodik in der Mittelschule
- Heterogenität und Inklusion in der Mittelschule
- Spezifische Handlungs- kompetenzen in der Mittel- schule
- Basismodul Berufsorientierung1
- Masterarbeit

### pdf vom 19.02.2009

PO-Quelle: [`pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/sto-po-berufspaedagogik-eei.md`](../pruefungsordnungen/lehramt/berufspaedagogik-und-zusatzstudien/sto-po-berufspaedagogik-eei.md)

**Pflichtmodule (6):**
- Grundlagen der Elektrotechnik, Energie und Antriebstechnik
- Informatik und Mathematik
- Hochfrequenztechnik
- Kommunikationselektronik und Schaltungstechnik
- Systeme und Regelungen
- Seminar und Laborpraktikum aus der Elektro- und Informationstech- nik

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

### 14. September 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aes-la-arbeitslehre.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aes-la-arbeitslehre.md)

**Pflichtmodule (5):**
- Grundlagen der Fachdidaktik (GFD)
- Grundlagen der Fachwissenschaft (GFW)
- Medien und Methoden I (MuM I)
- Medien und Methoden II (MuM II)2
- Arbeit und Beruf

### 26. Juni 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/1aesa-la-mathe.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/1aesa-la-mathe.md)

**Pflichtmodule (17):**
- Analysis I
- Lineare Algebra I
- Analysis II
- Lineare Algebra II
- Angewandte Mathematik
- Stochastische ModellbildungIa
- Stochastische Mo- dellbildung Ib
- Algebra Ia
- Algebra Ib
- Elemente der Linearen Al- gebra I1
- Elemente der Linearen Al- gebra IIa2
- Elemente der Linearen Al- gebra IIb2
- Elemente der Analysis I2
- Elemente der Analysis IIa~~1~~
- Elemente der Analysis IIb1
- Analytische Geometrie1
- Aufbaumodul Analysis2

### 9. Oktober 2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-chemie.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-chemie.md)

**Pflichtmodule (2):**
- Grundlagen der anorga- nisch-chemischen Labor- praxis
- Prüfungsvorbereitung

### 29. September 2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-franzoesisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-franzoesisch.md)

**Pflichtmodule (4):**
- Basismodul Französische Sprachpraxis 1
- Basismodul Französische Sprachpraxis 2
- Basismodul Einführung in die Frankoromanistik
- Basismodul Didaktik der romanischen Sprachen

### 27. September 2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-griechisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-griechisch.md)

**Pflichtmodule (4):**
- Sprachübungen I
- Poesie
- Prosa
- Lektüre

### 29. September 2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-italienisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-italienisch.md)

**Pflichtmodule (3):**
- Basismodul Italienische Sprachpraxis 1
- Basismodul Italienische Sprachpraxis 2
- Basismodul Einführung in die Italoromanistik

### 29. September 2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-spanisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-spanisch.md)

**Pflichtmodule (4):**
- Basismodul Spanische Sprachpraxis 1
- Basismodul Spanische Sprachpraxis 2
- Basismodul Einführung in die Iberoromanistik
- Basismodul Didaktik der romanischen Sprachen

### 27. Februar 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-wirtschaftswiss.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/2aes-la-wirtschaftswiss.md)

**Pflichtmodule (4):**
- Grundlagen der Fachdidaktik Wirtschaftswissenschaft en(Gymnasium)
- Praxisfelder der Fachdidaktik
- Grundlagen der Fachdidaktik Wirtschaftswissenschaft en(Realschule)
- Praxisfelder der Fachdidaktik Wirtschaftswissenschaft en

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

**Pflichtmodule (5):**
- Basismodul Französische Sprachpraxis 1
- Basismodul Französische Sprachpraxis 2
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen

### 8. August 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-italienisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-italienisch.md)

**Pflichtmodule (4):**
- Basismodul Italienische Sprachpraxis 1
- Basismodul Italienische Sprachpraxis 2
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft

### 8. August 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-spanisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/3aesa-fpo-la-spanisch.md)

**Pflichtmodule (5):**
- Basismodul Spanische Sprachpraxis 1
- Basismodul Spanische Sprachpraxis 2
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen

### 2. April 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/4aes-la-griechisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/4aes-la-griechisch.md)

**Pflichtmodule (5):**
- Shüb I
- pracungen
- Poesie
- Prosa
- Sprachübungen II

### 25. Oktober 2016

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/4aesa-la-sozialkunde.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/4aesa-la-sozialkunde.md)

**Pflichtmodule (7):**
- Grundlagen der politi- schen Bildung
- Methodik und Wertorien- tierung im Politikunterricht
- Grundlagen der politischen Bildung
- Methodik, Praxis und Wertorientierung im Politikunterricht
- Methodik und Wertorientierung im Politikunterricht
- Praxis des Politikunterrichts
- Praxisprobleme der Politischen Bil- dung

### 14. Dezember 2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/5aesa-la-ev-religion.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/5aesa-la-ev-religion.md)

**Pflichtmodule (17):**
- Basismodul: Theologie und wissenschaftliches Arbeiten
- Biblisches Grundwissen (Lehramt GS/MS/RS)
- Grundlagen der Theologie und Religionspädagogik
- Biblih Thli 1 AT
- sce eooge ()
- Biblische Theologie 2 (NT)
- Biblih Thli 3
- sce eooge
- Systematische Theologie 1: Dogmatik (GMRS)
- Systematische Theologie 2: Ethik (GMRS)
- Kirchengeschichte 1
- Kihhiht 2
- rcengescce
- Biblische Theologie 1 (AT)
- Biblische Theologie 3
- Kirchengeschichte 2
- Religionswissenschaft

### 16. Januar 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/6aes-la-deutsch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/6aes-la-deutsch.md)

**Pflichtmodule (4):**
- Grundlagen der Germanistischen Linguistik (Ling1)
- Grundlagen der Germanistischen Mediävistik (Med 1)
- Grundlagen der Neueren deutschen Literatur (NdL 1)
- Grundlagen der Fachdidaktik Deutsch (BM FDD)

### 24. September 2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/7aes-la-deutsch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/7aes-la-deutsch.md)

**Pflichtmodule (6):**
- Grundlagen des Deutschen als Zweitsprache
- Sprachsystem und Zweitspracherwerb
- Lehren und Lernen in der zweiten Sprache
- Sprachmodul 1
- Sprachmodul 2
- Praktikumsmodul

### 27. September 2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/7aes-la-englisch.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/7aes-la-englisch.md)

**Pflichtmodule (10):**
- Basismodul I Language
- Basismodul II Liii
- ngustcs
- Basismodul III Literature
- Basismodul IV Culture/Landeskunde
- Zwischenmodul L‐GYM Linguistics
- Zwischenmodul L‐GYM Literature
- Zwischenmodul L‐GYM Language
- Basismodul Englischdidaktik
- Basismodul Language

### 10. November 2016

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/8aes-la-dt-didaz.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/8aes-la-dt-didaz.md)

**Pflichtmodule (11):**
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1) Grundlagen der
- Germanistischen Linguistik 2 (Ling BM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1 (Med BM 1)
- Grundlagen der Germanistischen Mediävistik 2 (Med BM 2)
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
- Grundlagen der Germanistischen Mediävistik 2(Med BM 2)
- Basismodul DiDaZ (LA GS)
- Basismodul DiDaZ (LA MS)

### FPO LA DaZ 20200203 i.d.F. 20201123.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-daz-20200203-idf-20201123.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-daz-20200203-idf-20201123.md)

**Pflichtmodule (9):**
- Basismodul DaZ (LA GS)
- Basismodul DaZ (LA MS)
- Grundlagen des Deutschen als Zweit- sprache
- Sprachsystem und Zithb
- wespracerwer
- Lehren und Lernen in der zweiten Sprache
- Sprachmodul 13
- Sprachmodul 23
- Praktikumsmodul

### FPO LA DaZ 20250702.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-daz-20250702.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-daz-20250702.md)

**Pflichtmodule (1):**
- Basismodul Partnersprache5

### FPO LA DiDaZ 20200203.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-didaz-20200203.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-didaz-20200203.md)

**Pflichtmodule (9):**
- Basismodul DiDaZ (LA GS)
- Basismodul DiDaZ (LA MS)
- Grundlagen des Deutschen als Zweit- sprache
- Sprachsystem und Zithb
- wespracerwer
- Lehren und Lernen in der zweiten Sprache
- Sprachmodul 1
- Sprachmodul 2
- Praktikumsmodul

### FPO LA Mathe 20151111 i.d.F. 20191010.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20191010.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20191010.md)

**Pflichtmodule (7):**
- Analysis I1)
- Lineare Algebra I1)
- Analysis II1)
- Lineare Algebra II1)
- Algebra2)
- Körpertheorie2)
- Analysis für Lehramt

### FPO LA Mathe 20151111 i.d.F. 20201029.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20201029.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20201029.md)

**Pflichtmodule (7):**
- Analysis I1)
- Lineare Algebra I1)
- Analysis II1)
- Lineare Algebra II1)
- Algebra2)
- Körpertheorie2)
- Analysis für Lehramt

### FPO LA Mathe 20151111 i.d.F. 20230426.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20230426.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20151111-idf-20230426.md)

**Pflichtmodule (13):**
- Analysis I1)
- Lineare Algebra I1)
- Analysis II1)
- Lineare Algebra II1)
- Algebra2)
- Körpertheorie2)
- Analysis für Lehramt
- Elemente der Linearen Algebra I1)
- Elemente der Linearen Algebra II2)
- Elemente der Analysis I2)
- Elemente der Analysis II1)
- Analytische Geometrie1)
- Aufbaumodul Analysis2)

### FPO LA Mathe 20260331.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20260331.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/fpo-la-mathe-20260331.md)

**Pflichtmodule (3):**
- Elemente der Analysis II1)
- Analytische Geometrie1)
- Aufbaumodul Analysis2)

### LA Arbeitslehre FPO LA ArbL 20090727 i.d.F. 20190913.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-arbeitslehre-fpo-la-arbl-20090727-idf-20190913.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-arbeitslehre-fpo-la-arbl-20090727-idf-20190913.md)

**Pflichtmodule (5):**
- Grundlagen der Fach- didaktik (GFD)
- Grundlagen der Fach- wissenschaft (GFW)
- Medien und Methoden I (MuM I)
- Medien und Methoden II (MuM II)2
- Arbeit und Beruf (AuB)

### LA Beruf und Wirtschaft FPO LA BuW 20090727 i.d.F. 20210301.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-beruf-und-wirtschaft-fpo-la-buw-20090727-idf-20210301.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-beruf-und-wirtschaft-fpo-la-buw-20090727-idf-20210301.md)

**Pflichtmodule (5):**
- Grundlagen der Fach- wissenschaft (GFW)
- Grundlagen der Fach- didaktik (GFD)
- Medien und Methoden I (MuM I)
- Medien und Methoden II (MuM II)2
- Arbeit und Beruf (AuB)

### LA Chin ÄSa 20260331.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-chin-aesa-20260331.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-chin-aesa-20260331.md)

**Pflichtmodule (1):**
- Basismodul Chinesischdi- daktik

### LA Deutsch FPO LA Deutsch 20090226 i.d.F. 20200203.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20200203.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20200203.md)

**Pflichtmodule (17):**
- Grundlagen der Germanistischen Linguistik 1(LingBM 1)
- Grundlagen der Germanistischen Linguistik 2(LingBM 2)
- Grundlagen der Neueren deut- schen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deut- schen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1 (Med BM 1)
- Grundlagen der Germanistischen Mediävistik 2(MedBM 2)
- Basismodul Fachdidaktik Deutsch (BM FDD)
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

**Pflichtmodule (13):**
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1(MedBM 1)
- Grundlagen der Germanistischen Mediävistik 2(MedBM 2)
- Basismodul Fachdidaktik Deutsch (BM FDD)
- Grundlagen der Neueren deutschen Literatur- wissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literatur- wissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik (Med-BM-LANV)
- Grundlagen der Germanistischen Linguistik 1 (LingBM 1)
- Grundlagen der Germanistischen Linguistik 2 (LingBM 2)
- Grundlagen der Germanistischen Mediävistik(MedBM LANV)

### LA Deutsch FPO LA Deutsch 20090226 i.d.F. 20220914.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20220914.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20090226-idf-20220914.md)

**Pflichtmodule (6):**
- Basismodul Fachdidaktik Deutsch (BM FDD)
- Ling BM-12 Grundlagen der germanisti- schen Linguistik
- NdL BM-14 Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- Ling BM-22 Grundlagen der historischen Linguistik
- NdL BM-24 Grundlagen der Neueren deut- schen Literaturwissenschaft 2
- Med BM nv4 Grundlagen der Germanisti- schen Mediävistik – nicht ver- tieftes LA

### LA Deutsch FPO LA Deutsch 20200203 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20200203-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20200203-aes.md)

**Pflichtmodule (1):**
- Basismodul Fachdidaktik Deutsch (BM FDD)

### LA Deutsch FPO LA Deutsch 20220914 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20220914-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-deutsch-fpo-la-deutsch-20220914-aes.md)

**Pflichtmodule (10):**
- Ling BM-12 Grundlagen der germanistischen Linguistik
- Lit BM4 Grundlagen des wissenschaftli- chen Arbeitens in der Literatur- wissenschaft
- NdL BM-15 Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- Ling BM-22 Grundlagen der historischen Linguistik
- Med BM6 Grundlagen der Germanisti- schen Mediävistik
- NdL BM-25 Grundlagen der Neueren deut- schen Literaturwissenschaft 2
- Ling BM-12 Grundlagen der germanisti- schen Linguistik
- NdL BM-14 Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- NdL BM-24 Grundlagen der Neueren deut- schen Literaturwissenschaft 2
- Med BM nv4 Grundlagen der Germanisti- schen Mediävistik – nicht ver- tieftes LA

### LA Englisch 20090226 i.d.F. 20200124.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20090226-idf-20200124.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20090226-idf-20200124.md)

**Pflichtmodule (20):**
- Basismodul I Language
- Basismodul II Linguistics (A)
- Basismodul III
- Linguistics (B)
- Basismodul IV Literature(A)
- Basismodul V Literature(B)
- Basismodul VI Culture
- Basismodul VII Landeskunde
- Zwischenmodul L-GYM Linguistics
- Zwischenmodul L-GYM Literature
- Zwischenmodul L-GYM Language
- Basismodul Englischdidaktik
- Basismodul Language
- Elementarmodul L-UF Linguistics I
- Elementarmodul L-UF Linguistics II
- Elementarmodul L-UF Literature I
- Elementarmodul L-UF Literature II
- Elementarmodul L-UF Ldkd
- anesune
- Zwischenmodul L-UF Language

### LA Englisch 20200124 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20200124-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-englisch-20200124-aes.md)

**Pflichtmodule (20):**
- Basismodul I Language
- Basismodul II Linguistics (A)
- Basismodul III
- Linguistics (B)
- Basismodul IV Literature(A)
- Basismodul V Literature(B)
- Basismodul VI Culture
- Basismodul VII Landeskunde
- Zwischenmodul L-GYM Linguistics
- Zwischenmodul L-GYM Literature
- Zwischenmodul L-GYM Language
- Basismodul Englischdidaktik
- Basismodul Language
- Elementarmodul L-UF Linguistics I
- Elementarmodul L-UF Linguistics II
- Elementarmodul L-UF Literature I
- Elementarmodul L-UF Literature II
- Elementarmodul L-UF Ldkd
- anesune
- Zwischenmodul L-UF Language

### LA Erweiterungsfach Chinesisch FPO LA Chin. 20161111 i.d.F. 20190828.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20161111-idf-20190828.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20161111-idf-20190828.md)

**Pflichtmodule (1):**
- Basismodul Chine- sischdidaktik

### LA Erweiterungsfach Chinesisch FPO LA Chin. 20230822 i.d.F. 20260331.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822-idf-20260331.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822-idf-20260331.md)

**Pflichtmodule (1):**
- Basismodul Chinesischdidak- tik

### LA Erweiterungsfach Chinesisch FPO LA Chin. 20230822.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-erweiterungsfach-chinesisch-fpo-la-chin-20230822.md)

**Pflichtmodule (1):**
- Basismodul Chinesischdi- daktik

### LA Französisch 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-20210624-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-20210624-aes.md)

**Pflichtmodule (4):**
- Basismodul Französische Sprachwissenschaft3
- Basismodul Französische Literaturwissenschaft4
- Französische Sprachpraxis 32
- Basismodul Didaktik der romanischen Sprachen

### LA Französisch FPO LA Französisch 20090309 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-fpo-la-franzoesisch-20090309-idf-20210624.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-franzoesisch-fpo-la-franzoesisch-20090309-idf-20210624.md)

**Pflichtmodule (4):**
- Basismodul Französische Sprachwissenschaft3
- Basismodul Französische Literaturwissenschaft4
- Französische Sprachpraxis 32
- Basismodul Didaktik der romanischen Sprachen

### LA Geschichte FPO LA Geschichte 20090310 i.d.F. 20180911.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20090310-idf-20180911.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20090310-idf-20180911.md)

**Pflichtmodule (12):**
- Basismodul I
- Basismodul II
- Basismodul III
- Basismodul IV
- Methodische und Theoretische Grundlagen
- Methodische Grundlagen
- Theoretische Grundlagen
- Landesgeschichte
- Basismodul Didaktik der Geschichte
- Basismodul I2
- Basismodul II3
- Basismodul III4

### LA Geschichte FPO LA Geschichte 20180911 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20180911-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-geschichte-fpo-la-geschichte-20180911-aes.md)

**Pflichtmodule (8):**
- Basismodul I
- Basismodul II
- Basismodul III
- Basismodul IV
- Basismodul Didaktik der Geschichte
- Basismodul I2
- Basismodul II3
- Landesgeschichte

### LA Griechisch FPO LA Griechisch 20090310 i.d.F. 20200806.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-griechisch-fpo-la-griechisch-20090310-idf-20200806.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-griechisch-fpo-la-griechisch-20090310-idf-20200806.md)

**Pflichtmodule (5):**
- Shüb I
- pracungen
- Poesie
- rosa
- Sprachübungen II

### LA Informatik FPO LA INF 20220421.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20220421.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20220421.md)

**Pflichtmodule (12):**
- Grundlagen der Programmierung
- Sichere Systeme
- Einführung in die Algorithmik
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende
- Parallele und funktionale Programmierung
- Softwareentwicklung in Großprojekten*
- Konzeptionelle Modellierung und Grundlagen von Datenbanken
- Grundlagen der Systemprogrammie- rung
- Grundlagen des Maschinellen Lernens und der Künstlichen Intelligenz
- Konzeptionelle Modellie- rung und Grundlagen von Datenbanken
- Praktikum Maschinen- programmierung
- Praktikum Informatik

### LA Informatik FPO LA INF 20240904.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20240904.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-informatik-fpo-la-inf-20240904.md)

**Pflichtmodule (14):**
- Grundlagen der Programmierung
- Sichere Systeme
- Einführung in die Algorithmik
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende
- Parallele und funktionale Programmierung
- Einführung in das Software Engineering
- Einführung in Datenbanken
- Praktikum Maschinenprogrammierung
- Grundlagen der Systemprogrammierung
- Grundlagen des Maschinellen Lernens und der Künstlichen Intelligenz
- Praktikum Informatik
- Praktikum Maschinen- programmierung
- Grundlagen der Informatik(GdI-Kompakt)
- Didaktik der Informatik 1

### LA Italienisch 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-20210624-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-20210624-aes.md)

**Pflichtmodule (5):**
- Basismodul Italienische Sprachpraxis 11
- Basismodul Italienische Sprachpraxis 21, 2
- Basismodul Italienische Sprachwissenschaft4
- Basismodul Italienische Literaturwissenschaft5
- Basismodul Didaktik der romanischen Sprachen

### LA Italienisch FPO LA Italienisch 20090325 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-fpo-la-italienisch-20090325-idf-20210624.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-italienisch-fpo-la-italienisch-20090325-idf-20210624.md)

**Pflichtmodule (5):**
- Basismodul Italienische Sprachpraxis 11
- Basismodul Italienische Sprachpraxis 21, 2
- Basismodul Italienische Sprachwissenschaft4
- Basismodul Italienische Literaturwissenschaft5
- Basismodul Didaktik der romanischen Sprachen

### LA Katholische Religionslehre 20210415 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-20210415-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-20210415-aes.md)

**Pflichtmodule (1):**
- Basismodul Grundlagen der Fachdidaktik

### LA Katholische Religionslehre FPO LA KathRel 20090727 i.d.F. 20210415.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20090727-idf-20210415.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20090727-idf-20210415.md)

**Pflichtmodule (1):**
- Basismodul Grundlagen der Fachdidaktik

### LA Katholische Religionslehre FPO LA KathRel 20240118.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20240118.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-katholische-religionslehre-fpo-la-kathrel-20240118.md)

**Pflichtmodule (1):**
- Basismodul Grundlagen der Fachdidaktik

### LA Mathematik  FPO LA Mathe 20191010 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-fpo-la-mathe-20191010-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-fpo-la-mathe-20191010-aes.md)

**Pflichtmodule (7):**
- Analysis I1)
- Lineare Algebra I1)
- Analysis II1)
- Lineare Algebra II1)
- Algebra2)
- Körpertheorie2)
- Analysis für Lehramt

### LA Mathematik FPO LA Mathe 20201029 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-fpo-la-mathe-20201029-aes.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-fpo-la-mathe-20201029-aes.md)

**Pflichtmodule (8):**
- Analysis I1)
- Lineare Algebra I1)
- Analysis II1)
- Lineare Algebra II1)
- Algebra2)
- Körpertheorie2)
- Analysis für Lehramt
- Funktionentheorie2)

### pdf vom 11.11.2015 i.d.F. 26.06.2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-juni2017.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-juni2017.md)

**Pflichtmodule (17):**
- Stochastische Modellbildung Ia
- Stochastische Modellbildung Ib
- Algebra Ia
- gebra b
- örperteore
- Analysis für Lehramt Ia
- Analysis für
- LehramtIb
- Geometrie
- Elemente der Linearen Algebra I1
- Elemente der Linearen Algebra IIa2
- Elemente der Linearen Algebra IIb2
- Elemente der Analysis I2
- Elemente der Analysis IIa1
- Elemente der Analysis IIb1
- Analytische Geometrie1
- Aufbaumodul Analysis2

### pdf vom 11.11.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-ws2015-2016.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-mathematik-ws2015-2016.md)

**Pflichtmodule (12):**
- Analysis I
- Lineare Algebra I
- Analysis II
- Lineare Algebra II
- Angewandte Mathematik
- Stochastische Modellbildung
- Algebra
- Körpertheorie
- Elemente der Linearen Algebra I1
- Elemente der Linearen Algebra II2
- Elemente der Analysis I2
- Elemente der Analysis II1

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

**Pflichtmodule (4):**
- Basismodul Spanische Sprachwissenschaft5
- Basismodul Spanische Literatur- wissenschaft6
- Spanische Sprachpraxis 31, 3
- Basismodul Didaktik der romanischen Spra- chen

### LA Spanisch FPO LA Spanisch 20090401 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-spanisch-fpo-la-spanisch-20090401-idf-20210624.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-spanisch-fpo-la-spanisch-20090401-idf-20210624.md)

**Pflichtmodule (4):**
- Basismodul Spanische Sprachwissenschaft5
- Basismodul Spanische Literatur- wissenschaft6
- Spanische Sprachpraxis 31, 3
- Basismodul Didaktik der romanischen Sprachen

### LA Wirtschaftswissenschaften FPO LA WiWi 20090401 i.d.F. 20210225.pdf

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/la-wirtschaftswissenschaften-fpo-la-wiwi-20090401-idf-20210225.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/la-wirtschaftswissenschaften-fpo-la-wiwi-20090401-idf-20210225.md)

**Pflichtmodule (6):**
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Wirtschaftsprivatrecht
- Grundlagen der Fachdidaktik Wirtschaftswissenschaften (Gymnasium)
- Praxisfelder der Fachdidaktik
- Grundlagen der Fachdidaktik Wirtschaftswissenschaften (Realschule)
- Praxisfelder der Fachdidaktik Wirtschaftswissenschaften

### pdf vom 26.02.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20ev-20religion.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20ev-20religion.md)

**Pflichtmodule (1):**
- (4) Pflichtmodul Praktikum

### pdf vom 25.03.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20informatik.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-20-20informatik.md)

**Pflichtmodule (2):**
- Grundlagen der Technischen Informatik
- Systemprogrammierung

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

**Pflichtmodule (6):**
- Grundlagen der Germanistischen Linguistik (Ling1)
- Grundlagen der Germanisti- schen Mediävistik (Med1)
- Grundlagen der Neueren deutschen Literatur (NdL 1)
- Grundlagen der Fachdidaktik Deutsch (BM FDD)
- Grundlagen der Germanisti- schen Linguistik (Ling1)
- Grundlagen der Neueren deut- schen Literatur (NdL 1)

### pdf vom 26.02.2009 i.d.F. 10.11.2016

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-nov2016.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-nov2016.md)

**Pflichtmodule (23):**
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
- Grundlagen der Neueren deut- schen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deut- schen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1(Med BM 1)
- Grundlagen der Germanistischen Mediävistik 2(Med BM 2)
- Grundlagen der Fachdidaktik Deutsch (BM FDD)
- Grundlagen der Neueren deutschen Literatur- wissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literatur- wissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 2(MedBM 2)
- Grundlagen der Germanistischen Lingu- istik 1 (Ling BM 1)
- Grundlagen der Germanistischen Lingu- istik 2 (Ling BM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Medi- ävistik 2(Med BM 2)
- Basismodul DiDaZ (LA GS)
- Basismodul DiDaZ (LA MS)
- Grundlagen des Deutschen als Zweitsprache
- Sprachsystem und Zweitspracherwerb
- Lehren und Lernen in der zweiten Sprache
- Sprachmodul 1
- Sprachmodul 2
- Praktikumsmodul

### pdf vom 26.02.2009 i.d.F. 24.09.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-sept2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-deutsch-neu-sept2015.md)

**Pflichtmodule (12):**
- Grundlagen der Germanistischen Linguistik (Ling1)
- Grundlagen der Germanisti- schen Mediävistik (Med 1)
- Grundlagen der Neueren deutschen Literatur (NdL 1)
- Grundlagen der Fachdidaktik Deutsch (BM FDD)
- Grundlagen der Germanisti- schen Linguistik (Ling1)
- Grundlagen der Neueren deut- schen Literatur (NdL 1)
- Grundlagen des Deutschen als Zweitsprache
- Sprachsystem und Zweitspracherwerb
- Lehren und Lernen in der zweiten Sprache
- Sprachmodul 1
- Sprachmodul 2
- Praktikumsmodul

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

**Pflichtmodule (14):**
- Basismodul I Language
- Basismodul II Liii
- ngustcs
- Basismodul III Literature
- Basismodul IV Culture/Landeskunde
- Zwischenmodul L‐GYM Linguistics
- Zwischenmodul L‐GYM Literature
- Zwischenmodul L‐GYM Language
- Basismodul Englischdidaktik
- Basismodul Language
- Elementarmodul L‐UF Linguistics
- Elementarmodul L‐UF Literature
- Elementarmodul L‐UF
- Landeskunde

### pdf vom 26.02.2009 i.d.F. 09.06.2011

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-juni2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-juni2011.md)

**Pflichtmodule (5):**
- Grundlagen und Fragen christlicher Ethik
- Religionswissenschaft
- (2Ü) Das Judentum(in seinem Verhältnis zum Christentum)
- Der Islam (in seinem Verhältnis zum Christentum)
- Grundfragen der Religionswissenschaft

### pdf vom 26.02.2009 i.d.F. 01.12.2009

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-neu.md)

**Pflichtmodule (1):**
- (4) Pflichtmodul Praktikum

### pdf vom 26.02.2009 i.d.F. 15.09.2011

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-sept2011.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-20religion-sept2011.md)

**Pflichtmodule (5):**
- Grundlagen und Fragen christlicher Ethik
- Religionswissenschaft
- (2Ü) Das Judentum(in seinem Verhältnis zum Christentum)
- Der Islam (in seinem Verhältnis zum Christentum)
- Grundfragen der Religionswissenschaft

### (pdf vom 26.02.2009 i.d.F. 14.12.2017)

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-religion-dez2017.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-ev-religion-dez2017.md)

**Pflichtmodule (10):**
- Basismodul: Theologie und wissenschaftliches Arbeiten
- Biblisches Grundwissen (Lehramt GS/MS/RS)
- Grundlagen der Theologie und Religionspädagogik
- Biblische Theologie 1 (AT)
- Biblische Theologie 2 (NT)
- Biblische Theologie 3
- Systematische Theologie 1: Dogmatik (GMRS)
- Systematische Theologie 2: Ethik (GMRS)
- Kirchengeschichte 1
- Kirchengeschichte 2

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

**Pflichtmodule (7):**
- Basismodul Französische Sprachpraxis 1
- Basismodul Französische Sprachpraxis 2
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen
- Bidl Föih Shi 2
- assmou ranzssce pracpraxs

### pdf vom 09.03.2009 i.d.F. 24.09.2010

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-neu.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-neu.md)

**Pflichtmodule (3):**
- Abschlussmodul Schriftliche Hausarbeit
- Kolloquium zur Besprechung der schriftlichen Hausarbeit
- Schriftliche Hausarbeit

### pdf vom 09.03.2009 i.d.F. 29.09.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-sept2014.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-franzoesisch-sept2014.md)

**Pflichtmodule (4):**
- Basismodul Französische Sprachpraxis 1
- Basismodul Französische Sprachpraxis 2
- Basismodul Einführung in die Frankoro- manistik
- Basismodul Didaktik der roma- nischen Sprachen

### pdf vom 10.03.2009 i.d.F. 02.04.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-april2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-april2015.md)

**Pflichtmodule (5):**
- Shüb I
- pracungen
- Poesie
- Prosa
- Sprachübungen II

### pdf vom 10.03.2009 i.d.F. 23.07.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-juli2014.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-juli2014.md)

**Pflichtmodule (3):**
- Sprachübungen I
- Poesie
- Prosa

### pdf vom 10.03.2009 i.d.F. 27.09.2013

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-sept2013.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-griechisch-sept2013.md)

**Pflichtmodule (3):**
- Sprachübungen I
- Poesie
- Prosa

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

**Pflichtmodule (5):**
- Basismodul Italienische Sprachpraxis 1
- Basismodul Italienische Sprachpraxis 2
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen

### pdf vom 25.03.2009 i.d.F. 29.09.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-sept2014.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-italienisch-sept2014.md)

**Pflichtmodule (3):**
- Basismodul Italienische Sprachpraxis 1
- Basismodul Italienische Sprachpraxis 2
- Basismodul Einführung in die Italoromanistik

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

**Pflichtmodule (7):**
- Grundlagen der politi- schen Bildung
- Methodik und Wertorien- tierung im Politikunterricht
- Grundlagen der politischen Bildung
- Methodik, Praxis und Wertorientierung im Politikunterricht
- Methodik und Wertorientierung im Politikunterricht
- Praxis des Politikunterrichts
- Praxisprobleme der Politischen Bil- dung

### pdf vom 01.04.2009 i.d.F. 08.08.2017

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-aug2017.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-aug2017.md)

**Pflichtmodule (6):**
- Basismodul Spanische Sprachpraxis 1
- Basismodul Spanische
- Sprachpraxis 2
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Basismodul Didaktik der romanischen Sprachen

### pdf vom 01.04.2009 i.d.F. 29.09.2014

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-sept2014.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lapo-spanisch-sept2014.md)

**Pflichtmodule (4):**
- Basismodul Spanische Sprachpraxis 1
- Basismodul Spanische Sprachpraxis 2
- Basismodul Einführung in die Iberoromanistik
- Basismodul Didaktik der romanischen Sprachen

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

**Pflichtmodule (4):**
- Grundlagen der Fachdidaktik Wirtschaftswissenschaft en(Gymnasium)
- Praxisfelder der Fachdidaktik
- Grundlagen der Fachdidaktik Wirtschaftswissenschaft en(Realschule)
- Praxisfelder der Fachdidaktik Wirtschaftswissenschaft en

### pdf vom 27.07.2009 i.d.F. 14.09.2015

PO-Quelle: [`pruefungsordnungen/lehramt/lehramtsfaecher/lehramt-arbeitslehre-sept2015.md`](../pruefungsordnungen/lehramt/lehramtsfaecher/lehramt-arbeitslehre-sept2015.md)

**Pflichtmodule (5):**
- Grundlagen der Fachdi- daktik (GFD)
- Grundlagen der Fach- wissenschaft (GFW)
- Medien und Methoden I (MuM I)
- Medien und Methoden II (MuM II)2
- Arbeit und Beruf (AuB)

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

**Pflichtmodule (9):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch-chemisches Praktikum
- Biochemie und Grundzüge der Molekularen Medizin
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Grundlagen der Physiologie des Menschen und Grundlagen der Bioinformatik
- Organische Chemie

### 18. Februar 2016

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/5aes-ba-ma-molekulare-medizin.md`](../pruefungsordnungen/medizinische-fakultaet/5aes-ba-ma-molekulare-medizin.md)

**Pflichtmodule (6):**
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Research Design
- Laboratory Animal Science and Biological Safety

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20070928 i.d.F. 20210113.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210113.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210113.md)

**Pflichtmodule (6):**
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Research Design
- Laboratory Animal Science and Biological Safety

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20070928 i.d.F. 20210429.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210429.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20070928-idf-20210429.md)

**Pflichtmodule (6):**
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Research Design
- Laboratory Animal Science and Biological Safety

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20210113 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20210113-aes.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20210113-aes.md)

**Pflichtmodule (6):**
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Research Design
- Laboratory Animal Science and Biological Safety

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20230822 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822-idf-20240926.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822-idf-20240926.md)

**Pflichtmodule (18):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch- chemisches Praktikum 3)
- Biochemie und Grundzüge der Mlkl Mdii
- oeuaren ezn
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Grundlagen der Physiologie des Menschen und Grundlagen der Bioinformatik
- Organische Chemie
- Bachelorarbeit
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Research Design
- Laboratory Animal Science and Biological Safety
- Masterarbeit mit Masterkolloquium

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20230822 i.d.F. 20250711.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822-idf-20250711.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822-idf-20250711.md)

**Pflichtmodule (7):**
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Research Design
- Laboratory Animal Science and Biological Safety
- Masterarbeit mit Masterkolloquium

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed 20230822.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-20230822.md)

**Pflichtmodule (18):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch- chemisches Praktikum 3)
- Biochemie und Grundzüge der Mlkl Mdii
- oeuaren ezn
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Grundlagen der Physiologie des Menschen und Grundlagen der Bioinformatik
- Organische Chemie
- Bachelorarbeit
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Research Design
- Laboratory Animal Science and Biological Safety
- Masterarbeit mit Masterkolloquium

### BSc Molekulare Medizin-MSc Molecular Medicine PO MolMed ÄS 20250711.pdf

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-aes-20250711.md`](../pruefungsordnungen/medizinische-fakultaet/bsc-molekulare-medizin-msc-molecular-medicine-po-molmed-aes-20250711.md)

**Pflichtmodule (21):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch- chemisches Praktikum4)
- Biochemie und Grundzüge der Mlkl Mdii
- oeuaren ezn
- Funktionelle Anatomie des Menschen für Molekulare Medizin
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Grundlagen der Physiologie des Menschen und
- Grundlagen der Bioinformatik
- Organische Chemie
- Vegetative Physiologie
- Neurophysiologie und Neuroanatomie
- Biochemie und Molekularbiologie I
- Biochemie und Molekularbiologie II
- Biochemisches Praktikum I
- Biochemisches Praktikum II
- Mikrobiologie, Immunologie und Virologie
- Strahlenschutz in der experimentellen Medizin
- Humangenetik
- Bachelorarbeit

### PDF vom 28.09.2007 i.d.F. 18.02.2016

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-feb2016.md`](../pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-feb2016.md)

**Pflichtmodule (20):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch-chemisches Praktikum
- Biochemie und Grundzüge der
- Molekularen Medizin
- Funktionelle Anatomie des Menschen
- Allgemeine Histologie und Embryologie
- Spezielle Histologie und Organogenese
- Grundlagen der Physiologie des Menschen und Grundlagen der Bioinformatik
- Oranische Chemie
- Bachelorarbeit
- Pflichtbereich (35 ECTS-Leistungspunkte)
- Advanced Lectures in Molecular Medicine 1
- Advanced Lectures in Molecular Medicine 2
- Architecture of Biopolymers
- Research Design
- Laboratory Animal Science and Biological Safety
- Masterarbeit (30 ECTS-Leistungspunkte)
- Master’s Thesis
- Master’s Colloquium

### PDF vom 28.09.2007 i.d.F. 22.07.2014

PO-Quelle: [`pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-juli2014.md`](../pruefungsordnungen/medizinische-fakultaet/pro-ba-ma-molekmedizin-juli2014.md)

**Pflichtmodule (9):**
- Grundlagen der Zellbiologie
- Allgemeine und Anorganische Chemie
- Anorganisch-chemisches Prakti- kum
- Biochemie und Grundzüge der
- Molekularen Medizin
- Funktionelle Anatomie des Men- schen
- Allgemeine Histologie und Emb- ryologie
- Spezielle Histologie und Orga- nogenese
- Grundlagen der Physiologie des Menschen und Grundlagen der Bioinformatik

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

**Pflichtmodule (15):**
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

### (PDF vom 22.07.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bio-zellmolekbio-neu.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bio-zellmolekbio-neu.md)

**Pflichtmodule (14):**
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

### FPO BSc-MSc ILS FPO BAMA ILS 20191028.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20191028.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20191028.md)

**Pflichtmodule (10):**
- Itdti t Sttiti d
- nroucon o ascs an Statistical Prorammin
- Biomathematics
- Systems Biology
- Bioimaging & Biophysics A
- Bioimaging & Biophysics B
- Interactions of Biological Macromolecules A
- Intrtin f Bilil
- eacos o oogca Mll B
- acromoecues

### FPO BSc-MSc ILS FPO BAMA ILS 20230822 i.d.F. 20260331.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20230822-idf-20260331.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20230822-idf-20260331.md)

**Pflichtmodule (6):**
- Introduction to Statistics and Statistical Program- ming
- Biomathematics
- Systems Biology
- Bioimaging & Biophysics A
- Interactions of Biological Macromolecules A
- Interactions of Biological Macromolecules B

### FPO BSc-MSc ILS FPO BAMA ILS 20230822.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20230822.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/biologie/fpo-bsc-msc-ils-fpo-bama-ils-20230822.md)

**Pflichtmodule (6):**
- Introduction to Statistics and Statistical Program- ming
- Biomathematics
- Systems Biology
- Bioimaging & Biophysics A
- Interactions of Biological Macromolecules A
- Interactions of Biological Macromolecules B

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
- (16) Masterarbeit gemäß § 79

### BA-MA Kulturgeographie FPO Kulturgeo 20200827 i.d.F. 20221011.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20200827-idf-20221011.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20200827-idf-20221011.md)

**Pflichtmodule (8):**
- Kulturgeographische Theorien
- Wahlmodul Kulturgeographie
- Gesellschaft, Technik, Raum
- Methoden der digitalen Geistes- und Sozialwissenschaften
- KGV: Vertiefte Kulturgeo- graphie
- EE: Externe Expertise4)
- LF: Lehrforschung
- RGV: Vertiefte Regionale Geographie

### BA-MA Kulturgeographie FPO Kulturgeo 20200827.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20200827.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20200827.md)

**Pflichtmodule (2):**
- Kulturgeographische Theorien
- ARB: Masterarbeit

### BA-MA Kulturgeographie FPO Kulturgeo 20230822.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20230822.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/ba-ma-kulturgeographie-fpo-kulturgeo-20230822.md)

**Pflichtmodule (8):**
- Kulturgeographische Theorien
- Wahlmodul Kulturgeographie
- Gesellschaft, Technik, Raum
- Methoden der digitalen Geistes- und Sozialwissenschaften
- KGV: Vertiefte Kulturgeographie
- EE: Externe Expertise4)
- LF: Lehrforschung
- RGV: Vertiefte Regionale Geographie

### PDF vom 29.02.2016 i.d.F. 02.03.2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-maerz2017.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-maerz2017.md)

**Pflichtmodule (24):**
- Grundlagen der Geowissenschaften I
- Minerale und Gesteine
- Mathematik
- Biologie
- Chemie
- Geowissenschaftliche Arbeitsmethoden I
- Grundlagen der Geowissenschaften II
- Dynamik des Systems Erde
- Mineralogie I
- Physik
- Paläobiologie I
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

### PDF vom 29.02.2016 i.d.F. 30.09.2016

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-sept2016.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften-sept2016.md)

**Pflichtmodule (25):**
- Grundlagen der Geowissenschaften I
- Minerale und Gesteine
- Mathematik
- Biologie
- Chemie
- Geowissenschaftliche Arbeitsmethoden I
- Grundlagen der Geowissenschaften II
- Dynamik des Systems Erde
- Mineralogie I
- Physik
- Paläobiologie I
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

### PDF vom 29.02.2016

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-ba-ma-geowissenschaften.md)

**Pflichtmodule (25):**
- Grundlagen der Geowissenschaften I
- Minerale und Gesteine
- Mathematik
- Biologie
- Chemie
- Geowissenschaftliche Arbeitsmethoden I
- Grundlagen der Geowissenschaften II
- Dynamik des Systems Erde
- Mineralogie I
- Physik
- Paläobiologie I
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

### FPO BAMA Geow 20191028 i.d.F. 20200604.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028-idf-20200604.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028-idf-20200604.md)

**Pflichtmodule (2):**
- Schriftliche Masterarbeit
- Verteidigung der Masterarbeit

### FPO BAMA Geow 20191028 i.d.F. 20220908.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028-idf-20220908.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028-idf-20220908.md)

**Pflichtmodule (1):**
- Masterarbeit gemäß § 54

### FPO BAMA Geow 20191028.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20191028.md)

**Pflichtmodule (2):**
- Schriftliche Masterarbeit
- Verteidigung der Masterarbeit

### FPO BAMA Geow 20250513.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20250513.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-bama-geow-20250513.md)

**Pflichtmodule (1):**
- Masterarbeit (gemäß § 54)

### FPO Kulturgeo 20221011 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-kulturgeo-20221011-aes.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/geographie-und-geowissenschaften/fpo-kulturgeo-20221011-aes.md)

**Pflichtmodule (7):**
- Kulturgeographische Theorien
- Wahlmodul Kulturgeographie
- Gesellschaft, Technik, Raum
- Methoden der digitalen Geistes- und Sozialwissenschaften
- KGV: Vertiefte Kulturgeo- graphie
- EE: Externe Expertise4)
- LF: Lehrforschung

### BSc-MSc Data Science FPODataScience 20210805 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/bsc-msc-data-science-fpodatascience-20210805-aes.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/bsc-msc-data-science-fpodatascience-20210805-aes.md)

**Pflichtmodule (10):**
- (1) Mathematics of Learning
- (2) Deep Learning
- (3) Selected Topics in Mathematics of Learning
- cences
- (4) Wahlpflicht- module aus dem
- Katalog der ge- ählt Ht
- wen aup- studienrichtung gemäß § 51
- aupsuenrcung
- (5) Wahlpflicht- module aus den Katalogen der nicht gewählten Nebenstudien- richtungen gemäß § 51
- eensuenrcung

### BSc-MSc Data Science FPODataScience 20220328 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/bsc-msc-data-science-fpodatascience-20220328-aes.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/bsc-msc-data-science-fpodatascience-20220328-aes.md)

**Pflichtmodule (15):**
- (1) Mathematics of Learning
- (2) Deep Learning
- (3) Selected Topics in Mathe- matics of Learning
- cece
- (4) Wahlpflichtmodule aus
- dem Katalog der gewählten Httdiiht
- aupsuenrcung gemäß § 51
- eep earnng
- (3) Selected Topics in Mathematics of Learning
- (4) Wahlpflichtmodule aus dem Katalog der ge- wählten Hauptstudien- richtung gemäß § 51
- (5) Wahlpflichtmodule aus den Katalogen der nicht gewählten Neben- studienrichtungen gemäß § 51
- (6) Wahlpflichtmodule aus dem Katalog der An- wendungsfachmodule gemäß § 52
- (5) Wahlpflichtmodule aus den Katalogen der nicht gewählten Nebenstudi- enrichtungen gemäß § 51
- (7) Wahlmodule der Tech- nischen Schlüsselquali- fiki äß 53
- aton gem §

### PDF vom 11.03.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-mathematik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-mathematik.md)

**Pflichtmodule (5):**
- Analysis I
- Analysis II
- Analysis III
- Lineare Algebra I
- Lineare Algebra II

### PDF vom 11.03.2015 i.d.F. 27.02.2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik-feb2017.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik-feb2017.md)

**Pflichtmodule (12):**
- Analysis I
- Analysis II
- Analysis III
- Lineare Algebra I
- Lineare Algebra II
- Lineare und Kombinatorische Optimierung
- Stochastische Modellbildung
- Numerische Mathematik
- Diskretisierung und numerische Optimierung
- Numerik partieller Differential- gleichungen
- Mathematische Modellierung Theorie
- Nichtlineare Optimierung

### PDF 27th of February 2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik-fpotechnomathe-20150311-idf-20170227-en.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik-fpotechnomathe-20150311-idf-20170227-en.md)

**Pflichtmodule (16):**
- Vorlesung Analysis I
- Übung Analysis I
- Tafelübung Analysis I
- Vorlesung Analysis II
- Übung Analysis II
- Tafelübung Analysis II
- Vorlesung Analysis III
- Übung Analysis III
- Tafelübung Analysis III
- Vorlesung Lineare Algebra I
- Übung Lineare Algebra I
- Tafelübung Lineare Algebra I
- Vorlesung Lineare Algebra II
- Übung Lineare Algebra II
- Tafelübung Lineare Algebra II
- (GM)

### PDF vom 11.03.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-technomathematik.md)

**Pflichtmodule (12):**
- Analysis I
- Analysis II
- Analysis III
- Lineare Algebra I
- Lineare Algebra II
- Lineare und Kombinatorische Optimierung
- Stochastische Modellbildung
- Numerische Mathematik
- Diskretisierung und numerische Optimierung
- Numerik partieller Differential- gleichungen
- Mathematische Modellierung Theorie
- Nichtlineare Optimierung

### PDF vom 11.03.2015 i.d.F. 13.03.2017

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik-maerz2017.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik-maerz2017.md)

**Pflichtmodule (9):**
- Analysis I
- Analysis II
- Analysis III
- Lineare Algebra I
- Lineare Algebra II
- Lineare und Kombinatorische Optimierung1
- Projektseminar Optimierung2
- Stochastische Modellbildung1
- Introduction to Statistics and Statistical Programming2

### PDF vom 11.03.2015

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpo-ba-ma-wirtschaftsmathematik.md)

**Pflichtmodule (9):**
- Analysis I
- Analysis II
- Analysis III
- Lineare Algebra I
- Lineare Algebra II
- Lineare und Kombinatorische Optimierung1
- Projektseminar Optimierung2
- Stochastische Modellbildung1
- Introduction to Statistics and Statistical Programming2

### FPODataScience 20200820 i.d.F. 20210311.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210311.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210311.md)

**Pflichtmodule (14):**
- (1) Seminar Data Science in Forschung und Industrie
- (2) Einführung in die mathematische Datenanalyse
- (3) Wahlpflichtmodule aus dem Katalog für Machine Learning gem. § 42
- (4) Wahlpflichtmodule aus dem Katalog für Projekt Data Science gem. § 42
- (1) Mathematical Data Science (MaDS)
- (2) Deep Learning
- (3) Mathematics of Learning
- cences
- (4) Wahlpflicht- module aus dem Katalog
- der gewählten
- Hauptstudien- richtung gemäß § 51
- aupsuenrcung
- (5) Wahlpflicht- module aus den Katalogen der nicht ge- wählten Nebenstudien- richtungen ge- mäß § 51
- eensuenrcung

### FPODataScience 20200820 i.d.F. 20210805.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210805.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20210805.md)

**Pflichtmodule (21):**
- (1) Seminar Data Science in Forschung und Industrie
- (2) Einführung in die mathematische Datenanalyse
- (3) Wahlpflichtmodule aus dem Katalog für Machine Learning gem. § 42
- (4) Wahlpflichtmodule aus dem Katalog für Projekt Data Science gem. § 42
- (1) Mathematics of Learning
- (2) Deep Learning
- (3) Selected Topics in Mathematics of Learning
- cences
- (4) Wahlpflicht- module aus
- dem Katalog der ählt Ht-
- gewen aup studienrichtung gemäß § 51
- aupsuenrcung
- (5) Wahlpflicht- module aus den Katalogen der nicht gewähl- ten Nebenstudi- enrichtungen gemäß § 51
- eensuenrcung
- (6) Wahlpflicht- module aus dem
- Katalog der Adfh-
- nwenungsac module gemäß § 52
- (9) Masterarbeit gemäß § 55
- Katalog der ge- ählt Ht-
- wen aup studienrichtung gemäß § 51
- (5) Wahlpflicht- module aus den Katalogen der nicht gewählten Nebenstudien- richtungen gemäß § 51

### FPODataScience 20200820 i.d.F. 20220328.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20220328.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820-idf-20220328.md)

**Pflichtmodule (24):**
- (1) Seminar Data Science in Forschung und Industrie
- (2) Einführung in die mathematische Datenanalyse
- (3) Wahlpflichtmodule aus dem Katalog für Machine Learning gem. § 42
- (4) Wahlpflichtmodule aus dem Katalog für Projekt Data Science gem. § 42
- (1) Mathematics of Learning
- (2) Deep Learning
- (3) Selected Topics in Mathematics of Learning
- (4) Wahlpflicht- module aus dem Katalog der
- gewählten
- Hauptstudien- richtung gemäß § 51
- upuug
- (5) Wahlpflicht- module aus den Katalogen der nicht ge- wählten Neben- studienrichtun- gen gemäß § 51
- (6) Wahlpflicht- module aus
- dem Katalog der Ad-
- nwenungs fachmodule gemäß § 52
- (4) Wahlpflichtmodule aus dem
- Katalog der gewählten Httdiiht
- aupsuenrcung gemäß § 51
- eep earnng
- (4) Wahlpflichtmodule aus dem Katalog der gewählten Haupt- studienrichtung gemäß § 51
- (5) Wahlpflichtmodule aus den Katalogen der nicht gewählten Nebenstudienrich- tungen gemäß § 51
- (6) Wahlpflichtmodule aus dem Katalog der Anwendungs- fachmodule gemäß §52
- (4) Wahlpflichtmodule aus dem Katalog der gewählten Hauptstu- dienrichtung gemäß § 51
- (6) Wahlpflichtmodule aus dem Katalog der Anwendungsfach- module gemäß § 52

### FPODataScience 20200820.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20200820.md)

**Pflichtmodule (14):**
- (1) Seminar Data Science in Forschung und Industrie
- (2) Einführung in die mathematische Datenanalyse
- (3) Wahlpflichtmodule aus dem Katalog für Machine Learning gem. § 42
- (4) Wahlpflichtmodule aus dem Katalog für Projekt Data Science gem. § 42
- (1) Mathematical Data Science (MaDS)
- (2) Deep Learning
- (3) Mathematics of Learning
- cences
- (4) Wahlpflicht- module aus dem Katalog
- der gewählten
- Hauptstudien- richtung gemäß § 51
- aupsuenrcung
- (5) Wahlpflicht- module aus den Katalogen der nicht ge- wählten Nebenstudien- richtungen ge- mäß § 51
- eensuenrcung

### FPODataScience 20260305.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20260305.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpodatascience-20260305.md)

**Pflichtmodule (15):**
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
- (2) Deep Learning
- (3) Selected Topics in Mathematics of Learning
- (4) Wahlpflichtmodule aus dem Katalog der gewählten Hauptstudienrichtung gemäß § 57
- (5) Wahlpflichtmodule aus den Katalogen der nicht gewähl- ten Nebenstudienrichtungen gemäß § 57
- (3) Selected Topics in Mathe- matics of Learning

### FPOMathe 20150311 i.d.F. 20190715.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20150311-idf-20190715.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20150311-idf-20190715.md)

**Pflichtmodule (5):**
- (1) Analysis I
- (2) Analysis II
- (3) Analysis III
- (4) Lineare Algebra I
- (5) Lineare Algebra II

### FPOMathe 20150311 i.d.F. 20210805.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20150311-idf-20210805.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20150311-idf-20210805.md)

**Pflichtmodule (5):**
- (1) Analysis I
- (2) Analysis II
- (3) Analysis III
- (4) Lineare Algebra I
- (5) Lineare Algebra II

### FPOMathe 20190715 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20190715-aes.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20190715-aes.md)

**Pflichtmodule (5):**
- (1) Analysis I
- (2) Analysis II
- (3) Analysis III
- (4) Lineare Algebra I
- (5) Lineare Algebra II

### FPOMathe 20260305.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20260305.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpomathe-20260305.md)

**Pflichtmodule (6):**
- (1) Analysis I
- (2) Analysis II
- (3) Analysis III
- (4) Lineare Algebra I
- (5) Lineare Algebra II
- (11) Bachelorarbeit

### FPOTechnoMathe 20150311 i.d.F. 20190715.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20190715.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20190715.md)

**Pflichtmodule (8):**
- (1) Modeling and Analysis in Continuum Mechanics I
- (2) Modeling and Analysis in Continuum Mechanics II
- (3) Modeling, Simulation and Optimization
- (4) Programming Techniques for Super- computers in CAM
- (5) Architectures of Super- computers
- MApA
- MApA/ NASi/ Opti
- Programming Techniques for Supercomputers in CAM

### FPOTechnoMathe 20150311 i.d.F. 20200820.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20200820.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20200820.md)

**Pflichtmodule (7):**
- (1) MApA
- (3) MApA/ NASi/ Opti
- Modeling and Analysis in Continuum Mechanics I
- Modeling and Analysis in Continuum Mechanics II
- Modeling, Simulation and Optimization
- Programming Techniques for Supercomputers in CAM
- Architectures of Super- computers

### FPOTechnoMathe 20150311 i.d.F. 20210805.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20210805.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20210805.md)

**Pflichtmodule (2):**
- (1) MApA
- (3) MApA/ NASi/ Opti

### FPOTechnoMathe 20150311 i.d.F. 20220811.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20220811.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20150311-idf-20220811.md)

**Pflichtmodule (8):**
- MApA
- MApA/ NASi/ Opti
- Modeling and Analysis in Continuum Mechanics I
- Modeling and Analysis in Continuum Mechanics II
- Modeling, Simulation and Optimization
- Programming Techniques for Super- computers in CAM
- Architectures of Super- computers
- Programming Techniques for Supercomputers in CAM

### FPOTechnomathe 20260305.pdf

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20260305.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/mathematik/fpotechnomathe-20260305.md)

**Pflichtmodule (2):**
- MApA
- MApA/ NASi/ Opti

### PDF vom 25.09.1980 i.d.F. 28.12.2004

PO-Quelle: [`pruefungsordnungen/naturwissenschaftliche-fakultaet/modul-und-zusatzstudien/zwischenpruefungso.md`](../pruefungsordnungen/naturwissenschaftliche-fakultaet/modul-und-zusatzstudien/zwischenpruefungso.md)

**Pflichtmodule (13):**
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

**Pflichtmodule (14):**
- Basismodul Französische Sprach- praxis 1
- Grundlagen der Neueren deut- schen Literatur(NdL 1)
- Grundlagen der Buchwissenschaft
- Einführung in das wissenschaftli- che Arbeiten Buchwissenschaft
- Basismodul Französische Sprach- praxis 2
- Einführung französische Literatur- wissenschaft
- Systematische Aspekte der Litera- turwissenschaft (LitS)
- Lesen und Lese(r)geschichte im Überblick
- Lehrveranstaltungen an der Part- neruniversität*
- Grundlagen E-Publishing/E- Commerce
- Typographie Grundlagen
- Literatur und Buch D – F
- Buchwirtschaftliches Praktikum
- Bachelorarbeit

### PDF vom 18.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1fachba-soziologie.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/1fachba-soziologie.md)

**Pflichtmodule (6):**
- Grundlagen der soziologischen Analyse (SozG)
- Qualifikationsprofil I (SozQ-I)
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Vertiefung Soziologische Metho- denlehre (SozM-V)

### 22. Juli 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/2aes-1fachba-islamischreligioesestudien.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/2aes-1fachba-islamischreligioesestudien.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### 21. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/3aes-1fachba-archaeologwissenschaften.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/3aes-1fachba-archaeologwissenschaften.md)

**Pflichtmodule (3):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/6aesa-ba-ma-psychologie.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/6aesa-ba-ma-psychologie.md)

**Pflichtmodule (4):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M 1Multivariate Statistik
- M 2Forschungsmethoden
- M 3Psychologische Diagnostik

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

**Pflichtmodule (2):**
- Bachelorarbeit
- Kompetenzreflexion (Schlüsselqualifikation)

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20200911.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20200911.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20200911.md)

**Pflichtmodule (4):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1Multivariate Statistik
- M2Forschungsmethoden
- M3Psychologische Diagnostik

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20210806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20210806.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20210806.md)

**Pflichtmodule (4):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1Multivariate Statistik
- M2Forschungsmethoden
- M3Psychologische Diagnostik

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20220328.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20220328.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20220328.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20220328 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20220328-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20220328-aes.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Fhthd
- orscungsmeoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20240229.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240229.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240229.md)

**Pflichtmodule (5):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Forschungsmethoden
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240926.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240926.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20241219.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md)

**Pflichtmodule (5):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Forschungsmethoden
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/bsc-msc-psychologie-bmstpo-psl-20230822.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20071009 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20180730.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20180730.md)

**Pflichtmodule (8):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Bachelorarbeit und –prüfung
- Bachelorarbeit

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20071009 i.d.F. 20190220.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20190220.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20071009-idf-20190220.md)

**Pflichtmodule (11):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Klassische Archäologie
- Klassische Archäologie: Griechische Archäologie I A
- Klassische Archäologie: Griechische Archäologie I B
- Bachelorarbeit und -prüfung
- Bachelorarbeit

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20180730 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20180730-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20180730-aes.md)

**Pflichtmodule (8):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Bachelorarbeit und -prüfung
- Bachelorarbeit

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20190220 ÄS zu 5ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20190220-aes-zu-5aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20190220-aes-zu-5aes.md)

**Pflichtmodule (16):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Klassische Archäologie
- Klassische Archäologie: Griechische Archäologie I A
- Klassische Archäologie: Griechische Archäologie I B
- Klassische Archäologie: Römische Archäologie I A
- Klassische Archäologie: Römische Archäologie I B
- Christliche Archäologie
- Christliche Archäologie: Kulturgeschichte I A
- Christliche Archäologie: Kulturgeschichte I B
- Bachelorarbeit und -prüfung
- Bachelorarbeit

### Ein-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Ein-Fach 20240430.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20240430.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-ein-fach-20240430.md)

**Pflichtmodule (8):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
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

**Pflichtmodule (1):**
- Bachelorarbeit

### Ein-Fach-BA Islamisch-Religiöse Studien BA IRS Ein-Fach 20210318 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20210318-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-ba-irs-ein-fach-20210318-aes.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### Ein-Fach-BA  Islamisch Religiöse Studien FPO BA IRS Ein-Fach 20121109 i.d.F. 20210318.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-fpo-ba-irs-ein-fach-20121109-idf-20210318.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-islamisch-religioese-studien-fpo-ba-irs-ein-fach-20121109-idf-20210318.md)

**Pflichtmodule (3):**
- Bachelorarbeit
- Bhlbi
- aceoraret

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20140718 i.d.F. 20190806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20190806.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20190806.md)

**Pflichtmodule (11):**
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Vertiefung Soziologische Metho- denlehre(SozM-V)
- Einführung Soziologische Theo- rien(SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Qualifikationsprofil II (SozQ-II), vgl. § 5
- Bachelorarbeit

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20140718 i.d.F. 20200818.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20200818.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20140718-idf-20200818.md)

**Pflichtmodule (14):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Vertiefung Soziologische Methodenlehre (SozM-V)
- Einführung Soziologische Theorien(SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Bachelorarbeit
- Grundlagen der soziologischen Analyse I(SozB)
- Grundlagen der soziologischen Analyse II(SozW)

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20190806 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20190806-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20190806-aes.md)

**Pflichtmodule (8):**
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Vertiefung Soziologische Methoden- lehre(SozM-V)
- Bachelorarbeit

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20200818 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20200818-aes.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20200818-aes.md)

**Pflichtmodule (13):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Grundlagen der soziologischen Analyse I (SozB)
- Grundlagen der soziologischen Analyse II (SozW)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Vertiefung Soziologische Methodenlehre (SozM-V)
- Einführung Soziologische Theorien(SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Bachelorarbeit
- Einführung Soziologische Theorien (SozT-E)

### Ein-Fach-BA Soziologie FPOSoz Ein-Fach 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/ein-fach-ba-soziologie-fposoz-ein-fach-20230822.md)

**Pflichtmodule (14):**
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

**Pflichtmodule (8):**
- Basismodule: Kulturentwicklung
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I
- Prähistorische Archäologie: Jüngere Urgeschichte I
- Klassische Archäologie
- Klassische Archäologie: Vorgriechische und griechische Archäologie I
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

**Pflichtmodule (9):**
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Schrift und Lesen in Kultur und Gesell- schaft
- Methoden
- Französische Sprachpraxis 2
- Basismodul Französische Literaturwis- senschaft
- Grundlagen der Neueren deutschen Lite- raturwissenschaft 2 (NdL BM 2)
- Mediennutzung und Leseverhalten
- Lehrveranstaltungen an der Partneruni- versität2
- Bachelorarbeit

### PDF vom 28.09.2007 i.d.F. 11.08.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psycho.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psycho.md)

**Pflichtmodule (6):**
- psychologischen
- Diagnostik
- Diagnostische
- Verfahren
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 04.06.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psychojuni2010.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-20ba-ma-psychojuni2010.md)

**Pflichtmodule (5):**
- psychologischen Diagnostik
- Diagnostische
- Verfahren
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-ba-ma-psycho-bmstpo-psl-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-ba-ma-psycho-bmstpo-psl-aug2017.md)

**Pflichtmodule (4):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M 1Multivariate Statistik
- M 2Forschungsmethoden
- M 3Psychologische Diagnostik

### PDF vom 28.09.2007 i.d.F. 31.07.2012

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-ba-ma-psycho-juli2012.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/prostuo-ba-ma-psycho-juli2012.md)

**Pflichtmodule (7):**
- psychologischen Diagnostik
- Diagnostische
- Verfahren
- Klinische
- Psychologie
- M14 Hauptformen der
- Psychotherapie

### PDF vom 09.11.2012 i.d.F. 22.07.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/stuopro-ba-1fach-islam-relig-studien-juli2015.md`](../pruefungsordnungen/philosophische-fakultaet/ein-fach-bachelor/stuopro-ba-1fach-islam-relig-studien-juli2015.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### 29. August 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/1aes-european-ma-lexicography.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/1aes-european-ma-lexicography.md)

**Pflichtmodule (13):**
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

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/6aesa-ba-ma-psychologie.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/6aesa-ba-ma-psychologie.md)

**Pflichtmodule (4):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M 1Multivariate Statistik
- M 2Forschungsmethoden
- M 3Psychologische Diagnostik

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20200911.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20200911.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20200911.md)

**Pflichtmodule (4):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1Multivariate Statistik
- M2Forschungsmethoden
- M3Psychologische Diagnostik

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20210806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20210806.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20210806.md)

**Pflichtmodule (4):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1Multivariate Statistik
- M2Forschungsmethoden
- M3Psychologische Diagnostik

### BSc-MSc Psychologie BMStPO-PSL 20070928 i.d.F. 20220328.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20220328.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20070928-idf-20220328.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20220328 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20220328-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20220328-aes.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Fhthd
- orscungsmeoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20240229.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240229.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240229.md)

**Pflichtmodule (5):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Forschungsmethoden
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20240926.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240926.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20240926.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822 i.d.F. 20241219.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822-idf-20241219.md)

**Pflichtmodule (5):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Forschungsmethoden
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### BSc-MSc Psychologie BMStPO-PSL 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/bsc-msc-psychologie-bmstpo-psl-20230822.md)

**Pflichtmodule (6):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M1 Multivariate Statistik
- M2 Fhhd
- orscungsmetoen
- M3 Psychologische Diagnostik I
- M4 Psychologische Diagnostik II

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20190308.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190308.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190308.md)

**Pflichtmodule (13):**
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

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20190723.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190723.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20190723.md)

**Pflichtmodule (13):**
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

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20230223.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230223.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230223.md)

**Pflichtmodule (13):**
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

### European MA Lexicography  MPOEMLex 20090904 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230731.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20090904-idf-20230731.md)

**Pflichtmodule (13):**
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

### European MA Lexicography  MPOEMLex 20190723 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20190723-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20190723-aes.md)

**Pflichtmodule (13):**
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

### European MA Lexicography  MPOEMLex 20230223 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20230223-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/european-ma-lexicography-mpoemlex-20230223-aes.md)

**Pflichtmodule (13):**
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

**Pflichtmodule (6):**
- psychologischen
- Diagnostik
- Diagnostische
- Verfahren
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 04.06.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-20ba-ma-psychojuni2010.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-20ba-ma-psychojuni2010.md)

**Pflichtmodule (5):**
- psychologischen Diagnostik
- Diagnostische
- Verfahren
- Klinische
- Psychologie

### PDF vom 28.09.2007 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-ba-ma-psycho-bmstpo-psl-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-ba-ma-psycho-bmstpo-psl-aug2017.md)

**Pflichtmodule (4):**
- Pflichtmodule Methodenfächer: Es sind alle Module zu absolvieren.
- M 1Multivariate Statistik
- M 2Forschungsmethoden
- M 3Psychologische Diagnostik

### PDF vom 28.09.2007 i.d.F. 31.07.2012

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-ba-ma-psycho-juli2012.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/prostuo-ba-ma-psycho-juli2012.md)

**Pflichtmodule (7):**
- psychologischen Diagnostik
- Diagnostische
- Verfahren
- Klinische
- Psychologie
- M14 Hauptformen der
- Psychotherapie

### PDF vom 04.09.2009 i.d.F. 29.08.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/stuopro-ma-lexicography-aug2016.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge-eigenstaendige-po-und-konsekutiv/stuopro-ma-lexicography-aug2016.md)

**Pflichtmodule (13):**
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

### 9. März 2011

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-20ma-komparatroman.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-20ma-komparatroman.md)

**Pflichtmodule (3):**
- (8) Basismodul Sprachpraxis
- (4) Elementarkurs 1
- (4) Elementarkurs 2

### 28. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-ma-nahoststudien.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-ma-nahoststudien.md)

**Pflichtmodule (4):**
- Raum und Region
- Transregionale Themen und Methoden I
- Transregionale Themen und Methoden II
- Forschungskolloquium

### 13. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-ma-philosophie.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aes-ma-philosophie.md)

**Pflichtmodule (2):**
- Masterarbeit Praktische Philo- sophie
- Masterarbeit Theoretische Philosophie

### 6. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-fpo-ma-archaeologwiss.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-fpo-ma-archaeologwiss.md)

**Pflichtmodule (1):**
- sich um eine Empfehlung. Näheres regelt das Modulhandbuch.

### 2. März 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-ma-mittelalterfrueheneuzeit.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/2aesa-ma-mittelalterfrueheneuzeit.md)

**Pflichtmodule (12):**
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

**Pflichtmodule (2):**
- Basismodul Französische Sprachpraxis 1
- Basismodul Französische Sprachpraxis 2

### 26. Januar 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-theaterpaedagogik.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/3aes-ma-theaterpaedagogik.md)

**Pflichtmodule (16):**
- Grundlagen und Rahmen
- der Theaterpädagogik
- Theaterwissenschaft I: Dimensionen des Theatralen und Performativen
- Kulturpädagogik II: Handlungsfelder und Hand- lungsformen
- Angewandte theaterpäda- gogische Forschung
- Theaterwissenschaft II: Kulturen, Funktionen und Wahrnehmungsformen der theatralen Praktiken
- Theaterpädagogische Pra- xisreflexion
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

**Pflichtmodule (4):**
- Sprachnorm und Variation (I LING)
- Systematische Aspekte NDL (I NDL)
- Systematische Aspekte ÄDL (I MED)
- Es sind Aufbaumodule im

### 3. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aes-ma-mittelneulatein.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/4aes-ma-mittelneulatein.md)

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

**Pflichtmodule (6):**
- Basismodul Aktuelle Interkulturalitäts- und Intermedialitätstheorien
- América Latina: Cultura y literatura
- Modul 4: Sprachpraxis Sprache A: Es ist ein Modul zur Erweiterung bestehender Kenntnisse in der Schwerpunktsprache
- Französisch als Sprache A
- Italienischals Sprache A
- Spanischals Sprache A

### 24. August 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/6aesa-ma-fpo-englstudies.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/6aesa-ma-fpo-englstudies.md)

**Pflichtmodule (6):**
- Masterarbeit
- MA Thesis Module: Linguistics and Applied Linguistics
- Masterarbeit:Es ist eines der beiden Module zu wählen.
- Masterarbeit im Schwerpunkt Culture and Literature
- MA Thesis Module: Culture and Literature
- Masterarbeit im Schwerpunkt Linguistics and Applied Linguistics

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

**Pflichtmodule (2):**
- Masterarbeit
- MA Thesis

### PDF vom 08.06.2010 i.d.F. 24.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-aug2017.md)

**Pflichtmodule (6):**
- Masterarbeit
- MA Thesis Module: Linguis- tics and Applied Linguistics
- Masterarbeit:Es ist eines der beiden Module zu wählen.
- Masterarbeit im Schwerpunkt Culture and Literature
- MA Thesis Module: Culture and Literature
- Masterarbeit im Schwerpunkt Linguistics and Applied Linguistics

### PDF vom 08.06.2010 i.d.F. 07.03.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-maerz2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-englstudies-maerz2017.md)

**Pflichtmodule (2):**
- Masterarbeit
- MA Thesis

### PDF vom 08.06.2010 i.d.F. 28.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-germanistik-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-germanistik-juli2014.md)

**Pflichtmodule (4):**
- Sprachnorm und Variation (I LING)
- Systematische Aspekte NDL (I NDL)
- Systematische Aspekte ÄDL (I MED)
- Es sind Aufbaumodule im Umfang von insgesamt 30 ECTS-Punkten zu wählen.

### PDF vom 08.06.2010 i.d.F. 13.06.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2014.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2014.md)

**Pflichtmodule (2):**
- Basismodul Französi- sche Sprachpraxis 1
- Basismodul Französi- sche Sprachpraxis 2

### PDF vom 08.06.2010 i.d.F. 11.06.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2015.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-komparatromanistik-juni2015.md)

**Pflichtmodule (2):**
- Basismodul Französi- sche Sprachpraxis 1
- Basismodul Französi- sche Sprachpraxis 2

### PDF vom 08.06.2010 i.d.F. 08.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-aug2017.md)

**Pflichtmodule (4):**
- Grundlagen der Museologie
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul

### PDF vom 08.06.2010 i.d.F. 02.10.2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-okt2013.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-kunstgesch-okt2013.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-aug2017.md)

**Pflichtmodule (12):**
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

### PDF vom 08.06.2010 i.d.F. 02.03.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-maerz2017.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelalterfrueheneuzeit-maerz2017.md)

**Pflichtmodule (12):**
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

### PDF vom 08.06.2010 i.d.F. 03.08.3015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelneulatein-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-mittelneulatein-aug2015.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 08.06.2010 i.d.F. 28.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-nahoststudien-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fachstuopro-ma-nahoststudien-juli2014.md)

**Pflichtmodule (4):**
- Raum und Region
- Transregionale Themen und Methoden I
- Transregionale Themen und Methoden II
- Forschungskolloquium

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

**Pflichtmodule (16):**
- Grundlagen und Rahmen
- der Theaterpädagogik
- Theaterwissenschaft I: Dimensionen des Theatralen und Performativen
- Kulturpädagogik II: Handlungsfelder und Hand- lungsformen
- Angewandte theaterpäda- gogische Forschung
- Theaterwissenschaft II: Kulturen, Funktionen und Wahrnehmungsformen der theatralen Praktiken
- Theaterpädagogische Pra- xisreflexion
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

**Pflichtmodule (1):**
- Masterarbeit

### FPO MA DH 20250411.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-dh-20250411.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-dh-20250411.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 15.05.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-islamisch-relig-studien.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-islamisch-relig-studien.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 18.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-kunstvermittlung.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-kunstvermittlung.md)

**Pflichtmodule (4):**
- Grundlagen der Psychologie für Nichtpsychologen (Importmodul)
- Der Mensch im Spiegel des künst- lerischen Handelns
- Methoden der empirischen Bil- dungsforschung (Importmodul)
- Masterarbeit

### FPO MA L.D. 20230223 i.d.F. 20250320.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-l-d-20230223-idf-20250320.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-l-d-20230223-idf-20250320.md)

**Pflichtmodule (7):**
- Wissenschaftliches Basismodul
- Educational Techno- logy
- Praxis Digital Educa- tion
- Lernumgebungen
- E-Assessment
- Masterarbeit
- Masterabschluss- Modul

### FPO MA L.D. 20230223.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-l-d-20230223.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/fpo-ma-l-d-20230223.md)

**Pflichtmodule (8):**
- Wissenschaftliches Basismodul
- Educational Techno- logy
- Praxis Digital Educa- tion
- Lernumgebungen
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

**Pflichtmodule (16):**
- Pädagogik
- Kulturpädagogische Grundlagen und Dynamiken
- Kunstgeschichte
- Kunst(geschichte) + Mu- seum I
- Kunst(geschichte) + Mu- seum II
- Kunstpädagogik
- Kunst & Bildung
- Künstlerische Praxis 1
- Künstlerische Praxis 2
- Vermittlungspraxis
- Forschungsmethoden
- Einführung in die soziologi- sche Methodenlehre (SozM-E)
- Vertiefung Soziologische Methodenlehre (SozM-V)
- Kulturpädagogische Grund- lagen und Dynamiken
- Kunst(geschichte) + Mu- seum I-II
- Kunst(geschichte) + Mu- seum III

### M.A. Learning Design ÄSa 20250320 20250702 .pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/m-a-learning-design-aesa-20250320-20250702.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/m-a-learning-design-aesa-20250320-20250702.md)

**Pflichtmodule (4):**
- Wissenschaftliches Basismodul
- Educational Technology
- Praxis Digital Education
- Lernumgebungen

### MA Antike Sprachen und Kulturen FPOAnSK 20100608 i.d.F. 20190326.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20190326.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20190326.md)

**Pflichtmodule (9):**
- Pflichtmodul für alle Studienrichtungen
- Motive und Formen
- Indogermanistik und Indoiranistik
- Basisbereich Indogermanistik und Indoiranistik2
- Fragestellungen und Geschichte der Indogermanistik
- Mykenisch und die griechischen Dialekte4
- Indoiranisch
- Historische Linguistik und Sprachwandel (II LING 2)
- Masterarbeit

### MA Antike Sprachen und Kulturen FPOAnSK 20100608 i.d.F. 20210222.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20210222.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20100608-idf-20210222.md)

**Pflichtmodule (9):**
- Pflichtmodul für alle Studienrichtungen
- Motive und Formen
- Indogermanistik und Indoiranistik
- Basisbereich Indogermanistik und Indoiranistik2
- Fragestellungen und Geschichte der Indogermanistik
- Mykenisch und die griechischen Dialekte4
- Indoiranisch
- Historische Linguistik und Sprachwandel (II LING 2)
- Masterarbeit

### MA Antike Sprachen und Kulturen FPOAnSK 20190326 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20190326-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20190326-aes.md)

**Pflichtmodule (8):**
- Pflichtmodul für alle Studienrichtungen
- Motive und Formen
- Indogermanistik und Indoiranistik
- Basisbereich Indogermanistik und Indoiranistik2
- Fragestellungen und Geschichte der Indogermanistik
- Mykenisch und die griechischen Dialekte4
- Indoiranisch
- Historische Linguistik und Sprachwandel (II LING 2)

### MA Antike Sprachen und Kulturen FPOAnSk 20250131.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20250131.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-antike-sprachen-und-kulturen-fpoansk-20250131.md)

**Pflichtmodule (9):**
- Pflichtmodul für alle Studienrichtungen
- Motive und Formen
- Indogermanistik und Indoiranistik
- Basisbereich Indogermanistik und Indoiranistik2
- Fragestellungen und Geschichte der Indogermanistik
- Mykenisch und die griechischen Dialekte4
- Indoiranisch
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

**Pflichtmodule (8):**
- Wissenschaftstheorie
- Transformationsprozesse
- Kernmodul 1: Medienkommunikation
- Kernmodul 2: Medienwirtschaft
- Projekt
- Projektarbeit
- Forschungsperspektiven
- Masterarbeit

### MA Buchwissenschaft FPOBuWi 20230223 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpobuwi-20230223-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-buchwissenschaft-fpobuwi-20230223-aes.md)

**Pflichtmodule (5):**
- Kernmodul 1: Rahmenbedingungen
- Kernmodul 2: Praktiken
- Projekt
- Projektarbeit
- Masterarbeit

### MA DEIS FPODEIS 20100608 i.d.F. 20180221.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20180221.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20180221.md)

**Pflichtmodule (13):**
- Development Economics I
- Development Economics II
- International Economics I
- International Economics II
- Research Methods I
- Research Methods II
- International Business Ethics I
- International Business Ethics II
- Regionale Vertiefung gemäß § 5 (10 ECTS)
- Regional Module I
- Regional Module II
- Masterarbeit
- Master Thesis

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
- Regionale Vertiefung gemäß § 5 (10 ECTS)
- Regional Module I
- Regional Module II

### MA DEIS FPODEIS 20100608 i.d.F. 20200408.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20200408.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-deis-fpodeis-20100608-idf-20200408.md)

**Pflichtmodule (13):**
- Development Economics I
- Development Economics II
- International Economics I
- International Economics II
- Research Methods I
- Research Methods II
- International Business Ethics I
- International Business Ethics II
- Regionale Vertiefung gemäß § 5 (10 ECTS)
- Regional Module I
- Regional Module II
- Masterarbeit
- Master Thesis

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
- Regionale Vertiefung gemäß § 5 (10 ECTS)
- Regional Module I
- Regional Module II
- Masterarbeit
- Master Thesis

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
- Regionale Vertiefung gemäß § 5 (10 ECTS)
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

**Pflichtmodule (8):**
- Masterarbeit
- MA Thesis Module:
- Masterarbeit:Es ist eines der beiden Module zu wählen.
- Masterarbeit im Schwerpunkt Culture and Literature
- MA Thesis Module: Culture and Literature
- Masterarbeit im Schwerpunkt Linguistics and Applied Linguistics
- MA Thesis Module: Linguistics and Applied Linguistics
- W ETPk

### MA Germanistik 20100608 i.d.F. 20180213.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20180213.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-germanistik-20100608-idf-20180213.md)

**Pflichtmodule (10):**
- Sprachnorm und Variation (I LING)
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

**Pflichtmodule (18):**
- Fachmodulegemäß§ 5
- Fachmodul I2)
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

**Pflichtmodule (22):**
- Fachmodul I2)
- Fachmodul II2)
- Fachmodul III
- Profilbereich (gem. FPO § 3 Abs. 2)
- Profilmodul Germanistische Linguistik3)
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

**Pflichtmodule (22):**
- Fachmodul I2)
- Fachmodul II2)
- Fachmodul III
- Profilbereich (gem. FPO § 3 Abs. 2)
- Profilmodul Germanistische Linguistik3)
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

**Pflichtmodule (10):**
- Sprachnorm und Variation (I LING)
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
- Fachmodule gemäß § 5
- Fachmodul I2)
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

**Pflichtmodule (26):**
- Fachmodul I2)
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
- Fachmodule gemäß § 5
- Fachmodul I2)
- Fachmodul II2)
- Fachmodul III
- Profilbereich (gem. FPO § 3 Abs. 2)
- Profilmodul Germanistische Linguistik3)
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

**Pflichtmodule (4):**
- Grundlagen der Museologie
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul

### MA Kunstgeschichte MFPOKunstGesch 20100608 i.d.F. 20200214.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20100608-idf-20200214.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20100608-idf-20200214.md)

**Pflichtmodule (5):**
- Grundlagen der Museologie I
- Grundlagen der Museologie II
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul

### MA Kunstgeschichte MFPOKunstGesch 20200214 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20200214-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20200214-aes.md)

**Pflichtmodule (5):**
- Grundlagen der Museologie I
- Grundlagen der Museologie II
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul

### MA Kunstgeschichte MFPOKunstGesch 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-kunstgeschichte-mfpokunstgesch-20230822.md)

**Pflichtmodule (5):**
- Grundlagen der Museologie I
- Grundlagen der Museologie II
- Grundlagen der Informatik
- Masterarbeit
- Mastermodul

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

**Pflichtmodule (4):**
- Interdisziplinäres Basismodul zur Einführung in den Theoriekomplex Literatur/Kultur/Medien
- Basismodul Aktuelle Interkulturalitäts- und Intermedialitätstheorien
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität
- Masterarbeit

### MA Literaturstudien FPOLitStud 20240430.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-fpolitstud-20240430.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-fpolitstud-20240430.md)

**Pflichtmodule (8):**
- Interdisziplinäres Basismodul zur Einführung in den Theoriekomplex Literatur/Kultur/Medien
- Einführungsmodul: Theorien und Methoden
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität
- Kernfachgemäß§ 41)
- Masterarbeit im Kernfach
- Masterarbeit
- Interdisziplinäres Basismodul zur Einführung in den Theorienkomplex Literatur/Kultur/Medien
- mind .

### MA Literaturstudien MFPOLitStud 20180515 Äs.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-mfpolitstud-20180515-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-literaturstudien-mfpolitstud-20180515-aes.md)

**Pflichtmodule (4):**
- Interdisziplinäres Basismodul zur Einführung in den Theoriekomplex Literatur/Kultur/Medien
- Basismodul Aktuelle Interkulturali- täts- und Intermedialitätstheorien
- Interdisziplinäres Basismodul zur konkreten Analyse von Medialität und Kulturalität
- Masterarbeit

### MA Mittelalter und Frühe Neuzeit FPOMiFNZ 20100608 i.d.F. 20190809.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20100608-idf-20190809.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20100608-idf-20190809.md)

**Pflichtmodule (12):**
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

### MA Mittelalter und Frühe Neuzeit FPOMiFNZ 20240131.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20240131.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-mittelalter-und-fruehe-neuzeit-fpomifnz-20240131.md)

**Pflichtmodule (12):**
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

### MA Nahoststudien FPONahOstStud 20100608 i.d.F. 20180817 .pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20100608-idf-20180817.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20100608-idf-20180817.md)

**Pflichtmodule (5):**
- Raum und Region
- Transregionale Themen und Methoden I
- Transregionale Themen und Methoden II
- Forschungskolloquium
- Masterarbeit

### MA Nahoststudien FPONahOstStud 20180817 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20180817-aes.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20180817-aes.md)

**Pflichtmodule (5):**
- Raum und Region
- Transregionale Themen und Methoden I
- Transregionale Themen und Methoden II
- Forschungskolloquium
- Masterarbeit

### MA Nahoststudien FPONahOstStud 20230822.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20230822.md`](../pruefungsordnungen/philosophische-fakultaet/masterstudiengaenge/ma-nahoststudien-fponahoststud-20230822.md)

**Pflichtmodule (6):**
- Pflichtbereich(40 ECTS-Punkte)
- Raum und Region
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

**Pflichtmodule (5):**
- Kernmodul 1: Rahmenbedingungen
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

### PO Zusatzstudien Gender 20260305.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/po-zusatzstudien-gender-20260305.md`](../pruefungsordnungen/philosophische-fakultaet/modulstudien-und-zusatzstudien/po-zusatzstudien-gender-20260305.md)

**Pflichtmodule (2):**
- Basismodul: Was ist Gender?
- Gender in Natur- und Technik- wissenschaften

### 7. Dezember 2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/2aenderungssatzung-ma-20medienethikreligion.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/2aenderungssatzung-ma-20medienethikreligion.md)

**Pflichtmodule (2):**
- Grundlagen der Kommunikationswissenschaft
- Oder:Vertiefung Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach)

### 13. November 2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/3aes-ma-medien-ethik-religion.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/3aes-ma-medien-ethik-religion.md)

**Pflichtmodule (4):**
- Grundlagen der Kommunikations‐ oder Medienwissenschaft (Importmodul)
- _Oder_: Vertiefung der Kommunikations‐ oder Medienwissenschaft (je nach bisherigem Studienfach1) (Importmodul)
- Medienethik
- Medienkunde, Journalismus und PR/Öffentlichkeitsarbeit

### Evangelische Theologie StuPO EvTheol 20150811 i.d.F. 20200916.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20200916.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20200916.md)

**Pflichtmodule (16):**
- Basismodule (Pflichtbereich)
- Propädeuticum
- Propäd – Grundlagen des Theologiestudiums / Pro- pädeuticum
- Fächergruppe AT/NT:Es muss ein Basismodul AT und ein Basismodul NT absolviert werden. Dabei muss mindestens in einem der beiden Module die Leistungsvariante A (12 ECTS- Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- AT1-A – Basismodul
- Altes Testament
- AT1-B – Basismodul Altes Testament
- NT1-A – Basismodul
- Neues Testament
- NT1-B – Basismodul Neues Testament
- Fächergruppe ST/KG:Es muss ein Basismodul KG und ein Basismodul ST absolviert werden. Dabei muss mindestens in einem der beiden Module die Leistungsvariante A (12 ECTS- Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- KG1-A – Basismodul
- Kirchengeschichte4
- KG1-B – Basismodul Kirchengeschichte4
- ST1-A – Basismodul Systematische Theologie
- ST1-B – Basismodul Systematische Theologie

### Evangelische Theologie StuPO EvTheol 20150811 i.d.F. 20230314.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20230314.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20150811-idf-20230314.md)

**Pflichtmodule (16):**
- Basismodule (Pflichtbereich)
- Propädeuticum
- Propäd – Grundlagen des Theologiestudiums / Pro- pädeuticum
- Fächergruppe AT/NT:Es muss ein Basismodul AT und ein Basismodul NT absolviert werden. Dabei muss mindestens in einem der beiden Module die Leistungsvariante A (12 ECTS- Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- AT1-A – Basismodul
- Altes Testament
- AT1-B – Basismodul Altes Testament
- NT1-A – Basismodul
- Neues Testament
- NT1-B – Basismodul Neues Testament
- Fächergruppe ST/KG:Es muss ein Basismodul KG und ein Basismodul ST absolviert werden. Dabei muss mindestens in einem der beiden Module die Leistungsvariante A (12 ECTS- Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- KG1-A – Basismodul
- Kirchengeschichte4
- KG1-B – Basismodul Kirchengeschichte4
- ST1-A – Basismodul Systematische Theologie
- ST1-B – Basismodul Systematische Theologie

### Evangelische Theologie StuPO EvTheol 20200916 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20200916-aes.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/evangelische-theologie-stupo-evtheol-20200916-aes.md)

**Pflichtmodule (16):**
- Basismodule (Pflichtbereich)
- Propädeuticum
- Propäd – Grundlagen des Theologiestudiums / Pro- pädeuticum
- Fächergruppe AT/NT:Es muss ein Basismodul AT und ein Basismodul NT absolviert werden. Dabei muss mindestens in einem Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- AT1-A – Basismodul
- Altes Testament
- AT1-B – Basismodul Altes Testament
- NT1-A – Basismodul
- Neues Testament
- NT1-B – Basismodul Neues Testament
- Fächergruppe ST/KG:Es muss ein Basismodul KG und ein Basismodul ST absolviert werden. Dabei muss mindestens in einem Punkte) gewählt werden. In Summe sind Module im Umfang von mindestens 19 (und maximal 24) ECTS-Punkten zu wählen.
- KG1-A – Basismodul
- Kirchengeschichte4
- KG1-B – Basismodul Kirchengeschichte4
- ST1-A – Basismodul Systematische Theologie
- ST1-B–Basismodul

### MA Christliche Medienkommunikation FPO C-M-K 20150611 i.d.F. 20180711.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20150611-idf-20180711.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20150611-idf-20180711.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Christliche Medienkommunikation FPO C-M-K 20150611 i.d.F. 20191212.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20150611-idf-20191212.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20150611-idf-20191212.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Christliche Medienkommunikation FPO C-M-K 20180711 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20180711-aes.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-christliche-medienkommunikation-fpo-c-m-k-20180711-aes.md)

**Pflichtmodule (1):**
- Masterarbeit

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20180711.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20180711.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20180711.md)

**Pflichtmodule (14):**
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
- Praxismodul
- Praxisfeld Medien
- Masterarbeit

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20191212.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20191212.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20191212.md)

**Pflichtmodule (14):**
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
- Praxismodul
- Praxisfeld Medien
- Masterarbeit

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20200909.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20200909.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20200909.md)

**Pflichtmodule (12):**
- Grundlagen der Kommunikationswissenschaft
- Grundlagen der Kommunikations- wissenschaft
- Grundzüge der Theologie(Es istgemäß desgewählten Schwerpunkts eines der beiden Module
- Grundzüge der Theologie für Nicht- Theologen (ChristentumundMedien)
- Grundzüge der Theologie für Nicht- Theologen (IslamundMedien)
- Medienethik
- Mediensysteme/Journalismus(Es sind alle Module zu belegen)
- Mediensysteme, Journalismus und Öffentlichkeitsarbeit
- Praxismodul
- Praxisfeld Medien
- Masterarbeit
- Grundzüge der Theologie(Es ist gemäß des gewählten Schwerpunkts eines der beiden Module zu belegen)

### MA Medien-Ethik-Religion FPO M-E-R 20081209 i.d.F. 20230731.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20230731.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20081209-idf-20230731.md)

**Pflichtmodule (13):**
- Grundlagen der Kommunikationswissenschaft
- Grundlagen der Kommunikations- wissenschaft
- Grundzüge der Theologie(Es istgemäß desgewählten Schwerpunkts eines der beiden Module
- Grundzüge der Theologie für Nicht- Theologen (Christentum und Medien)
- Grundzüge der Theologie für Nicht- Theologen (Islam und Medien)
- Medienethik
- Mediensysteme/Journalismus(Es sind alle Module zu belegen)
- Mediensysteme, Journalismus und Öffentlichkeitsarbeit
- Praxismodul
- Praxisfeld Medien
- Masterarbeit
- Grundzüge der Theologie(Es ist gemäß des gewählten Schwerpunkts eines der beiden Module zu belegen)
- Mediensysteme/Journalismus

### MA Medien-Ethik-Religion FPO M-E-R 20180711 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20180711-aes.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20180711-aes.md)

**Pflichtmodule (14):**
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
- Praxismodul
- Praxisfeld Medien
- Masterarbeit

### MA Medien-Ethik-Religion FPO M-E-R 20200909 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20200909-aes.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20200909-aes.md)

**Pflichtmodule (12):**
- Grundlagen der Kommunikationswissenschaft
- Grundlagen der Kommunikations- wissenschaft
- Grundzüge der Theologie(Es istgemäß desgewählten Schwerpunkts eines der beiden Module
- Grundzüge der Theologie für Nicht- Theologen (ChristentumundMedien)
- Grundzüge der Theologie für Nicht- Theologen (IslamundMedien)
- Medienethik
- Mediensysteme/Journalismus(Es sind alle Module zu belegen)
- Mediensysteme, Journalismus und Öffentlichkeitsarbeit
- Praxismodul
- Praxisfeld Medien
- Masterarbeit
- Grundzüge der Theologie(Es ist gemäß des gewählten Schwerpunkts eines der

### MA Medien-Ethik-Religion FPO M-E-R 20240904.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20240904.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/ma-medien-ethik-religion-fpo-m-e-r-20240904.md)

**Pflichtmodule (15):**
- Grundlagen – Methoden - Kate- gorien
- Grundzüge der Theologie(Es istgemäß desgewählten Schwerpunkts eines der beiden Module
- Grundlagen im Schwerpunkt Religion (Christentum und Me- dien): Grundzüge der Theologie und Kirchenkunde für Nichttheolo- gen
- Grundlagen im Schwerpunkt Religion (Islam und Medien): Grundzüge des Islam
- Medienethik
- Grundlagen: Medienethik
- Mediensysteme/Journalismus(Es sind alle Module zu belegen)
- Grundlagen Medienpraxis: Journalismus, Öffentlichkeitsar- beit, Social Media
- Praxismodul2
- Vertiefung Medienpraxis: Pra- xisfeld (digitale) Medien
- max. 42
- Grundzüge der Theologie(Es ist gemäß des gewählten Schwerpunkts eines der beiden Module zu belegen)
- Grundlagen im Schwerpunkt Religion (Christentum und Me- dien): Grundzüge der Theolo- gie und Kirchenkunde für Nicht- theologen
- Mediensysteme/Journalismus
- Praxismodul

### PDF vom 09.12.2008

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-20ma-medien-ethik-relig.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-20ma-medien-ethik-relig.md)

**Pflichtmodule (5):**
- Grundlagen der Kommunikations- wissenschaft (Import)
- Medienethik und Medienrecht
- Theorie und Praxis des Journalismus
- Öffentlichkeitsarbeit und Präsentation
- Praxismodul

### PDF vom 11.06.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-christliche-medienkommunikation.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-christliche-medienkommunikation.md)

**Pflichtmodule (1):**
- Masterarbeit

### PDF vom 09.12.2008 i.d.F. 05.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-aug2015.md)

**Pflichtmodule (4):**
- Masterarbeit (Christentum und Medien)
- Masterarbeit
- (Islam und Medien)
- Masterarbeit (Islam und Medien)

### PDF vom 09.12.2008 i.d.F. 07.12.2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-dez2010.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-dez2010.md)

**Pflichtmodule (5):**
- Grundlagen der Kommunikationswis- senschaft
- Oder:Vertiefung Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach)
- Medienethik
- Medienkunde und Journalistik
- Praxismodul I

### PDF vom 09.12.2008 i.d.F. 08.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-juli2014.md)

**Pflichtmodule (6):**
- Grundlagen der Kommunikations- oder Medienwissenschaft (Importmodul)
- Oder: Vertiefung der Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach1) (Importmodul)
- Medienethik
- Einführung theologische und religi- onswissenschaft-liche Grundlagen
- Oder: Vertiefungsmodul Theologie3 (Importmodul)
- Praxismodul I

### PDF vom 09.12.2008 i.d.F. 13.11.2013

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-nov2013.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/pro-ma-medien-ethik-relig-nov2013.md)

**Pflichtmodule (4):**
- Grundlagen der Kommunikations‐ oder Medienwissenschaft (Importmodul)
- _Oder_: Vertiefung der Kommunikations‐ oder Medienwissenschaft (je nach bisherigem Studienfach1) (Importmodul)
- Medienethik
- Medienkunde, Journalismus und PR/Öffentlichkeitsarbeit

### PDF vom 09.12.2008 i.d.F. 24.11.2009

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/proma-medienethikrelig.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/proma-medienethikrelig.md)

**Pflichtmodule (5):**
- Grundlagen der Kommunikations- wissenschaft
- Oder:Vertiefung Kommunikations- oder Medienwissenschaft (je nach bisherigem Studienfach)
- Medienethik und Medienrecht
- Theorie und Praxis des Journalis- mus
- Praxismodul I

### PDF vom 11.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/stpo-evangelische-theologie-neu.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/stpo-evangelische-theologie-neu.md)

**Pflichtmodule (9):**
- Grundlagen des Theolo- giestudiums / Propädeuti- cum
- Basismodul Altes Testament
- Basismodul Neues Testament
- Kirchengeschichte
- Basismodul Systematische Theologie
- Basismodul Praktische Theologie
- Basismodul Theoriebegleitetes Prakti- kum
- Interdisziplinäres Basismodul
- Basismodul Religionswissenschaft

### PDF vom 27. Juli 2012

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/stuo-magister-20theologiae.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/stuo-magister-20theologiae.md)

**Pflichtmodule (9):**
- Grundlagen des Theologie- studiums/ Propädeuticum
- Basismodul Altes Testa- ment
- Basismodul Neues Testa- ment
- Kirchen- geschichte
- Basismodul Systematische Theologie
- Basismodul Praktische Theologie
- Basismodul Gemeinde- praktikum
- Inter- disziplinäres Basismodul
- Basismodul Religions- wissenschaft

### PDF vom 25.09.1980 i.d.F. 28.12.2004

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/theologie/zwischenpruefungso.md`](../pruefungsordnungen/philosophische-fakultaet/theologie/zwischenpruefungso.md)

**Pflichtmodule (13):**
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

### 12. Juni 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/1aesa-wtb-organisations-personalentw.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/1aesa-wtb-organisations-personalentw.md)

**Pflichtmodule (10):**
- Grundlagen der Organisations- und Personalentwicklung
- Grundlagen Organisation
- Konzepte der Organisationsentwicklung
- Umsetzung von Organisationsentwicklungsprozessen
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Umsetzung von Personalentwicklung
- Management und Führung
- Instrumente der Mitarbeiterführung
- Personalmanagement

### 11. August 2010

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/2aes-20wtb-ma-20multimediadidaktik.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/2aes-20wtb-ma-20multimediadidaktik.md)

**Pflichtmodule (5):**
- (2) Referat (einschl. Präsentation)
- Hausaufgabe, Referat (einschl. Präsentation) Hausaufgabe Referat (einschl. Präsentation)
- mündl. Prüfung Referat (einschl. Präsentation)
- mündl. Prüfung
- (1) Hausarbeit

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

**Pflichtmodule (12):**
- Grundlagen der Organisations- und Personalentwicklung
- Grundlagen Organisation
- Konzepte der Organisations- entwicklung
- Umsetzung von Organisations- entwicklungsprozessen
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Umsetzung von Personalentwicklung
- Management und Führung
- Instrumente der Mitarbeiterführung
- Personalmanagement
- VertiefungOrganisations- und Personalentwicklung
- Praktische Vertiefung

### PO MA OEPE 20170307 i.d.F. 20220629.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20170307-idf-20220629.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20170307-idf-20220629.md)

**Pflichtmodule (10):**
- Grundlagen der Organisations- und Personalentwicklung
- Grundlagen Organisation
- Konzepte der Organisations- entwicklung
- Umsetzung von Organisations- entwicklungsprozessen
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Umsetzung von Personalentwicklung
- Management und Führung
- Instrumente der Mitarbeiterführung
- Personalmanagement

### PO MA OEPE 20170307 i.d.F. 20250711.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20170307-idf-20250711.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20170307-idf-20250711.md)

**Pflichtmodule (10):**
- Grundlagen der Organisations- und Personalentwicklung
- Grundlagen Organisation
- Konzepte der Organisations- entwicklung
- Umsetzung von Organisations- entwicklungsprozessen
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Umsetzung von Personalentwicklung
- Management und Führung
- Instrumente der Mitarbeiterführung
- Personalmanagement

### PO MA OEPE 20220629 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20220629-aes.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-ma-oepe-20220629-aes.md)

**Pflichtmodule (10):**
- Grundlagen der Organisations- und Personalentwicklung
- Grundlagen Organisation
- Konzepte der Organisations- entwicklung
- Umsetzung von Organisations- entwicklungsprozessen
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Umsetzung von Personalentwicklung
- Management und Führung
- Instrumente der Mitarbeiterführung
- Personalmanagement

### PDF vom 07.03.2017 i.d.F. 12.06.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-organisationpersonalentw-weiterbld-ma-juni2017.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-organisationpersonalentw-weiterbld-ma-juni2017.md)

**Pflichtmodule (12):**
- Grundlagen der Organisations- und Personalentwicklung
- Grundlagen Organisation
- Konzepte der Organisationsentwicklung
- Umsetzung von Organisationsentwick- lungsprozessen
- Grundlagen Personal
- Konzepte der Personalentwicklung
- Umsetzung von Personalentwicklung
- Management und Führung
- Instrumente der Mitarbeiterführung
- Personalmanagement
- VertiefungOrganisations- und Personalentwicklung
- Praktische Vertiefung

### PDF vom 07.03.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-organisationpersonalentw-weiterbld-ma.md`](../pruefungsordnungen/philosophische-fakultaet/weiterbildungs-und-elitestudiengaenge-sowie-weitere/po-organisationpersonalentw-weiterbld-ma.md)

**Pflichtmodule (12):**
- Grundlagen der Organisations- und Personalentwicklung
- Qualifikationsplanung und Personal- entwicklung
- Grundlagen Organisation
- Konzepte der Organisationsentwicklung
- Umsetzung von Organisationsentwick- lungsprozessen
- Grundlage Personal
- Methoden und Instrumente der Personalentwicklung
- Personalmanagement und Arbeitsrecht
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

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20140718 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20180730.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20180730.md)

**Pflichtmodule (11):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie – Ältere Urgeschichte2
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Prähistorische Archäologie – Jüngere Urgeschichte2
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Klassische Archäologie – Griechische Archäologie2
- Klassische Archäologie: Griechische Archäologie I A
- Bachelorarbeit und –prüfung
- Bachelorarbeit5

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20140718 i.d.F. 20190220.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20190220.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20140718-idf-20190220.md)

**Pflichtmodule (11):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie – Ältere Urgeschichte2
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Prähistorische Archäologie – Jüngere Urgeschichte2
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Klassische Archäologie – Griechische Archäologie2
- Klassische Archäologie: Griechische Archäologie I A
- Bachelorarbeit und -prüfung
- Bachelorarbeit5

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20180730 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20180730-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20180730-aes.md)

**Pflichtmodule (9):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie – Ältere Urgeschichte2
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Prähistorische Archäologie – Jüngere Urgeschichte2
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Bachelorarbeit und -prüfung
- Bachelorarbeit5

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20190220 ÄS zu 2ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20190220-aes-zu-2aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20190220-aes-zu-2aes.md)

**Pflichtmodule (17):**
- Basismodule: Kulturentwicklung und Kulturgeschichte
- Prähistorische Archäologie – Ältere Urgeschichte2
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Prähistorische Archäologie – Jüngere Urgeschichte2
- Prähistorische Archäologie: Jüngere Urgeschichte I A
- Prähistorische Archäologie: Jüngere Urgeschichte I B
- Klassische Archäologie – Griechische Archäologie2
- Klassische Archäologie: Griechische Archäologie I A
- Klassische Archäologie: Griechische Archäologie I B
- Klassische Archäologie – Römische Archäologie2
- Klassische Archäologie: Römische Archäologie I A
- Klassische Archäologie: Italisch-römische Archäologie I B
- Christliche Archäologie – Kulturgeschichte2
- Christliche Archäologie: Kulturgeschichte I A
- Bachelorarbeit und -prüfung
- Bachelorarbeit5

### 2-Fach-BA Archäologische Wissenschaften FPO Archäol Wiss Zwei-Fach 20240430.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20240430.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-archaeologische-wissenschaften-fpo-archaeol-wiss-zwei-fach-20240430.md)

**Pflichtmodule (9):**
- Basismodule: Kulturentwicklung und Kulturgeschichte2
- Prähistorische Archäologie – Ältere Urgeschichte
- Prähistorische Archäologie: Ältere Urgeschichte I A
- Prähistorische Archäologie: Ältere Urgeschichte I B
- Prähistorische Archäologie – Jüngere Urgeschichte
- Bachelorarbeit im Erstfach (Archäologische Wissenschaften)
- Bachelorarbeit
- Basismodule: Kulturentwicklung und Kulturgeschichte3
- Bachelorarbeit im Erstfach

### 2-Fach-BA Computerlinguistik FPO CompLing 20071005 i.d.F. 20220411.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-computerlinguistik-fpo-compling-20071005-idf-20220411.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-computerlinguistik-fpo-compling-20071005-idf-20220411.md)

**Pflichtmodule (13):**
- Grundlagen der Computerlinguistik I (traditionelle Verfahren)
- Programmierung und Infrastrukturen I
- Grundlagen der Computerlinguistik II (statistische Verfahren)
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

**Pflichtmodule (10):**
- Grundlagen der Informatik
- Konzeptionelle Modellierung
- Mathematik für Naturwissen- schaftler
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende2
- Grundlagen der Logik in der Informatik2
- Mathematische Modell- bildung und Statistik für Naturwissenschaftler
- DH-Modul 1: Schwerpunkt Sprache und Text
- DH-Modul 2: Schwerpunkt Gesellschaft und Raum
- DH-Modul 3: Schwerpunkt Bild und Medien
- Praxis-/Projektmodul

### 2-Fach-BA English and American Studies 20071004 i.d.F. 20200124.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20071004-idf-20200124.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20071004-idf-20200124.md)

**Pflichtmodule (16):**
- Basismodule: 35 ECTS-Punkte
- Basismodul I _Language_
- Basismodul II _Linguistics_(A)
- Basismodul III3 _Linguistics_(B)
- Basismodul IV _Literature_(A)
- Basismodul V _Literature_(B)
- Basismodul VI _Culture_(A)
- Basismodul VII _Culture_ (B)
- Studienrichtung_American Studies_: 45 ECTS-Punkte (vgl. § 4a)**
- Zwischenmodul I _Culture_
- Import-Kombi-Modul _Politics & Culture_
- Bachelorarbeit im Erstfach (_English and American Studies_) **
- Bachelorarbeit10
- Basismodul III4 _Linguistics_(B)
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA English and American Studies 20200124 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20200124-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20200124-aes.md)

**Pflichtmodule (17):**
- Basismodule: 35 ECTS-Punkte
- Basismodul I _Language_
- Basismodul II _Linguistics_(A)
- Basismodul III3 _Linguistics_(B)
- Basismodul IV _Literature_(A)
- Basismodul V _Literature_(B)
- Basismodul VI _Culture_(A)
- Basismodul VII _Culture_ (B)
- Studienrichtung_American Studies_: 45 ECTS-Punkte (vgl.**
- Zwischenmodul I _Culture_
- Import-Kombi-Modul _Politics & Culture_
- Bachelorarbeit im Erstfach (_English and American Studies_) **
- Bachelorarbeit10
- Basismodul III4 _Linguistics_(B)
- Studienrichtung_American Studies_: 35 ECTS-Punkte (vgl.**
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA English and American Studies 20250930.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20250930.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-english-and-american-studies-20250930.md)

**Pflichtmodule (17):**
- Basismodule: 35 ECTS-Punkte
- Basismodul I Language
- Basismodul II Linguistics (A)
- Basismodul III3 Linguistics (B)
- Basismodul IV Literature (A)
- Basismodul V Literature (B)
- Basismodul VI Culture (A)
- Basismodul VII Culture (B)
- Studienrichtung American Studies: 45 ECTS-Punkte (vgl.§ 5)
- Zwischenmodul I Culture
- Import-Kombi-Modul Politics & Culture
- Bachelorarbeit im Erstfach (English and American Studies)
- Bachelorarbeit10
- Basismodul III4 Linguistics (B)
- Studienrichtung American Studies: 35 ECTS-Punkte (vgl. § 4a)
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA FPO BA SKAND 20071004 i.d.F. 20190520.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20190520.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20190520.md)

**Pflichtmodule (11):**
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

### 2-Fach-BA FPO BA SKAND 20071004 i.d.F. 20211201.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20211201.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-fpo-ba-skand-20071004-idf-20211201.md)

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
- Bachelorarbeit im Erstfach (Skandinavistik)
- Abschlussmodul Bachelorarbeit
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
- Basismodule (40 ECTS-Punkte)
- Nordische Erstsprache 25
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA Frankoromanistik 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-20210624-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-20210624-aes.md)

**Pflichtmodule (7):**
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Französische Sprachpraxis 32
- Bachelorarbeit im Erstfach (Frankoromanistik)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA Frankoromanistik FPO BA Frankorom 20071004 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-fpo-ba-frankorom-20071004-idf-20210624.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-frankoromanistik-fpo-ba-frankorom-20071004-idf-20210624.md)

**Pflichtmodule (7):**
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Französische Sprachpraxis 32
- Bachelorarbeit im Erstfach (Frankoromanistik)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA Germanistik FPO BA Germ 20071004 i.d.F. 20220914.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-ba-germ-20071004-idf-20220914.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-ba-germ-20071004-idf-20220914.md)

**Pflichtmodule (14):**
- Ling BM-1 Grundlagen der germanistischen Linguistik
- Lit BM Grundlagen des wissenschaftlichen Arbeitens in der Literaturwissen- schaft
- NdL BM-1 Grundlagen der Neueren deutschen Literaturwissenschaft 1
- Ling BM-2 Grundlagen der historischen Linguistik
- Med BM Grundlagen der Germanistischen Mediävistik
- NdL BM-2 Grundlagen der Neueren deutschen Literaturwissenschaft2
- Bachelorarbeit im Erstfach (Germanistik)
- Abschlussmodule5
- Ling Finit Abschlussmodul Bachelorarbeit Linguistik
- NdL Finit Abschlussmodul Bachelorarbeit Neuere deutsche Literaturwissen- schaft
- NdL BM-1 Grundlagen der Neueren deutschen Literaturwissenschaft1
- NdL BM-2 Grundlagen der Neueren deutschen Literaturwissenschaft 2
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA Germanistik FPO BA Germ 20260115.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-ba-germ-20260115.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-ba-germ-20260115.md)

**Pflichtmodule (13):**
- Ling BM-1 Grundlagen der germanistischen Linguistik
- Lit BM Grundlagen des wissenschaftlichen Arbeitens in der Literaturwissen- schaft
- NdL BM-1 Grundlagen der Neueren deutschen Literaturwissenschaft 1
- Ling BM-2 Grundlagen der historischen Linguistik
- Med BM Grundlagen der Germanistischen Mediävistik
- NdL BM-2 Grundlagen der Neueren deutschen Literaturwissenschaft2
- Bachelorarbeit im Erstfach(Germanistik)
- Abschlussmodule5
- Ling Finit Abschlussmodul Bachelorarbeit
- Lit BM Grundlagen des wissenschaftli- chen Arbeitens in der Literatur- wissenschaft
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
- Abschlussmodul Bachelorarbeit Neuere deutsche Literaturwissen- schaft(NdL Finit)
- Abschlussmodul Bachelorarbeit Mediävistik(MedFinit)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Bachelorarbeit

### 2-Fach-BA Germanistik FPO Germanistik Zwei-Fach 20220914 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-germanistik-zwei-fach-20220914-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-germanistik-fpo-germanistik-zwei-fach-20220914-aes.md)

**Pflichtmodule (15):**
- Ling BM-1 Grundlagen der germanistischen Linguistik
- Lit BM Grundlagen des wissenschaftli- chen Arbeitens in der Literaturwis- senschaft
- NdL BM-1 Grundlagen der Neueren deut- schen Literaturwissenschaft 1
- Ling BM-2 Grundlagen der historischen Linguistik
- Med BM Grundlagen der Germanistischen Mediävistik
- NdL BM-2 Grundlagen der Neueren deut- schen Literaturwissenschaft2
- Bachelorarbeit im Erstfach (Germanistik)
- Abschlussmodule5
- Ling Finit Abschlussmodul Bachelorarbeit Linguistik
- NdL Finit Abschlussmodul Bachelorarbeit Neuere deutsche Literaturwissen- schaft
- Med Finit Abschlussmodul Bachelorarbeit Mediävistik
- Lit BM Grundlagen des wissenschaftli- chen Arbeitens in der Literatur- wissenschaft
- NdL BM-2 Grundlagen der Neueren deut- schen Literaturwissenschaft 2
- Bachelorarbeit im Erstfach
- Bachelorarbeit

### 2-Fach-BA Iberoromanistik 20210624 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-20210624-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-20210624-aes.md)

**Pflichtmodule (7):**
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Spanische Sprachpraxis 32
- Bachelorarbeit im Erstfach (Iberomanistik)
- Bachelorarbeit
- SummeECTS-Punkteim Zwei-Fach-Bachelorstudium:
- Bachelorarbeit im Erstfach

### 2-Fach-BA Iberoromanistik FPO BA Iberorom 20071004 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-fpo-ba-iberorom-20071004-idf-20210624.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-iberoromanistik-fpo-ba-iberorom-20071004-idf-20210624.md)

**Pflichtmodule (7):**
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Spanische Sprachpraxis 32
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

**Pflichtmodule (8):**
- Basismodul Italienische Sprachpraxis 1
- Basismodul Italienische Sprachpraxis 22
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft
- Bachelorarbeit im Erstfach (Italoromanistik)
- Bachelorarbeit
- Basismodul Italienische Sprachpraxis 23
- Bachelorarbeit im Erstfach

### 2-Fach-BA Italoromanistik FPO BA Italorom 20071004 i.d.F. 20210624.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-italoromanistik-fpo-ba-italorom-20071004-idf-20210624.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-italoromanistik-fpo-ba-italorom-20071004-idf-20210624.md)

**Pflichtmodule (9):**
- Basismodul Italienische Sprachpraxis 1
- Basismodul Italienische Sprachpraxis 22
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft
- Bachelorarbeit im Erstfach (Italoromanistik)
- Bachelorarbeit
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

**Pflichtmodule (5):**
- Basismodul 1: Einführung in die Sprache und Literatur deslateinischen Europas
- Basismodul 2: Einführungindielateinische Schrift
- Einführung in die Indogermanistik9
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

**Pflichtmodule (13):**
- Grundlagen der Computerlinguistik I (traditionelle Verfahren)
- Programmierung und Infrastrukturen I
- Grundlagen der Computerlinguistik II (statistische Verfahren)
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

**Pflichtmodule (10):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Basismodul 2: Einführung in die lateinische Schrift (Paläographie)
- Basismodul 3A: Das Klassische Erbe A2 (gemäß§4a)
- Basismodul 3B: Das Klassische Erbe B2
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
- Basismodul 2: Einführung in die lateinische Schrift (Paläographie)
- Basismodul 3A: Das Klassische Erbe A2 (gemäß §4a)
- Basismodul 3B: Das Klassische Erbe B2
- Basismodul 4: Europäische Mediävistik I (gemäß §4a)
- Basismodul 5: Europäische Mediävistik II (gemäß §4a)
- Bachelorarbeit im Erstfach (Mittellatein und Neulatein)
- Bachelorarbeit
- Basismodul 3A: Das Klassische Erbe A3 (gemäß §4a)
- Basismodul 3B: Das Klassische Erbe B3

### 2-Fach-BA Mittel- und Neulatein FPO Mittellatein Zwei-Fach 20240430.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20240430.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-mittel-und-neulatein-fpo-mittellatein-zwei-fach-20240430.md)

**Pflichtmodule (10):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Basismodul 2: Einführung in die lateinische Schrift (Paläographie)
- Basismodul 3A: Das Klassische Erbe A2 (gemäß§5)
- Basismodul 3B: Das Klassische Erbe B2
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

**Pflichtmodule (12):**
- Grundkurs Praktische Philosophie
- Grundkurs Theoretische Philosophie
- Basismodul Philosophie
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

**Pflichtmodule (12):**
- Grundkurs Praktische Philosophie
- Grundkurs Theoretische Philosophie
- Basismodul Philosophie
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

**Pflichtmodule (11):**
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

### 2-Fach-BA Skandinavistik FPO BA SKAND 20211201 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-skandinavistik-fpo-ba-skand-20211201-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-skandinavistik-fpo-ba-skand-20211201-aes.md)

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
- Bachelorarbeit im Erstfach (Skandinavistik)
- Abschlussmodul Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20071005 i.d.F. 20190806.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20190806.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20190806.md)

**Pflichtmodule (14):**
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
- Einführung Soziologische Theorien(SozT-E)
- Einführung in die soziologische Methoden- lehre (SozM-E)
- Bachelorarbeit im Erstfach

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20071005 i.d.F. 20200818.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20200818.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20071005-idf-20200818.md)

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

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20190806 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20190806-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20190806-aes.md)

**Pflichtmodule (14):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Einführung in die soziolo- gische Methodenlehre (SozM-E)
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Qualifikationsprofil I (SozQ-I), vgl. § 5
- Qualifikationsprofil II (SozQ-II), vgl. § 5
- Bachelorarbeit im Erstfach (Soziologie)
- Bachelorarbeit
- Einführung in die soziologische Metho- denlehre (SozM-E)
- Qualifikationsprofil II
- Bachelorarbeit im Erstfach

### 2-Fach BA Soziologie FPOSoz Zwei-Fach 20200818 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20200818-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-soziologie-fposoz-zwei-fach-20200818-aes.md)

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

**Pflichtmodule (8):**
- Basismodul Medienwissenschaft
- Basismodul Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Bachelorarbeit im Erstfach (Theater- und Medienwissenschaft)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Theater- und Medienwissenschaft FPO B.A. Theatermedien 20071004 i.d.F. 20220512.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20071004-idf-20220512.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20071004-idf-20220512.md)

**Pflichtmodule (8):**
- Basismodul Medienwissenschaft
- Basismodul Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Bachelorarbeit im Erstfach (Theater- und Medienwissenschaft)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 2-Fach-BA Theater- und Medienwissenschaft FPO B.A. Theatermedien 20190815 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20190815-aes.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2-fach-ba-theater-und-medienwissenschaft-fpo-b-a-theatermedien-20190815-aes.md)

**Pflichtmodule (8):**
- Basismodul Medienwissenschaft
- Basismodul Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Bachelorarbeit im Erstfach (Theater- und Medienwissenschaft)
- Bachelorarbeit
- Bachelorarbeit im Erstfach

### 17. Februar 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2aes-2fachba-oeffentlichesrecht.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2aes-2fachba-oeffentlichesrecht.md)

**Pflichtmodule (9):**
- Grundlagen-modul
- Staats- organisationsrecht
- Grundrechte
- Allgemeine Grundlagen des Verwaltungsrechts
- Europa- und
- Völkerrecht I
- Verwaltungs-recht I
- Europa- und Völkerecht II
- Verwaltungs-recht II

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

**Pflichtmodule (6):**
- Basismodule: Kulturentwicklung und Kulturgeschichte~~3)~~
- Prähistorische Archäologie
- Prähistorische Archäologie: Ältere Urgeschichte I3)
- Prähistorische Archäologie: Jüngere Urgeschichte I3)
- Bachelorarbeit und -prüfung
- Bachelorarbeit6)

### PDF vom 18.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fachba-archaeologischewissenschaften.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/2fachba-archaeologischewissenschaften.md)

**Pflichtmodule (6):**
- Basismodule: Kulturentwicklung und Kulturgeschichte3)
- PrähistorischeArchäologie
- Prähistorische Archäologie: Ältere Urgeschichte I3)
- Prähistorische Archäologie: Jüngere Urgeschichte I3)
- Bachelorarbeit und -prüfung
- Bachelorarbeit6)

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

**Pflichtmodule (9):**
- Grundlagen Japanologie 1
- Grundlagen Japanologie 2
- Japanisch 3
- Japanisch 4
- Grundlagen Japanologie 31
- Grundlagen Japanologie 41
- Japanische Literatur und Film
- Japanisch 5
- Japanisches Theater1

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

**Pflichtmodule (9):**
- Basismodule:
- Nordistische Linguistik 12
- Nordistische Linguistik 22
- Nordistische Literatur- und Kulturwissenschaft 12
- Nordistische Literatur- und Kulturwissenschaft22
- Altnordisch 12
- Altnordisch 22
- Nordische Erstsprache 12
- Nordische Erstsprache 22

### 15. Juli 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-theater-und-medien.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/6aes-2fachba-theater-und-medien.md)

**Pflichtmodule (6):**
- Medienwissenschaft
- Basismodul Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Bachelorarbeit

### 11. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fach-ba-linginformatik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/7aes-2fach-ba-linginformatik.md)

**Pflichtmodule (8):**
- Grundlagen der Computerlinguistik I
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

**Pflichtmodule (10):**
- Basismodule: Es müssen alle Basismodule belegt werden (40 ECTS).
- Nordistische Literaturwissenschaft 1
- Nordistische Literaturwissenschaft 2
- Nordistische Literaturwissenschaft 3
- Nordische Kulturgeschichte 1
- Nordische Kulturgeschichte 2
- Nordische Erstsprache 1
- Nordische Erstsprache 2
- Bachelorarbeit (nur im Erstfach): 10
- Abschlussmodul Bachelorarbeit

### 10. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-frankoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-frankoromanistik.md)

**Pflichtmodule (3):**
- Basismodul Französische Sprachpraxis 1
- Basismodul Französische Sprachpraxis 2
- Basismodul Einführung in die Frankoromanistik

### 10. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-iberoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-iberoromanistik.md)

**Pflichtmodule (3):**
- Basismodul Spanische Sprachpraxis 1
- BasismodulSpanische Sprachpraxis 2
- Basismodul Einführung in die Iberoromanistik

### 10. Juni 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-italoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-italoromanistik.md)

**Pflichtmodule (3):**
- Basismodul Italienische Sprachpraxis 1
- Basismodul Italienische Sprachpraxis 2
- Basismodul Einführung in die Italoromanistik

### 2. Juni 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-philosophie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fach-ba-philosophie.md)

**Pflichtmodule (8):**
- Grundkurs PraktischePhilosophie
- Grundkurs Theoretische Philosophie
- Basismodul Philosophie
- Basismodul Praktische Philosophie
- Basismodul Theoretische Philosophie
- Philosophiegeschichte2
- Philosophie systematisch3
- Bachelorarbeit

### 5. August 2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fachba-germanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fachba-germanistik.md)

**Pflichtmodule (6):**
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1 (NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft 2 (NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1 (MedBM 1)
- Grundlagen der Germanistischen Mediävistik 2 (Med BM 2)

### 3. August 2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fachba-mittelneulatein.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/8aes-2fachba-mittelneulatein.md)

**Pflichtmodule (8):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Basismodul 2: Einführung in die lateinische Schrift (Paläographie)
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

**Pflichtmodule (7):**
- Grundlagen der Informatik
- Konzeptionelle Mo- dellierung
- Mathematik
- Theoretische Infor- matik
- Grundlagen der Logik in der Infor- matik
- Mathematische Modellbildung und Statistik
- Kernmodul 1: Ein- führung in die Digi- talen Geistes- und Sozialwissenschaf- ten

### 22. Juli 2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aes-2fachba-soziologie.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aes-2fachba-soziologie.md)

**Pflichtmodule (9):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien (SozT-V)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Qualifikationsprofil I (SozQ-I)
- Qualifikationsprofil II (SozQ-II)

### 28. Juli 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-frankoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-frankoromanistik.md)

**Pflichtmodule (5):**
- Basismodul Französische Sprachpraxis 1
- Basismodul Französische Sprachpraxis 2
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Bachelorarbeit

### 28. Juli 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-iberoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-iberoromanistik.md)

**Pflichtmodule (5):**
- Basismodul Spanische Sprachpraxis 1
- Basismodul Spanische Sprachpraxis 2
- Basismodul Spanische Sprachwissenschaft
- Basismodul Spanische Literaturwissenschaft
- Bachelorarbeit

### 28. Juli 2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-italoromanistik.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/9aesa-fpo-2fba-italoromanistik.md)

**Pflichtmodule (4):**
- Basismodul Italienische Sprachpraxis 1
- Basismodul Italienische Sprachpraxis 2
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft

### PDF vom 05.10.2007 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-ba-kunstgesch-aug2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-ba-kunstgesch-aug2017.md)

**Pflichtmodule (1):**
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 18.08.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-fbo-b-a-theatermedienaug2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-fbo-b-a-theatermedienaug2017.md)

**Pflichtmodule (6):**
- Medienwissenschaft
- Basismodul Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 10.06.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankorom-10juni2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankorom-10juni2014.md)

**Pflichtmodule (4):**
- Basismodul Französische Sprachpraxis 1
- Basismodul Französische Sprachpraxis 2
- Basismodul Einführung in die Frankoromanistik
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F: 28.07.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankoromjuli2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-frankoromjuli2017.md)

**Pflichtmodule (5):**
- Basismodul Französische Sprachpraxis 1
- Basismodul Französische Sprachpraxis 2
- Basismodul Französische Sprachwissenschaft
- Basismodul Französische Literaturwissenschaft
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 05.08.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-aug2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-aug2016.md)

**Pflichtmodule (6):**
- Grundlagen der Germanistischen Linguistik 1 (Ling BM 1)
- Grundlagen der Germanistischen Linguistik 2 (Ling BM 2)
- Grundlagen der Neueren deutschen Literaturwissenschaft 1(NdL BM 1)
- Grundlagen der Neueren deutschen Literaturwissenschaft2(NdL BM 2)
- Grundlagen der Germanistischen Mediävistik 1(Med BM 1)
- Grundlagen der Germanistischen Mediävistik 2(MedBM 2)

### PDF vom 04.10.2007 i.d.F. 07.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-juli-2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-germanist-juli-2014.md)

**Pflichtmodule (4):**
- Grundlagen der Germanistischen Linguistik (Ling1)
- Alternative für ausländische Studierende: Grundlagen der Germanistischen Linguistik (DaF) (Ling1a)
- Grundlagen der Germanistischen Mediävistik (Med 1)
- Grundlagen der Neueren deutschen Literatur (NdL 1)

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

**Pflichtmodule (4):**
- Basismodul Spanische Sprachpraxis 1
- BasismodulSpanische Sprachpraxis 2
- Basismodul Einführung in die Iberoromanistik
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 28.07.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-iberoromjuli2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-iberoromjuli2017.md)

**Pflichtmodule (5):**
- Basismodul Spanische Sprachpraxis 1
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

**Pflichtmodule (10):**
- Grundlagen der Informatik
- Konzeptionelle Modellierung
- Mathematik
- Theoretische Informatik
- Grundlagen der Logik in der Informatik
- Mathematische Modellbildung und Statistik
- Kernmodul 1: Einführung in die Digitalen Geistes- und Sozial- wissenschaften
- Kernmodul 2: Nutzung digitaler Daten in den Geistes- und So- zialwissenschaften
- Kernmodul 3: Wissenschaft und Gesellschaft im digitalen Zeitalter
- Praxismodul

### PDF vom 04.10.2007 i.d.F. 10.06.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italorom-10juni2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italorom-10juni2014.md)

**Pflichtmodule (3):**
- Basismodul Italienische Sprachpraxis 1
- Basismodul Italienische Sprachpraxis 2
- Basismodul Einführung in die Italoromanistik

### PDF vom 04.10.2007 i.d.F. 28.07.2017

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italoromjuli2017.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-italoromjuli2017.md)

**Pflichtmodule (5):**
- Basismodul Italienische Sprachpraxis 1
- Basismodul Italienische Sprachpraxis 2
- Basismodul Italienische Sprachwissenschaft
- Basismodul Italienische Literaturwissenschaft
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 17.02.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-japan-februar2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-japan-februar2014.md)

**Pflichtmodule (11):**
- Grundlagen Japanologie 1
- Grundlagen Japanologie 2
- Japanisch 3
- Japanisch 4
- Grundlagen Japanologie 31
- Grundlagen Japanologie 41
- Japanische Literatur und Film
- Japanisch 5
- Japanisches Theater1
- Japanologie 1
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 07.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-japan-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-japan-juli2014.md)

**Pflichtmodule (11):**
- Grundlagen Japanologie 1
- Grundlagen Japanologie 2
- Japanisch 3
- Japanisch 4
- Grundlagen Japanologie 31
- Grundlagen Japanologie 41
- Japanische Literatur und Film
- Japanisch 5
- Japanisches Theater1
- Japanologie 1
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 03.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-mittellatein-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-mittellatein-aug2015.md)

**Pflichtmodule (8):**
- Basismodul 1: Einführung in die Sprache und Literatur des lateinischen Europas
- Basismodul 2: Einführung in die lateinische Schrift (Paläographie)
- Basismodul 3A: Das Klassische Erbe A2
- Basismodul 3B:
- Das Klassische Erbe B2
- Basismodul 4: Europäische Mediävistik I
- Basismodul 5: Europäische Mediävistik
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 25.06.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-nordphil-juni2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-nordphil-juni2015.md)

**Pflichtmodule (11):**
- Basismodule:
- Nordistische Linguistik 12
- Nordistische Linguistik 22
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

**Pflichtmodule (10):**
- Basismodule: Es müssen alle Basismodule belegt werden (40 ECTS).
- Nordistische Literaturwissenschaft 1
- Nordistische Literaturwissenschaft 2
- Nordistische Literaturwissenschaft 3
- Nordische Kulturgeschichte 1
- Nordische Kulturgeschichte 2
- Nordische Erstsprache 1
- Nordische Erstsprache 2
- Bachelorarbeit (nur im Erstfach): 10 ECTS
- Abschlussmodul Bachelorarbeit

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

**Pflichtmodule (8):**
- Grundkurs PraktischePhilosophie
- Grundkurs TheoretischePhilosophie
- Basismodul Philosophie
- Basismodul Praktische Philosophie
- Basismodul Theoretische Philosophie
- Philosophiegeschichte2
- Philosophie systematisch3
- Bachelorarbeit

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

**Pflichtmodule (9):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien(SozT-V)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Qualifikationsprofil I (SozQ-I)
- Qualifikationsprofil II (SozQ-II)

### PDF vom 05.10.2007 i.d.F. 02.07.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-soziol-juli2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-soziol-juli2015.md)

**Pflichtmodule (10):**
- Einführung (SozE)
- Sozialstrukturanalyse (SozStruk)
- Einführung Soziologische Theorien (SozT-E)
- Vertiefung Soziologische Theorien(SozT-V)
- Einführung in die soziologische Methodenlehre (SozM-E)
- Statistische Analyseverfahren I (SozS-I)
- Statistische Analyseverfahren II (SozS-II)
- Qualifikationsprofil I (SozQ-I)
- Qualifikationsprofil II (SozQ-II)
- Bachelorarbeit

### PDF vom 04.10.2007 i.d.F. 15.07.2016

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-theater-juli2016.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuo-pro-theater-juli2016.md)

**Pflichtmodule (6):**
- Medienwissenschaft
- Basismodul Theaterwissenschaft
- Thematisches Modul Medienwissenschaft
- Thematisches Modul Theaterwissenschaft
- Praxis
- Bachelorarbeit

### PDF vom 05.10.2007 i.d.F. 11.08.2015

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-aug2015.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-aug2015.md)

**Pflichtmodule (8):**
- Grundlagen der Computerlinguistik I
- Grundlagen der Informatik (Importmodul)
- Grundlagen der Computerlinguistik II
- Programmierung I
- Programmierung II
- Proseminar Computerlinguistik
- Werkzeuge und Infrastrukturen
- Konzeptionelle Modellierung (Importmodul)

### PDF vom 05.10.2007 i.d.F. 22.07.2014

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-juli2014.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fachstuopro-linginform-juli2014.md)

**Pflichtmodule (5):**
- Grundlagen der Computerlinguistik I
- Grundlagen der Informatik (Importmodul)
- Grundlagen der Computerlinguistik II
- Programmierung
- Bachelorarbeit*

### FPO 2-Fach BA DGSW 20080722 i.d.F. 20180829.pdf

PO-Quelle: [`pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-2-fach-ba-dgsw-20080722-idf-20180829.md`](../pruefungsordnungen/philosophische-fakultaet/zwei-fach-bachelor/fpo-2-fach-ba-dgsw-20080722-idf-20180829.md)

**Pflichtmodule (10):**
- Grundlagen der Informatik
- Konzeptionelle Modellierung
- Mathematik für Naturwissen- schaftler
- Theoretische Informatik für Wirtschaftsinformatik und Lehramtsstudierende2
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

**Pflichtmodule (28):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissenschaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik: Analysis und Lineare Algebra
- Statistik
- BWL/VWL
- Absatz
- Mikroökonomie
- Grundzüge der Kommunikationswissen- schaft
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

**Pflichtmodule (28):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissenschaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik: Analysis und Lineare Algebra
- Statistik
- BWL/VWL
- Absatz
- Mikroökonomie
- Grundzüge der Kommunikationswissen- schaft
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

**Pflichtmodule (28):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissenschaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik: Analysis und Lineare Algebra
- Statistik
- BWL/VWL
- Absatz
- Mikroökonomie
- Grundzüge der Kommunikationswissen- schaft
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

**Pflichtmodule (33):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissenschaft
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik
- Data Science: Datenauswertung
- Data Science: Statistik
- BWL/VWL
- Absatz
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Kernbereich des Schwerpunkts Verhaltenswissenschaften
- Empirische Methoden und Statistik
- Personal und Organisation I
- Digital Technologies & Society
- Sozialpolitische Grundlagen
- Grundzüge der Kommunikationswissen- schaft
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

**Pflichtmodule (33):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International Politics II
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
- Marketing
- Grundlagen des öffentlichen Rechts und des Zivilrechts
- Kernbereich des Schwerpunkts Verhaltenswissenschaften
- Empirische Methoden und Statistik
- Personal und Organisation I
- Digital Technologies & Society
- Sozialpolitische Grundlagen
- Unternehmen, Märkte, Volkswirtschaf- ten
- Grundzüge der Kommunikationswis- senschaft
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

**Pflichtmodule (17):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik: Die Europäische In- tegration
- International Politics: Global Sustainabi- lity
- Unternehmer und Unternehmen
- Soziologie II
- Medien und Kommunikation
- Sozialpsychologie
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

**Pflichtmodule (42):**
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
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Wirtschaftsprivatrecht
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
- Kernbereich des Schwerpunkts WiPäd I
- Grundlagen der Wirtschafts- und Betriebs- pädagogik
- Betriebliche Aus- und Weiterbildung
- Präsentations- und Moderationstechniken
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Kernbereich des Schwerpunkts WiPäd II

### BA Wirtschaftswissenschaften FPO BA WiWi 20170810 i.d.F. 20190731.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20190731.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/ba-wirtschaftswissenschaften-fpo-ba-wiwi-20170810-idf-20190731.md)

**Pflichtmodule (42):**
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
- Grundlagen des öffentlichen Rechts und desZivilrechts
- Wirtschaftsprivatrecht
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
- Mikroökonomie
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

**Pflichtmodule (19):**
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

### BSc Wirtschaftsinformatik FPO BA WInf 20170810 i.d.F. 20210222.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210222.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210222.md)

**Pflichtmodule (19):**
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

### BSc Wirtschaftsinformatik FPO BA WInf 20170810 i.d.F. 20210806.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210806.md`](../pruefungsordnungen/rw/wiso/bachelorstudiengaenge/bsc-wirtschaftsinformatik-fpo-ba-winf-20170810-idf-20210806.md)

**Pflichtmodule (19):**
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

**Pflichtmodule (19):**
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

**Pflichtmodule (18):**
- Sozialökonomische Grundlagen
- Soziologie I (inkl. Planspiel)
- Unternehmen, Märkte, Volkswirtschaften
- Internationale Politik I
- International politics II
- Unternehmer und Unternehmen
- Soziologie II
- Grundzüge der Kommunikationswissenschaften
- Sozialpsychologie
- Methodische Grundlagen der Wirtschaftswissenschaften
- Empirische Sozialforschung I
- Empirische Sozialforschung II
- Mathematik: Analysis und Lineare Algebra
- Statistik
- BWL/VWL
- Absatz
- Mikroökonomie
- Grundzüge der Kommunikationswissen- schaften

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

**Pflichtmodule (2):**
- Masterarbeit
- Mindestens 41 SWS

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

**Pflichtmodule (1):**
- Masterarbeit

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

**Pflichtmodule (1):**
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

**Pflichtmodule (1):**
- Masterarbeit

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

**Pflichtmodule (1):**
- Masterarbeit

### FPOAuP 20090717 i.d.F. 20200221.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200221.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200221.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOAuP 20090717 i.d.F. 20200731.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200731.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20200731.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOAuP 20090717 i.d.F. 20210726.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20210726.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20210726.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOAuP 20090717 i.d.F. 20250227.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20250227.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoaup-20090717-idf-20250227.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOECO 20090720 i.d.F. 20191129.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20191129.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20191129.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOECO 20090720 i.d.F. 20210311.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20210311.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20210311.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOECO 20090720 i.d.F. 20220328.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20220328.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20090720-idf-20220328.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOECO 20250320.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20250320.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fpoeco-20250320.md)

**Pflichtmodule (1):**
- Masterarbeit

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

**Pflichtmodule (1):**
- Mind. 40 SWS4

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

**Pflichtmodule (2):**
- Masterarbeit
- Masterareit

### FPOSozialökonomik 20090902 i.d.F. 20220727.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20090902-idf-20220727.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20090902-idf-20220727.md)

**Pflichtmodule (2):**
- Masterarbeit
- asterarbet

### FPOSozialökonomik 20240807 i.d.F. 20241122.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20240807-idf-20241122.md`](../pruefungsordnungen/rw/wiso/masterstudiengaenge/fposozialoekonomik-20240807-idf-20241122.md)

**Pflichtmodule (2):**
- Masterarbeit
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

**Pflichtmodule (2):**
- Masterarbeit
- Masterareit

### Modulstudien Berufspädagogik POMBPäd 20240807.pdf

PO-Quelle: [`pruefungsordnungen/rw/wiso/modul-und-zusatzstudien/modulstudien-berufspaedagogik-pombpaed-20240807.md`](../pruefungsordnungen/rw/wiso/modul-und-zusatzstudien/modulstudien-berufspaedagogik-pombpaed-20240807.md)

**Pflichtmodule (8):**
- (2) Grundlagen der Wirtschafts- und Betriebspädagogik
- Schulorganisation und Bildungssystem
- Betriebliche Aus- und Weiterbildung
- Betriebspädagogisches Seminar
- Schulpraktische Studien
- Berufspädagogische Vertiefung
- Zweitfach gemäß § 2
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
- SummeECTS 60

### PDF vom 18.02.2014 i.d.F. 22.07.2015

PO-Quelle: [`pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/wtb-pro-marketing-management-juli2015.md`](../pruefungsordnungen/rw/wiso/weiterbildungs-masterstudiengaenge/wtb-pro-marketing-management-juli2015.md)

**Pflichtmodule (2):**
- Masterarbeit
- Berufspraxis

### 3. Juli 2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/3aes-ba-ma-chemicaleng-nct.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/3aes-ba-ma-chemicaleng-nct.md)

**Pflichtmodule (2):**
- Masterarbeit mit Referat
- Masterarbeit mit Reerat

### BSc MSc Chemical Engineering FPOCEN 20230426 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/bsc-msc-chemical-engineering-fpocen-20230426-aes.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/bsc-msc-chemical-engineering-fpocen-20230426-aes.md)

**Pflichtmodule (1):**
- Masterarbeit mit Hauptseminar

### FPO-BA-MA ChemEngin-NachhaltigeChemTechn 20110607 i.d.F. 20230426.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-20110607-idf-20230426.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-20110607-idf-20230426.md)

**Pflichtmodule (2):**
- Masterarbeit mit Hauptse- minar
- Masterarbeit mit Hauptseminar

### PDF vom 07.06.2011 i.d.F. 26.01.2016

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-jan2016.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-jan2016.md)

**Pflichtmodule (2):**
- Masterarbeit mit Referat
- Masterarbeit mit Reerat

### PDF vom 07.06.2011 i.d.F. 03.07.2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-juli2015.md`](../pruefungsordnungen/technische-fakultaet/chemie-und-bioingenieurwesen/fpo-ba-ma-chemengin-nachhaltigechemtechn-juli2015.md)

**Pflichtmodule (2):**
- Masterarbeit mit Referat
- Masterarbeit mit Reerat

### FPOCME 20230822.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/fpocme-20230822.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/fpocme-20230822.md)

**Pflichtmodule (1):**
- Masterarbeit

### FPOCME 20250320.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/fpocme-20250320.md`](../pruefungsordnungen/technische-fakultaet/elektrotechnik-elektronik-informationstechnik/fpocme-20250320.md)

**Pflichtmodule (1):**
- Masterarbeit

### 24. Juli 2014

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/6aes-ba-ma-computengineering.md`](../pruefungsordnungen/technische-fakultaet/informatik/6aes-ba-ma-computengineering.md)

**Pflichtmodule (1):**
- Masterarbeit

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

**Pflichtmodule (18):**
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

### BSc-MSc Computational Engineering 20070919 i.d.F. 20180116.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180116.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180116.md)

**Pflichtmodule (6):**
- Bachelorarbeit
- (4) Grundlagen der Elektrotechnik I
- (2) Grundlagen der Elektrotechnik III
- (1) Elektromagnetische Felder I
- (2) Sensorik
- Masterarbeit

### BSc-MSc Computational Engineering 20070919 i.d.F. 20180730.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180730.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20070919-idf-20180730.md)

**Pflichtmodule (6):**
- Bachelorarbeit
- (4) Grundlagen der Elektrotechnik I
- (2) Grundlagen der Elektrotechnik III
- (1) Elektromagnetische Felder I
- (2) Sensorik
- Masterarbeit

### BSc-MSc Computational Engineering 20180116 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20180116-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20180116-aes.md)

**Pflichtmodule (4):**
- (4) Grundlagen der Elektrotechnik I
- (2) Grundlagen der Elektrotechnik III
- (1) Elektromagnetische Felder I
- (2) Sensorik

### BSc-MSc Computational Engineering 20180730 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20180730-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-20180730-aes.md)

**Pflichtmodule (5):**
- (4) Grundlagen der Elektrotechnik I
- (2) Grundlagen der Elektrotechnik III
- (1) Elektromagnetische Felder I
- (2) Sensorik
- Masterarbeit

### BSc-MSc Computational Engineering FPOCE 20070919 i.d.F. 20220421.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20070919-idf-20220421.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20070919-idf-20220421.md)

**Pflichtmodule (27):**
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
- Grundlagen der Elektrotechnik I
- Grundlagen der Elektrotechnik III
- Einführungin die Regelungstechnik1
- Sensorik
- Masterarbeit

### BSc-MSc Computational Engineering FPOCE 20220421 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20220421-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20220421-aes.md)

**Pflichtmodule (4):**
- Grundlagen der Elektrotechnik I
- Grundlagen der Elektrotechnik III
- Einführungin die Regelungstechnik1
- Sensorik

### BSc-MSc Computational Engineering FPOCE 20250604.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20250604.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-computational-engineering-fpoce-20250604.md)

**Pflichtmodule (27):**
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
- Grundlagen der Elektrotechnik I
- Grundlagen der Elektrotechnik III
- Einführungin die Regelungstechnik1
- Sensorik
- Masterarbeit

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20180801.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20180801.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20180801.md)

**Pflichtmodule (18):**
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

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20190306.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20190306.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20190306.md)

**Pflichtmodule (10):**
- Grundlagen der Technischen Informatik
- Parallele und funktionale Programmierung
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Schaltungs- technik
- Systemprogrammierung
- Grundlagen der Logik in der Informatik
- Softwareentwicklung in Großprojekten
- Berechenbarkeit und Formale Sprachen
- Bachelorarbeit
- Masterarbeit

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20191203.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20191203.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20191203.md)

**Pflichtmodule (10):**
- Grundlagen der Technischen Informatik
- Parallele und funktionale Programmierung
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Schaltungs- technik
- Systemprogrammierung
- Grundlagen der Logik in der Informatik
- Softwareentwicklung in Großprojekten
- Berechenbarkeit und Formale Sprachen
- Bachelorarbeit
- Masterarbeit

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20200820.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20200820.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20200820.md)

**Pflichtmodule (13):**
- Grundlagen der Programmie- rung
- Grundlagen der Logik in der Informatik
- Sichere Systeme
- Grundlagen der Technischen Informatik
- Einführung in die Algorithmik
- Systemprogrammierung
- Grundlagen der Rechner- architektur und -organisation
- Rechnerkommunikation
- Parallele und funktionale Programmierung
- Softwareentwicklung in Großprojekten
- Berechenbarkeit und Formale Sprachen
- Bachelorarbeit
- Masterarbeit

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20210701.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20210701.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20210701.md)

**Pflichtmodule (13):**
- Grundlagen der Programmie- rung
- Grundlagen der Logik in der Informatik
- Sichere Systeme
- Grundlagen der Technischen Informatik
- Einführung in die Algorithmik
- Systemprogrammierung
- Grundlagen der Rechner- architektur und -organisation
- Rechnerkommunikation
- Parallele und funktionale Programmierung
- Softwareentwicklung in Großprojekten
- Berechenbarkeit und Formale Sprachen
- Bachelorarbeit
- Masterarbeit

### BSc-MSc Informatik FPOINF 20070920 i.d.F. 20220301.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20220301.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070920-idf-20220301.md)

**Pflichtmodule (12):**
- Grundlagen der Program- mierung
- Grundlagen der Logik in der Informatik
- Sichere Systeme
- Grundlagen der Technischen Informatik
- Einführung in die Algorithmik
- Systemprogrammierung
- Grundlagen der Rechner- architektur und -organisation
- Rechnerkommunikation
- Parallele und funktionale Programmierung
- Softwareentwicklung in Großprojekten
- Bachelorarbeit
- Masterarbeit

### BSc-MSc Informatik FPOINF 20070921 i.d.F. 20220726.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070921-idf-20220726.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070921-idf-20220726.md)

**Pflichtmodule (12):**
- Grundlagen der Programmie- rung
- Grundlagen der Logik in der Informatik
- Sichere Systeme
- Grundlagen der Technischen Informatik
- Einführung in die Algorithmik
- Systemprogrammierung
- Grundlagen der Rechner- architektur und -organisation
- Rechnerkommunikation
- Parallele und funktionale Programmierung
- Einführung in das Software Engineering
- Bachelorarbeit
- Masterarbeit

### BSc-MSc Informatik FPOINF 20070921 i.d.F. 20230426.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070921-idf-20230426.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20070921-idf-20230426.md)

**Pflichtmodule (12):**
- Grundlagen der Programmie- rung
- Grundlagen der Logik in der Informatik
- Sichere Systeme
- Grundlagen der Technischen Informatik
- Einführung in die Algorithmik
- Systemprogrammierung
- Grundlagen der Rechner- architektur und -organisation
- Rechnerkommunikation
- Parallele und funktionale Programmierung
- Einführung in das Software Engineering
- Bachelorarbeit
- Masterarbeit

### BSc-MSc Informatik FPOINF 20190306 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20190306-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20190306-aes.md)

**Pflichtmodule (17):**
- Grundlagen der Technischen Informatik
- Parallele und funktionale Programmierung
- Grundlagen der Rechner- architektur und -organisation
- Grundlagen der Schaltungs- technik
- Systemprogrammierung
- Grundlagen der Logik in der Informatik
- Softwareentwicklung in Großprojekten
- Berechenbarkeit und Formale Sprachen
- Theorie der Programmierung
- Rechnerkommunikation
- Algorithmik kontinuierlicher Systeme
- Implementierung von Daten- banksystemen
- Hauptseminar (Schlüssel- qualifikation)
- Mathematik für INF 12)
- Mathematik für INF 22)
- Bachelorarbeit
- Masterarbeit

### BSc-MSc Informatik FPOINF 20200820 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20200820-aes.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20200820-aes.md)

**Pflichtmodule (13):**
- Grundlagen der Programmie- rung
- Grundlagen der Logik in der Informatik
- Sichere Systeme
- Grundlagen der Technischen Informatik
- Einführung in die Algorithmik
- Systemprogrammierung
- Grundlagen der Rechner- architektur und -organisation
- Rechnerkommunikation
- Parallele und funktionale Programmierung
- Softwareentwicklung in Großprojekten
- Berechenbarkeit und Formale Sprachen
- Bachelorarbeit
- Masterarbeit

### BSc-MSc Informatik FPOINF 20240328 iF 20250604.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328-if-20250604.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328-if-20250604.md)

**Pflichtmodule (11):**
- Grundlagen der Programmierung
- Grundlagen der Logik in der Informatik
- Sichere Systeme
- Grundlagen der Technischen Informatik
- Einführung in die Algorithmik
- Systemprogrammierung
- Grundlagen der Rechner- architektur und -organisation
- Rechnerkommunikation
- Parallele und funktionale Programmierung
- Bachelorarbeit
- Masterarbeit

### BSc-MSc Informatik FPOINF 20240328 iF 20260115.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328-if-20260115.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328-if-20260115.md)

**Pflichtmodule (3):**
- Masterarbeit
- S SWS d ECTSPk
- ummen un -unte:

### BSc-MSc Informatik FPOINF 20240328.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328.md`](../pruefungsordnungen/technische-fakultaet/informatik/bsc-msc-informatik-fpoinf-20240328.md)

**Pflichtmodule (11):**
- Grundlagen der Programmierung
- Grundlagen der Logik in der Informatik
- Sichere Systeme
- Grundlagen der Technischen Informatik
- Einführung in die Algorithmik
- Systemprogrammierung
- Grundlagen der Rechner- architektur und -organisation
- Rechnerkommunikation
- Parallele und funktionale Programmierung
- Bachelorarbeit
- Masterarbeit

### PDF vom 19.09.2007 i.d.F. 18.01.2016

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-jan2016.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-jan2016.md)

**Pflichtmodule (5):**
- Bachelorarbeit
- Begleitseminar + Referat Bachelor
- Schriftliche Bachelorarbeit
- SummeECTS
- Masterarbeit

### PDF vom 19.09.2007 i.d.F. 24.07.2014

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-juli2014.md`](../pruefungsordnungen/technische-fakultaet/informatik/fpo-ba-ma-compeng-juli2014.md)

**Pflichtmodule (1):**
- Masterarbeit

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

**Pflichtmodule (27):**
- BWL für Ingenieure
- Absatz
- Statistik
- IT und E-Business
- Buchführung
- Produktion, Logistik, Beschaffung
- Makroökonomie
- Mathematik für WING 1~~1)~~ Übung
- EinführungindieIuK-Technik
- Digitaltechnik
- Mathematik für WING 2~~1)~~ Ü
- bung
- Praktikum Software für die Mathematik
- Elektronik und Schaltungstechnik
- Praktikum Elektronik und Schaltungstechnik
- Halbleiterbauelemente
- Grundlagen der Informatik
- Signale und SystemeI
- Signale und Systeme II
- Nachrichtentechnische Systeme
- Wahlpflichtmodul 1
- Wahlpflichtmodul 2
- Technisches Wahlmodul
- Hochschulpraktikum
- Wirtschaftswissen- schaftlicher Bereich
- StochastischeProzesse
- Produktion,Logistik,Beschaffung

### BA-MA FPOWING 20070925 i.d.F. 20180515.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20070925-idf-20180515.md`](../pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20070925-idf-20180515.md)

**Pflichtmodule (10):**
- BWL für Ingenieure
- Absatz
- Statistik
- IT und E-Business
- Buchführung
- Produktion,Logistik,Beschaffung
- Makroökonomie
- Mikroökonomie
- Wirtschaftsrecht5)
- Produktion, Logistik, Beschaffung

### BA-MA FPOWING 20070925 i.d.F. 20190815.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20070925-idf-20190815.md`](../pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20070925-idf-20190815.md)

**Pflichtmodule (9):**
- BWL für Ingenieure
- Absatz
- Statistik
- IT und E-Business
- Buchführung
- Produktion,Logistik,Beschaffung
- Makroökonomie
- Mikroökonomie
- Wirtschaftsrecht7)

### BA-MA FPOWING 20180515 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20180515-aes.md`](../pruefungsordnungen/technische-fakultaet/maschinenbau/ba-ma-fpowing-20180515-aes.md)

**Pflichtmodule (24):**
- Mathematik für WING11)
- StatikundFestigkeitslehre
- Werkstoffkunde
- Mathematik für WING21)
- Mathematik für WING 3 1)
- Dynamikstarrer Körper
- Technische Darstellungslehre I
- Technische DarstellungslehreII
- Grundlagen der Produktentwicklung
- Konstruktionstechnisches Praktikum
- Grundlagen der Elektrotechnik
- Grundlagender Informatik
- Produktionstechnik IundII
- BWL für Ingenieure
- Absatz
- Statistik
- ITundE-Business
- Buchführung
- Produktion, Logistik, Beschaffung
- Makroökonomie
- Mikroökonomie
- Wirtschaftsrecht 5)
- Produktion, Logistik, Be- schaffung
- Wirtschaftsrecht5)

### PDF vom 25.09.2007 i.d.F. 24.07.2014

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/maschinenbau/fpo-ba-ma-wing-juli2014.md`](../pruefungsordnungen/technische-fakultaet/maschinenbau/fpo-ba-ma-wing-juli2014.md)

**Pflichtmodule (40):**
- Mathematik für WING 1~~1)~~
- Statik und Festigkeitslehre
- Werkstoffkunde
- Mathematik für WING 2~~1)~~
- Dynamikstarrer Körper
- Technische Darstellungslehre I
- Technische Darstellungslehre II
- Grundlagen der Produktentwicklung
- Konstruktionsübung
- Grundlagen der Elektrotechnik
- Grundlagender Informatik
- Produktionstechnik I und II
- BWL für Ingenieure
- Absatz
- Statistik
- IT und E-Business
- Buchführung
- Produktion,Logistik,Beschaffung
- Makroökonomie
- Mikroökonomie
- Wirtschaftsrecht
- Mathematik für WING1~~1)~~
- EinführungindieIuK-Technik
- Digitaltechnik
- Mathematik für WING 21)
- bung
- PraktikumSoftwarefürdieMathematik
- Elektronik und Schaltungstechnik
- Praktikum Elektronik und Schaltungstechnik
- Halbleiterbauelemente
- Grundlagen der Informatik
- Signale und Systeme I
- Signale und Systeme II
- Nachrichtentechnische Systeme
- Wahlpflichtmodul 1
- Wahlpflichtmodul 2
- Technisches Wahlmodul
- Hochschulpraktikum
- Wirtschaftswissenschaftlicher Bereich
- Stochastische Prozesse

### PDF vom 03.03.2003 i.d.F. 22.02.2007

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/maschinenbau/fpo-maschinenbau-neu.md`](../pruefungsordnungen/technische-fakultaet/maschinenbau/fpo-maschinenbau-neu.md)

**Pflichtmodule (1):**
- ECTS- Punkte

### 2. Juli 2015

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/7aes-ba-ma-nanotechnologie.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/7aes-ba-ma-nanotechnologie.md)

**Pflichtmodule (13):**
- M1 Nanocharakterisierung (Pflicht)
- (2) Elektronenmikroskopie
- (2) NanoSpektroskopie
- (2) Rastersondenmikroskopie/ Nanoinden- tierung
- M2 Praktikum Synthe- se/Charakterisierung (Pflicht)
- M3 Computational Nanoscience (Pflicht)
- (2) Computational Nanoscience
- M4 Top-Down Nanostrukturierung (Pflicht)
- (2) Nanoelektronik
- (2) Photolithographie
- (2) Beschichtungstechnologie
- M5 Bottom-up Nano-Synthese/Self- assembly (Pflicht)
- (2) MolekulareNanostrukturen

### Elite-MA Advanced Materials and Processes FPO MAP 20060515 i.d.F. 20190115.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-20060515-idf-20190115.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-20060515-idf-20190115.md)

**Pflichtmodule (1):**
- Masterarbeit

### Elite-MA Advanced Materials and Processes FPO MAP-M 20190115 ÄS.pdf

PO-Quelle: [`pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-m-20190115-aes.md`](../pruefungsordnungen/technische-fakultaet/werkstoffwissenschaften/elite-ma-advanced-materials-and-processes-fpo-map-m-20190115-aes.md)

**Pflichtmodule (1):**
- Masterarbeit
