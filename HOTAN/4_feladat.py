import numpy as np
import matplotlib.pyplot as plt

V = 7.945 #!ezeket be kell irjad
I = 6.455
C_termosz = 107.5
m_x = 0.774

filename = "5_feladat.csv"
data = np.genfromtxt(filename, delimiter=',', skip_header=0)

time = data[:, 0]
resistance = data[:, 1]
temp = (resistance - 100)/0.385




m, c = np.polyfit(time, temp, 1)
delta_t = time[-1]
delta_T = m * delta_t
c_x = (V*I*delta_t - C_termosz*delta_T)/(m_x*delta_T)

plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='b', label='homerseklet az ido fuggvenyeben')
plt.plot(time, m*time + c, linestyle='-', color='r', label=f'illesztett egyenes: y={m:.4f}x+{c:.4f}')
plt.xlabel("Ido (s)")
plt.ylabel("Homerseklet (C)")
plt.title(f"4_feladat: Futott viz homersekletfuggese a futes ideje alatt, a szamolt fajho: {c_x}")
plt.legend()
plt.tight_layout()
plt.savefig('4_1_graf.pdf')
plt.show()
