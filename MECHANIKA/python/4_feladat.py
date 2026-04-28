import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fájl elérésének beállítása
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, '..', 'csv', '4_feladat.csv')

try:
    # A fájl olvasása szóköz elválasztóval
    df = pd.read_csv(filename, header=None, sep=r'\s+', names=['R', 'T10'])
except:
    print(f"nem talaltam a {filename} fajlt, bocs")
    exit(1)

# X érték: Sugár négyzete (r^2)
r = df['R'].values
x = r**2

# Y érték: Periódusidő négyzete (T^2)
# A második oszlop a 10x-es periódusidő
t10 = df['T10'].values
t = t10 / 10.0
y = t**2

# Egyenes illesztése
m, c = np.polyfit(x, y, 1)

# Grafikon beállítások és rajzolás
plt.rcParams.update({'font.size': 18})

plt.figure(figsize=(10, 6))
plt.scatter(x, y, marker='o', color='b', label="Mért adatok")

# Illesztett egyenes rajzolása a min és max X értékek között a szép folytonos vonalért
x_fit = np.array([np.min(x), np.max(x)])
plt.plot(x_fit, c + m*x_fit, linestyle='-', color='r', label=f"Illesztett: y = {m:.3f}x + {c:.3f}")

plt.title("4. feladat")
plt.xlabel("Sugár négyzete, $r^2$ [m$^2$]")
plt.ylabel("Periódusidő négyzete, $T^2$ [s$^2$]")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(script_dir, '..', 'images', '4_feladat.png'))
plt.show()



print(f"A meredekség: {m:.5f}, a tengelymetszet {c:.5f}")


print(f"k csillag: {4*3.14*3.14*0.05142/m:.5f},  {0.05142*c/m-1.6*0.00001:.5f}")
