# 🚀 Schnellstart-Anleitung

## Sofort loslegen (5 Minuten)

### 1. App lokal testen

**Öffne eine Kommandozeile/Terminal:**

```bash
# Navigiere zum Projektordner
cd "C:\Users\Lehrer\Documents\blitzlesen-trainer"

# Starte lokalen Webserver (Python)
python -m http.server 8000
```

**Dann im Browser öffnen:** http://localhost:8000

### 2. Netlify Deployment (10 Minuten)

#### Vorbereitung:
1. Gehe zu https://app.netlify.com
2. Klicke "Sign up" → Mit GitHub/Email registrieren (kostenlos)

#### Deploy:
1. Nach Login: **"Add new site"** → **"Deploy manually"**
2. **Drag & Drop:** Kompletten Ordner `blitzlesen-trainer` ins Browser-Fenster ziehen
3. **Warten:** ~30 Sekunden Upload
4. **Fertig!** Du bekommst eine URL wie: `https://blitzlesen-abc123.netlify.app`

#### Optional: Domain anpassen
- In Netlify Dashboard: **"Site settings"** → **"Change site name"**
- Z.B. zu: `blitzlesen-trainer.netlify.app`

---

## Erste Schritte

### Test-Durchlauf

1. **Einstellungen prüfen:**
   - Basisdauer: 150ms (Standard)
   - Silbenfaktor: 1.4 (Standard)
   
2. **Training starten:**
   - Countdown beobachten (3-2-1)
   - Wort kurz gezeigt (verschwindet automatisch)
   - Bewerten: "✓ Erkannt" oder "✗ Nicht erkannt"

3. **Nach 5-10 Wörtern:**
   - "Beenden" klicken
   - Ergebnis ansehen
   - "Exportieren (CSV)" testen

### Für dein erstes Coaching

1. **Vor der Session:**
   - App auf Tablet/iPad öffnen
   - Einstellungen testen (z.B. langsamer: 200ms)
   
2. **Während der Session:**
   - Kind selbst bewerten lassen
   - Bei Bedarf pausieren
   
3. **Nach der Session:**
   - Ergebnis gemeinsam ansehen
   - CSV exportieren für Dokumentation

---

## Häufige Fragen

### "Wie schnell soll ich anfangen?"

**Empfehlung für den Start:**
- Basisdauer: 200ms (langsamer)
- Silbenfaktor: 1.5
- Beispiel "Sonne": 200 × 1.5 × 2 = 600ms (gut für Anfänger)

**Nach 2-3 erfolgreichen Sessions:**
- Basisdauer: 150ms (Standard)
- Silbenfaktor: 1.4

### "Wann ist ein Training erfolgreich?"

- **Gut:** 70-80% erkannt → Geschwindigkeit beibehalten
- **Sehr gut:** 85-95% erkannt → Nächstes Mal schneller
- **Zu schwer:** <60% erkannt → Nächstes Mal langsamer

### "Kann ich eigene Wörter hinzufügen?"

Ja! Siehe README.md → "Wortliste anpassen"

Kurz:
1. Öffne `js/words.js`
2. Füge Wörter zu `WORD_LIST` hinzu
3. Speichern → Browser neu laden

---

## Support

Bei technischen Problemen:
1. README.md lesen (Troubleshooting-Sektion)
2. Browser-Konsole öffnen (F12) → Fehlermeldungen kopieren
3. Kontakt aufnehmen

---

**Viel Erfolg beim Coaching! 🎯**