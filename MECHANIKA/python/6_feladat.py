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

m, c = np.polyfit(num, d, 1)

plt.rcParams.update({'font.size': 18})

plt.figure(figsize=(10, 6))
plt.scatter(num, d, marker='o', color='b', label="Mért adatok")
plt.plot(num, c + num*m, linestyle='-', color='r', label=f"Illesztett: y = {m:.3f}x + {c:.3f}")

plt.title("6. feladat")
plt.xlabel("Sorszám")
plt.ylabel("d")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(script_dir, '..', 'images', '6_feladat.png'))
plt.show()

print(f"A meredekség: {m:.5f}, a tengelymetszet {c:.5f}")
