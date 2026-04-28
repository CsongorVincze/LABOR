import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Get the absolute path to the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, '..', 'csv', '1_feladat.csv')

try:
    # Read the file with space separator. Using names to handle missing values on the first row
    df = pd.read_csv(filename, header=None, sep=r'\s+', names=['X', 'Y1', 'Y2'])
except:
    print(f"nem talaltam a {filename} fajlt, bocs")
    exit(1)

# X értékek (golyók száma)
x = df['X'].values

# Tömeg kiszámítása (g-ban)
# Kezdeti tömeg 4.6g + 4.07g minden golyó után
mass = 4.6 + x * 4.07

# Átlagoljuk a 2. és 3. oszlopot (NaN értékeket kihagyva)
y_vals = df[['Y1', 'Y2']].values
y = np.nanmean(y_vals, axis=1)

# Illesztés (kihagyva az első elemet, ami esetleg eltérő lehet vagy 0, ha az előző kódban is ki volt hagyva)
m, c = np.polyfit(mass, y, 1)

plt.rcParams.update({'font.size': 18})

plt.figure(figsize=(10, 6))
plt.scatter(mass, df['Y1'], marker='o', color='gray', alpha=0.5, label="Egyedi mérések")
plt.scatter(mass, df['Y2'], marker='o', color='gray', alpha=0.5)
plt.scatter(mass, y, marker='o', color='b', label="Átlagolt adatok")
x_fit = np.linspace(0, np.max(mass), 100)
plt.plot(x_fit, c + m*x_fit, linestyle='-', color='r', label=f"Illesztett egyenes: y = {m:.3f}x + {c:.2f}")
plt.xlim(left=0)

plt.title("Szögkitérés a tömeg függvényében")
plt.xlabel("Tömeg [g]")
plt.ylabel("Szögkitérés")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(script_dir, '..', 'images', '1_feladat_mass.png'))
plt.show()

print(f"A meredekség (szög/g): {m:.5f}")
print(f"Az y-tengelymetszet (szög): {c:.5f}")
