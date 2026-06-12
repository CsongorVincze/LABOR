import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, '..', 'csv', '6_feladat.csv')

try:
    # A fájl olvasása szóköz elválasztóval
    df = pd.read_csv(filename, header=None, sep=r'\s+', names=['num', 'd'])
except:
    print(f"nem talaltam a {filename} fajlt, bocs")
    exit(1)
    
num = df['num'].values
d = df['d'].values

# Egy súly tömege 25g = 0.025 kg
mass = num * 0.025

m, c = np.polyfit(mass, d, 1)

plt.rcParams.update({'font.size': 18})

plt.figure(figsize=(10, 6))
plt.scatter(mass, d, marker='o', color='b', label="Mért adatok", zorder=3)
plt.plot(mass, c + mass*m, linestyle='-', color='r', label=f"Illesztett: y = {m:.3f}x + {c:.3f}", zorder=2)

# Értékek feliratozása a pontoknál
for m_val, d_val in zip(mass, d):
    plt.text(m_val, d_val + 0.15, f'{d_val}', ha='center', va='bottom', fontsize=14, color='blue', zorder=4)

plt.title("6. feladat")
plt.xlabel("Tömeg [kg]")
plt.ylabel("Megnyúlás [cm]")
plt.xticks(mass)
plt.grid(True, linestyle='--', alpha=0.7, zorder=0)
plt.margins(0.15)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(script_dir, '..', 'images', '6_feladat.png'))
plt.show()

# Rugóállandó (k) számítása a meredekségből (m = delta_d / delta_mass)
# k = F / d = (mass * g) / d = g / (d / mass) = g / (meredekség_cm_per_kg / 100)
g = 9.81
k = g / (m / 100)

print(f"A meredekség: {m:.5f} cm/kg, a tengelymetszet {c:.5f} cm")
print(f"A rugóállandó (k): {k:.2f} N/m (feltételezve, hogy a megnyúlás cm-ben van)")
