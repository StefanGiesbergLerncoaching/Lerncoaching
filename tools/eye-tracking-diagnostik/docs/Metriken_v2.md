# VollstÃ¤ndige Metriken-Ãœbersicht fÃ¼r Eye-Tracking-Projekt v2.0

---

## **ARCHITEKTUR-ÃœBERSICHT**

### **Multi-Line-Tracking-Strategie:**
Das System erfasst **3 verschiedene Zeilen mit spezialisierten Tracking-Modi**, um unterschiedliche Aspekte des Leseverhaltens zu messen:

- **Zeile 1:** OberlÃ¤ngen-SensitivitÃ¤t (Vertikal: Oben vs. Unten)
- **Zeile 2:** Silben-Sequenz (Horizontal: Lesereihenfolge)
- **Zeile 3:** Standard-Wort-Tracking (4-Regionen: Links/Rechts Ã— Oben/Unten)

**Rationale:** Verschiedene Leserprofile zeigen unterschiedliche Muster:
- **Dekodierer:** Nutzen alle Wort-Teile gleichmÃ¤ÃŸig
- **Rater:** Fokus auf OberlÃ¤ngen, chaotische Sequenz
- **Kompensatoren:** Viele RÃ¼cksprÃ¼nge, hoher Nachbearbeitungs-Aufwand

---

## **1. ZEILE 1: VERTICAL TRACKING (OberlÃ¤ngen-Analyse)**

### **Konzept:**
- **WÃ¶rter werden zu "Chunks" gruppiert** (kleine WÃ¶rter <4 Buchstaben werden kombiniert)
- **2 Regionen pro Chunk:** Oben (0-50% der HÃ¶he) / Unten (50-100%)
- **Ziel:** Messen, ob Kind Ober-/UnterlÃ¤ngen nutzt oder nur "mittlere Zone" scannt

### **Metriken (10 pro Chunk):**

| Metrik | KÃ¼rzel | Typ | Beschreibung | Diagnostischer Wert |
|--------|--------|-----|--------------|---------------------|
| **Chunk ID** | - | Integer | Fortlaufender Index (0-basiert) | Identifikation |
| **Text** | - | String | Chunk-Text (z.B. "Im Garten") | Menschenlesbar |
| **First Fixation Duration** | FFD | Integer (ms) | Dauer der ersten Fixation auf dem Chunk | Dekodierungsschwierigkeit |
| **Total Reading Time** | TRT | Integer (ms) | Gesamtverweildauer inkl. Regressionen | VerstÃ¤ndnisprobleme |
| **Fixation Count** | FC | Integer | Anzahl aller Fixationen | Verarbeitungsaufwand |
| **Revisits** | REV | Integer | Anzahl der RÃ¼cksprÃ¼nge (Re-Fixationen) | Kompensationsstrategien |
| **Skipped** | - | Boolean (0/1) | Wurde Chunk Ã¼bersprungen? | Raten vs. grÃ¼ndliches Lesen |
| **Top Duration** | - | Integer (ms) | Fixationsdauer in oberer HÃ¤lfte | OberlÃ¤ngen-Nutzung |
| **Bottom Duration** | - | Integer (ms) | Fixationsdauer in unterer HÃ¤lfte | UnterlÃ¤ngen-Nutzung |
| **Top Ratio** | - | Float (0-1) | `top_duration / (top + bottom)` | Balance-Indikator |

### **CSV-Beispiel:**
```csv
chunk_id,text,FFD,TRT,fixation_count,revisits,skipped,top_duration,bottom_duration,top_ratio
0,"Im Garten",234,567,3,1,0,320,247,0.564
1,"steht",187,187,1,0,0,95,92,0.508
2,"ein groÃŸer",312,845,4,2,0,510,335,0.604
3,"Apfelbaum.",423,1234,5,3,0,687,547,0.557
```

### **Diagnostische Interpretation:**

| Top Ratio | Interpretation | Profil |
|-----------|----------------|--------|
| **0.45-0.55** | Ausgeglichen (nutzt alle Buchstaben) | Dekodierer |
| **>0.60** | Top-betont (nur OberlÃ¤ngen) | Rater |
| **<0.40** | Bottom-betont (ungewÃ¶hnlich) | Atypisch |

**Beispiel-Interpretation:**
- "ein groÃŸer": `top_ratio=0.604` â†’ **Leicht top-betont**, kÃ¶nnte auf Raten hindeuten
- "steht": `top_ratio=0.508` â†’ **Perfekt ausgeglichen**, typisch Dekodierer

---

## **2. ZEILE 2: SYLLABLE TRACKING (Silben-Sequenz-Analyse)**

### **Konzept:**
- **Jede Silbe ist eine eigene AOI** (Area of Interest)
- **Tracking der Lesereihenfolge:** In welcher Sequenz werden Silben fixiert?
- **Ziel:** Unterscheiden zwischen sequenziellem Dekodieren vs. chaotischem Raten

### **Metriken (8 pro Silbe):**

| Metrik | Typ | Beschreibung | Diagnostischer Wert |
|--------|-----|--------------|---------------------|
| **Syllable ID** | Integer | Fortlaufender Index (0-basiert) | Position im Text |
| **Syllable** | String | Silbentext (z.B. "Sei") | Menschenlesbar |
| **Word** | String | ZugehÃ¶riges Wort (z.B. "Seine") | Kontext |
| **FFD** | Integer (ms) | First Fixation Duration | Dekodierungsgeschwindigkeit |
| **Skipped** | Boolean (0/1) | Wurde Silbe Ã¼bersprungen? | Raten-Indikator |
| **Read Order** | Integer | Zeitliche Reihenfolge der ersten Fixation | Sequenz-Analyse |
| **From Syllable ID** | Integer | Von welcher Silbe kam der Blick? | Sprung-Analyse |
| **Jump Distance** | Integer | Silben-Index-Differenz (kann negativ sein) | Regressionen/Progressionen |

### **CSV-Beispiel:**
```csv
syl_id,syllable,word,FFD,skipped,read_order,from_syl_id,jump_distance
0,"Sei","Seine",145,0,1,NULL,NULL
1,"ne","Seine",87,0,2,0,1
2,"Ã„s","Ã„ste",156,0,3,1,1
3,"te","Ã„ste",0,1,NULL,2,NULL
4,"hÃ¤n","hÃ¤ngen",189,0,4,2,2
5,"gen","hÃ¤ngen",234,0,5,4,1
6,"vol","voller",178,0,6,5,1
7,"ler","voller",92,0,8,6,1
8,"ro","roter",203,0,7,7,-1
9,"ter","roter",156,0,9,8,1
```

### **Diagnostische Interpretation:**

#### **A) Sequenz-Analyse:**

| Muster | Read Order | Interpretation | Profil |
|--------|-----------|----------------|--------|
| **Perfekt sequenziell** | 0â†’1â†’2â†’3â†’4â†’5... | Silbe fÃ¼r Silbe, kein Ãœberspringen | Dekodierer |
| **Chaotisch** | 0â†’3â†’7â†’1â†’9... | GroÃŸe SprÃ¼nge, viel Skipping | Rater |
| **Sequenziell + Regressionen** | 0â†’1â†’3â†’2â†’4... | VorwÃ¤rts, aber RÃ¼cksprÃ¼nge | Kompensator |

#### **B) Jump-Distance-Analyse:**

| Jump Distance | Bedeutung | Profil |
|---------------|-----------|--------|
| **+1** | NÃ¤chste Silbe (normal) | Alle |
| **>+2** | Ãœberspringen von Silben | Rater |
| **Negativ** | Regression (RÃ¼cksprung) | Kompensator |

**Beispiel-Interpretation:**
- Syl 3 ("te"): `skipped=1` â†’ **Ãœbersprungen**, typisch fÃ¼r Rater
- Syl 8 ("ro"): `jump_distance=-1` â†’ **Regression** (von 7â†’8, dann zurÃ¼ck zu 8â†’7), typisch Kompensator
- Mean Jump Distance = 1.2 â†’ **Ãœberwiegend sequenziell** (Dekodierer)
- Mean Jump Distance = 2.5 â†’ **Viele SprÃ¼nge** (Rater)

---

## **3. ZEILE 3: STANDARD WORD TRACKING (4-Regionen-Analyse)**

### **Konzept:**
- **Jedes Wort hat 4 Regionen:** Top-Left, Top-Right, Bottom-Left, Bottom-Right (2Ã—2-Grid)
- **Ziel:** Kombinierte Analyse von horizontaler (Links/Rechts) und vertikaler (Oben/Unten) Fokussierung

### **Metriken (13 pro Wort):**

| Metrik | Typ | Beschreibung | Diagnostischer Wert |
|--------|-----|--------------|---------------------|
| **Word ID** | Integer | Fortlaufender Index (0-basiert) | Position |
| **Word** | String | Worttext | Menschenlesbar |
| **FFD** | Integer (ms) | First Fixation Duration | Dekodierungsgeschwindigkeit |
| **TRT** | Integer (ms) | Total Reading Time | VerstÃ¤ndnisprobleme |
| **Fixation Count** | Integer | Anzahl Fixationen | Verarbeitungsaufwand |
| **Revisits** | Integer | Anzahl RÃ¼cksprÃ¼nge | Kompensationsstrategien |
| **Skipped** | Boolean (0/1) | Wort Ã¼bersprungen? | Raten-Indikator |
| **Top-Left Duration** | Integer (ms) | Fixationsdauer Top-Left Region | Wortanfang + OberlÃ¤ngen |
| **Top-Right Duration** | Integer (ms) | Fixationsdauer Top-Right Region | Wortende + OberlÃ¤ngen |
| **Bottom-Left Duration** | Integer (ms) | Fixationsdauer Bottom-Left Region | Wortanfang + UnterlÃ¤ngen |
| **Bottom-Right Duration** | Integer (ms) | Fixationsdauer Bottom-Right Region | Wortende + UnterlÃ¤ngen |
| **Left Ratio** | Float (0-1) | `(TL + BL) / total` | Links-Fokus (Wortanfang) |
| **Top Ratio** | Float (0-1) | `(TL + TR) / total` | Oben-Fokus (OberlÃ¤ngen) |

### **CSV-Beispiel:**
```csv
word_id,word,FFD,TRT,fixation_count,revisits,skipped,tl_dur,tr_dur,bl_dur,br_dur,left_ratio,top_ratio
0,"Jeden",234,567,3,1,0,145,123,156,143,0.531,0.472
1,"Herbst",187,345,2,0,0,89,98,78,80,0.484,0.542
2,"pflÃ¼cken",423,1326,5,3,0,79,0,536,711,0.464,0.060
3,"wir",178,178,1,0,0,178,0,0,0,1.000,1.000
```

### **Diagnostische Interpretation:**

#### **A) Left Ratio (Horizontal):**

| Left Ratio | Interpretation | Profil |
|------------|----------------|--------|
| **>0.55** | Links-betont (Wortanfang-Fokus) | Dekodierer |
| **0.45-0.55** | Ausgeglichen | Neutral |
| **<0.45** | Rechts-betont (Wortende-Antizipation) | Fortgeschrittene Leser |

**Beispiel:**
- "wir": `left_ratio=1.000` â†’ **Extrem links-betont**, nur Wortanfang fixiert (typisch Dekodierer bei kurzen WÃ¶rtern)

#### **B) Top Ratio (Vertikal):**

| Top Ratio | Interpretation | Profil |
|-----------|----------------|--------|
| **>0.60** | Top-betont (nur OberlÃ¤ngen) | Rater |
| **0.45-0.55** | Ausgeglichen | Dekodierer |
| **<0.40** | Bottom-betont (UnterlÃ¤ngen-Fokus) | Atypisch |

**Beispiel:**
- "pflÃ¼cken": `top_ratio=0.060` â†’ **Extrem bottom-betont** (nur UnterlÃ¤ngen: Ã¼, p), ungewÃ¶hnlich!

#### **C) Kombination (2D-Analyse):**

| Left Ratio | Top Ratio | Interpretation | Profil |
|------------|-----------|----------------|--------|
| **>0.55** | **0.45-0.55** | Wortanfang, alle Buchstaben | Klassischer Dekodierer |
| **0.45-0.55** | **>0.60** | Mittig, nur OberlÃ¤ngen | Rater (Wortform-Erkennung) |
| **<0.45** | **>0.60** | Wortende, nur OberlÃ¤ngen | Fortgeschrittener Rater |
| **>0.55** | **<0.40** | Wortanfang, UnterlÃ¤ngen | Atypisch (visuomotorisch?) |

---

## **4. GLOBALE STATISTIKEN (Ãœber alle Zeilen)**

Diese Metriken werden **im Python-Script berechnet** (nicht im CSV):

### **A) Skip-Rates:**

| Metrik | Berechnung | Interpretation |
|--------|-----------|----------------|
| **Line 1 Skip Rate** | `(skipped_chunks / total_chunks) * 100` | % Ã¼bersprungener Chunks |
| **Line 2 Skip Rate** | `(skipped_syllables / total_syllables) * 100` | % Ã¼bersprungener Silben |
| **Line 3 Skip Rate** | `(skipped_words / total_words) * 100` | % Ã¼bersprungener WÃ¶rter |

**Diagnostischer Wert:**
- Skip Rate <10%: GrÃ¼ndlicher Dekodierer
- Skip Rate 10-30%: Normal/Kompensator
- Skip Rate >30%: Rater

---

### **B) Mean-Werte:**

| Metrik | Zeile(n) | Berechnung | Interpretation |
|--------|----------|-----------|----------------|
| **Mean FFD** | 1, 2, 3 | Durchschnitt aller FFD-Werte | Dekodierungsgeschwindigkeit |
| **Mean TRT** | 1, 3 | Durchschnitt aller TRT-Werte | Gesamtaufwand |
| **Mean Fixation Count** | 1, 3 | Durchschnitt Fixationen/Wort | Verarbeitungstiefe |
| **Mean Revisits** | 1, 3 | Durchschnitt RÃ¼cksprÃ¼nge/Wort | Kompensation |
| **Mean Jump Distance** | 2 | Durchschnitt Silben-SprÃ¼nge | Lesefluss |
| **Regressions** | 2 | Anzahl negativer Jump-Distances | RÃ¼cksprung-HÃ¤ufigkeit |

---

### **C) Ratios:**

| Metrik | Zeile(n) | Berechnung | Interpretation |
|--------|----------|-----------|----------------|
| **Mean Top Ratio** | 1, 3 | Durchschnitt aller Top-Ratios | OberlÃ¤ngen-PrÃ¤ferenz |
| **Mean Left Ratio** | 3 | Durchschnitt aller Left-Ratios | Wortanfang-PrÃ¤ferenz |

---

## **5. DIAGNOSTISCHE INTERPRETATIONS-MATRIX**

### **Dekodierer-Profil:**

| Metrik | Erwarteter Wert | Zeile |
|--------|-----------------|-------|
| **FFD** | >300ms | 1, 2, 3 |
| **TRT** | Sehr hoch (>1000ms) | 1, 3 |
| **Fixation Count** | >3 pro Wort | 1, 3 |
| **Revisits** | Mittel (0.5-1.5) | 1, 3 |
| **Top Ratio** | 0.45-0.55 (ausgeglichen) | 1, 3 |
| **Left Ratio** | >0.55 (links-betont) | 3 |
| **Skip Rate** | <10% | 1, 2, 3 |
| **Jump Distance** | ~1.0 (sequenziell) | 2 |

**Verhaltensbeschreibung:**
- Liest jedes Wort, jeden Buchstaben
- Nutzt Ober-/UnterlÃ¤ngen gleichmÃ¤ÃŸig
- Fokus auf Wortanfang (Links-Bias)
- Langsam, aber grÃ¼ndlich

---

### **Rater-Profil:**

| Metrik | Erwarteter Wert | Zeile |
|--------|-----------------|-------|
| **FFD** | <200ms | 1, 2, 3 |
| **TRT** | Niedrig in Baseline, **hoch in Intervention** | 1, 3 |
| **Fixation Count** | <2 pro Wort | 1, 3 |
| **Revisits** | Niedrig (<0.5) | 1, 3 |
| **Top Ratio** | >0.60 (top-betont) | 1, 3 |
| **Left Ratio** | 0.45-0.55 (neutral) | 3 |
| **Skip Rate** | >30% | 1, 2, 3 |
| **Jump Distance** | >2.0 (groÃŸe SprÃ¼nge) | 2 |

**Verhaltensbeschreibung:**
- Ãœberfliegt Text schnell
- Nutzt nur OberlÃ¤ngen/Wortformen
- Ãœberspringt viele WÃ¶rter/Silben
- RÃ¤t basierend auf Kontext

**Kritische Intervention:**
- Bei **Leetspeak** (OberlÃ¤ngen verÃ¤ndert): **Massiver Leistungseinbruch**

---

### **Kompensator-Profil:**

| Metrik | Erwarteter Wert | Zeile |
|--------|-----------------|-------|
| **FFD** | Mittel (200-300ms) | 1, 2, 3 |
| **TRT** | **Sehr hoch** (Nacharbeit!) | 1, 3 |
| **Fixation Count** | Mittel (2-3) | 1, 3 |
| **Revisits** | **Sehr hoch** (>1.5) | 1, 3 |
| **Top Ratio** | 0.48-0.58 (leicht top-betont) | 1, 3 |
| **Left Ratio** | 0.48-0.58 (neutral-leicht links) | 3 |
| **Skip Rate** | 10-30% (selektiv) | 1, 2, 3 |
| **Jump Distance** | 1.2-1.8 (mit Regressionen) | 2 |
| **Regressions** | >2 | 2 |

**Verhaltensbeschreibung:**
- Versucht schnell zu lesen (wie Rater)
- Merkt VerstÃ¤ndnisprobleme
- Springt zurÃ¼ck, korrigiert
- Hoher kognitiver Aufwand

---

## **6. KLASSIFIKATIONS-ALGORITHMUS (Python)**

### **Scoring-System:**

```python
scores = {'decoder': 0, 'guesser': 0, 'compensator': 0}

# ===== DEKODIERER-INDIKATOREN =====
if mean_FFD > 300: scores['decoder'] += 2
if mean_FFD > 250: scores['decoder'] += 1
if mean_fixations > 3: scores['decoder'] += 2
if mean_fixations > 2: scores['decoder'] += 1
if 0.45 <= top_ratio <= 0.55: scores['decoder'] += 2
if left_ratio > 0.55: scores['decoder'] += 1
if skip_rate < 10: scores['decoder'] += 2

# ===== RATER-INDIKATOREN =====
if mean_FFD < 200: scores['guesser'] += 2
if skip_rate > 30: scores['guesser'] += 3
if skip_rate > 20: scores['guesser'] += 2
if top_ratio > 0.60: scores['guesser'] += 2
if mean_jump_distance > 2.0: scores['guesser'] += 2
if mean_jump_distance > 1.5: scores['guesser'] += 1
if mean_fixations < 2: scores['guesser'] += 1

# ===== KOMPENSATOR-INDIKATOREN =====
if mean_revisits > 1: scores['compensator'] += 3
if mean_revisits > 0.5: scores['compensator'] += 2
if regressions > 2: scores['compensator'] += 2
if regressions > 0: scores['compensator'] += 1
if TRT > FFD * 2 and FFD < 300: scores['compensator'] += 2
if 10 <= skip_rate <= 30: scores['compensator'] += 1

# ===== KLASSIFIKATION =====
profile = max(scores, key=scores.get)
confidence = scores[profile] / sum(scores.values())
```

### **Konfidenz-Interpretation:**

| Confidence | Interpretation |
|------------|----------------|
| **>0.70** | Sehr sicher |
| **0.50-0.70** | Sicher |
| **0.30-0.50** | Unsicher (gemischtes Profil) |
| **<0.30** | Sehr unsicher (mehr Daten nÃ¶tig) |

---

## **7. CSV-EXPORT-WORKFLOW**

### **Ablauf:**

```
1. User klickt "Fertig"
   â†“
2. tracker.stopTracking()
   â†“
3. _processGazeData()
   - _clusterFixations() (Rohdaten â†’ Fixationen)
   - _processVerticalLine() (Zeile 1)
   - _processSyllableLine() (Zeile 2)
   - _processStandardLine() (Zeile 3)
   â†“
4. exportToCSV()
   - _exportLine1CSV()
   - _exportLine2CSV()
   - _exportLine3CSV()
   â†“
5. downloadData() (in index.html)
   - 3Ã— downloadCSVFile()
   - Metadaten-Header hinzufÃ¼gen
```

### **Metadaten-Header (in allen 3 CSVs):**

```csv
# EXPERIMENT METADATA
# Participant ID: TEST_1767970168463
# Date: 2026-01-09T14:49:28.463Z
# Text: baseline_multiline_v1
```

---

## **8. PYTHON-ANALYSE-METRIKEN**

Diese werden **zusÃ¤tzlich** zu den CSV-Daten berechnet:

### **A) Deskriptive Statistiken:**

| Metrik | Python-Funktion | Output |
|--------|-----------------|--------|
| **Mean** | `df['FFD'].mean()` | Durchschnitt |
| **Median** | `df['FFD'].median()` | Median (robuster) |
| **Std Dev** | `df['FFD'].std()` | Standardabweichung |
| **Min/Max** | `df['FFD'].min()`, `.max()` | Extremwerte |

### **B) Visualisierungen:**

| Plot | Typ | Zeile(n) | Zweck |
|------|-----|----------|-------|
| **Vertical Distribution** | Bar Chart | 1 | Top vs. Bottom Duration |
| **Syllable Sequence** | Line Plot | 2 | Read Order vs. Ideal Sequence |
| **Regions Heatmap** | Heatmap | 3 | 4 Regionen Ã— WÃ¶rter |
| **Profile Radar** | Radar Chart | Alle | Decoder/Guesser/Compensator Scores |
| **Statistics Summary** | 4 Subplots | Alle | Skip-Rates, FFD, Fixations, Ratios |

---

## **9. GEPLANTE ERWEITERUNGEN (Phase 2+)**

### **A) Intervention-Metriken (Phase 2):**

ZusÃ¤tzliche Spalten in CSV:

| Metrik | Beschreibung |
|--------|--------------|
| **intervention_type** | "baseline", "leetspeak", "oberlÃ¤ngen" |
| **delta_FFD** | FFD_Intervention - FFD_Baseline |
| **delta_TRT** | TRT_Intervention - TRT_Baseline |
| **delta_skip_rate** | Skip_Rate_Intervention - Skip_Rate_Baseline |

**Ziel:** Messen, wie stark Performance bei Intervention einbricht

---

### **B) Wortarten-Kategorisierung (Phase 3):**

| Metrik | Beschreibung |
|--------|--------------|
| **word_type** | "noun", "verb", "function_word" |
| **word_length** | Anzahl Buchstaben |
| **frequency** | WorthÃ¤ufigkeit (aus Korpus) |

**Ziel:** Analyse nach linguistischen Kategorien

---

### **C) Longitudinale Metriken (Phase 3):**

| Metrik | Beschreibung |
|--------|--------------|
| **session_id** | Test-Sitzung (1, 2, 3...) |
| **days_since_baseline** | Tage seit erstem Test |
| **improvement_score** | (Session_N - Session_1) / Session_1 |

**Ziel:** Lernkurven Ã¼ber Zeit messen

---

## **10. QUALITÃ„TSKONTROLLE-METRIKEN**

| Check | Metrik | Schwellenwert | Aktion |
|-------|--------|---------------|--------|
| **Kalibrierung OK?** | Vertical Drift | <30px | Warnung wenn hÃ¶her |
| **Tracking valide?** | Gaze Points | >100 | Wenn weniger â†’ Neu-Kalibrierung |
| **Genug Daten?** | Skip Rate | <80% | Wenn hÃ¶her â†’ Test wiederholen |
| **Plausibel?** | FFD Range | 50-1000ms | Wenn auÃŸerhalb â†’ Daten prÃ¼fen |

---

## **ZUSAMMENFASSUNG: Was wird erfasst?**

### **Pro Zeile:**

| Zeile | AOIs | Metriken/AOI | Total | CSV-Name |
|-------|------|--------------|-------|----------|
| **1** | 4 Chunks | 10 | 40 | `line1_vertical.csv` |
| **2** | 12 Silben | 8 | 96 | `line2_syllables.csv` |
| **3** | 7 WÃ¶rter | 13 | 91 | `line3_words.csv` |
| **TOTAL** | **23 AOIs** | - | **227 Datenpunkte** | - |

### **Pro Test-Session:**

- 3 CSV-Dateien
- 227+ einzelne Datenpunkte
- 5 Visualisierungen (PNG)
- 1 Text-Report mit Klassifikation
- ~2-5 MB Daten-Output

---

**ENDE METRIKEN-DOKUMENTATION v2.0**