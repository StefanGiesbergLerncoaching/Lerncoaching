// ===== GLOBALE KONFIGURATION =====
// Diese Datei wird von allen anderen Scripts importiert

const CONFIG = {
    // Experiment-Metadaten
    experimentName: "Okulomotorik-Diagnostik HB-Kinder",
    version: "1.0.0",
    researcher: "Stefan Giesberg",
    
    // Teilnehmer-Daten
    participant: {
        id: null,
        age: null,
        iq: null,
        diagnosis: null
    },
    
    // WebGazer-Einstellungen
    eyeTracking: {
        calibrationPoints: 9,
        calibrationRepetitions: 3,
        gazeUpdateFrequency: 60,  // Hz
        predictionModel: 'ridge',
    },
    
    // Experiment-Timing
    timing: {
        calibrationDuration: 5000,
        textPresentationMax: 300000,  // 5 Min
        interTrialInterval: 2000,     // 2 Sek
    },
    
    // AOI-Definitionen
    aoi: {
        marginTop: 100,
        marginLeft: 200,
        wordHeight: 40,
        wordSpacing: 10,
        lineHeight: 80,
    },
    
    // Datenexport
    export: {
        format: 'csv',
        includeRawGaze: true,
        includeAggregated: true,
        filenamePrefix: 'gaze_data_',
    }
};

// Hilfsfunktionen
function generateParticipantId() {
    const timestamp = Date.now();
    const random = Math.floor(Math.random() * 1000);
    return `P${timestamp}_${random}`;
}

// Falls Du später ES6 Modules nutzt:
// export { CONFIG, generateParticipantId };

// Für jetzt (ohne Module):
// Die Variablen sind global verfügbar
```

---

### **analysis/requirements.txt**
```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0