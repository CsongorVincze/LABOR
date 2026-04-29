import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

# Címtár és fájlok beállítása
script_dir = os.path.dirname(os.path.abspath(__file__))
filename1 = os.path.join(script_dir, '..', 'csv', '7_feladat.csv')
filename2 = os.path.join(script_dir, '..', 'csv', '7_feladat_2.csv')

try:
    df1 = pd.read_csv(filename1)
    df2 = pd.read_csv(filename2)
except Exception as e:
    print(f"Hiba a fájlok beolvasásakor: {e}")
    exit(1)

# Adatok vágása a kért időpontoktól
df1 = df1[df1['Time'] >= 7.5]
df2 = df2[df2['Time'] >= 2.0]

# Periódusidő meghatározása a csúcsok (lokális maximumok) keresésével
time1 = df1['Time'].values
pos1 = df1['Position'].values
# find_peaks distance paramétere: legalább hány adatpont legyen két csúcs között
peaks1, _ = find_peaks(pos1, distance=5, prominence=0.005)
if len(peaks1) > 1:
    period1 = np.mean(np.diff(time1[peaks1]))
else:
    period1 = np.nan

time2 = df2['Time'].values
pos2 = df2['Position'].values
peaks2, _ = find_peaks(pos2, distance=5, prominence=0.005)
if len(peaks2) > 1:
    period2 = np.mean(np.diff(time2[peaks2]))
else:
    period2 = np.nan

print(f"7_feladat.csv periódusideje: {period1:.4f} s")
print(f"7_feladat_2.csv periódusideje: {period2:.4f} s")

# Globális betűméret beállítása
plt.rcParams.update({'font.size': 14})

# Rajzolás
plt.figure(figsize=(12, 10))

# Első mérés grafikonja
plt.subplot(2, 1, 1)
plt.plot(time1, pos1, label='Adat 1', color='b')
plt.plot(time1[peaks1], pos1[peaks1], "rx", markersize=8, label=f'Csúcsok (T = {period1:.3f} s)')
plt.title('7. feladat - 1. mérés')
plt.xlabel('Idő [s]')
plt.ylabel('Pozíció [m]')
plt.legend()
plt.grid(True)

# Második mérés grafikonja
plt.subplot(2, 1, 2)
plt.plot(time2, pos2, label='Adat 2', color='g')
plt.plot(time2[peaks2], pos2[peaks2], "rx", markersize=8, label=f'Csúcsok (T = {period2:.3f} s)')
plt.title('7. feladat - 2. mérés')
plt.xlabel('Idő [s]')
plt.ylabel('Pozíció [m]')
plt.legend()
plt.grid(True)

plt.tight_layout()

# Kép mentése
images_dir = os.path.join(script_dir, '..', 'images')
os.makedirs(images_dir, exist_ok=True)
plt.savefig(os.path.join(images_dir, '7_feladat.png'))

plt.show()
