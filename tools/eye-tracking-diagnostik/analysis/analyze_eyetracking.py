#!/usr/bin/env python3
"""
Eye-Tracking Analyse-Script v2.0
Analysiert CSV-Dateien aus dem Multi-Line-Tracking-System
und erstellt Visualisierungen + diagnostischen Report
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import re
from datetime import datetime

class EyeTrackingAnalyzer:
    def __init__(self, line1_csv, line2_csv, line3_csv):
        """Initialisiere Analyzer mit 3 CSV-Dateien"""
        self.line1_csv = line1_csv
        self.line2_csv = line2_csv
        self.line3_csv = line3_csv
        
        self.line1_df = None
        self.line2_df = None
        self.line3_df = None
        
        self.metadata = {}
        self.statistics = {}
        self.profile = None
        self.confidence = 0
        
        print("[Analyzer] Initialisiert")
    
    def load_data(self):
        """Lade alle 3 CSV-Dateien + extrahiere Metadaten"""
        print("[Analyzer] Lade Daten...")
        
        # Line 1: Vertical Tracking
        self.line1_df = self._load_csv_with_metadata(self.line1_csv)
        
        # Line 2: Syllable Tracking
        self.line2_df = self._load_csv_with_metadata(self.line2_csv)
        
        # Line 3: Standard Word Tracking
        self.line3_df = self._load_csv_with_metadata(self.line3_csv)
        
        print(f"[Analyzer] Daten geladen:")
        print(f"  - Line 1: {len(self.line1_df)} Chunks")
        print(f"  - Line 2: {len(self.line2_df)} Silben")
        print(f"  - Line 3: {len(self.line3_df)} Wörter")
    
    def _load_csv_with_metadata(self, filepath):
        """Lade CSV + extrahiere Metadaten aus Header"""
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Metadaten extrahieren (# Zeilen am Anfang)
        data_start = 0
        for i, line in enumerate(lines):
            if line.startswith('# Participant ID:'):
                self.metadata['participant_id'] = line.split(':')[1].strip()
            elif line.startswith('# Date:'):
                self.metadata['date'] = line.split(':', 1)[1].strip()
            elif line.startswith('# Text:'):
                self.metadata['text_id'] = line.split(':')[1].strip()
            elif not line.startswith('#'):
                data_start = i
                break
        
        # CSV ab Datenzeile laden
        df = pd.read_csv(filepath, skiprows=data_start)
        return df
    
    def calculate_statistics(self):
        """Berechne deskriptive Statistiken pro Zeile"""
        print("[Analyzer] Berechne Statistiken...")
        
        # Line 1: Vertical
        self.statistics['line1'] = {
            'mean_FFD': self.line1_df['FFD'].mean(),
            'mean_TRT': self.line1_df['TRT'].mean(),
            'mean_fixations': self.line1_df['fixation_count'].mean(),
            'mean_revisits': self.line1_df['revisits'].mean(),
            'skip_rate': (self.line1_df['skipped'].sum() / len(self.line1_df)) * 100,
            'mean_top_ratio': self.line1_df['top_ratio'].astype(float).mean()
        }
        
        # Line 2: Syllables
        self.statistics['line2'] = {
            'mean_FFD': self.line2_df['FFD'].mean(),
            'skip_rate': (self.line2_df['skipped'].sum() / len(self.line2_df)) * 100,
            'mean_jump_distance': self.line2_df['jump_distance'].dropna().mean(),
            'regressions': (self.line2_df['jump_distance'] < 0).sum()
        }
        
        # Line 3: Standard Words
        self.statistics['line3'] = {
            'mean_FFD': self.line3_df['FFD'].mean(),
            'mean_TRT': self.line3_df['TRT'].mean(),
            'mean_fixations': self.line3_df['fixation_count'].mean(),
            'mean_revisits': self.line3_df['revisits'].mean(),
            'skip_rate': (self.line3_df['skipped'].sum() / len(self.line3_df)) * 100,
            'mean_left_ratio': self.line3_df['left_ratio'].astype(float).mean(),
            'mean_top_ratio': self.line3_df['top_ratio'].astype(float).mean()
        }
        
        print("[Analyzer] Statistiken berechnet")
    
    def classify_reader_profile(self):
        """Klassifiziere Leserprofil via Scoring-System"""
        print("[Analyzer] Klassifiziere Leserprofil...")
        
        scores = {'decoder': 0, 'guesser': 0, 'compensator': 0}
        
        # Extrahiere Metriken
        mean_FFD = np.mean([
            self.statistics['line1']['mean_FFD'],
            self.statistics['line2']['mean_FFD'],
            self.statistics['line3']['mean_FFD']
        ])
        
        mean_fixations = np.mean([
            self.statistics['line1']['mean_fixations'],
            self.statistics['line3']['mean_fixations']
        ])
        
        mean_revisits = np.mean([
            self.statistics['line1']['mean_revisits'],
            self.statistics['line3']['mean_revisits']
        ])
        
        mean_skip_rate = np.mean([
            self.statistics['line1']['skip_rate'],
            self.statistics['line2']['skip_rate'],
            self.statistics['line3']['skip_rate']
        ])
        
        top_ratio = np.mean([
            self.statistics['line1']['mean_top_ratio'],
            self.statistics['line3']['mean_top_ratio']
        ])
        
        left_ratio = self.statistics['line3']['mean_left_ratio']
        jump_distance = self.statistics['line2']['mean_jump_distance']
        regressions = self.statistics['line2']['regressions']
        
        # ===== DEKODIERER-INDIKATOREN =====
        if mean_FFD > 300:
            scores['decoder'] += 2
        elif mean_FFD > 250:
            scores['decoder'] += 1
        
        if mean_fixations > 3:
            scores['decoder'] += 2
        elif mean_fixations > 2:
            scores['decoder'] += 1
        
        if 0.45 <= top_ratio <= 0.55:
            scores['decoder'] += 2
        
        if left_ratio > 0.55:
            scores['decoder'] += 1
        
        if mean_skip_rate < 10:
            scores['decoder'] += 2
        
        # ===== RATER-INDIKATOREN =====
        if mean_FFD < 200:
            scores['guesser'] += 2
        
        if mean_skip_rate > 30:
            scores['guesser'] += 3
        elif mean_skip_rate > 20:
            scores['guesser'] += 2
        
        if top_ratio > 0.60:
            scores['guesser'] += 2
        
        if jump_distance > 2.0:
            scores['guesser'] += 2
        elif jump_distance > 1.5:
            scores['guesser'] += 1
        
        if mean_fixations < 2:
            scores['guesser'] += 1
        
        # ===== KOMPENSATOR-INDIKATOREN =====
        if mean_revisits > 1:
            scores['compensator'] += 3
        elif mean_revisits > 0.5:
            scores['compensator'] += 2
        
        if regressions > 2:
            scores['compensator'] += 2
        elif regressions > 0:
            scores['compensator'] += 1
        
        # TRT >> FFD (viel Nacharbeit)?
        mean_TRT = np.mean([
            self.statistics['line1']['mean_TRT'],
            self.statistics['line3']['mean_TRT']
        ])
        if mean_TRT > mean_FFD * 2 and mean_FFD < 300:
            scores['compensator'] += 2
        
        if 10 <= mean_skip_rate <= 30:
            scores['compensator'] += 1
        
        # ===== KLASSIFIKATION =====
        total_score = sum(scores.values())
        if total_score == 0:
            self.profile = 'UNBESTIMMT'
            self.confidence = 0
        else:
            self.profile = max(scores, key=scores.get).upper()
            self.confidence = (scores[max(scores, key=scores.get)] / total_score) * 100
        
        self.scores = scores
        
        print(f"[Analyzer] Profil: {self.profile} (Konfidenz: {self.confidence:.1f}%)")
        print(f"[Analyzer] Scores: {scores}")
    
    def create_visualizations(self):
        """Erstelle alle 5 Visualisierungen"""
        print("[Analyzer] Erstelle Visualisierungen...")
        
        output_dir = Path('output_analysis')
        output_dir.mkdir(exist_ok=True)
        
        # 1. Line1: Vertical Distribution
        self._viz_line1_vertical(output_dir)
        
        # 2. Line2: Syllable Sequence
        self._viz_line2_syllables(output_dir)
        
        # 3. Line3: Regions Heatmap
        self._viz_line3_heatmap(output_dir)
        
        # 4. Profile Radar
        self._viz_profile_radar(output_dir)
        
        # 5. Statistics Summary
        self._viz_statistics_summary(output_dir)
        
        print("[Analyzer] Visualisierungen gespeichert in output_analysis/")
    
    def _viz_line1_vertical(self, output_dir):
        """Line 1: Top vs Bottom Duration Bar Chart"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        chunks = self.line1_df['text']
        top_dur = self.line1_df['top_duration']
        bottom_dur = self.line1_df['bottom_duration']
        
        x = np.arange(len(chunks))
        width = 0.35
        
        ax.bar(x - width/2, top_dur, width, label='Oben (Oberlängen)', color='skyblue')
        ax.bar(x + width/2, bottom_dur, width, label='Unten (Unterlängen)', color='lightcoral')
        
        ax.set_xlabel('Chunks')
        ax.set_ylabel('Fixationsdauer (ms)')
        ax.set_title('Zeile 1: Vertikale Fixationsverteilung (Oberlängen vs. Unterlängen)')
        ax.set_xticks(x)
        ax.set_xticklabels(chunks, rotation=45, ha='right')
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(output_dir / 'line1_vertical_distribution.png', dpi=150)
        plt.close()
    
    def _viz_line2_syllables(self, output_dir):
        """Line 2: Syllable Sequence Line Plot"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Nur gelesene Silben (nicht übersprungen)
        read_syls = self.line2_df[self.line2_df['skipped'] == 0].copy()
        
        if len(read_syls) > 0:
            read_syls = read_syls.sort_values('read_order')
            
            ax.plot(read_syls['read_order'], read_syls['syl_id'], 
                   marker='o', linewidth=2, markersize=8, label='Tatsächliche Sequenz')
            
            # Ideale Sequenz (0→1→2→...)
            ideal_x = range(1, len(read_syls) + 1)
            ideal_y = range(len(read_syls))
            ax.plot(ideal_x, ideal_y, linestyle='--', color='gray', 
                   alpha=0.5, label='Ideale Sequenz')
        
        ax.set_xlabel('Lesereihenfolge (zeitlich)')
        ax.set_ylabel('Silben-Index')
        ax.set_title('Zeile 2: Silben-Lesereihenfolge (Sequenzanalyse)')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(output_dir / 'line2_syllable_sequence.png', dpi=150)
        plt.close()
    
    def _viz_line3_heatmap(self, output_dir):
        """Line 3: 4-Regionen Heatmap"""
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Matrix erstellen: Wörter × 4 Regionen
        words = self.line3_df['word']
        matrix = self.line3_df[['tl_dur', 'tr_dur', 'bl_dur', 'br_dur']].values.T
        
        sns.heatmap(matrix, annot=True, fmt='.0f', cmap='YlOrRd', 
                   xticklabels=words, 
                   yticklabels=['Top-Left', 'Top-Right', 'Bottom-Left', 'Bottom-Right'],
                   cbar_kws={'label': 'Fixationsdauer (ms)'},
                   ax=ax)
        
        ax.set_title('Zeile 3: 4-Regionen-Heatmap (Fixationsdauer pro Wort)')
        ax.set_xlabel('Wörter')
        ax.set_ylabel('Regionen')
        
        plt.tight_layout()
        plt.savefig(output_dir / 'line3_regions_heatmap.png', dpi=150)
        plt.close()
    
    def _viz_profile_radar(self, output_dir):
        """Profile Radar Chart"""
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
        
        categories = ['Decoder', 'Guesser', 'Compensator']
        values = [self.scores['decoder'], self.scores['guesser'], self.scores['compensator']]
        
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        values += values[:1]
        angles += angles[:1]
        
        ax.plot(angles, values, 'o-', linewidth=2, color='blue')
        ax.fill(angles, values, alpha=0.25, color='blue')
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, size=12)
        ax.set_ylim(0, max(values) + 2)
        ax.set_title(f'Leserprofil-Radar\n{self.profile} (Konfidenz: {self.confidence:.1f}%)', 
                    size=14, weight='bold', pad=20)
        ax.grid(True)
        
        plt.tight_layout()
        plt.savefig(output_dir / 'profile_radar.png', dpi=150)
        plt.close()
    
    def _viz_statistics_summary(self, output_dir):
        """Statistics Summary: 4 Subplots"""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. Skip Rates
        ax1 = axes[0, 0]
        skip_rates = [
            self.statistics['line1']['skip_rate'],
            self.statistics['line2']['skip_rate'],
            self.statistics['line3']['skip_rate']
        ]
        ax1.bar(['Zeile 1', 'Zeile 2', 'Zeile 3'], skip_rates, color=['skyblue', 'lightgreen', 'coral'])
        ax1.set_ylabel('Skip Rate (%)')
        ax1.set_title('Skip-Rates pro Zeile')
        ax1.grid(axis='y', alpha=0.3)
        
        # 2. FFD Comparison
        ax2 = axes[0, 1]
        ffds = [
            self.statistics['line1']['mean_FFD'],
            self.statistics['line2']['mean_FFD'],
            self.statistics['line3']['mean_FFD']
        ]
        ax2.bar(['Zeile 1', 'Zeile 2', 'Zeile 3'], ffds, color=['skyblue', 'lightgreen', 'coral'])
        ax2.set_ylabel('FFD (ms)')
        ax2.set_title('First Fixation Duration (Mittelwert)')
        ax2.grid(axis='y', alpha=0.3)
        
        # 3. Fixation Counts
        ax3 = axes[1, 0]
        fix_counts = [
            self.statistics['line1']['mean_fixations'],
            self.statistics['line3']['mean_fixations']
        ]
        ax3.bar(['Zeile 1', 'Zeile 3'], fix_counts, color=['skyblue', 'coral'])
        ax3.set_ylabel('Fixationen pro Wort/Chunk')
        ax3.set_title('Durchschnittliche Fixationsanzahl')
        ax3.grid(axis='y', alpha=0.3)
        
        # 4. Ratios (Top & Left)
        ax4 = axes[1, 1]
        ratios = [
            self.statistics['line1']['mean_top_ratio'],
            self.statistics['line3']['mean_top_ratio'],
            self.statistics['line3']['mean_left_ratio']
        ]
        ax4.bar(['Top (L1)', 'Top (L3)', 'Left (L3)'], ratios, color=['skyblue', 'coral', 'lightgreen'])
        ax4.set_ylabel('Ratio (0-1)')
        ax4.set_title('Regionen-Ratios (0.5 = ausgeglichen)')
        ax4.axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='Ausgeglichen')
        ax4.legend()
        ax4.grid(axis='y', alpha=0.3)
        
        plt.suptitle('Statistik-Übersicht: Alle Zeilen', size=16, weight='bold')
        plt.tight_layout()
        plt.savefig(output_dir / 'statistics_summary.png', dpi=150)
        plt.close()
    
    def generate_report(self):
        """Generiere Text-Report"""
        print("[Analyzer] Generiere Report...")
        
        output_dir = Path('output_analysis')
        output_dir.mkdir(exist_ok=True)
        
        report_filename = f"report_{self.metadata.get('participant_id', 'UNKNOWN')}.txt"
        
        with open(output_dir / report_filename, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("EYE-TRACKING ANALYSE-REPORT v2.0\n")
            f.write("=" * 80 + "\n\n")
            
            # Metadaten
            f.write("METADATEN:\n")
            f.write(f"  Participant ID: {self.metadata.get('participant_id', 'N/A')}\n")
            f.write(f"  Datum: {self.metadata.get('date', 'N/A')}\n")
            f.write(f"  Text ID: {self.metadata.get('text_id', 'N/A')}\n\n")
            
            # Klassifikation
            f.write("=" * 80 + "\n")
            f.write("LESERPROFIL-KLASSIFIKATION:\n")
            f.write("=" * 80 + "\n")
            f.write(f"  Profil: {self.profile}\n")
            f.write(f"  Konfidenz: {self.confidence:.1f}%\n\n")
            
            f.write("  Scores:\n")
            f.write(f"    - Decoder: {self.scores['decoder']}\n")
            f.write(f"    - Guesser: {self.scores['guesser']}\n")
            f.write(f"    - Compensator: {self.scores['compensator']}\n\n")
            
            # Interpretation
            f.write("  Interpretation:\n")
            if self.profile == 'DECODER':
                f.write("    → Langsames, gründliches Dekodieren (jeder Buchstabe wird gelesen)\n")
                f.write("    → Hohe Fixationsdauer, wenig Skipping\n")
                f.write("    → Ausgeglichene Nutzung von Ober-/Unterlängen\n")
            elif self.profile == 'GUESSER':
                f.write("    → Schnelles Überfliegen/Raten basierend auf Wortformen\n")
                f.write("    → Viele übersprungene Wörter/Silben\n")
                f.write("    → Fokus auf Oberlängen\n")
            elif self.profile == 'COMPENSATOR':
                f.write("    → Hoher kognitiver Aufwand durch viele Rücksprünge\n")
                f.write("    → Viele Korrekturen und Re-Fixationen\n")
                f.write("    → Misslungene Kompensationsstrategien\n")
            else:
                f.write("    → Profil nicht eindeutig bestimmbar (mehr Daten nötig)\n")
            
            f.write("\n" + "=" * 80 + "\n")
            f.write("DETAILLIERTE STATISTIKEN:\n")
            f.write("=" * 80 + "\n\n")
            
            # Zeile 1
            f.write("ZEILE 1 (Vertical Tracking):\n")
            f.write(f"  - Chunks: {len(self.line1_df)}\n")
            f.write(f"  - Mean FFD: {self.statistics['line1']['mean_FFD']:.1f} ms\n")
            f.write(f"  - Mean TRT: {self.statistics['line1']['mean_TRT']:.1f} ms\n")
            f.write(f"  - Mean Fixations: {self.statistics['line1']['mean_fixations']:.2f}\n")
            f.write(f"  - Mean Revisits: {self.statistics['line1']['mean_revisits']:.2f}\n")
            f.write(f"  - Skip Rate: {self.statistics['line1']['skip_rate']:.1f}%\n")
            f.write(f"  - Mean Top Ratio: {self.statistics['line1']['mean_top_ratio']:.3f}\n\n")
            
            # Zeile 2
            f.write("ZEILE 2 (Syllable Tracking):\n")
            f.write(f"  - Silben: {len(self.line2_df)}\n")
            f.write(f"  - Mean FFD: {self.statistics['line2']['mean_FFD']:.1f} ms\n")
            f.write(f"  - Skip Rate: {self.statistics['line2']['skip_rate']:.1f}%\n")
            f.write(f"  - Mean Jump Distance: {self.statistics['line2']['mean_jump_distance']:.2f}\n")
            f.write(f"  - Regressions: {self.statistics['line2']['regressions']}\n\n")
            
            # Zeile 3
            f.write("ZEILE 3 (Standard Word Tracking):\n")
            f.write(f"  - Wörter: {len(self.line3_df)}\n")
            f.write(f"  - Mean FFD: {self.statistics['line3']['mean_FFD']:.1f} ms\n")
            f.write(f"  - Mean TRT: {self.statistics['line3']['mean_TRT']:.1f} ms\n")
            f.write(f"  - Mean Fixations: {self.statistics['line3']['mean_fixations']:.2f}\n")
            f.write(f"  - Mean Revisits: {self.statistics['line3']['mean_revisits']:.2f}\n")
            f.write(f"  - Skip Rate: {self.statistics['line3']['skip_rate']:.1f}%\n")
            f.write(f"  - Mean Left Ratio: {self.statistics['line3']['mean_left_ratio']:.3f}\n")
            f.write(f"  - Mean Top Ratio: {self.statistics['line3']['mean_top_ratio']:.3f}\n\n")
            
            f.write("=" * 80 + "\n")
            f.write("EMPFEHLUNGEN:\n")
            f.write("=" * 80 + "\n\n")
            
            if self.profile == 'DECODER':
                f.write("  - Intervention: Lesefluss-Training (Chunking, Blickspanne erweitern)\n")
                f.write("  - Fokus: Automatisierung von Worterkennungsmustern\n")
            elif self.profile == 'GUESSER':
                f.write("  - Intervention: Leetspeak-Training (Oberlängen verändern)\n")
                f.write("  - Fokus: Aufmerksamkeit auf alle Buchstaben lenken\n")
            elif self.profile == 'COMPENSATOR':
                f.write("  - Intervention: Oberlängen-Masking + gezieltes Fixationstraining\n")
                f.write("  - Fokus: Reduktion von Regressionen, Stärkung Dekodierung\n")
            else:
                f.write("  - Weitere Tests durchführen für klarere Klassifikation\n")
            
            f.write("\n" + "=" * 80 + "\n")
            f.write(f"Report generiert: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n")
        
        print(f"[Analyzer] Report gespeichert: output_analysis/{report_filename}")
    
    def run(self):
        """Führe komplette Analyse-Pipeline aus"""
        print("\n" + "=" * 80)
        print("EYE-TRACKING ANALYSE-PIPELINE v2.0")
        print("=" * 80 + "\n")
        
        self.load_data()
        self.calculate_statistics()
        self.classify_reader_profile()
        self.create_visualizations()
        self.generate_report()
        
        print("\n" + "=" * 80)
        print("ANALYSE ABGESCHLOSSEN ✓")
        print("=" * 80 + "\n")
        print(f"Profil: {self.profile} (Konfidenz: {self.confidence:.1f}%)")
        print("Output: output_analysis/")
        print("  - 5 PNG-Visualisierungen")
        print("  - 1 Text-Report\n")


def main():
    if len(sys.argv) != 4:
        print("Usage: python analyze_eyetracking.py <line1.csv> <line2.csv> <line3.csv>")
        print("\nBeispiel:")
        print("  python analyze_eyetracking.py \\")
        print("    line1_vertical_123.csv \\")
        print("    line2_syllables_123.csv \\")
        print("    line3_words_123.csv")
        sys.exit(1)
    
    line1_csv = sys.argv[1]
    line2_csv = sys.argv[2]
    line3_csv = sys.argv[3]
    
    # Dateien prüfen
    for csv_file in [line1_csv, line2_csv, line3_csv]:
        if not Path(csv_file).exists():
            print(f"ERROR: Datei nicht gefunden: {csv_file}")
            sys.exit(1)
    
    # Analyse starten
    analyzer = EyeTrackingAnalyzer(line1_csv, line2_csv, line3_csv)
    analyzer.run()


if __name__ == '__main__':
    main()
