# ✅ EYE-TRACKING-DIAGNOSTIK v2.0 - KOMPLETT BEREIT!

## 📦 WAS IST IM PAKET?

### **Komplette Projektstruktur (14 Dateien):**

```
eye-tracking-diagnostik/
├── .gitignore                          ✓ Git-Konfiguration
├── LICENSE                             ✓ MIT-Lizenz
├── README.md                           ✓ GitHub-Hauptseite
├── CHANGELOG.md                        ✓ Version-History
├── SETUP.md                            ✓ Lokale Einrichtung (NEU!)
│
├── docs/
│   ├── Struktur_und_Stand_v2.md        ✓ Vollständige Projekt-Doku
│   ├── Metriken_v2.md                  ✓ Detaillierte Metrik-Beschreibungen
│   └── IP_Schutz_und_Workflow.md       ✓ Lizenzierung & Klienten-Workflow
│
├── index.html                          ✓ v2.0 Multi-Line-Interface
├── js/
│   └── aoi-tracker-v2.js               ✓ Multi-Line-Tracking-Engine
│
├── stimuli/
│   └── baseline/
│       └── text_multiline.json         ✓ 3-Zeilen-Test-Text
│
├── analysis/
│   ├── analyze_eyetracking.py          ✓ Python-Analyse (vollständig)
│   └── requirements.txt                ✓ Dependencies
│
└── output_analysis/
    └── .gitkeep                        ✓ Placeholder für Outputs
```

**Archiv-Größe:** 41 KB (komprimiert)

---

## 🚀 WIE GEHT ES WEITER?

### **SCHRITT 1: ORDNER KOPIEREN**

#### A) Via Terminal (direkt kopieren):

```bash
# Vom Projekt-Ordner aus:
cp -r /home/claude/eye-tracking-diagnostik ~/Documents/GitHub/

# Oder wo auch immer dein lokaler GitHub-Ordner ist:
cp -r /home/claude/eye-tracking-diagnostik /PFAD/ZU/DEINEM/GITHUB-ORDNER/
```

#### B) Via Archiv (falls du den Ordner woanders hin brauchst):

```bash
# Archiv liegt in: /home/claude/eye-tracking-diagnostik.tar.gz

# Entpacken:
cd ~/Documents/GitHub/
tar -xzf /home/claude/eye-tracking-diagnostik.tar.gz

# Oder lokal speichern und dann entpacken
```

---

### **SCHRITT 2: DEPENDENCIES INSTALLIEREN**

```bash
cd ~/Documents/GitHub/eye-tracking-diagnostik

# Python-Dependencies:
pip install pandas numpy matplotlib seaborn --break-system-packages

# Oder via requirements.txt:
pip install -r analysis/requirements.txt --break-system-packages
```

**Test:**
```bash
python -c "import pandas; import matplotlib; print('✓ Dependencies OK')"
```

---

### **SCHRITT 3: ERSTEN TEST DURCHFÜHREN**

#### A) Live Server starten:

**In VS Code:**
1. Ordner öffnen: `File → Open Folder` → `eye-tracking-diagnostik`
2. `index.html` öffnen
3. Rechtsklick → "Open with Live Server"
4. Browser öffnet: `http://127.0.0.1:5500/index.html`

**Oder manuell:**
```bash
cd eye-tracking-diagnostik
python -m http.server 8000
# Dann Browser: http://localhost:8000
```

#### B) Test durchführen:

1. **Willkommens-Screen:** "Starten" klicken
2. **Webcam erlauben**
3. **Kalibrierung:** 9 Punkte, jeden 3× anklicken
   - **WICHTIG:** Punkt anschauen, nicht Maus!
   - Brille abnehmen!
4. **Text lesen:** Langsam laut vorlesen
5. **"Fertig"** → 3 CSVs werden heruntergeladen

---

### **SCHRITT 4: DATEN ANALYSIEREN**

```bash
# CSVs liegen in ~/Downloads/
cd ~/Documents/GitHub/eye-tracking-diagnostik

# CSVs ins Projekt kopieren (optional):
cp ~/Downloads/line*.csv .

# Python-Analyse starten:
python analysis/analyze_eyetracking.py \
  line1_vertical_*.csv \
  line2_syllables_*.csv \
  line3_words_*.csv
```

**Output:**
- `output_analysis/line1_vertical_distribution.png`
- `output_analysis/line2_syllable_sequence.png`
- `output_analysis/line3_regions_heatmap.png`
- `output_analysis/profile_radar.png`
- `output_analysis/statistics_summary.png`
- `output_analysis/report_TEST_*.txt`

**Report öffnen:**
```bash
cat output_analysis/report_*.txt
```

---

### **SCHRITT 5: GITHUB-INTEGRATION**

#### A) Lokales Git-Repository initialisieren:

```bash
cd ~/Documents/GitHub/eye-tracking-diagnostik

git init
git add .
git commit -m "Initial commit: Eye-Tracking v2.0 MVP"
```

#### B) Remote-Repository erstellen:

1. Gehe zu https://github.com/new
2. Repository-Name: `eye-tracking-diagnostik`
3. **Private** (für IP-Schutz) oder Public
4. **NICHT** "Initialize with README" (hast du schon lokal!)
5. "Create repository"

#### C) Lokal mit Remote verbinden:

```bash
# Remote hinzufügen (URL von GitHub kopieren):
git remote add origin https://github.com/DEIN-USERNAME/eye-tracking-diagnostik.git

# Push:
git branch -M main
git push -u origin main
```

#### D) GitHub Desktop (optional):

1. GitHub Desktop öffnen
2. `File → Add Local Repository`
3. Ordner auswählen
4. "Publish repository"

---

## 📚 DOKUMENTATION

### **Welche Datei wofür:**

| Datei | Zweck | Wann lesen? |
|-------|-------|-------------|
| **README.md** | GitHub-Hauptseite, Projekt-Überblick | Immer zuerst! |
| **SETUP.md** | Lokale Einrichtung, Step-by-Step | Beim ersten Setup |
| **docs/Struktur_und_Stand_v2.md** | Vollständige technische Doku | Für Details zu Code/Architektur |
| **docs/Metriken_v2.md** | Alle 227+ Metriken erklärt | Für wissenschaftliche Interpretation |
| **docs/IP_Schutz_und_Workflow.md** | Lizenzierung, Klienten-Workflow | Für Business-Planung |
| **CHANGELOG.md** | Version-History | Bei Updates |

---

## 🔄 TYPISCHER WORKFLOW (NACH SETUP)

### A) Test durchführen:
```bash
# 1. VS Code öffnen (Live Server)
# 2. Test im Browser
# 3. CSVs herunterladen
```

### B) Daten analysieren:
```bash
cd eye-tracking-diagnostik
python analysis/analyze_eyetracking.py line1_*.csv line2_*.csv line3_*.csv
open output_analysis/report_*.txt  # macOS
# oder: cat output_analysis/report_*.txt
```

### C) Ergebnisse dokumentieren:
```bash
# CSVs umbenennen für Tracking:
mkdir -p data
mv line1_vertical_*.csv data/test_001_line1.csv
mv line2_syllables_*.csv data/test_001_line2.csv
mv line3_words_*.csv data/test_001_line3.csv

# Report speichern:
cp output_analysis/report_*.txt data/test_001_report.txt
```

### D) Git committen:
```bash
git add .
git commit -m "Test 001: Kind 8 Jahre, Profil Dekodierer"
git push
```

---

## 🎨 ANPASSUNGEN (HÄUFIGE FRAGEN)

### **Schriftgröße ändern:**
In `index.html`, Zeile ~30:
```css
.text-stimulus {
    font-size: 48px;  /* Ändern auf 32px, 60px, etc. */
}
```

### **Text ändern:**
In `index.html`, Zeile ~200:
```javascript
const response = await fetch('stimuli/baseline/text_multiline.json');
// Ändern auf andere Datei
```

### **Neuen Text erstellen:**
```bash
cp stimuli/baseline/text_multiline.json stimuli/baseline/text_neu.json
# In text_neu.json: Texte anpassen
```

---

## 🐛 TROUBLESHOOTING

### **Problem: "WebGazer not defined"**
```bash
# Lösung: Browser-Cache leeren
# Chrome/Edge: Cmd+Shift+R (macOS) oder Ctrl+Shift+R (Windows)
```

### **Problem: Webcam funktioniert nicht**
```bash
# Lösung: Browser-Einstellungen → Datenschutz → Kamera erlauben
# Oder anderen Browser testen (Chrome empfohlen)
```

### **Problem: Python findet Pandas nicht**
```bash
pip install --upgrade pandas numpy matplotlib seaborn --break-system-packages
```

### **Problem: CSVs haben falsche Zeichen (Ä → Ã„)**
```bash
# Lösung: In Excel: "Daten → Aus Text/CSV" → Encoding: UTF-8
```

---

## 📊 WAS SIND DIE NÄCHSTEN SCHRITTE?

Nach erfolgreichem Setup:

### **Kurzfristig (nächste 2 Wochen):**
1. **5-10 Test-Sessions durchführen** (verschiedene Altersgruppen)
2. **Daten-Tracking-Sheet aufsetzen** (Google Sheets/Airtable)
3. **Erste Muster beobachten**

### **Mittelfristig (Monat 2-3):**
1. **30+ weitere Tests** (Normwerte aufbauen)
2. **Statistische Auswertung** (Validierung Klassifikation)
3. **Leetspeak-Intervention entwickeln** (Phase 2)

### **Langfristig (Monat 4-6):**
1. **Backend-MVP** (Google Colab → Netlify Functions)
2. **Markenanmeldung** (2.300 €)
3. **Beta-Lizenznehmer** (3 Personen)

Details: Siehe `docs/IP_Schutz_und_Workflow.md`

---

## ✅ CHECKLISTE: BIN ICH BEREIT?

- [ ] Ordner kopiert nach `~/Documents/GitHub/eye-tracking-diagnostik`
- [ ] Python-Dependencies installiert (`pip install ...`)
- [ ] VS Code + Live Server Extension installiert
- [ ] Ersten Test im Browser durchgeführt
- [ ] 3 CSVs heruntergeladen
- [ ] Python-Analyse ausgeführt
- [ ] Report gelesen
- [ ] Git-Repository initialisiert
- [ ] GitHub-Remote verbunden
- [ ] README.md + SETUP.md gelesen

**Wenn alle Punkte ✓ → DU BIST BEREIT! 🚀**

---

## 🆘 SUPPORT

- **Dokumentation:** `docs/` Ordner (3 Dateien)
- **Code-Referenz:** Inline-Kommentare in allen Files
- **GitHub Issues:** (nach Push auf GitHub)
- **Claude AI:** Frag mich bei Problemen!

---

**VIEL ERFOLG MIT DEINEM EYE-TRACKING-PROJEKT! 👁️📊🚀**

---

*Erstellt: 16.02.2026*
*Version: 2.0 MVP*
*Archiv: eye-tracking-diagnostik.tar.gz (41 KB)*
