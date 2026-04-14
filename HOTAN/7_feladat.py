import os
import numpy as np
import matplotlib.pyplot as plt

m_alu = 0.534
m_meleg = 0.415
# 134.4C meleg
r_hideg = 110.29
r_meleg = 134.45

c_v = 4178
C_termosz = 95
t_hideg = 25.45
t_meleg = (r_meleg - 100 - 1.7)/0.385

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'adatok', '7_feladat.csv')

data = np.genfromtxt(filename, delimiter=',', skip_header=0)

time = data[:, 0]
resistance = data[:, 1]
temp = (resistance - 100 - 1.7)/0.385

print(f"Kezdeti mert homerseklet: {temp[0]:.2f} C, Vegso: {temp[-1]:.2f} C, t_meleg: {t_meleg:.2f} C, t_hideg: {t_hideg:.2f}")

t_kozos = temp[-1]
c_alu = (c_v * m_meleg * (t_kozos - t_meleg) + C_termosz * (t_kozos - t_meleg)) / (m_alu*(t_hideg - t_kozos))

print( f"alu_fajho: {c_alu:.1f} kJ/kg" )

plt.rcParams.update({'font.size': 18})
plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='b', label='homerseklet az ido fuggvenyeben')
plt.xlabel("Ido (s)")
plt.ylabel("Homerseklet (C)")
plt.title(f"7_feladat: Aluminium fajho merese")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(script_dir, '7_1_graf.pdf'))
plt.show()
