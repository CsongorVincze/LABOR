import os
import numpy as np
import matplotlib.pyplot as plt

V = 7.945 #!ezeket be kell irjad
I = 6.455
C_termosz = 107.5
m_x = 0.774

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'adatok', '5_feladat.csv')

data = np.genfromtxt(filename, delimiter=',', skip_header=0)

time = data[:, 0]
resistance = data[:, 1]
temp = (resistance - 100 - 1.3)/0.425

# Filter data between 70s and 650s for the fitting
mask = (time >= 70) & (time <= 650)
time_fit = time[mask]
temp_fit = temp[mask]

m, c = np.polyfit(time_fit, temp_fit, 1)
delta_t = time[-1]
delta_T = m * delta_t
c_x = (V*I*delta_t - C_termosz*delta_T)/(m_x*delta_T)

print(f"viz szamolt fajho: {c_x}")
print(f"kezdeti homerseklet: {temp[0]}")
print(f"vegso homerseklet: {temp[-1]}")

plt.rcParams.update({'font.size': 18})
plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='b', label='Mért hőmérséklet')
plt.plot(time, m*time + c, linestyle='-', color='r', label=f'Illesztett egyenes: y={m:.4f}x+{c:.4f}')
plt.xlabel("Idő (s)")
plt.ylabel("Hőmérséklet (°C)")
plt.title(f"Fűtött víz hőmérsékletfüggése a fűtés ideje alatt\nA számolt fajhő: {c_x:.0f} J/kgK")
plt.legend()
plt.tight_layout()
plt.savefig('4_1_graf.pdf')
plt.show()
