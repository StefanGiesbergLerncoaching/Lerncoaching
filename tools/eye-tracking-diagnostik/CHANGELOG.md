# Changelog

Alle wichtigen Ã„nderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2026-01-09

### ðŸŽ‰ Major Release: Multi-Line-Tracking & Python-Analyse

### Added
- **Multi-Line-Tracking-System** mit 3 spezialisierten Modi:
  - Zeile 1: Vertical Tracking (OberlÃ¤ngen/UnterlÃ¤ngen-Analyse)
  - Zeile 2: Syllable Tracking (Silben-Sequenz-Analyse)
  - Zeile 3: Standard Word Tracking (4-Regionen pro Wort)
- **Python-Analyse-Pipeline** (`analyze_eyetracking.py`):
  - Automatische Klassifikation (Dekodierer/Rater/Kompensator)
  - 5 Visualisierungen (PNG): Vertical Distribution, Syllable Sequence, Regions Heatmap, Profile Radar, Statistics Summary
  - Text-Report mit diagnostischen Empfehlungen
- **3 separate CSV-Exports** (line1_vertical, line2_syllables, line3_words)
- **Responsive Layout** mit Media Queries (768px - 1200px+)
- **Metadaten-Header** in allen CSVs (Participant ID, Date, Text ID)
- **Chunking-Feature** fÃ¼r Zeile 1 (kleine WÃ¶rter <4 Buchstaben werden kombiniert)
- **Jump-Distance-Tracking** fÃ¼r Zeile 2 (Regressionen/Progressionen)
- **Left/Top-Ratio-Metriken** fÃ¼r rÃ¤umliche Fixations-Analyse

### Changed
- **AOI-Tracker komplett Ã¼berarbeitet** (v1.0 â†’ v2.0):
  - Hybrid-Architektur: Live-Tracking (Rohdaten) + Post-Processing (Metriken)
  - Fixations-Clustering-Algorithmus implementiert
  - Regionen-Zuordnung via Durchschnitts-X/Y
- **index.html:**
  - Script von `</body>` in `<head>` verschoben (verhindert "function not defined"-Fehler)
  - Webcam-Preview automatisch rechts unten positioniert (JavaScript)
  - Button fest am unteren Bildschirmrand (CSS `position: fixed`)
  - Kompakteres Layout (reduziertes Padding/Margin)
  - Responsive SchriftgrÃ¶ÃŸe (32px - 60px je nach BildschirmhÃ¶he)
- **Text-Format:** JSON erweitert mit `lines[]`-Array fÃ¼r Multi-Line-Support
- **Kalibrierungs-Instruktionen** aktualisiert (Brille abnehmen, langsam lesen)

### Fixed
- **Duration-Bug:** 1-Point-Fixationen hatten `duration=0` â†’ Jetzt korrekt berechnet
- **Webcam-Overlap:** Preview verdeckte erstes Wort â†’ Jetzt rechts unten
- **Button auÃŸerhalb Bildschirm:** Erforderte Scrollen â†’ Jetzt fest am unteren Rand
- **UTF-8-Encoding:** Verbesserter Umgang mit Umlauten (Ã¤, Ã¶, Ã¼)

### Deprecated
- **Externe CSS-Dateien** (main.css, text-stimulus.css) â†’ Alles inline in index.html
- **jsPsych-basierter Ansatz** (v0.1) â†’ VollstÃ¤ndig verworfen zugunsten Custom-LÃ¶sung

---

## [1.0.0] - 2026-01-08

### ðŸŽ‰ Initial Release: MVP funktionsfÃ¤hig

### Added
- **WebGazer.js-Integration** (manuelle Implementierung ohne Plugins)
- **9-Punkte-Kalibrierung** mit visuellen Hinweisen
- **AOI-Tracking pro Wort** (simple Version):
  - FFD (First Fixation Duration)
  - TRT (Total Reading Time)
  - Fixation Count
  - Revisits
- **CSV-Export** mit Basis-Metriken
- **3 Test-Texte** in `stimuli/baseline/`:
  - text_01.json: "Das Kaninchen" (kurz)
  - text_02.json: "Sommerausflug" (lang, problematisch)
  - text_03.json: "Der Apfelbaum" (optimal)
- **Ordnerstruktur** angelegt (stimuli/, js/, css/, analysis/, docs/)
- **GitHub Repository** initialisiert

### Changed
- **SchriftgrÃ¶ÃŸe:** Auf 48px erhÃ¶ht fÃ¼r bessere AOI-PrÃ¤zision
- **Zeilenabstand:** Auf 2.0 reduziert fÃ¼r Vollbild-Darstellung ohne Scrollen

### Fixed
- **Scrollen-Problem:** Text passt nun komplett auf Bildschirm (keine Scroll-Interaktion)
- **AOI-Koordinaten:** Werden nur beim Start berechnet (keine dynamische Aktualisierung nÃ¶tig)

---

## [0.1.0] - 2026-01-07

### ðŸ—ï¸ Setup & GrundgerÃ¼st

### Added
- **Projekt-Setup:**
  - GitHub Repository erstellt
  - VS Code Workspace konfiguriert
  - Live Server Extension eingerichtet
- **Basis-Code** (jsPsych-basiert, spÃ¤ter verworfen):
  - Experiment-Timeline mit Instruktionen
  - Kalibrierungs-Plugin-Versuch
  - Text-Display-Plugin
- **Ordnerstruktur:**
  ```
  eye-tracking-diagnostik/
  â”œâ”€â”€ index.html
  â”œâ”€â”€ css/
  â”œâ”€â”€ js/
  â”œâ”€â”€ stimuli/
  â”œâ”€â”€ analysis/
  â””â”€â”€ docs/
  ```
- **Erste Dokumentation:**
  - README.md (basic)
  - requirements.txt (Python)

### Changed
- N/A (Erste Version)

### Deprecated
- **jsPsych-Ansatz:** Zu komplex fÃ¼r WebGazer-Integration â†’ Verworfen in v1.0

### Removed
- N/A (Erste Version)

### Fixed
- N/A (Erste Version)

---

## [Unreleased] - Geplante Features

### Phase 2: Intervention (In Arbeit)
- [ ] **Leetspeak-Generator** (Python-Script)
  - Automatische Text-Konvertierung: "Apfelbaum" â†’ "Ap7e1b4um"
  - Neue JSON-Dateien in `stimuli/intervention/`
- [ ] **OberlÃ¤ngen-Intervention** (CSS-Maskierung)
  - Nur obere 60% des Textes sichtbar
  - Neue Test-Datei: `text_oberlÃ¤ngen.json`
- [ ] **Timeline-Erweiterung:**
  - Baseline â†’ Intervention â†’ Retest
  - Delta-Metriken in Python-Script
- [ ] **Mehr Test-Texte:**
  - 5-10 verschiedene Texte (Schwierigkeitsgrade: leicht, mittel, schwer)
  - Altersgerechte Themen (6-12 Jahre)

### Phase 3: Validierung (Geplant)
- [ ] **Probanden-Tests:**
  - Rekrutierung (n=20-30 Kinder)
  - Ethik-Antrag
  - Datenerhebung (3-5 Sitzungen pro Kind)
- [ ] **Validierungs-Studien:**
  - Inter-Rater-ReliabilitÃ¤t (Îº > 0.70)
  - Vergleich mit etablierten Tests (SLRT-II, ELFE)
  - SensitivitÃ¤t/SpezifitÃ¤t-Analyse
- [ ] **Wissenschaftliche Publikation:**
  - Paper fÃ¼r Dyslexia Journal
  - Trainingskonzept fÃ¼r Diagnostiker
  - Potenzielle Lizenzierung

---

## Version-Format

- **Major.Minor.Patch** (z.B. 2.0.0)
  - **Major:** Breaking Changes (API-Ã„nderungen, komplette Neuarchitektur)
  - **Minor:** Neue Features (abwÃ¤rtskompatibel)
  - **Patch:** Bugfixes (keine neuen Features)

---

## Release-Tags

- `v2.0.0` - Multi-Line-Tracking & Python-Analyse (09.01.2026)
- `v1.0.0` - MVP funktionsfÃ¤hig (08.01.2026)
- `v0.1.0` - Setup & GrundgerÃ¼st (07.01.2026)

---

## Mitwirkende

- **Stefan Giesberg** - Projektentwickler & Maintainer
- **Anthropic Claude** - KI-assistierte Entwicklung

---

*Letztes Update: 09.01.2026*