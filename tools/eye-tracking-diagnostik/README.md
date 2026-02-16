# 👁️ Eye-Tracking Lese-Diagnostik v2.0

**Browser-basiertes Eye-Tracking-System zur Diagnose von Lesetaktiken bei hochbegabten Kindern mit Lese-Rechtschreib-Schwäche**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![WebGazer.js](https://img.shields.io/badge/WebGazer.js-v3.0-green.svg)](https://webgazer.cs.brown.edu/)

---

## 🎯 Projektziel

Entwicklung eines **objektiven, web-basierten Diagnose-Tools**, das verschiedene Lesetaktiken bei hochbegabten Kindern identifiziert:

- **Dekodierer:** Langsames, buchstabenweises Lesen
- **Rater:** Schnelles Überfliegen/Raten basierend auf Wortformen
- **Kompensatoren:** Hoher kognitiver Aufwand durch ständige Rücksprünge und Korrekturen

Das System ermöglicht:
1. **Interventions-Dokumentation** (Vorher-Nachher-Vergleiche)
2. **Taxonomie von Lesetaktiken** (automatische Klassifikation)
3. **Wissenschaftliche Verwertung** (Paper-Publikation, Trainingskonzept)

---

## ✨ Features

### **Multi-Line-Tracking v2.0:**
- ✅ **Zeile 1:** Oberlängen/Unterlängen-Analyse (Vertikal-Tracking)
- ✅ **Zeile 2:** Silben-Sequenz-Analyse (Horizontal-Tracking)
- ✅ **Zeile 3:** Standard-Wort-Tracking (4-Regionen pro Wort)

### **Automatische Analyse:**
- ✅ Python-Script mit **5 Visualisierungen** (PNG)
- ✅ **Automatische Klassifikation** (Dekodierer/Rater/Kompensator)
- ✅ **Detaillierter Report** mit diagnostischen Empfehlungen

### **Technologie:**
- ✅ **WebGazer.js** - Webcam-basiertes Eye-Tracking (keine Hardware nötig!)
- ✅ **Responsive Design** - Funktioniert auf 768px - 1200px+ Bildschirmen
- ✅ **CSV-Export** - 3 separate Dateien mit 227+ Datenpunkten

---

## 🚀 Quick Start

### **1. Repository klonen:**
```bash
git clone https://github.com/[YOUR-USERNAME]/eye-tracking-diagnostik.git
cd eye-tracking-diagnostik
```

### **2. Dependencies installieren:**
```bash
pip install pandas numpy matplotlib seaborn --break-system-packages
```

### **3. Test im Browser starten:**
```bash
# VS Code mit Live Server Extension:
# Rechtsklick auf index.html → "Open with Live Server"

# Oder mit Python:
python -m http.server 8000
# Dann öffnen: http://localhost:8000
```

### **4. Test durchführen:**
1. Browser öffnet Willkommens-Screen
2. "Starten" klicken → Webcam erlauben
3. **9-Punkte-Kalibrierung** (jeden Punkt 3× anklicken)
4. Text **langsam laut vorlesen**
5. "Fertig" klicken → 3 CSV-Dateien werden heruntergeladen

### **5. Daten analysieren:**
```bash
python analysis/analyze_eyetracking.py \
  line1_vertical_123.csv \
  line2_syllables_123.csv \
  line3_words_123.csv

# Output: output_analysis/ Ordner mit 5 PNGs + 1 Report
```

**Detaillierte Anleitung:** Siehe [`SETUP.md`](SETUP.md)

---

## 📊 Beispiel-Output

### **Automatische Klassifikation:**
```
Profil: DEKODIERER
Konfidenz: 75.3%
Begründung: Langsames, gründliches Dekodieren (jeder Buchstabe wird gelesen)

Scores:
  - Decoder: 9
  - Guesser: 3
  - Compensator: 0
```

### **Visualisierungen:**
- `line1_vertical_distribution.png` - Oberlängen vs. Unterlängen
- `line2_syllable_sequence.png` - Silben-Lesereihenfolge
- `line3_regions_heatmap.png` - 4-Regionen-Heatmap
- `profile_radar.png` - Leserprofil-Radar-Chart
- `statistics_summary.png` - Statistik-Übersicht

---

## 📁 Projektstruktur

```
eye-tracking-diagnostik/
├── index.html                  # Haupt-Interface (v2.0)
├── js/
│   └── aoi-tracker-v2.js       # Multi-Line-Tracking-Engine
├── stimuli/
│   └── baseline/
│       └── text_multiline.json # 3-Zeilen-Test-Text
├── analysis/
│   ├── analyze_eyetracking.py  # Python-Analyse-Script
│   └── requirements.txt        # Dependencies
├── output_analysis/            # Auto-generiert
│   ├── *.png                   # Visualisierungen
│   └── report_*.txt            # Diagnostischer Report
└── docs/                       # Vollständige Dokumentation
    ├── Struktur_und_Stand_v2.md
    ├── Metriken_v2.md
    └── IP_Schutz_und_Workflow.md
```

---

## 🔬 Wissenschaftlicher Hintergrund

### **Theoretische Basis:**
- **Asynchrone Entwicklung** (Silverman, 1997)
- **Twice-Exceptional Profiles** (Kranz et al., 2024)
- **Eye-Movement Control in Reading** (Rayner, 1998)

### **Technologie:**
- **WebGazer.js** (Papoutsaki et al., 2016, Brown University)
  - Browser-basiertes Eye-Tracking via Webcam
  - ~50-100px Genauigkeit, 10-15 Hz Sampling-Rate

---

## 📈 Metriken

### **Zeile 1: Vertical Tracking**
- **10 Metriken pro Chunk:** FFD, TRT, Fixation Count, Revisits, Top/Bottom-Duration, Top-Ratio
- **Diagnostischer Fokus:** Oberlängen-Sensitivität

### **Zeile 2: Syllable Tracking**
- **8 Metriken pro Silbe:** FFD, Skip, Read-Order, Jump-Distance
- **Diagnostischer Fokus:** Sequenzielle vs. chaotische Lesereihenfolge

### **Zeile 3: Standard Word Tracking**
- **13 Metriken pro Wort:** FFD, TRT, 4×Region-Duration, Left/Top-Ratio
- **Diagnostischer Fokus:** Horizontale/vertikale Fixations-Verteilung

**→ Total: 227+ Datenpunkte pro Test-Session**

Details: Siehe [`docs/Metriken_v2.md`](docs/Metriken_v2.md)

---

## 🛠️ System-Anforderungen

### **Client-Seite:**
- **Browser:** Chrome/Edge (neueste Version empfohlen)
- **Webcam:** 720p+ (1080p ideal)
- **Bildschirm:** 1366×768 Minimum, 1920×1080 empfohlen
- **Internet:** Nur für WebGazer.js-CDN (einmalig beim Laden)

### **Analyse (optional):**
- **Python:** 3.8+
- **Dependencies:** pandas, numpy, matplotlib, seaborn

---

## 📝 Verwendung für Forschung

### **Zitiervorschlag:**
```
Giesberg, S. (2026). Eye-Tracking Lese-Diagnostik v2.0: 
Browser-basiertes System zur Taxonomie von Lesetaktiken bei 
hochbegabten Kindern. GitHub Repository. 
https://github.com/[YOUR-USERNAME]/eye-tracking-diagnostik
```

### **Lizenz:**
MIT License - Siehe [LICENSE](LICENSE) für Details

### **Ethik:**
Dieses Tool ist für **Forschungs- und Diagnostik-Zwecke** gedacht. Bei Verwendung mit Kindern:
- ✅ Elterneinwilligung einholen
- ✅ Ethik-Kommission konsultieren (bei institutioneller Forschung)
- ✅ Datenschutz beachten (keine Webcam-Aufzeichnung!)

---

## 🚧 Roadmap

### **Phase 2: Intervention (In Arbeit)**
- [ ] Leetspeak-Generator (automatische Text-Konvertierung)
- [ ] Oberlängen-Intervention (CSS-Maskierung)
- [ ] Timeline-Erweiterung (Baseline → Intervention → Retest)
- [ ] Delta-Metriken (Intervention vs. Baseline)

### **Phase 3: Validierung (Geplant)**
- [ ] Tests mit echten Probanden (n=20-30 Kinder)
- [ ] Inter-Rater-Reliabilität
- [ ] Vergleich mit etablierten Tests (SLRT-II, ELFE)
- [ ] Paper-Publikation (Dyslexia, Gifted Child Quarterly)

---

## 🤝 Contributing

Beiträge sind willkommen! Bitte:
1. Fork das Repository
2. Erstelle einen Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Commit deine Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne einen Pull Request

---

## 📧 Kontakt

**Projektentwickler:** Stefan Giesberg  
**Zweck:** Hochbegabten-Diagnostik & Lesetaktik-Taxonomie  
**Status:** MVP v2.0 funktionsfähig (Januar 2026)

**GitHub Issues:** [https://github.com/[YOUR-USERNAME]/eye-tracking-diagnostik/issues](https://github.com/[YOUR-USERNAME]/eye-tracking-diagnostik/issues)

---

## 📚 Weitere Dokumentation

- [SETUP.md](SETUP.md) - Lokale Einrichtung Schritt-für-Schritt
- [docs/Struktur_und_Stand_v2.md](docs/Struktur_und_Stand_v2.md) - Vollständige Projekt-Dokumentation
- [docs/Metriken_v2.md](docs/Metriken_v2.md) - Detaillierte Metrik-Beschreibungen
- [docs/IP_Schutz_und_Workflow.md](docs/IP_Schutz_und_Workflow.md) - Lizenzierung & Klienten-Workflow
- [CHANGELOG.md](CHANGELOG.md) - Version-History

---

## ⚠️ Bekannte Limitationen

- **WebGazer-Ungenauigkeit:** ~50-100px, keine echte Saccade-Erkennung
- **Kalibrierungs-Sensitivität:** Brille/Beleuchtung stark einflussreich
- **Speedreading-Problem:** Hohe Skip-Rates bei zu schnellem Lesen
  - **Lösung:** Instruktion betonen: "Langsam laut vorlesen!"

---

## 🙏 Acknowledgments

- **WebGazer.js** - Papoutsaki et al. (2016), Brown University
- **Matplotlib/Seaborn** - Python-Community
- **Anthropic Claude** - KI-assistierte Entwicklung

---

**⭐ Star dieses Projekt, wenn es dir hilft!**

---

*Letztes Update: 16.02.2026 - v2.0*
