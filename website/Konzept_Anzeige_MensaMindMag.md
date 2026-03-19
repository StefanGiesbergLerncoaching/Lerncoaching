# Konzept: Anzeige Mensa MindMag

**Status:** Konzeptphase — Designentscheidungen getroffen, Umsetzung steht aus  
**Erstellt:** 2026-03-07  
**Kontext:** Anzeige im Mensa MinD Magazin zur Lead-Generierung für Lerncoaching-Praxis

---

## 1. RAHMENBEDINGUNGEN

### Format
- **1/4 Seite**, solo (ohne Gregor Kowalski)
- Gregor-Kooperation vorerst pausiert ("braucht zu lange zum Sortieren")
- Gemeinsame Anzeige ggf. später, separate Entscheidung

### Zielgruppe im MindMag
- Mensa-Mitglieder, selbst HB, teilweise mit HB-Kindern
- Lesen das Magazin beiläufig, nicht suchend
- Intellektuell anspruchsvoll, allergisch gegen Marketing-Sprech
- Reagieren auf kognitive Dissonanz ("Moment, das stimmt ja gar nicht")
- Physisches Blättern → halbe Sekunde für Blickkontakt

### Ziel der Anzeige
- **Primär:** Lead-Generierung → Domain eintippen → Landingpage → Erstgespräch buchen
- **Sekundär:** Namens-Wiedererkennung (Stefan Giesberg ist durch Buchprojekt im Mensa-Umfeld bekannt)
- Die Anzeige muss NICHT alles erklären — sie muss genug Spannung erzeugen, damit jemand `stefangiesberg.de` eintippt

---

## 2. STEFANS INITIALE IDEEN (Brainstorming-Input)

### Header-Ideen (provokativ, zielgerichtet — sortiert falsche Kunden aus)
- "Lerncoaching für HB Kids"
- "LRS trotz HB?"
- "HB Kinder sind anders!"
- "Intelligente Lösungen für intelligente Kinder"
- "Was, wenn es kein LRS ist?"

### Erklärtext-Ideen (weitere Qualifizierung, ggf. Knappheit andeuten)
- "9 von 10 HB Kindern mit Lese- und Schreibschwierigkeiten haben kein klassisches LRS"
- "Was, wenn statt langwieriger LRS-Förderung weniger als 5 Stunden helfen würden"

### CTA-Ideen
- "Jetzt (kostenlos/unverbindlich) herausfinden, ob ich helfen kann"
- "Verzweifelt, weil Ihr Kind mit Lese-/Schreibblockaden kämpft?"
- "9 von 10 Kindern schreiben und lesen nach nur einem Termin erkennbar besser! Ihres auch?"

### Kontakt-Ideen
- QR-Code, Kurzlink, Foto?

### Geplante Grundstruktur
1. Header (provokativ und zielgerichtet)
2. Kurzer Erklärtext (weitere Qualifizierung)
3. CTA (herausfinden ob wir zusammenpassen)
4. Kontakt (QR-Code, Kurzlink, Foto?)

---

## 3. DESIGNENTSCHEIDUNGEN (Stand 2026-03-07)

### Gesamtarchitektur: Drei Elemente statt vier
Die Anzeige wurde radikal reduziert. Statt Header + Erklärtext + CTA + Kontaktblock gibt es nur:
1. **Header/Claim** (Spannung erzeugen)
2. **Einzelsatz** (Substanz liefern)
3. **Domain-Balken** (Handlung auslösen)

Begründung: Die Domain `stefangiesberg.de` IST der Name, IST der Kontakt, IST der CTA. Ein Element ersetzt drei.

### Element 1: Header — Favorisierte Variante

```
Was, wenn es kein LRS ist?
Bei 8 von 10 hochbegabten Kindern ist es keins.
```

**Warum diese Variante:**
- Frage + Antwort in zwei Zeilen — Header IST die Botschaft
- Kognitive Lücke aufreißen: Mensa-Leser wollen Rätsel lösen, nicht Angebote lesen
- "Was, wenn es kein LRS ist?" war die stärkste aus Stefans Ideenliste
- Sortiert sofort: Wer kein HB-Kind mit Leseproblemen hat, liest nicht weiter

**Verworfene Header-Varianten:**
- "Lerncoaching für HB Kids" → zu generisch, kein Hook
- "HB Kinder sind anders!" → Binsenweisheit für Mensa-Leser
- "Intelligente Lösungen für intelligente Kinder" → Werbesprech
- "LRS trotz HB?" → gut, aber weniger Spannung als die Frage-Antwort-Kombination
- Name-first-Variante ("Stefan Giesberg / Was, wenn es kein LRS ist?") → Name wandert besser in den Domain-Balken

### Element 2: Erklärtext — Einzelsatz

```
Eine Sitzung zeigt, ob das auch für Ihr Kind gilt.
```

**Warum nur ein Satz:**
- Bei 1/4 Seite ist Whitespace der beste Freund
- Der Header hat bereits die zentrale These geliefert
- Der Einzelsatz macht das Angebot konkret (eine Sitzung) ohne zu überfrachten
- Impliziert Effizienz und Kompetenz

**Verworfene Erklärtext-Varianten:**
- Zweisatz-Variante ("Hochbegabte Kinder lernen anders...") → bei diesem Header redundant
- "Was, wenn statt langwieriger LRS-Förderung weniger als 5 Stunden helfen würden" → zu lang, "weniger als 5 Stunden" ist weniger prägnant als "eine Sitzung"
- "Verzweifelt, weil Ihr Kind mit Lese-/Schreibblockaden kämpft?" → zu emotional für Mensa-Zielgruppe

### Element 3: Invertierter Domain-Balken (unten)

```
▓▓▓▓▓▓  stefangiesberg.de  ▓▓▓▓▓▓
```

**Warum unten:**
- Leseauge wandert von oben nach unten: Spannung → Substanz → Handlung
- Balken wird zum natürlichen Endpunkt ("Jetzt weiß ich genug, jetzt tippe ich das ein")
- Oben würde er den Header kannibalisieren

**Warum Domain statt QR-Code/Kurzlink:**
- `stefangiesberg.de` IST der Name → Absender, Kontakt und Wiedererkennung in einem Element
- Invertierter Balken (weiß auf dunkel oder dunkel auf hell) gibt der Anzeige eine visuelle Kante beim Blättern
- Kein QR-Code nötig: wer den Namen kennt (Buchprojekt), googelt ohnehin
- Kurzlinks wie `hb-lesen.de` verworfen → Domain-Kosten und Weiterleitung vs. Direktheit des eigenen Namens

### Verworfene Kontakt-Elemente
- **QR-Code:** Wird in Print überschätzt, kostet Platz
- **Separater Kurzlink:** Unnötig wenn Domain = Name
- **Foto:** Bei drei Elementen kein Platz/Bedarf — Vertrauen baut die Landingpage auf
- **Telefonnummer:** Noch offen (siehe offene Fragen)

### Zahlen-Entscheidung: "8 von 10" statt "9 von 10"

**Begründung für Understatement:**
- "9 von 10" klingt nach Zahnpasta-Werbung
- "8 von 10" klingt nach jemandem, der ehrlich zählt und die schwierigen Fälle nicht wegdiskutiert
- Mensa-Leser erkennen den Unterschied zwischen Marketing-Rundung und intellektueller Redlichkeit
- "7 von 10" wäre zu viel Understatement ("funktioniert meistens" statt "funktioniert fast immer")
- Zahl stammt aus Praxiserfahrung (~20 Fälle), nicht aus publizierter Studie → auf Landingpage absichern mit "In meiner bisherigen Praxis..."

### CTA-Entscheidung: Kein expliziter CTA in der Anzeige

**Begründung:**
- "Kostenlos" und "unverbindlich" schwächen die Positionierung (kein Fitnessstudio-Probetraining)
- Mensa-Eltern mit leidendem Kind wollen Kompetenz, nicht Rabatt
- Die Domain im Balken IST der CTA — implizit, nicht plakativ
- Selektion statt Einladung: "Passt mein Ansatz zu Ihrem Kind?" passiert auf der Landingpage

---

## 4. LAYOUT-SKIZZE

```
┌─────────────────────────────────┐
│                                 │
│   Was, wenn es kein LRS ist?    │  ← Header (Frage)
│                                 │
│   Bei 8 von 10 hochbegabten     │  ← Antwort/Claim
│   Kindern ist es keins.         │
│                                 │
│   Eine Sitzung zeigt, ob das    │  ← Einzelsatz
│   auch für Ihr Kind gilt.       │
│                                 │
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
│▓▓▓▓  stefangiesberg.de    ▓▓▓▓▓│  ← Invertierter Balken
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
└─────────────────────────────────┘
```

**Kein QR-Code, kein Foto, kein "kostenlos", kein Rauschen.**  
Drei Elemente, eine Handlung.

---

## 5. HOMEPAGE ALS LANDINGPAGE — Systemarchitektur

### Kernidee
Die Anzeige verlagert die gesamte Conversion-Arbeit auf `stefangiesberg.de`. Die Homepage muss daher als Landingpage funktionieren:

### Prinzipien
- **Erste Ansicht (above the fold):** Kernaussage + "Jetzt anrufen" / "Erstgespräch buchen" — keine Navigation nötig für ersten CTA
- **Jede Sektion endet mit demselben CTA** — Repetition ist Conversion-Architektur
- **Erste Seite erklärt kurz und knackig:** Für wen arbeite ich, was mache ich
- **Details über Links:** Wer mehr wissen will, findet Tiefe — aber niemand muss scrollen, um zu handeln
- **Konsistenter CTA:** Jede Seite mit "Ruf jetzt an" oder equivalent

### Seitenarchitektur (TODO — noch auszuarbeiten)
- Detailliertes Konzept für Sektionen, Reihenfolge, CTA-Platzierung steht noch aus
- Muss mit bestehendem Design-System (Acorn-Spacing, Editorial-Look, Farbpalette #2D4059 / #F39C12 / #ECF0F1) konsistent sein
- WordPress Coachify Theme + Elementor als technische Basis

---

## 6. OFFENE FRAGEN

1. **Telefonnummer im Domain-Balken?**  
   `stefangiesberg.de | 0203-XXXXXXX` gibt Sofort-Anrufern den Shortcut. Oder bewusst nicht, um Traffic über Homepage zu steuern?

2. **Hoch- oder Querformat der 1/4 Seite?**  
   Hochformat (ca. 90 × 125mm, halbe Spalte) vs. Querformat (ca. 180 × 62mm, volle Breite) verändert die Elementanordnung fundamental. Abhängig von MindMag-Vorgaben.

3. **Farbgebung der Anzeige:**  
   Website-CI (Petrol #2D4059 / Gelb #F39C12) übernehmen? Oder bewusst reduziert (Schwarz/Weiß + ein Akzent) für Magazin-Kontext?

4. **Typografie:**  
   Welche Schrift? Muss im Print funktionieren. Serif (Editorial-Anmutung) vs. Sans-Serif (Modern/Clean)?

5. **Homepage-Umbau — Seitenarchitektur:**  
   Welche Sektionen in welcher Reihenfolge, wo welcher CTA, was fliegt raus? Anzeige + Landingpage als zusammenhängendes System konzipieren.

6. **Absicherung der "8 von 10"-Zahl auf der Landingpage:**  
   Formulierung wie "In meiner bisherigen Praxis mit über 20 Kindern..." → wo genau platzieren?

---

## 7. ZUSAMMENHANG MIT ANDEREN PROJEKTEN

- **Homepage-Redesign:** Die Anzeige zwingt zur Überarbeitung der Startseite als Landingpage (siehe Abschnitt 5)
- **Gregor-Kooperation:** Gemeinsame Anzeige vorerst pausiert, kann später als eigene 1/3-Seite-Variante reaktiviert werden
- **Buchprojekt:** Name als Hook funktioniert nur, solange Buchprojekt im Mensa-Umfeld präsent ist → Timing beachten
- **Google Ads (on hold):** Landingpage-Umbau für Anzeige kommt auch Google Ads zugute, wenn reaktiviert
- **Train-the-Trainer:** Anzeige richtet sich an Eltern (Phase 1), nicht an Trainer (Phase 2)
