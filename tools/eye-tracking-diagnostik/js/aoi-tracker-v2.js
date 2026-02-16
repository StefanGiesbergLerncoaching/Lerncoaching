// ========================================================================
// AOI TRACKER v2.0 - Multi-Line-Tracking-Engine
// ========================================================================
// 
// ARCHITEKTUR:
// Phase 1: Initialisierung (AOIs für alle 3 Zeilen)
// Phase 2: Live-Tracking (nur Rohdaten sammeln)
// Phase 3: Post-Processing (Fixationen clustern, Metriken berechnen)
// Phase 4: CSV-Export (3 separate Dateien)
//
// TRACKING-MODI:
// - Zeile 1: Vertical Tracking (Oberlängen/Unterlängen, Chunking)
// - Zeile 2: Syllable Tracking (Silben-Sequenz, horizontal)
// - Zeile 3: Standard Word Tracking (4-Regionen: 2×2)
//
// ========================================================================

class AOITracker {
    constructor(textData) {
        this.textData = textData;
        
        // State
        this.isTracking = false;
        this.startTime = null;
        
        // Rohdaten (Live-Tracking)
        this.gazePoints = [];
        
        // AOI-Definitionen (pro Zeile)
        this.line1_chunks = [];  // Vertical Tracking
        this.line2_syllables = [];  // Syllable Tracking
        this.line3_words = [];  // Standard Word Tracking
        
        // Verarbeitete Daten (Post-Processing)
        this.line1_data = [];
        this.line2_data = [];
        this.line3_data = [];
        
        console.log('[AOITracker v2.0] Initialisiert');
    }
    
    // ====================================================================
    // PHASE 1: INITIALISIERUNG
    // ====================================================================
    
    initializeAOIs() {
        console.log('[AOITracker] Initialisiere AOIs...');
        
        this.textData.lines.forEach(line => {
            switch(line.tracking_mode) {
                case 'vertical':
                    this._initLine1Vertical(line);
                    break;
                case 'syllables':
                    this._initLine2Syllables(line);
                    break;
                case 'standard':
                    this._initLine3Standard(line);
                    break;
            }
        });
        
        console.log('[AOITracker] AOIs fertig:', {
            line1_chunks: this.line1_chunks.length,
            line2_syllables: this.line2_syllables.length,
            line3_words: this.line3_words.length
        });
    }
    
    _initLine1Vertical(line) {
        line.chunks.forEach((chunk, idx) => {
            const element = document.getElementById(`line1_chunk_${idx}`);
            if (!element) {
                console.warn(`[Line1] Element nicht gefunden: line1_chunk_${idx}`);
                return;
            }
            
            const rect = element.getBoundingClientRect();
            
            this.line1_chunks.push({
                chunk_id: idx,
                text: chunk.text,
                x: rect.left,
                y: rect.top,
                width: rect.width,
                height: rect.height,
                centerY: rect.top + rect.height / 2
            });
        });
    }
    
    _initLine2Syllables(line) {
        line.syllables.forEach((syl, idx) => {
            const element = document.getElementById(`line2_syl_${idx}`);
            if (!element) {
                console.warn(`[Line2] Element nicht gefunden: line2_syl_${idx}`);
                return;
            }
            
            const rect = element.getBoundingClientRect();
            
            this.line2_syllables.push({
                syl_id: idx,
                syllable: syl.text,
                word: syl.word,
                x: rect.left,
                y: rect.top,
                width: rect.width,
                height: rect.height,
                centerX: rect.left + rect.width / 2,
                centerY: rect.top + rect.height / 2
            });
        });
    }
    
    _initLine3Standard(line) {
        line.words.forEach((word, idx) => {
            const element = document.getElementById(`line3_word_${idx}`);
            if (!element) {
                console.warn(`[Line3] Element nicht gefunden: line3_word_${idx}`);
                return;
            }
            
            const rect = element.getBoundingClientRect();
            
            this.line3_words.push({
                word_id: idx,
                word: word.text,
                x: rect.left,
                y: rect.top,
                width: rect.width,
                height: rect.height,
                centerX: rect.left + rect.width / 2,
                centerY: rect.top + rect.height / 2
            });
        });
    }
    
    // ====================================================================
    // PHASE 2: LIVE-TRACKING
    // ====================================================================
    
    startTracking() {
        this.isTracking = true;
        this.startTime = Date.now();
        this.gazePoints = [];
        
        console.log('[AOITracker] Tracking gestartet');
    }
    
    processGazePoint(x, y, timestamp) {
        if (!this.isTracking) return;
        
        // Nur Rohdaten speichern (kein Processing während Tracking)
        this.gazePoints.push({
            x: Math.round(x),
            y: Math.round(y),
            timestamp: Math.round(timestamp)
        });
    }
    
    stopTracking() {
        this.isTracking = false;
        console.log('[AOITracker] Tracking gestoppt. Gaze Points:', this.gazePoints.length);
        
        // PHASE 3: Post-Processing starten
        this._processGazeData();
    }
    
    // ====================================================================
    // PHASE 3: POST-PROCESSING
    // ====================================================================
    
    _processGazeData() {
        console.log('[AOITracker] Starte Post-Processing...');
        
        // 1. Fixationen clustern (aus Rohdaten)
        const fixations = this._clusterFixations(this.gazePoints);
        console.log('[AOITracker] Fixationen erkannt:', fixations.length);
        
        // 2. Pro Zeile verarbeiten
        this._processLine1Vertical(fixations);
        this._processLine2Syllables(fixations);
        this._processLine3Standard(fixations);
        
        console.log('[AOITracker] Post-Processing fertig');
    }
    
    _clusterFixations(gazePoints) {
        // Fixations-Clustering: 
        // Fixation = mehrere Gaze-Points auf gleicher AOI innerhalb 200ms
        
        const fixations = [];
        let currentFixation = null;
        
        gazePoints.forEach(gaze => {
            // Prüfen ob Gaze in einem AOI liegt
            const aoi = this._findAOIForGaze(gaze.x, gaze.y);
            
            if (!aoi) {
                // Inter-Word-Fixation (außerhalb AOIs)
                if (currentFixation) {
                    fixations.push(currentFixation);
                    currentFixation = null;
                }
                return;
            }
            
            // Neue Fixation oder Fortsetzung?
            if (!currentFixation) {
                // Neue Fixation starten
                currentFixation = {
                    aoi_type: aoi.type,
                    aoi_id: aoi.id,
                    start_timestamp: gaze.timestamp,
                    end_timestamp: gaze.timestamp,
                    gaze_points: [gaze]
                };
            } else if (
                currentFixation.aoi_type === aoi.type &&
                currentFixation.aoi_id === aoi.id &&
                gaze.timestamp - currentFixation.end_timestamp < 200
            ) {
                // Fixation fortsetzen (gleiche AOI, <200ms Abstand)
                currentFixation.end_timestamp = gaze.timestamp;
                currentFixation.gaze_points.push(gaze);
            } else {
                // Neue AOI oder zu lange Pause → Fixation beenden
                fixations.push(currentFixation);
                
                currentFixation = {
                    aoi_type: aoi.type,
                    aoi_id: aoi.id,
                    start_timestamp: gaze.timestamp,
                    end_timestamp: gaze.timestamp,
                    gaze_points: [gaze]
                };
            }
        });
        
        // Letzte Fixation hinzufügen
        if (currentFixation) {
            fixations.push(currentFixation);
        }
        
        return fixations;
    }
    
    _findAOIForGaze(x, y) {
        // Prüfe alle 3 Zeilen (Reihenfolge: 1, 2, 3)
        
        // Line 1: Chunks
        for (let chunk of this.line1_chunks) {
            if (this._isInside(x, y, chunk)) {
                return { type: 'chunk', id: chunk.chunk_id };
            }
        }
        
        // Line 2: Syllables
        for (let syl of this.line2_syllables) {
            if (this._isInside(x, y, syl)) {
                return { type: 'syllable', id: syl.syl_id };
            }
        }
        
        // Line 3: Words
        for (let word of this.line3_words) {
            if (this._isInside(x, y, word)) {
                return { type: 'word', id: word.word_id };
            }
        }
        
        return null;
    }
    
    _isInside(x, y, aoi) {
        return (
            x >= aoi.x &&
            x <= aoi.x + aoi.width &&
            y >= aoi.y &&
            y <= aoi.y + aoi.height
        );
    }
    
    // ====================================================================
    // LINE 1: VERTICAL TRACKING
    // ====================================================================
    
    _processLine1Vertical(fixations) {
        const chunkFixations = fixations.filter(f => f.aoi_type === 'chunk');
        
        this.line1_chunks.forEach(chunk => {
            const chunkFix = chunkFixations.filter(f => f.aoi_id === chunk.chunk_id);
            
            if (chunkFix.length === 0) {
                // Chunk übersprungen
                this.line1_data.push({
                    chunk_id: chunk.chunk_id,
                    text: chunk.text,
                    FFD: 0,
                    TRT: 0,
                    fixation_count: 0,
                    revisits: 0,
                    skipped: 1,
                    top_duration: 0,
                    bottom_duration: 0,
                    top_ratio: 0
                });
                return;
            }
            
            // Metriken berechnen
            const FFD = chunkFix[0].end_timestamp - chunkFix[0].start_timestamp;
            const TRT = chunkFix.reduce((sum, fix) => 
                sum + (fix.end_timestamp - fix.start_timestamp), 0
            );
            
            // Top/Bottom-Verteilung
            let topDuration = 0;
            let bottomDuration = 0;
            
            chunkFix.forEach(fix => {
                const avgY = fix.gaze_points.reduce((sum, gp) => sum + gp.y, 0) 
                    / fix.gaze_points.length;
                
                const duration = fix.end_timestamp - fix.start_timestamp;
                
                if (avgY < chunk.centerY) {
                    topDuration += duration;
                } else {
                    bottomDuration += duration;
                }
            });
            
            const topRatio = topDuration + bottomDuration > 0 
                ? topDuration / (topDuration + bottomDuration) 
                : 0;
            
            this.line1_data.push({
                chunk_id: chunk.chunk_id,
                text: chunk.text,
                FFD: FFD,
                TRT: TRT,
                fixation_count: chunkFix.length,
                revisits: chunkFix.length - 1,
                skipped: 0,
                top_duration: topDuration,
                bottom_duration: bottomDuration,
                top_ratio: topRatio.toFixed(3)
            });
        });
    }
    
    // ====================================================================
    // LINE 2: SYLLABLE TRACKING
    // ====================================================================
    
    _processLine2Syllables(fixations) {
        const sylFixations = fixations.filter(f => f.aoi_type === 'syllable');
        
        // Read-Order ermitteln (zeitliche Reihenfolge der ersten Fixation)
        const readOrder = {};
        sylFixations.forEach((fix, idx) => {
            if (!(fix.aoi_id in readOrder)) {
                readOrder[fix.aoi_id] = idx + 1;
            }
        });
        
        this.line2_syllables.forEach(syl => {
            const sylFix = sylFixations.filter(f => f.aoi_id === syl.syl_id);
            
            if (sylFix.length === 0) {
                // Silbe übersprungen
                this.line2_data.push({
                    syl_id: syl.syl_id,
                    syllable: syl.syllable,
                    word: syl.word,
                    FFD: 0,
                    skipped: 1,
                    read_order: null,
                    from_syl_id: null,
                    jump_distance: null
                });
                return;
            }
            
            // Erste Fixation
            const firstFix = sylFix[0];
            const FFD = firstFix.end_timestamp - firstFix.start_timestamp;
            
            // From-Syllable (welche Silbe wurde davor fixiert?)
            const fixIndex = sylFixations.findIndex(f => 
                f.aoi_type === 'syllable' && f.aoi_id === syl.syl_id
            );
            
            let fromSylId = null;
            let jumpDistance = null;
            
            if (fixIndex > 0) {
                const prevFix = sylFixations[fixIndex - 1];
                fromSylId = prevFix.aoi_id;
                jumpDistance = syl.syl_id - prevFix.aoi_id;
            }
            
            this.line2_data.push({
                syl_id: syl.syl_id,
                syllable: syl.syllable,
                word: syl.word,
                FFD: FFD,
                skipped: 0,
                read_order: readOrder[syl.syl_id] || null,
                from_syl_id: fromSylId,
                jump_distance: jumpDistance
            });
        });
    }
    
    // ====================================================================
    // LINE 3: STANDARD WORD TRACKING
    // ====================================================================
    
    _processLine3Standard(fixations) {
        const wordFixations = fixations.filter(f => f.aoi_type === 'word');
        
        this.line3_words.forEach(word => {
            const wordFix = wordFixations.filter(f => f.aoi_id === word.word_id);
            
            if (wordFix.length === 0) {
                // Wort übersprungen
                this.line3_data.push({
                    word_id: word.word_id,
                    word: word.word,
                    FFD: 0,
                    TRT: 0,
                    fixation_count: 0,
                    revisits: 0,
                    skipped: 1,
                    tl_dur: 0,
                    tr_dur: 0,
                    bl_dur: 0,
                    br_dur: 0,
                    left_ratio: 0,
                    top_ratio: 0
                });
                return;
            }
            
            // Metriken berechnen
            const FFD = wordFix[0].end_timestamp - wordFix[0].start_timestamp;
            const TRT = wordFix.reduce((sum, fix) => 
                sum + (fix.end_timestamp - fix.start_timestamp), 0
            );
            
            // 4 Regionen (2×2)
            let tlDur = 0, trDur = 0, blDur = 0, brDur = 0;
            
            wordFix.forEach(fix => {
                const avgX = fix.gaze_points.reduce((sum, gp) => sum + gp.x, 0) 
                    / fix.gaze_points.length;
                const avgY = fix.gaze_points.reduce((sum, gp) => sum + gp.y, 0) 
                    / fix.gaze_points.length;
                
                const duration = fix.end_timestamp - fix.start_timestamp;
                
                const isLeft = avgX < word.centerX;
                const isTop = avgY < word.centerY;
                
                if (isTop && isLeft) tlDur += duration;
                else if (isTop && !isLeft) trDur += duration;
                else if (!isTop && isLeft) blDur += duration;
                else brDur += duration;
            });
            
            const totalDur = tlDur + trDur + blDur + brDur;
            const leftRatio = totalDur > 0 ? (tlDur + blDur) / totalDur : 0;
            const topRatio = totalDur > 0 ? (tlDur + trDur) / totalDur : 0;
            
            this.line3_data.push({
                word_id: word.word_id,
                word: word.word,
                FFD: FFD,
                TRT: TRT,
                fixation_count: wordFix.length,
                revisits: wordFix.length - 1,
                skipped: 0,
                tl_dur: tlDur,
                tr_dur: trDur,
                bl_dur: blDur,
                br_dur: brDur,
                left_ratio: leftRatio.toFixed(3),
                top_ratio: topRatio.toFixed(3)
            });
        });
    }
    
    // ====================================================================
    // PHASE 4: CSV-EXPORT
    // ====================================================================
    
    exportToCSV() {
        return {
            line1: this._exportLine1CSV(),
            line2: this._exportLine2CSV(),
            line3: this._exportLine3CSV()
        };
    }
    
    _exportLine1CSV() {
        let csv = 'chunk_id,text,FFD,TRT,fixation_count,revisits,skipped,top_duration,bottom_duration,top_ratio\n';
        
        this.line1_data.forEach(row => {
            csv += `${row.chunk_id},"${row.text}",${row.FFD},${row.TRT},${row.fixation_count},${row.revisits},${row.skipped},${row.top_duration},${row.bottom_duration},${row.top_ratio}\n`;
        });
        
        return csv;
    }
    
    _exportLine2CSV() {
        let csv = 'syl_id,syllable,word,FFD,skipped,read_order,from_syl_id,jump_distance\n';
        
        this.line2_data.forEach(row => {
            csv += `${row.syl_id},"${row.syllable}","${row.word}",${row.FFD},${row.skipped},${row.read_order || ''},${row.from_syl_id !== null ? row.from_syl_id : ''},${row.jump_distance !== null ? row.jump_distance : ''}\n`;
        });
        
        return csv;
    }
    
    _exportLine3CSV() {
        let csv = 'word_id,word,FFD,TRT,fixation_count,revisits,skipped,tl_dur,tr_dur,bl_dur,br_dur,left_ratio,top_ratio\n';
        
        this.line3_data.forEach(row => {
            csv += `${row.word_id},"${row.word}",${row.FFD},${row.TRT},${row.fixation_count},${row.revisits},${row.skipped},${row.tl_dur},${row.tr_dur},${row.bl_dur},${row.br_dur},${row.left_ratio},${row.top_ratio}\n`;
        });
        
        return csv;
    }
}
