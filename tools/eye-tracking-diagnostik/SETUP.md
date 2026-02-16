# 🚀 Setup-Anleitung: Eye-Tracking-Diagnostik

**Ziel:** Lokales Projekt aufsetzen + GitHub-Integration + erste Tests

---

## 📋 VORAUSSETZUNGEN

### Software (einmalig installieren):

1. **VS Code** - https://code.visualstudio.com/
2. **Live Server Extension** für VS Code
   - In VS Code: `Cmd+Shift+X` → Suche "Live Server" → Installieren
3. **Python 3.8+** - https://www.python.org/downloads/
4. **GitHub Desktop** (optional) - https://desktop.github.com/

### Browser:
- **Chrome** oder **Edge** (neueste Version empfohlen)
- Webcam (720p+)

---

## 🗂️ SCHRITT 1: PROJEKT LOKAL EINRICHTEN

### A) Ordner erstellen

```bash
# Terminal öffnen (oder Finder/Explorer nutzen)
cd ~/Documents/GitHub/  # oder dein GitHub-Ordner

# Ordner erstellen
mkdir eye-tracking-diagnostik
cd eye-tracking-diagnostik
```

### B) Dateien kopieren

Kopiere **alle Dateien** aus diesem Projekt in den neuen Ordner.

**Checkliste:**
- [ ] `.gitignore`
- [ ] `LICENSE`
- [ ] `README.md`
- [ ] `CHANGELOG.md`
- [ ] `SETUP.md` (diese Datei)
- [ ] `index.html`
- [ ] `js/aoi-tracker-v2.js`
- [ ] `stimuli/baseline/text_multiline.json`
- [ ] `analysis/analyze_eyetracking.py`
- [ ] `analysis/requirements.txt`
- [ ] `docs/` (alle 3 Markdown-Dateien)

---

## 🔧 SCHRITT 2: PYTHON-DEPENDENCIES INSTALLIEREN

```bash
# Im Projekt-Ordner:
cd eye-tracking-diagnostik

# Dependencies installieren:
pip install pandas numpy matplotlib seaborn --break-system-packages

# Oder mit requirements.txt:
pip install -r analysis/requirements.txt --break-system-packages
```

**Hinweis:** `--break-system-packages` ist nötig auf macOS, um in System-Python zu installieren.

**Test ob es funktioniert:**
```bash
python -c "import pandas; import matplotlib; print('✓ Dependencies OK')"
```

---

## 🌐 SCHRITT 3: LIVE SERVER STARTEN

### In VS Code:

1. Ordner öffnen: `File → Open Folder` → `eye-tracking-diagnostik` auswählen
2. `index.html` öffnen (Linke Sidebar)
3. Rechtsklick auf `index.html` → **"Open with Live Server"**
4. Browser öffnet automatisch: `http://127.0.0.1:5500/index.html`

**Oder manuell:**
```bash
# Mit Python:
python -m http.server 8000

# Dann Browser öffnen:
# http://localhost:8000
```

---

## 🧪 SCHRITT 4: ERSTEN TEST DURCHFÜHREN

### A) Test im Browser:

1. **Willkommens-Screen:** "Starten" klicken
2. **Webcam erlauben** (Pop-up bestätigen)
3. **Kalibrierung:** 9 Punkte, jeden 3× anklicken
   - **WICHTIG:** Punkt anschauen, nicht die Maus!
   - Brille abnehmen für bessere Genauigkeit
4. **Text lesen:** Langsam laut vorlesen (NICHT speedreaden!)
5. **"Fertig"** klicken → 3 CSV-Dateien werden heruntergeladen

**Downloads landen in:** `~/Downloads/`
- `line1_vertical_[timestamp].csv`
- `line2_syllables_[timestamp].csv`
- `line3_words_[timestamp].csv`

### B) Daten analysieren:

```bash
# CSVs in Projekt-Ordner kopieren:
cd eye-tracking-diagnostik
cp ~/Downloads/line*.csv .

# Python-Analyse starten:
python analysis/analyze_eyetracking.py \
  line1_vertical_*.csv \
  line2_syllables_*.csv \
  line3_words_*.csv
```

**Output:**
- 5 PNG-Dateien in `output_analysis/`
- 1 Text-Report: `output_analysis/report_[ID].txt`

**Report öffnen:**
```bash
cat output_analysis/report_*.txt
```

---

## 🔄 SCHRITT 5: GITHUB-INTEGRATION

### A) Lokales Git-Repository initialisieren:

```bash
cd eye-tracking-diagnostik

# Git initialisieren:
git init

# Erste Commit:
git add .
git commit -m "Initial commit: Eye-Tracking v2.0 MVP"
```

### B) Remote-Repository erstellen (auf GitHub.com):

1. Gehe zu https://github.com/new
2. Repository-Name: `eye-tracking-diagnostik`
3. **Private** (wenn du IP schützen willst) oder Public
4. **NICHT** "Initialize with README" anklicken (hast du schon lokal!)
5. "Create repository"

### C) Lokal mit Remote verbinden:

```bash
# Remote hinzufügen (URL von GitHub kopieren):
git remote add origin https://github.com/DEIN-USERNAME/eye-tracking-diagnostik.git

# Push:
git branch -M main
git push -u origin main
```

### D) GitHub Desktop (optional):

Wenn du GitHub Desktop nutzen willst:
1. GitHub Desktop öffnen
2. `File → Add Local Repository`
3. Ordner auswählen: `eye-tracking-diagnostik`
4. "Publish repository" klicken

---

## 📊 SCHRITT 6: WORKFLOW-INTEGRATION

### Typischer Workflow nach Setup:

#### A) Test durchführen:
```bash
# 1. Live Server starten (VS Code)
# 2. Test im Browser durchführen
# 3. CSVs herunterladen
```

#### B) Daten analysieren:
```bash
cd eye-tracking-diagnostik
python analysis/analyze_eyetracking.py line1_*.csv line2_*.csv line3_*.csv
open output_analysis/report_*.txt  # macOS
# oder: cat output_analysis/report_*.txt
```

#### C) Ergebnisse dokumentieren:
```bash
# CSVs umbenennen (für Tracking):
mv line1_vertical_*.csv data/test_001_line1.csv
mv line2_syllables_*.csv data/test_001_line2.csv
mv line3_words_*.csv data/test_001_line3.csv

# Report speichern:
cp output_analysis/report_*.txt data/test_001_report.txt
```

#### D) Git committen:
```bash
git add .
git commit -m "Test 001: Kind 8 Jahre, Profil Dekodierer"
git push
```

---

## 🎨 SCHRITT 7: ANPASSUNGEN (Optional)

### Schriftgröße ändern:

In `index.html`, Zeile ~30:
```css
.text-stimulus {
    font-size: 48px;  /* Ändern auf 32px, 60px, etc. */
}
```

### Text ändern:

In `index.html`, Zeile ~200:
```javascript
const response = await fetch('stimuli/baseline/text_multiline.json');
// Andere Textdatei verwenden
```

### Neuen Text erstellen:

```bash
cp stimuli/baseline/text_multiline.json stimuli/baseline/text_neu.json
# In text_neu.json: Texte anpassen
```

---

## 🐛 TROUBLESHOOTING

### Problem: "WebGazer not defined"
**Lösung:** Browser-Cache leeren, Seite neu laden (`Cmd+Shift+R`)

### Problem: Webcam funktioniert nicht
**Lösung:** 
- Chrome/Edge Einstellungen → Datenschutz → Kamera erlauben
- Anderen Browser testen

### Problem: Python-Script findet Pandas nicht
**Lösung:**
```bash
pip install --upgrade pandas numpy matplotlib seaborn --break-system-packages
```

### Problem: CSVs haben falsche Zeichen (Ä → Ã„)
**Lösung:** In Excel: `Daten → Aus Text/CSV` → Encoding: **UTF-8**

### Problem: Live Server startet nicht
**Lösung:** 
- VS Code Extension prüfen (installiert?)
- Alternative: `python -m http.server 8000`

---

## 📚 NÄCHSTE SCHRITTE

Nach erfolgreichem Setup:

1. **10 Test-Sessions durchführen** (verschiedene Altersgruppen)
2. **Daten-Tracking-Sheet aufsetzen** (Google Sheets/Airtable)
3. **Erste Normwerte analysieren** (Python-Script erweitern)
4. **Leetspeak-Intervention entwickeln** (Phase 2)

Details: Siehe `docs/Struktur_und_Stand_v2.md`

---

## 🆘 SUPPORT

- **GitHub Issues:** https://github.com/DEIN-USERNAME/eye-tracking-diagnostik/issues
- **Dokumentation:** `docs/` Ordner
- **Code-Referenz:** Inline-Kommentare in `index.html` und `aoi-tracker-v2.js`

---

**✅ Setup abgeschlossen! Du bist bereit für die ersten Tests! 🚀**
