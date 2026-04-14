import os
import numpy as np
import matplotlib.pyplot as plt

m_rez = 1.587
m_meleg = 0.436

c_v = 4178
C_termosz = 95
t_hideg = 26.2

t_meleg = 82.3

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'adatok', '8_feladat.csv')

data = np.genfromtxt(filename, delimiter=',', skip_header=0)

time = data[10:, 0]
resistance = data[10:, 1]
temp = (resistance - 100 - 1.7)/0.385

print(f"Kezdeti mert homerseklet: {temp[0]:.2f} C, Vegso: {temp[-1]:.2f} C, t_meleg: {t_meleg:.2f} C, t_hideg: {t_hideg:.2f}")

t_kozos = temp[-1]
c_rez = (c_v * m_meleg * (t_kozos - t_meleg) + C_termosz * (t_kozos - t_meleg)) / (m_rez*(t_hideg - t_kozos))

print( f"rez_fajho: {c_rez:.1f} kJ/kg" )

# Fit line to the first 350 data points
m, c = np.polyfit(time[50:200], temp[50:200], 1)
# Fit line to the final stable tail (from index 1000 to end)
m2, c2 = np.polyfit(time[1000:], temp[1000:], 1)

T1 = m * time[199] + c
T2 = m2 * time[1000] + c2
T_mid = (T1 + T2) / 2

idx_intersect = np.argmin(np.abs(temp[200:1000] - T_mid)) + 200
t_intersect = time[idx_intersect]

T_fit1_intersect = m * t_intersect + c
T_fit2_intersect = m2 * t_intersect + c2

print(f"=====================================")
print(f"Metszespont (T_mid = {T_mid:.2f} C)")
print(f"t_intersect: {t_intersect:.2f} s")
print(f"T1 a t_intersect pillanatban: {T_fit1_intersect:.2f} C")
print(f"T2 a t_intersect pillanatban: {T_fit2_intersect:.2f} C")
print(f"=====================================")

plt.rcParams.update({'font.size': 18})
plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='b', label='Mért hőmérséklet')
plt.plot(time, m * time + c, color='r', linestyle='-', label=f'1. Illesztés (50-200): y={m:.4f}x+{c:.2f}')
plt.plot(time, m2 * time + c2, color='g', linestyle='-', label=f'2. Illesztés (végső szakasz): y={m2:.4f}x+{c2:.2f}')
plt.axhline(y=T_mid, color='black', linestyle='--', label=f'$T_{{mid}}$ = {T_mid:.2f} °C')
plt.axvline(x=t_intersect, color='magenta', linestyle=':', label=f'$t_{{intersect}}$ = {t_intersect:.1f} s')
plt.scatter([t_intersect, t_intersect], [T_fit1_intersect, T_fit2_intersect], color='orange', zorder=5, s=100, label='Illesztett értékek')
plt.xlabel("Ido (s)")
plt.ylabel("Homerseklet (C)")
plt.title(f"8_feladat: Rez fajho merese")
plt.legend(loc='upper right', fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(script_dir, '8_2_graf.pdf'))
plt.show()
