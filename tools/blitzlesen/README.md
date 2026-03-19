# Blitzlesen Trainer

Eine browserbasierte Web-App zum Training der Blitzlesefähigkeit für Kinder mit LRS (Lese-Rechtschreib-Schwäche).

## 📋 Features

- **Silbennormierte Wortblitze** - Anzeigedauer passt sich automatisch der Silbenanzahl an
- **Individuelle Einstellungen** - Basisdauer und Silbenfaktor anpassbar
- **Selbstbewertung** - Kinder bewerten ihre Erkennungsleistung selbst
- **Fortschrittsdokumentation** - Automatische Speicherung aller Trainings-Sessions
- **CSV-Export** - Für Coaching-Dokumentation
- **DSGVO-konform** - Alle Daten nur lokal im Browser gespeichert
- **Responsive Design** - Funktioniert auf Desktop, Tablet und Smartphone

## 🚀 Installation & Start

### Option 1: Lokal öffnen (ohne Server)

1. Projekt-Ordner öffnen: `blitzlesen-trainer`
2. `index.html` direkt im Browser öffnen (Doppelklick)

**Wichtig:** Aufgrund von CORS-Restriktionen funktionieren die ES6-Module nur mit einem lokalen Webserver!

### Option 2: Mit lokalem Webserver (Empfohlen)

#### Variante A: Python (wenn installiert)

```bash
cd blitzlesen-trainer
python -m http.server 8000
```

Dann öffnen: http://localhost:8000

#### Variante B: Node.js (wenn installiert)

```bash
cd blitzlesen-trainer
npx serve
```

#### Variante C: VS Code Live Server

1. VS Code öffnen
2. Extension "Live Server" installieren
3. Rechtsklick auf `index.html` → "Open with Live Server"

### Option 3: Netlify Deployment (Produktiv)

1. Bei [Netlify](https://app.netlify.com) anmelden
2. "New site" → "Deploy manually"
3. Kompletten `blitzlesen-trainer`-Ordner per Drag & Drop hochladen
4. Fertig! URL wird automatisch generiert

**Alternativ mit Netlify CLI:**

```bash
npm install -g netlify-cli
cd blitzlesen-trainer
netlify deploy --prod
```

## 🎯 Nutzung

### Training starten

1. **"Training starten"** klicken
2. **Geschwindigkeit einstellen:**
   - Basisdauer: 100-300ms (Standard: 150ms)
   - Silbenfaktor: 1.0-2.0 (Standard: 1.4)
3. **"Los geht's!"** klicken

### Während des Trainings

- Countdown (3-2-1) läuft automatisch
- Wort wird für berechnete Zeit angezeigt (Basisdauer × Silbenfaktor × Silbenanzahl)
- Nach Verschwinden: "✓ Ja, erkannt" oder "✗ Nein" klicken
- **Pause**: Training pausieren
- **Beenden**: Training vorzeitig beenden (Fortschritt wird gespeichert)

### Nach dem Training

- Ergebnisse werden angezeigt (Erfolgsquote, Anzahl erkannter Wörter)
- **"Exportieren (CSV)"**: Daten für Coaching-Dokumentation herunterladen
- **"Verlauf anzeigen"**: Alle bisherigen Sessions ansehen

## 📊 Berechnungsformel

```
Anzeigezeit (ms) = Basisdauer × Silbenfaktor × Silbenanzahl

Beispiele:
- "Haus" (1 Silbe): 150ms × 1.4 × 1 = 210ms
- "Sonne" (2 Silben): 150ms × 1.4 × 2 = 420ms
- "Blumentopf" (3 Silben): 150ms × 1.4 × 3 = 630ms
```

## 🗂️ Projektstruktur

```
blitzlesen-trainer/
├── index.html              # Haupt-HTML (Single Page App)
├── css/
│   └── styles.css          # Gesamtes Styling
├── js/
│   ├── app.js              # Haupt-App-Logik
│   ├── syllables.js        # Silbenerkennung
│   ├── words.js            # Wortliste (50 Wörter)
│   └── storage.js          # LocalStorage-Handler
└── README.md               # Diese Datei
```

## 🔧 Technische Details

### Tech-Stack

- **Frontend:** Vanilla JavaScript (ES6 Modules), HTML5, CSS3
- **Storage:** Browser LocalStorage (keine Server-Kommunikation)
- **Silbenerkennung:** Eigener deutscher Algorithmus
- **Hosting:** Netlify (oder jeder statische Hosting-Service)

### Browser-Kompatibilität

- Chrome/Edge: ✅ Vollständig unterstützt
- Firefox: ✅ Vollständig unterstützt
- Safari: ✅ Vollständig unterstützt
- Mobile Browser: ✅ iOS Safari, Chrome Android

**Minimum:** ES6-Module-Support erforderlich (alle modernen Browser seit 2018)

### Datenschutz

- ✅ Keine Cookies
- ✅ Keine Server-Kommunikation
- ✅ Alle Daten nur lokal im Browser
- ✅ Kein Tracking, keine Analytics
- ✅ DSGVO-konform

## 📝 Wortliste anpassen

Die Wortliste befindet sich in `js/words.js`:

```javascript
export const WORD_LIST = [
    'Ball',
    'Haus',
    // ... weitere Wörter
];
```

**So fügst du Wörter hinzu:**

1. Öffne `js/words.js`
2. Füge Wörter zum Array `WORD_LIST` hinzu
3. Speichern → Browser neu laden
4. Silbenerkennung erfolgt automatisch!

## 🐛 Troubleshooting

### Problem: "Failed to load module" Fehler

**Ursache:** Browser blockiert ES6-Module bei `file://`-Protokoll

**Lösung:** Nutze einen lokalen Webserver (siehe Installation)

### Problem: Einstellungen gehen verloren

**Ursache:** Browser-Cache wurde gelöscht oder Private-Mode aktiv

**Lösung:** 
- Normale Browser-Session nutzen
- Einstellungen werden automatisch in LocalStorage gespeichert

### Problem: CSV-Export funktioniert nicht

**Ursache:** Browser blockiert Downloads

**Lösung:**
- Download-Berechtigung in Browser-Einstellungen erlauben
- Pop-up-Blocker deaktivieren

## 🎨 Anpassungen

### Farben ändern

In `css/styles.css` unter `:root`:

```css
:root {
    --primary-color: #2563eb;    /* Hauptfarbe */
    --success-color: #10b981;     /* Erfolg (grün) */
    --danger-color: #ef4444;      /* Fehler (rot) */
}
```

### Wortgröße ändern

In `css/styles.css`:

```css
#word-text {
    font-size: 4rem;  /* Größer: 5rem, Kleiner: 3rem */
}
```

## 📈 Roadmap (Phase 2+)

- [ ] **Adaptive Geschwindigkeit** - Automatische Anpassung bei 80% Erfolgsquote
- [ ] **Eigene Wortlisten** - Upload von Custom-Listen
- [ ] **User-Accounts** - Mit Backend und Cloud-Sync
- [ ] **Erweiterte Statistiken** - Verlaufsdiagramme, Trends
- [ ] **Native Apps** - iOS und Android mit Capacitor
- [ ] **Silbentrennung mit Hyphenopoly.js** - Präzisere Erkennung

## 📄 Lizenz

Dieses Projekt ist für den Einsatz im Lerncoaching entwickelt.

Bei Fragen oder Problemen: stefan.giesberg@example.com

---

**Version:** 1.0.0 (MVP)  
**Letzte Aktualisierung:** Januar 2025