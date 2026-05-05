import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import re

# Címtárak beállítása
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_dir = os.path.join(script_dir, '..', 'csv')

# Összes 8-as feladathoz tartozó csv kikeresése
file_pattern = os.path.join(csv_dir, '8_*.csv')
files = glob.glob(file_pattern)

frequencies_1 = []
amplitudes_1 = []

frequencies_2 = []
amplitudes_2 = []

for file in files:
    basename = os.path.basename(file)
    
    # A csillapítatlan / nem gerjesztett fájlt kihagyjuk
    if 'nemgerj' in basename:
        continue
        
    # Meghatározzuk, hogy melyik adatsorhoz tartozik
    is_dataset_2 = basename.startswith('8_2_')
    
    # Frekvencia kinyerése a fájlnévből
    if is_dataset_2:
        match = re.search(r'8_2_(\d+(?:\.\d+)?)', basename)
    else:
        match = re.search(r'8_(\d+(?:\.\d+)?)', basename)
        
    if match:
        freq_str = match.group(1)
        freq = float(freq_str)
        
        try:
            df = pd.read_csv(file)
            
            # Csak azokat a sorokat vesszük, ahol van pozíció adat
            pos = df['Position'].dropna().values
            
            if len(pos) == 0:
                continue
                
            # Hogy elkerüljük a kezdeti tranzienseket, az adatok második felét használjuk
            pos_steady = pos[len(pos)//2:]
            
            if len(pos_steady) < 10:
                pos_steady = pos
                
            # Amplitúdó számítása: (max - min) / 2
            amplitude = (np.max(pos_steady) - np.min(pos_steady)) / 2.0
            
            if is_dataset_2:
                frequencies_2.append(freq)
                amplitudes_2.append(amplitude)
            else:
                frequencies_1.append(freq)
                amplitudes_1.append(amplitude)
        except Exception as e:
            print(f"Hiba a {basename} fájl feldolgozásakor: {e}")

# Segédfüggvény az adatok rendezésére és átlagolására
def process_dataset(freqs, amps):
    if len(freqs) == 0:
        return np.array([]), np.array([])
    
    sorted_indices = np.argsort(freqs)
    freqs = np.array(freqs)[sorted_indices]
    amps = np.array(amps)[sorted_indices]

    unique_freqs = []
    avg_amps = []
    for freq in np.unique(freqs):
        indices = np.where(freqs == freq)
        unique_freqs.append(freq)
        avg_amps.append(np.mean(amps[indices]))
        
    return np.array(unique_freqs), np.array(avg_amps)

u_freqs_1, avg_amps_1 = process_dataset(frequencies_1, amplitudes_1)
u_freqs_2, avg_amps_2 = process_dataset(frequencies_2, amplitudes_2)

# Globális betűméret beállítása
plt.rcParams.update({'font.size': 18})

plt.figure(figsize=(12, 8))

# Első adatsor ábrázolása
if len(u_freqs_1) > 0:
    plt.plot(u_freqs_1, avg_amps_1, marker='o', linestyle='-', color='b', label="1. mérés (8_...)")
    max_idx_1 = np.argmax(avg_amps_1)
    plt.plot(u_freqs_1[max_idx_1], avg_amps_1[max_idx_1], 'bo', markersize=10, label=f"Rezonancia 1: {u_freqs_1[max_idx_1]} kHz")

# Második adatsor ábrázolása
if len(u_freqs_2) > 0:
    plt.plot(u_freqs_2, avg_amps_2, marker='s', linestyle='-', color='g', label="2. mérés (8_2_...)")
    max_idx_2 = np.argmax(avg_amps_2)
    plt.plot(u_freqs_2[max_idx_2], avg_amps_2[max_idx_2], 'gs', markersize=10, label=f"Rezonancia 2: {u_freqs_2[max_idx_2]} kHz")

plt.title('8. feladat - Rezonanciagörbék')
plt.xlabel('Frekvencia [kHz]')
plt.ylabel('Amplitúdó [m]')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Kép mentése
images_dir = os.path.join(script_dir, '..', 'images')
os.makedirs(images_dir, exist_ok=True)
plt.savefig(os.path.join(images_dir, '8_feladat.png'))

plt.show()

# Konzolra kiírás
print("1. mérés (8_...) frekvencia-amplitúdó párok:")
for f, a in zip(u_freqs_1, avg_amps_1):
    print(f"{f:5.2f} kHz -> {a:.5f} m")

print("\n2. mérés (8_2_...) frekvencia-amplitúdó párok:")
for f, a in zip(u_freqs_2, avg_amps_2):
    print(f"{f:5.2f} kHz -> {a:.5f} m")
