import os
import numpy as np
import matplotlib.pyplot as plt

# Get the absolute path to the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'adatok', '3_feladat.csv')

try:
    data = np.genfromtxt(filename, delimiter=',', skip_header=0)
except:
    print(f"nem talaltam a {filename} fajlt, bocs")
    exit(1)
    
time = data[:, 0]
resistance = data[:, 1]

temp = resistance - 100 - 1.3
temp = temp/0.425

m, c = np.polyfit(time, temp, 1)

plt.rcParams.update({'font.size': 14}) # Ez megnöveli az összes szöveg méretét a grafikonon

plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='b', label="Hőmérséklet az idő függvényében")
plt.plot(time, c + m*time, linestyle='-', color='r', label=f"Illesztett egyenes: y = {m:.3f}x + {c:.2f}")
plt.title("3. feladat: A termosz hővesztesége az idő függvényében")
plt.xlabel("Idő (s)")
plt.ylabel("Hőmérséklet (°C)")
plt.legend()
plt.tight_layout()
plt.savefig('3_1_graf.pdf')
plt.show()

print(f"A meredekség: {m:.5f}")
print(f"Delta T: {temp[-1] - temp[0]:.4f} °C")
print(f"Delta T egy percre: { (temp[-1] - temp[0]) * 60 / (time[-1] - time[0]) } °C")