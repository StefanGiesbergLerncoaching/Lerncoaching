# Stefan Giesberg Lerncoaching - Website

Moderne, responsive Homepage für Stefan Giesberg Lerncoaching, basierend auf dem `giesberg-design.css` Design-System.

## 📁 Struktur

```
website/
├── index.html          # Homepage (Haupt-Landing-Page)
├── about.html          # Über mich Seite
├── contact.html        # Kontaktseite mit Formular
├── impressum.html      # Impressum (TODO: Adresse ergänzen)
├── datenschutz.html    # Datenschutzerklärung
└── assets/
    └── images/         # Bilder (11x JPG aus alter HP)
```

## 🎨 Design

- **Design-System**: `../shared/css/giesberg-design.css`
- **Farben**:
  - Primary: `#2D4059` (Dunkelblau)
  - Accent: `#F39C12` (Orange)
  - Secondary: `#7a9cc6` (Hellblau)
- **Schrift**: Inter (Google Fonts)
- **Responsive**: Mobile-first, funktioniert auf allen Geräten

## 📝 TODO vor dem Go-Live

### 1. Formspree einrichten
- Registrieren auf https://formspree.io (kostenlos, 50 Submissions/Monat)
- Formspree-Endpoint erhalten (Format: `https://formspree.io/f/YOUR_FORM_ID`)
- In `contact.html` Zeile 88 ersetzen:
  ```html
  <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  ```

### 2. Impressum vervollständigen
- In `impressum.html` die folgenden Platzhalter ersetzen:
  - `[IHRE ADRESSE]`
  - `[PLZ ORT]`
  - `[IHRE TELEFONNUMMER]`
  - Ggf. Kammer/Berufsbezeichnungen ergänzen

### 3. GitHub Pages aktivieren
1. In GitHub-Repo: Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main`, Folder: `/website`
4. Save → GitHub baut die Seite automatisch

### 4. Custom Domain einrichten ← **NÄCHSTER SCHRITT**

`CNAME`-Datei ist bereits in `website/CNAME` vorhanden (`stefangiesberg.de`).

**Beim Domain-Provider (z.B. Strato, 1&1) einstellen:**
```
A-Record:  @  →  185.199.108.153
A-Record:  @  →  185.199.109.153
A-Record:  @  →  185.199.110.153
A-Record:  @  →  185.199.111.153
CNAME:     www → stefangiesberglerncoaching.github.io
```

**In GitHub Pages Settings:**
1. Settings → Pages → Custom domain → `stefangiesberg.de` eingeben → Save
2. Warten bis DNS propagiert (~24h)
3. "Enforce HTTPS" aktivieren

## 🚀 Deployment-Status

| Schritt | Status |
|---------|--------|
| GitHub Pages aktiviert | ☐ noch nicht |
| CNAME-Datei committed | ✅ `website/CNAME` vorhanden |
| DNS A-Records beim Provider | ☐ noch nicht |
| Custom Domain in GitHub Settings | ☐ noch nicht |
| HTTPS aktiv | ☐ nach DNS-Propagation |

- URL (nach Custom Domain): `https://stefangiesberg.de`

## 🔗 Links

- Alte Homepage: Ordner `/alte HP` (als Referenz)
- Tools-Portal: `../portal/index.html`
- Design-System: `../shared/css/giesberg-design.css`

## ✅ Features

- ✅ Responsive Design (Mobile, Tablet, Desktop)
- ✅ Hamburger-Menü auf Mobile (alle Seiten)
- ✅ SEO-optimiert (Meta-Tags, semantisches HTML)
- ✅ Barrierearm (ARIA-Labels, semantische Struktur)
- ✅ Schnell (minimales CSS, kein JS-Framework)
- ✅ Kontaktformular via Formspree
- ✅ Datenschutzkonform (DSGVO-Text vorhanden)
- ✅ CNAME + .nojekyll für GitHub Pages / Custom Domain
