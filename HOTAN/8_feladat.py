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
filename = os.path.join(script_dir, 'adatok', '8_faladat.csv')

data = np.genfromtxt(filename, delimiter=',', skip_header=0)

time = data[:, 0]
resistance = data[:, 1]
temp = (resistance - 100 - 1.7)/0.385

print(f"Kezdeti mert homerseklet: {temp[0]:.2f} C, Vegso: {temp[-1]:.2f} C, t_meleg: {t_meleg:.2f} C, t_hideg: {t_hideg:.2f}")

t_kozos = temp[-1]
c_rez = (c_v * m_meleg * (t_kozos - t_meleg) + C_termosz * (t_kozos - t_meleg)) / (m_alu*(t_hideg - t_kozos))

print( f"alu_fajho: {c_rez:.1f} kJ/kg" )

plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='b', label='homerseklet az ido fuggvenyeben')
plt.xlabel("Ido (s)")
plt.ylabel("Homerseklet (C)")
plt.title(f"8_feladat: Rez fajho merese")
plt.legend()
plt.tight_layout()
plt.savefig('8_1_graf.pdf')
plt.show()
