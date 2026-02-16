📋 VOLLSTÄNDIGE PROJEKTZUSAMMENFASSUNG: EYE-TRACKING-DIAGNOSTIK FÜR 2E-KINDER
Lizenzierungs- & Schutzstrategie + Klienten-Workflow-Integration
🎯 PROJEKTVISION
Hauptziel: Entwicklung eines lizenzierbaren Eye-Tracking-basierten Diagnostik- und Interventionssystems für hochbegabte Kinder mit Lese-Rechtschreib-Schwäche (2e-Kinder).
Geschäftsmodell: Monatliche Lizenzierung an externe Lernberater mit:
Einführungswochenende (Schulung)
Zugang zur Eye-Tracking-Website (SaaS)
Diagnose- und Interventionshandbuch
Individualisierte Texte für verschiedene Altersgruppen
Kontinuierliche Updates und Normwerte-Zugang
Alleinstellungsmerkmal:
Sprachspezifisch (deutschsprachiger Raum)
Wissenschaftlich fundierte Taxonomie (Dekodierer/Rater/Kompensator)
Proprietäre Normwerte-Datenbank (wächst mit jeder Nutzung)
Kontinuierliche Weiterentwicklung
⚠️ KERNPROBLEM: KNOW-HOW-ABFLUSS
Größtes Risiko: Lizenznehmer könnten nach 3–6 Monaten Schulung + Materialnutzung das Konzept eigenständig weiterverfolgen, da:
Eye-Tracking-Technologie (WebGazer.js) Open Source ist
Taxonomie (3 Profile) nach Schulung "im Kopf" ist
Interventionsmethoden replizierbar sind
Lösung: 3-Säulen-Schutzstrategie (siehe unten)
🛡️ 3-SÄULEN-SCHUTZSTRATEGIE
SÄULE 1: JURISTISCHE ABSICHERUNG
(Schutz gegen dreiste Kopien, 2.000–5.000 € Investition)
1.1 Markenrecht (Priorität: SOFORT)
Kosten: 300–500 € (DPMA Deutschland), 900–1.500 € (EU-Marke später)
Was schützen: Produktname, Logo, Claim
Nizza-Klassen: 9 (Software), 41 (Schulungen), 42 (Wissenschaftliche Dienste)
Timeline: Anmeldung innerhalb 4 Wochen
1.2 Urheberrecht (automatisch, dokumentieren!)
Geschützt: Interventionshandbuch, Website-Code, Python-Skripte, Schulungsunterlagen
Nicht geschützt: Wissenschaftliche Methode, Metriken (Stand der Forschung)
Maßnahme: Copyright-Vermerke auf allen Materialien, GitHub-Lizenz "Proprietary"
1.3 Lizenzvertrag (Kern der Absicherung)
Kosten: 1.500–3.000 € (Fachanwalt IT-Recht/Franchiserecht, einmalig)
Kritische Klauseln:
Nutzungsrechte: Nur für eigene 1:1-Diagnostik, keine Weitergabe/Sublizenzierung
Wettbewerbsverbot: 24 Monate nach Vertragsende, geografisch DACH, sachlich "Eye-Tracking-basierte Lesediagnostik für 2e-Kinder"
Geheimhaltung (NDA): Normwerte, Klassifikationslogik, unveröffentlichte Forschung (5 Jahre nach Vertragsende)
Audit-Rechte: Jährliche Prüfung der ordnungsgemäßen Nutzung
Kündigung: Fristlos bei Verstößen (Weitergabe, Wettbewerb, Zahlungsverzug)
1.4 Patent/Gebrauchsmuster (Optional, später)
Kosten: 5.000–15.000 € (Patent), 500–2.000 € (Gebrauchsmuster)
Wann: Nach 1 Jahr, falls proprietäre Algorithmen entwickelt werden
Jetzt: Nicht prioritär
SÄULE 2: TECHNISCH-INHALTLICHE ABHÄNGIGKEIT
(Macht Abspringen teuer, 2.000–5.000 € Entwicklung)
2.1 Cloud-Backend-Architektur (SaaS-Modell)
Ziel: Lizenznehmer können Tests durchführen, aber Auswertung läuft auf deinem Server
Architektur:
Frontend (Browser):              Backend (Dein Server):
- Eye-Tracking (WebGazer.js)    - Login/Auth (API-Key)
- Kalibrierung                   - Python-Analyse-API
- Text-Anzeige                   - Normwerte-Datenbank
- CSV-Export (Rohdaten)          - Interventionsempfehlungen
                                 - Fortschrittstracking
Umsetzung:
Phase 1 (MVP, Monat 1–6): Google Colab mit Login-Schutz
Phase 2 (Monat 7–9): Migration auf Netlify Functions + PostgreSQL
Kosten: 10–50 €/Monat Hosting, 2.000–5.000 € Entwicklung (einmalig)
Vorteil:
Ohne gültigen Account → keine professionelle Auswertung
Kontrolle über Nutzung (Anzahl Tests pro Lizenznehmer)
Updates erreichen alle sofort
Normwerte bleiben proprietär
2.2 Proprietäre Normwerte-Datenbank
Stärkster Langfristschutz! Normwerte sind extrem schwer zu replizieren:
Erfordern hunderte Tests über Jahre
Werden mit jeder Nutzung wertvoller (größere Stichprobe)
Was sammeln:
FFD/TRT/Skip-Rates pro Alter/Klassenstufe
Region-Ratios, Profil-Verteilung
Interventionserfolge (Vorher-Nachher)
Datenschutz:
Nur anonymisiert (Alter, Klassenstufe, Metriken – KEINE Namen)
DSGVO-konforme Einwilligung der Eltern erforderlich
Timeline:
Ab sofort: Systematisches Datentracking starten
Nach 6 Monaten: Erste Normwerte (mit 40+ Tests)
Nach 12 Monaten: Publikation als Marketing-Asset
2.3 Kontinuierliche Content-Updates
Regelmäßige Lieferungen (wie Adobe Creative Cloud):
Update-Typ
Frequenz
Beispiel
Neue Texte
Monatlich
Baseline-Texte für verschiedene Altersgruppen
Neue Interventionen
Quartalsweise
Leetspeak-Varianten, Oberlängen-Masken
Algorithmus-Updates
Halbjährlich
Verbesserte Klassifikation basierend auf Daten
Normwerte-Updates
Jährlich
Aktualisierte Benchmarks
Schulungen
Jährlich
Advanced-Training, neue Methoden
Vorteil: Abspringen = Verlust von Updates = Veralten des eigenen Angebots
SÄULE 3: ÖKONOMISCHE BINDUNG
(Bleiben ist profitabler als Gehen)
3.1 Gestaffeltes Preismodell (Erfolgsbasiert)
Paket
Monatlich
Pro Test (zusätzlich)
Zielgruppe
Starter
49 €
15 € (bis 10 Tests/Monat)
Neue Lerncoaches
Professional
149 €
8 € (11–30 Tests/Monat)
Etablierte Praxen
Enterprise
299 €
5 € (unbegrenzt)
Große Institute
Zusatz-Revenue:
Zertifizierung: 500 € (einmalig)
Re-Zertifizierung: 200 € (alle 2 Jahre)
Supervision: 80 €/Stunde
Premium-Support: +50 €/Monat
Vorteil:
Niedriger Einstieg (124 € im ersten Monat)
Bei Erfolg automatisches Upgrade
Du verdienst mit
3.2 Qualitätssiegel + Empfehlungsnetzwerk
Angebot an Lizenznehmer:
Logo: "Zertifizierter [Produktname]-Diagnostiker"
Eintrag in Therapeuten-Verzeichnis auf deiner Website
Cross-Promotion (Weitervermittlung von Anfragen)
Bedingung: Nur bei aktiver Lizenz
Effekt: Abspringen = Verlust von Marketing-Asset
3.3 Community + Peer-Learning
Monatliche Zoom-Calls (Fallbesprechungen)
Slack/Discord-Community
Zugang zu Vergleichsdaten (anonymisiert)
Effekt: Soziale Bindung + kontinuierlicher Lerneffekt
👨‍👩‍👧‍👦 KLIENTEN-WORKFLOW-INTEGRATION
Aktueller Workflow (manuell/analog):
Phase 1: Vor Videokonferenz
Eltern schicken ausgefüllten Fragebogen:
Alter, Name, Klasse, Akzeleration
Testungen (IQ, LRS etc.)
Vorerkrankungen
Besondere Beobachtungen zu Fähigkeiten
Rückmeldung Schule
Genutzte Fibel in Grundschule
Phase 2: Videokonferenz – Diagnostik
Begrüßung/Vertrauensaufbau
Kennenlernen (Lieblingsfächer, Hassfächer, Hobbys, Einstellungen)
Farbtest
3 spielerische IQ-Test-ähnliche Fragen (kreatives Denken)
Vorlesen (aktuell analog, zukünftig mit Eye-Tracking)
Abschreiben (aktuell analog, zukünftig mit Eye-Tracking)
Phase 3: In Videokonferenz – Feedback & Entscheidung
Erläuterung der Beobachtungen
Einschätzung zu Sinn von Intervention (basierend auf beobachteten Techniken)
Entscheidung für/gegen Intervention
Phase 4: Intervention (wenn gewünscht)
Oberlängen lesen
Leetspeak lesen
Verdrehte Wörter lesen
Laufdiktat vorstellen (als Hausaufgabe, 5× wiederholen)
Optional: Vokabeln lernen anregen
Optional: Mentales Fotografieren von Lernwörtern
Alles nach Gefühl angepasst! (Bislang analog, zukünftig mit Eye-Tracking)
Phase 5: Retest
Vorlesen erneut (Vorher-Nachher-Vergleich)
Geplante Datenbank-Integration:
Ziel: Strukturierte Erfassung ALLER Beobachtungen + Eye-Tracking-Daten in zentraler Datenbank
Datenbankstruktur (vereinfacht):
KLIENT
├─ Stammdaten (Fragebogen)
├─ Diagnostik-Session
│  ├─ Qualitative Beobachtungen (Kennenlernen, Farbtest, IQ-Fragen)
│  ├─ Eye-Tracking-Daten Vorlesen (Baseline)
│  ├─ Eye-Tracking-Daten Abschreiben (Baseline)
│  └─ Klassifikation (Dekodierer/Rater/Kompensator)
├─ Interventions-Sessions
│  ├─ Eye-Tracking Oberlängen
│  ├─ Eye-Tracking Leetspeak
│  ├─ Eye-Tracking Verdrehte Wörter
│  └─ Hausaufgaben-Tracking (Laufdiktat, Vokabeln, etc.)
└─ Retest
   ├─ Eye-Tracking-Daten Vorlesen (Nachher)
   └─ Delta-Metriken (Vorher vs. Nachher)
Vorteile:
Longitudinale Analyse (Entwicklung über Zeit)
Vergleich qualitative (Gespräch) vs. quantitative (Eye-Tracking) Daten
Automatische Berichtsgenerierung
Normwerte-Sammlung für gesamtes System
Umsetzung: Details werden in Phase 2 (Monat 7–9) geklärt, parallel zu Backend-Entwicklung
📅 12-MONATS-ROADMAP
PHASE 1: FOUNDATION (Monat 1–3) – JETZT
Hauptziel: Konzept stabilisieren, erste Daten sammeln
Zeitraum
Tasks
Investition
Output
Woche 1–2
Tracking-Sheet aufsetzen, DSGVO-Einwilligung
0 € / 6h
Datenerfassung ready
Woche 3–4
Website auf Netlify deployen
0 € / 6h
Produktiv-URL
Woche 5–12
10 Tests durchführen + dokumentieren
0 € / 40h
Erste Rohdaten
Monat 3
Python-Analyse verbessern, DB-Schema
0 € / 14h
Bessere Auswertung
Gesamt: 0 € + 66h → 10+ dokumentierte Tests
PHASE 2: RESEARCH (Monat 4–6)
Hauptziel: Validierung + Normwerte aufbauen
Monat
Tasks
Investition
Output
4
30 weitere Tests (verschiedene Altersgruppen)
0 € / 60h
40 Tests total
5
Statistische Auswertung + Paper-Entwurf
0 € / 32h
Normwerte-Tabelle, Paper-Draft
6
Leetspeak entwickeln + Backend-MVP
0 € / 35h
Intervention ready, Cloud-Analyse
Gesamt: 0 € + 127h → 40+ Tests, Paper-Draft, funktionierendes Backend-MVP
PHASE 3: PRE-LAUNCH (Monat 7–9)
Hauptziel: Rechtliche + technische Absicherung
Monat
Tasks
Investition
Output
7
Markenanmeldung + Anwalt (Lizenzvertrag)
2.300 € / 7h
Marke + Vertrag
8
Backend auf Netlify migrieren, Normwerte-DB
20 €/Monat / 25h
Produktiv-Backend
9
Schulungskonzept + Pricing finalisieren
0 € / 25h
Launch-ready
Gesamt: 2.300 € + 57h → Wasserdichter Schutz, SaaS-Backend, Schulung
PHASE 4: BETA-LAUNCH (Monat 10–12)
Hauptziel: Erste Lizenznehmer, Feedback, Testimonials
Monat
Tasks
Revenue
Output
10
3 Beta-Lizenznehmer akquirieren + schulen
298 €
Erste Kunden
11–12
Support, Feedback, Paper einreichen
894 €
Testimonials, Publikation
Gesamt: 0 € Investition + 56h → 1.192 € Revenue, validiertes Konzept
GESAMTBILANZ (12 MONATE):
Phase
€ Investition
Zeit
€ Revenue
Ergebnis
1–3
0
66h
0
Daten-Setup, 10 Tests
4–6
0
127h
0
40 Tests, Paper, MVP-Backend
7–9
2.300
57h
0
Rechtsschutz, SaaS
10–12
0
56h
1.192
3 Lizenznehmer, Testimonials
TOTAL
2.300 €
306h
1.192 €
Launchfähiges Produkt
ROI ab Monat 13:
10 Lizenznehmer à 149 €/Monat = 1.490 €/Monat
Break-Even nach ~2 Monaten
🎯 KONKRETE NEXT STEPS (WOCHE 1–4)
Woche 1: Daten-Foundation
[ ] Tracking-Sheet erstellen (Google Sheets/Airtable)
Spalten: Test-ID, Datum, Alter, Klassenstufe, FFD, TRT, Skip-Rate, Profil, qualitative Beobachtungen
[ ] DSGVO-Einwilligungserklärung formulieren
[ ] Ersten Test mit neuem Tracking durchführen
Woche 2: Website-Deployment
[ ] Netlify-Account erstellen
[ ] GitHub-Repo mit Netlify verbinden
[ ] Produktiv-URL testen
Woche 3–4: Erste Datensammlung
[ ] 5–10 Tests durchführen (verschiedene Altersgruppen)
[ ] Daten in Tracking-Sheet + qualitative Notizen eintragen
[ ] Erste Muster beobachten
Nach 4 Wochen: Checkpoint
Review Datensammlung
Entscheidung über Backend-Entwicklungsstart
Planung Monat 2–3
🔥 KRITISCHE ERFOLGSFAKTOREN
Was MUSS funktionieren:
Normwerte-Aufbau: Ohne proprietäre Datenbank kein langfristiger Schutz
Backend-Abhängigkeit: Ohne Cloud-Komponente zu leicht kopierbar
Kontinuierliche Innovation: Ohne Updates verliert Lizenz Wert
Wissenschaftliche Legitimität: Paper-Publikation als Vertrauensbasis
Wasserdichter Lizenzvertrag: Fachanwalt NICHT einsparen!
Größte Risiken:
Erfahrene Lerncoaches als Lizenznehmer: Höchstes Absprung-Risiko
Zu schwache technische Bindung: WebGazer Open Source = replizierbar
Zu aggressives Wettbewerbsverbot: Könnte unwirksam sein
Zu wenig Daten: Ohne Normwerte kein USP
Keine kontinuierliche Entwicklung: Lizenz verliert Wert
Abwehr-Strategien:
Normwerte ab Tag 1 systematisch sammeln
Backend mit Cloud-Komponente (nicht nur statisches HTML)
Lizenzvertrag von Fachanwalt prüfen lassen
Updates als Teil des Lizenzwerts kommunizieren
Community + Qualitätssiegel als soziale Bindung
📊 POSITIONIERUNG: WISSENSCHAFT TRIFFT PRAXIS
Hybrid-Ansatz:
Wissenschaftliche Basis: Paper-Publikation, Normwerte, evidenzbasiert
Praxisorientierte Aufbereitung: Einfache Schulungen, klare Handlungsempfehlungen
USP: "Forschung trifft Praxis – Eye-Tracking-Diagnostik für jeden Lerncoach"
Marketing-Strategie:
Zielgruppe primär: Lerncoaches, Lerntherapeuten, Psychologen (DACH)
Kanäle: Paper-Publikation → Konferenzen → LinkedIn → Webinare → Empfehlungen
Positionierung: Premium-Tool (nicht Discounter), aber zugänglich (gestaffeltes Pricing)
✅ ZUSAMMENFASSUNG: WAS SCHÜTZT DICH WIRKLICH?
Schutz-Element
Wirksamkeit
Kosten
Timeline
Marke
⭐⭐⭐
300 €
4 Wochen
Urheberrecht
⭐⭐
0 €
Sofort
Lizenzvertrag
⭐⭐⭐⭐
2.000 €
8 Wochen
Normwerte-Datenbank
⭐⭐⭐⭐⭐
0 € (Zeit)
6–12 Monate
Cloud-Backend
⭐⭐⭐⭐
2.000–5.000 €
6–9 Monate
Kontinuierliche Updates
⭐⭐⭐⭐⭐
0 € (Zeit)
Laufend
Community-Bindung
⭐⭐⭐
0 € (Zeit)
Ab Launch
Fazit: Kombination aus allen Elementen = maximaler Schutz. Keine einzelne Maßnahme reicht!
ENDE DER ZUSAMMENFASSUNG
Bereit für Integration ins Projekt. Nächster Schritt: Woche 1 starten oder Details klären.