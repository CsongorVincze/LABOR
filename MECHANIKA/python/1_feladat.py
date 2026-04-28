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

# X értékek
x = df['X'].values

# Átlagoljuk a 2. és 3. oszlopot (NaN értékeket kihagyva)
y_vals = df[['Y1', 'Y2']].values
y = np.nanmean(y_vals, axis=1)

# Illesztés
m, c = np.polyfit(x[1:], y[1:], 1)

plt.rcParams.update({'font.size': 18})

plt.figure(figsize=(10, 6))
plt.scatter(x, y, marker='o', color='b', label="Mért adatok (átlag)")
plt.plot(x, c + m*x, linestyle='-', color='r', label=f"Illesztett egyenes: y = {m:.3f}x + {c:.2f}")

plt.title("1. feladat")
plt.xlabel("Golyók száma")
plt.ylabel("Szögkitérés")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(script_dir, '..', 'images', '1_feladat.png'))
plt.show()

print(f"A meredekség: {m:.5f}")
