import numpy as np
import matplotlib.pyplot as plt

filename = "3_feladat.csv"

try:
    data = np.genfromtxt(filename, delimiter=',', skip_header=0)
except:
    print(f"nem talaltam a {filename} fajlt, bocs")
    exit(1)
    
time = data[:, 0]
resistance = data[:, 1]

temp = resistance - 100
temp = temp/0.385

m, c = np.polyfit(time, temp, 1)

plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='y', label="homerseklet az ido fuggvenyeben")
plt.plot(time, c + m*time, linestyle='-', color='r', label=f"Illesztett egyenes: y = {m:.2f}x + {c:.2f}")
plt.title("3.feladat: a termosz hovesztesege az ido fuggvenyeben")
plt.xlabel("Ido (s)")
plt.ylabel("Homerseklet (C)")
plt.legend()
plt.tight_layout()
plt.show()