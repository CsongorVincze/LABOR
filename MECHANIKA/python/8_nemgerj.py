import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

# Fájl elérési útjának beállítása
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, '..', 'csv', '8_nemgerj.csv')

try:
    df = pd.read_csv(filename)
except Exception as e:
    print(f"Hiba a fájl beolvasásakor: {e}")
    exit(1)

# Üres mezők kiszűrése
df = df.dropna(subset=['Time', 'Position'])

# Az első 4 másodperc levágása
df = df[df['Time'] >= 4.0]

time = df['Time'].values
pos = df['Position'].values

# Csúcsok (lokális maximumok) megkeresése
# prominence: minimális kiemelkedés a zaj kiszűrésére
peaks, _ = find_peaks(pos, distance=5, prominence=0.002)

if len(peaks) > 1:
    periods = np.diff(time[peaks])
    avg_period = np.mean(periods)
    eigenfrequency = 1.0 / avg_period
else:
    avg_period = np.nan
    eigenfrequency = np.nan

print(f"Mért átlagos periódusidő: {avg_period:.5f} s")
print(f"Számított sajátfrekvencia: {eigenfrequency:.5f} Hz")

# Globális betűméret beállítása
plt.rcParams.update({'font.size': 18})

plt.figure(figsize=(12, 6))

plt.plot(time, pos, label="Szabad rezgés", color='b')
if len(peaks) > 1:
    plt.plot(time[peaks], pos[peaks], "rx", markersize=8, label=f"Csúcsok (f_saját = {eigenfrequency:.3f} Hz)")
else:
    plt.plot(time[peaks], pos[peaks], "rx", markersize=8, label="Csúcsok")

plt.title('8. feladat - Szabad rezgés vizsgálata')
plt.xlabel('Idő [s]')
plt.ylabel('Pozíció [m]')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Kép mentése
images_dir = os.path.join(script_dir, '..', 'images')
os.makedirs(images_dir, exist_ok=True)
plt.savefig(os.path.join(images_dir, '8_nemgerj.png'))

plt.show()
