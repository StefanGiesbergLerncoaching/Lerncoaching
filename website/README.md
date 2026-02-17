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

### 4. Custom Domain einrichten
1. In GitHub Pages Settings: Custom domain → `stefangiesberg.de`
2. Bei Ihrem Domain-Provider (z.B. Strato, 1&1):
   - A-Records für GitHub Pages IPs:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
   - CNAME für `www`: `stefangiesberglerncoaching.github.io`
3. "Enforce HTTPS" aktivieren (nach DNS-Propagation)

## 🚀 Deployment

Die Website wird automatisch über GitHub Pages deployed:
- Bei jedem Push auf `main` wird die Seite neu gebaut
- URL (temporär): `https://stefangiesberglerncoaching.github.io/lerncoaching/website/`
- URL (nach Custom Domain): `https://stefangiesberg.de`

## 🔗 Links

- Alte Homepage: Ordner `/alte HP` (als Referenz)
- Tools-Portal: `../portal/index.html`
- Design-System: `../shared/css/giesberg-design.css`

## ✅ Features

- ✅ Responsive Design (Mobile, Tablet, Desktop)
- ✅ SEO-optimiert (Meta-Tags, semantisches HTML)
- ✅ Barrierearm (ARIA-Labels, semantische Struktur)
- ✅ Schnell (minimales CSS, keine JS-Frameworks)
- ✅ Kontaktformular via Formspree
- ✅ Datenschutzkonform (DSGVO-Text vorhanden)
