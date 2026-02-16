# EYE-TRACKING PROJEKT: VOLLSTÃ„NDIGE ZUSAMMENFASSUNG v2.0

---

## PROJEKTSTAND: MVP v2.0 FUNKTIONSFÃ„HIG âœ“

**Datum:** 09.01.2026  
**Status:** Phase 2 gestartet - Multi-Line-Tracking lÃ¤uft, Python-Analyse implementiert

### **Was funktioniert:**
- âœ“ Browser-basiertes Eye-Tracking (WebGazer.js v3.0)
- âœ“ Manuelle 9-Punkte-Kalibrierung
- âœ“ **MULTI-LINE-TRACKING** (3 verschiedene Zeilen mit verschiedenen Strategien)
  - Zeile 1: Vertical Tracking (OberlÃ¤ngen/UnterlÃ¤ngen, Chunking)
  - Zeile 2: Syllable Tracking (Silben-Sequenz, horizontale Fokussierung)
  - Zeile 3: Standard Word Tracking (4-Regionen: 2Ã—2)
- âœ“ **3 separate CSV-Exports** (line1_vertical, line2_syllables, line3_words)
- âœ“ **Python-Analyse-Pipeline** mit Visualisierungen & Reports
- âœ“ **Automatische Leserprofil-Klassifikation** (Dekodierer/Rater/Kompensator)
- âœ“ Responsive Layout (funktioniert auf 768px - 1200px+ Bildschirmen)
- âœ“ Webcam-Preview rechts unten positioniert (verdeckt Text nicht)
- âœ“ Button fest am unteren Bildschirmrand (immer sichtbar)

### **Was noch fehlt:**
- â³ Leetspeak-Intervention (geplant Phase 2)
- â³ OberlÃ¤ngen-Intervention (geplant Phase 2)
- â³ Retest nach Intervention (geplant Phase 2)
- â³ Mehrere Test-Texte (nur 1 vorhanden)
- â³ Validierung mit echten Probanden (Phase 3)

---

## TECHNISCHER STACK

### **Frontend:**
- **WebGazer.js** (v3.0) - Eye-Tracking via Webcam
- **Vanilla JavaScript** - Kalibrierung & Experiment-Flow
- **Custom AOI-Tracker v2.0** - Multi-Line-Tracking mit Post-Processing
- **HTML/CSS** - Responsive Interface

### **Backend (Analyse):**
- **Python 3.8+** - Datenanalyse
- **Pandas/NumPy** - CSV-Verarbeitung & Statistik
- **Matplotlib/Seaborn** - Visualisierung (5 Plots)
- **Automatische Klassifikation** - Machine-Learning-Ã¤hnlicher Scoring-Algorithmus

### **Hosting:**
- **GitHub Pages** (Repository: eye-tracking-diagnostik)
- **Lokal:** VS Code + Live Server

---

## ORDNERSTRUKTUR v2.0

```
eye-tracking-diagnostik/
â”‚
â”œâ”€â”€ index.html                          âœ“ v2.0 (Multi-Line, responsive)
â”‚
â”œâ”€â”€ css/                                â—‹ (deprecated, alles in index.html)
â”‚   â””â”€â”€ *.css                           
â”‚
â”œâ”€â”€ js/
â”‚   â”œâ”€â”€ aoi-tracker.js                  âœ“ v1.0 (Backup)
â”‚   â””â”€â”€ aoi-tracker-v2.js               âœ“ v2.0 (Multi-Line-Tracking)
â”‚
â”œâ”€â”€ stimuli/
â”‚   â”œâ”€â”€ baseline/
â”‚   â”‚   â”œâ”€â”€ text_01.json                âœ“ v1.0 (Kaninchen, alt)
â”‚   â”‚   â”œâ”€â”€ text_02.json                âœ“ v1.0 (Sommerausflug, alt)
â”‚   â”‚   â”œâ”€â”€ text_03.json                âœ“ v1.0 (Apfelbaum, alt)
â”‚   â”‚   â””â”€â”€ text_multiline.json         âœ“ v2.0 (3-Zeilen-Format, aktuell)
â”‚   â”œâ”€â”€ intervention/                   â—‹ (leer, geplant)
â”‚   â””â”€â”€ retest/                         â—‹ (leer, geplant)
â”‚
â”œâ”€â”€ analysis/                           âœ“ NEU in v2.0
â”‚   â”œâ”€â”€ analyze_eyetracking.py          âœ“ Hauptanalyse-Script
â”‚   â””â”€â”€ requirements.txt                âœ“ Python-Dependencies
â”‚
â”œâ”€â”€ output_analysis/                    âœ“ Auto-generiert
â”‚   â”œâ”€â”€ line1_vertical_distribution.png
â”‚   â”œâ”€â”€ line2_syllable_sequence.png
â”‚   â”œâ”€â”€ line3_regions_heatmap.png
â”‚   â”œâ”€â”€ profile_radar.png
â”‚   â”œâ”€â”€ statistics_summary.png
â”‚   â””â”€â”€ report_[ID].txt
â”‚
â”œâ”€â”€ docs/                               â—‹ (leer, geplant)
â”‚
â””â”€â”€ README.md                           âœ“ Aktualisiert v2.0
```

**Legende:**
- âœ“ = FunktionsfÃ¤hig/Implementiert
- â—‹ = Vorbereitet/geplant, aber noch nicht aktiv

---

## AKTUELLER CODE-STAND

### **1. index.html (v2.0)**

**Neue Features:**
- Responsive Layout mit Media Queries
- Webcam-Preview automatisch rechts unten positioniert
- Button fest am unteren Bildschirmrand
- Text-Generierung fÃ¼r 3 verschiedene Tracking-Modi
- Script im `<head>` (verhindert "function not defined"-Fehler)

**Ã„nderungen zu v1.0:**
- âœ… Kompakteres Layout (weniger Padding/Margin)
- âœ… Responsive SchriftgrÃ¶ÃŸe (32px - 60px je nach BildschirmhÃ¶he)
- âœ… Keine externen CSS-Dateien mehr (alles inline)
- âœ… Webcam-Positionierung via JavaScript (setTimeout + CSS-Override)

---

### **2. js/aoi-tracker-v2.js (v2.0)**

**Architektur:**
- **Phase 1:** Initialisierung (AOIs fÃ¼r alle 3 Zeilen)
- **Phase 2:** Live-Tracking (nur Rohdaten sammeln)
- **Phase 3:** Post-Processing (Fixationen clustern, Metriken berechnen)
- **Phase 4:** CSV-Export (3 separate Dateien)

**Tracking-Modi:**

#### **Zeile 1: Vertical Tracking**
- Chunking kleiner WÃ¶rter (<4 Buchstaben)
- 2 Regionen pro Chunk: Oben (0-50%) / Unten (50-100%)
- **Metriken:** FFD, TRT, Fixation Count, Revisits, Top-Duration, Bottom-Duration, Top-Ratio

#### **Zeile 2: Syllable Tracking**
- Jede Silbe = eigene AOI
- Sequenz-Tracking (in welcher Reihenfolge gelesen?)
- **Metriken:** FFD, Skip, Read-Order, From-Syllable-ID, Jump-Distance

#### **Zeile 3: Standard Word Tracking**
- 4 Regionen pro Wort (2Ã—2: Top-Left, Top-Right, Bottom-Left, Bottom-Right)
- **Metriken:** FFD, TRT, Fixation Count, Revisits, 4Ã—Region-Duration, Left-Ratio, Top-Ratio

**Technische Details:**
- Fixationen werden via Clustering erkannt (gleiche AOI + <200ms Abstand)
- Regionen-Zuordnung via Durchschnitts-X/Y aller Gaze-Points einer Fixation
- Duration-Bug gefixt (auch 1-Point-Fixationen haben jetzt Duration)

---

### **3. stimuli/baseline/text_multiline.json (v2.0)**

**Struktur:**
```json
{
  "id": "baseline_multiline_v1",
  "title": "Der Apfelbaum (Multi-Line)",
  "lines": [
    {
      "line_id": 1,
      "tracking_mode": "vertical",
      "text": "Im Garten steht ein groÃŸer Apfelbaum.",
      "chunks": [
        { "chunk_id": 0, "text": "Im Garten", "words": ["Im", "Garten"] },
        { "chunk_id": 1, "text": "steht", "words": ["steht"] },
        ...
      ]
    },
    {
      "line_id": 2,
      "tracking_mode": "syllables",
      "text": "Seine Ã„ste hÃ¤ngen voller roter FrÃ¼chte.",
      "syllables": [
        { "syl_id": 0, "text": "Sei", "word": "Seine" },
        { "syl_id": 1, "text": "ne", "word": "Seine" },
        ...
      ]
    },
    {
      "line_id": 3,
      "tracking_mode": "standard",
      "text": "Jeden Herbst pflÃ¼cken wir die sÃ¼ÃŸen Ã„pfel.",
      "words": [
        { "word_id": 0, "text": "Jeden" },
        ...
      ]
    }
  ]
}
```

**Design-Entscheidungen:**
- Zeile 1: Chunking "Im Garten" (klein+groÃŸ) fÃ¼r realistischere AOI-GrÃ¶ÃŸen
- Zeile 2: Manuelle Silbentrennung (kein automatischer Silbentrenner)
- Zeile 3: Standard-Wortliste

---

### **4. analysis/analyze_eyetracking.py (v2.0)**

**Klasse:** `EyeTrackingAnalyzer`

**Pipeline:**
1. `load_data()` - LÃ¤dt 3 CSVs + extrahiert Metadaten
2. `calculate_statistics()` - Berechnet deskriptive Statistiken
3. `classify_reader_profile()` - Scoring-basierte Klassifikation
4. `create_visualizations()` - Erstellt 5 PNG-Plots
5. `generate_report()` - Schreibt Text-Report

**Klassifikations-Algorithmus:**

```python
scores = {'decoder': 0, 'guesser': 0, 'compensator': 0}

# Dekodierer-Indikatoren:
if mean_FFD > 300: scores['decoder'] += 2
if mean_fixations > 3: scores['decoder'] += 2
if 0.45 <= top_ratio <= 0.55: scores['decoder'] += 2
if left_ratio > 0.55: scores['decoder'] += 1
if skip_rate < 10: scores['decoder'] += 2

# Rater-Indikatoren:
if mean_FFD < 200: scores['guesser'] += 2
if skip_rate > 30: scores['guesser'] += 3
if top_ratio > 0.60: scores['guesser'] += 2
if mean_jump_distance > 2.0: scores['guesser'] += 2

# Kompensator-Indikatoren:
if mean_revisits > 1: scores['compensator'] += 3
if regressions > 2: scores['compensator'] += 2
if TRT > FFD * 2: scores['compensator'] += 2

# Klassifikation:
profile = max(scores, key=scores.get)
confidence = scores[profile] / sum(scores.values())
```

**Visualisierungen:**
1. **line1_vertical_distribution.png** - Bar-Chart: Top vs. Bottom Duration pro Chunk
2. **line2_syllable_sequence.png** - Line-Plot: Silben-Lesereihenfolge vs. ideale Sequenz
3. **line3_regions_heatmap.png** - Heatmap: 4 Regionen Ã— WÃ¶rter
4. **profile_radar.png** - Radar-Chart: Decoder/Guesser/Compensator-Scores
5. **statistics_summary.png** - 4 Subplots: Skip-Rates, FFD, Fixation Counts, Ratios

---

## CSV-OUTPUT-FORMAT v2.0

### **Datei 1: `line1_vertical_[timestamp].csv`**
```csv
# EXPERIMENT METADATA
# Participant ID: TEST_123
# Date: 2026-01-09...
# Text: baseline_multiline_v1

# LINE 1: VERTICAL TRACKING (Chunks)
chunk_id,text,FFD,TRT,fixation_count,revisits,skipped,top_duration,bottom_duration,top_ratio
0,"Im Garten",234,567,3,1,0,320,247,0.564
1,"steht",187,187,1,0,0,95,92,0.508
...
```

**Spalten:**
- `chunk_id`: Index (0-basiert)
- `text`: Chunk-Text (z.B. "Im Garten")
- `FFD`: First Fixation Duration (ms)
- `TRT`: Total Reading Time (ms)
- `fixation_count`: Anzahl Fixationen
- `revisits`: Anzahl RÃ¼cksprÃ¼nge (Re-Fixationen)
- `skipped`: 1 = Ã¼bersprungen, 0 = gelesen
- `top_duration`: Fixationsdauer obere HÃ¤lfte (ms)
- `bottom_duration`: Fixationsdauer untere HÃ¤lfte (ms)
- `top_ratio`: Anteil oben (0-1, 0.5 = ausgeglichen)

---

### **Datei 2: `line2_syllables_[timestamp].csv`**
```csv
# LINE 2: SYLLABLE TRACKING
syl_id,syllable,word,FFD,skipped,read_order,from_syl_id,jump_distance
0,"Sei","Seine",145,0,1,NULL,NULL
1,"ne","Seine",87,0,2,0,1
2,"Ã„s","Ã„ste",156,0,3,1,1
3,"te","Ã„ste",0,1,NULL,2,NULL
4,"hÃ¤n","hÃ¤ngen",189,0,4,2,2
...
```

**Spalten:**
- `syl_id`: Silben-Index (0-basiert)
- `syllable`: Silbentext (z.B. "Sei")
- `word`: ZugehÃ¶riges Wort
- `FFD`: First Fixation Duration (ms)
- `skipped`: 1 = Ã¼bersprungen, 0 = gelesen
- `read_order`: Zeitliche Reihenfolge der ersten Fixation
- `from_syl_id`: Von welcher Silbe kam der Blick?
- `jump_distance`: Silben-Index-Differenz (negativ = Regression)

**Diagnostischer Wert:**
- Perfekt sequenziell (0â†’1â†’2â†’3...): **Dekodierer**
- Chaotisch (0â†’3â†’7â†’...): **Rater**
- Sequenziell + Regressionen (0â†’1â†’3â†’2...): **Kompensator**

---

### **Datei 3: `line3_words_[timestamp].csv`**
```csv
# LINE 3: STANDARD WORD TRACKING
word_id,word,FFD,TRT,fixation_count,revisits,skipped,tl_dur,tr_dur,bl_dur,br_dur,left_ratio,top_ratio
0,"Jeden",234,567,3,1,0,145,123,156,143,0.531,0.472
1,"Herbst",187,345,2,0,0,89,98,78,80,0.484,0.542
...
```

**Spalten:**
- `word_id`: Wort-Index (0-basiert)
- `word`: Worttext
- `FFD`: First Fixation Duration (ms)
- `TRT`: Total Reading Time (ms)
- `fixation_count`: Anzahl Fixationen
- `revisits`: Anzahl RÃ¼cksprÃ¼nge
- `skipped`: 1 = Ã¼bersprungen, 0 = gelesen
- `tl_dur`: Top-Left Region Duration (ms)
- `tr_dur`: Top-Right Region Duration (ms)
- `bl_dur`: Bottom-Left Region Duration (ms)
- `br_dur`: Bottom-Right Region Duration (ms)
- `left_ratio`: Anteil links (0-1, >0.55 = Wortanfang-Fokus)
- `top_ratio`: Anteil oben (0-1, >0.60 = OberlÃ¤ngen-Fokus)

**Diagnostischer Wert:**
- `left_ratio > 0.55`: Wortanfang-Fokus (typisch Dekodierer)
- `top_ratio > 0.60`: Nur OberlÃ¤ngen (typisch Rater)
- `left_ratio â‰ˆ 0.5, top_ratio â‰ˆ 0.5`: Ausgeglichen (Dekodierer)

---

## BEKANNTE LIMITATIONEN

### **1. WebGazer.js-PrÃ¤zision**
**Problem:** ~50-100px rÃ¤umliche UnschÃ¤rfe, 10-15 Hz Sampling-Rate  
**Auswirkung:** Keine echte Saccade-Erkennung mÃ¶glich  
**Workaround:** Fokus auf Fixations-basierte Metriken (nicht Saccaden)

### **2. Kalibrierungs-SensitivitÃ¤t**
**Faktoren:**
- Brille (Reflexionen)
- Beleuchtung (zu dunkel/zu hell)
- Kopfbewegungen
- Webcam-QualitÃ¤t

**LÃ¶sung:**
- Klare Instruktionen ("Brille abnehmen, Licht an, Kopf ruhig")
- 9-Punkte-Kalibrierung (besser als 5-Punkte)
- Kalibrierungs-QualitÃ¤ts-Check (geplant Phase 3)

### **3. Scrollen bricht Tracking**
**Problem:** AOI-Koordinaten werden nur beim Start berechnet  
**LÃ¶sung:** Text muss komplett auf Bildschirm passen (responsive Layout)

### **4. UTF-8-Encoding-Probleme**
**Problem:** Umlaute werden manchmal falsch exportiert (Ã¤ â†’ ÃƒÂ¤)  
**Workaround:** CSV mit UTF-8-Encoding Ã¶ffnen (Excel: "Daten â†’ Aus Text/CSV")

---

## PARAMETER ZUM ANPASSEN

### **SchriftgrÃ¶ÃŸe (responsive):**
**In `index.html`, `<style>`, Zeile ~30:**
```css
.text-stimulus {
    font-size: 48px;  /* Standard */
}

@media (max-height: 900px) {
    .text-stimulus { font-size: 40px; }  /* Laptops */
}

@media (max-height: 768px) {
    .text-stimulus { font-size: 32px; }  /* Tablets */
}

@media (min-height: 1200px) {
    .text-stimulus { font-size: 60px; }  /* GroÃŸe Monitore */
}
```

### **Zeilenabstand:**
```css
line-height: 1.6;  /* Kompakt (v2.0) */
```

### **Fixations-Clustering-Schwellenwert:**
**In `aoi-tracker-v2.js`, Zeile ~180:**
```javascript
gaze.timestamp - currentFixation.endTime > 200  // 200ms Schwellenwert
```

### **Kalibrierungspunkte:**
**In `index.html`, Script-Bereich:**
```javascript
const calibrationPoints = [
    [10, 10], [10, 50], [10, 90],
    [50, 10], [50, 50], [50, 90],
    [90, 10], [90, 50], [90, 90]
];
```

---

## WORKFLOW FÃœR TESTS

### **1. Vorbereitung:**
- VS Code Ã¶ffnen
- Repository-Ordner Ã¶ffnen
- Live Server starten (Rechtsklick auf index.html)

### **2. Test durchfÃ¼hren:**
- Browser: Willkommens-Screen
- "Starten" â†’ Webcam erlauben
- Kalibrierung: 9 Punkte je 3x klicken (Punkt anschauen!)
- Text: **Langsam laut vorlesen** (KEIN Speedreading!)
- "Fertig" â†’ 3 CSVs werden heruntergeladen

### **3. Daten analysieren:**
**Terminal:**
```bash
cd eye-tracking-diagnostik
python analysis/analyze_eyetracking.py \
  line1_vertical_123.csv \
  line2_syllables_123.csv \
  line3_words_123.csv
```

**Output:**
- `output_analysis/` Ordner wird erstellt
- 5 PNG-Visualisierungen
- 1 Text-Report mit Klassifikation

### **4. Ergebnisse prÃ¼fen:**
- Report Ã¶ffnen: `output_analysis/report_TEST_123.txt`
- Visualisierungen ansehen
- Klassifikation interpretieren (Decoder/Guesser/Compensator)

### **5. GitHub committen:**
- GitHub Desktop Ã¶ffnen
- Ã„nderungen sehen
- Commit-Message schreiben
- "Commit to main"
- "Push origin"

---

## NÃ„CHSTE ENTWICKLUNGSSCHRITTE

### **Phase 2: Intervention (Aktuell in Arbeit)**

**PrioritÃ¤t 1: Leetspeak-Generator**
- Python-Script fÃ¼r automatische Text-Konvertierung
  - Input: `text_multiline.json`
  - Output: `text_leetspeak.json` ("Apfelbaum" â†’ "Ap7e1b4um")
- Neue JSON-Dateien in `stimuli/intervention/`
- Timeline erweitern: Baseline â†’ Leetspeak â†’ Retest

**PrioritÃ¤t 2: OberlÃ¤ngen-Intervention**
- CSS-Maskierung (nur obere 60% des Textes sichtbar)
- Neue Test-Datei: `text_oberlÃ¤ngen.json`
- Messen: Zusammenbruch der Lese-Performance?

**PrioritÃ¤t 3: Delta-Metriken in Python**
- `compare_baseline_intervention.py`
- Berechnet: TRT_Leetspeak - TRT_Baseline
- Visualisierung: Before/After-Plots

**PrioritÃ¤t 4: Mehr Test-Texte**
- 5-10 verschiedene Texte
  - Leicht (Grundwortschatz, 3 Zeilen)
  - Mittel (lÃ¤ngere SÃ¤tze, 5 Zeilen)
  - Schwer (FachwÃ¶rter, 7 Zeilen)
- Altersgerechte Themen (6-12 Jahre)
- Morphologisch interessant (fÃ¼r Grammatik-Traps)

---

### **Phase 3: Validierung (Geplant)**

**Ziel:** Wissenschaftliche Validierung mit echten Probanden

**Tasks:**
1. **Probanden-Rekrutierung** (n=20-30 Kinder, 6-12 Jahre)
2. **Ethik-Antrag** (bei Uni/IRB)
3. **Test-Protokoll** erstellen
4. **Elterneinwilligung** einholen
5. **Datenerhebung** (3-5 Sitzungen pro Kind)
6. **Inter-Rater-ReliabilitÃ¤t** (2 unabhÃ¤ngige Diagnostiker)
7. **Validierung gegen etablierte Tests** (z.B. SLRT-II, ELFE)

**Erwartete Ergebnisse:**
- SensitivitÃ¤t: >80% (erkennt LeseschwÃ¤che)
- SpezifitÃ¤t: >75% (keine False Positives)
- Inter-Rater-Agreement: Îº > 0.70 (Cohen's Kappa)

---

## WISSENSCHAFTLICHE ZIELE

### **Drei Hauptziele:**

**1. Interventions-Dokumentation**
- **Status:** â³ In Arbeit (Baseline funktioniert, Intervention fehlt)
- **Ziel:** Objektive Vorher-Nachher-Vergleiche
- **Nutzen:** Wirksamkeitsnachweis fÃ¼r ElterngesprÃ¤che & Kostenerstattung

**2. Taxonomie von Lesetaktiken**
- **Status:** âœ“ Implementiert (automatische Klassifikation)
- **Ziel:** Differenzierung zwischen:
  - **Dekodierer:** Langsam + viele Fixationen, geringer Interventions-Effekt
  - **Rater:** Schnell in Baseline, massiver Einbruch bei Leetspeak
  - **Kompensatoren:** Gemischt, viele Regressionen
- **Nutzen:** Individualisierte FÃ¶rderempfehlungen

**3. Wissenschaftliche Verwertung**
- **Status:** â³ Vorbereitet (Datenstruktur ready, Validierung fehlt)
- **Ziel:** Paper-Publikation (Dyslexia, Gifted Child Quarterly)
- **Nutzen:** Trainingskonzept fÃ¼r andere Diagnostiker, potenzielle Lizenzierung

---

## LITERATUR & QUELLEN

**Theoretische Grundlagen:**
- Silverman, L. K. (1997): "The Construct of Asynchronous Development"
- Shaw et al. (2006): "Intellectual ability and cortical development" (Nature)
- Columbus Group (1991): Definition von Hochbegabung

**Technische Basis:**
- WebGazer.js: Papoutsaki et al. (2016), Brown University
  - GitHub: https://github.com/brownhci/WebGazer
  - Paper: "WebGazer: Scalable Webcam Eye Tracking Using User Interactions"

**Eye-Tracking in Reading Research:**
- Rayner, K. (1998): "Eye movements in reading and information processing"
- Reichle et al. (2003): "The E-Z Reader model of eye-movement control in reading"

**Validierung:**
- Kranz et al. (2024): "Twice-exceptionality unmasked" (Dyslexia Journal)
- Davidson Institute, SENG, Colorado DoE: Twice-Exceptional Resources

---

## TECHNISCHE ANFORDERUNGEN

### **Client-Seite:**
- **Browser:** Chrome/Edge (neueste Version empfohlen)
  - Firefox funktioniert, aber schlechtere WebGazer-Performance
  - Safari: Nur eingeschrÃ¤nkt (iOS-Probleme)
- **Webcam:** 720p+ empfohlen (1080p ideal)
- **Bildschirm:** 1366Ã—768 Minimum, 1920Ã—1080 empfohlen
- **Internet:** Nur fÃ¼r WebGazer.js-CDN (einmalig beim Laden)

### **Entwicklungsumgebung:**
- **VS Code** + Live Server Extension
- **GitHub Desktop** (optional, fÃ¼r Version-Control)
- **Python 3.8+** (fÃ¼r Analyse)
  - Dependencies: `pip install pandas numpy matplotlib seaborn --break-system-packages`

### **Hosting (GitHub Pages):**
```bash
# Repository Settings â†’ Pages
# Source: main branch, / (root)
# URL: https://username.github.io/eye-tracking-diagnostik
```

---

## KONTAKT & SUPPORT

**GitHub Repository:**
```
https://github.com/[DEIN-USERNAME]/eye-tracking-diagnostik
```

**Live-Demo (nach GitHub Pages Deploy):**
```
https://[DEIN-USERNAME].github.io/eye-tracking-diagnostik
```

**Entwickler-Kontakt:**
- Stefan Giesberg
- Projekt: Eye-Tracking Diagnostik v2.0
- Zweck: Hochbegabten-Diagnostik & Lesetaktik-Taxonomie

---

## CHANGELOG

### **v2.0 (09.01.2026) - Multi-Line-Tracking & Python-Analyse**
- âœ… Implementiert: 3-Zeilen-Multi-Tracking (Vertical, Syllables, Standard)
- âœ… Implementiert: Python-Analyse-Pipeline mit 5 Visualisierungen
- âœ… Implementiert: Automatische Leserprofil-Klassifikation
- âœ… Implementiert: Responsive Layout (768px - 1200px+)
- âœ… Fix: Webcam-Preview rechts unten positioniert
- âœ… Fix: Button fest am unteren Bildschirmrand
- âœ… Fix: Duration-Berechnung fÃ¼r 1-Point-Fixationen
- âœ… Neu: 3 separate CSV-Exports (line1, line2, line3)
- âœ… Neu: Text-Report mit Interpretation

### **v1.0 (08.01.2026) - MVP funktionsfÃ¤hig**
- âœ… WebGazer-Integration manuell (ohne jsPsych-Plugins)
- âœ… 9-Punkte-Kalibrierung
- âœ… AOI-Tracking pro Wort (simple Version)
- âœ… CSV-Export mit Basis-Metriken
- âœ… Optimiert fÃ¼r groÃŸe Schrift (48px) + kein Scrollen
- âœ… Test-Text: "Der Apfelbaum" (19 WÃ¶rter, 3 Zeilen)

### **v0.1 (07.01.2026) - Setup & GrundgerÃ¼st**
- âœ… Repository erstellt
- âœ… Ordnerstruktur angelegt
- âœ… Basis-Code (jsPsych-basiert, spÃ¤ter verworfen)

---

## NOTIZEN FÃœR NEUES PROJEKT

### **Was funktioniert stabil:**
- âœ… `index.html` v2.0 (komplett in einer Datei, responsive)
- âœ… `js/aoi-tracker-v2.js` (Multi-Line-Tracking mit Post-Processing)
- âœ… `stimuli/baseline/text_multiline.json` (3-Zeilen-Format)
- âœ… `analysis/analyze_eyetracking.py` (vollstÃ¤ndige Analyse-Pipeline)

### **Was noch experimentell ist:**
- âš ï¸ Kalibrierungsgenauigkeit (abhÃ¤ngig von Hardware/Setup)
- âš ï¸ Klassifikations-Algorithmus (noch nicht validiert mit echten Probanden)
- âš ï¸ UTF-8-Encoding (manchmal Probleme bei Umlauten)

### **Was definitiv gebraucht wird:**
- ðŸŽ¯ Leetspeak-Intervention (fÃ¼r Rater-Erkennung)
- ðŸŽ¯ OberlÃ¤ngen-Intervention (fÃ¼r okulomotorische Herausforderung)
- ðŸŽ¯ Mehr Test-Texte (5-10 verschiedene Schwierigkeitsgrade)
- ðŸŽ¯ Validierung mit echten Probanden (n=20-30)
- ðŸŽ¯ Inter-Rater-ReliabilitÃ¤t (2 unabhÃ¤ngige Diagnostiker)

---

**ENDE DER ZUSAMMENFASSUNG v2.0**

**Status:** Bereit fÃ¼r Phase 2 (Intervention) âœ“