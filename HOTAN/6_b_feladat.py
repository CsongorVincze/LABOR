import os
import numpy as np
import matplotlib.pyplot as plt

m_hideg = 0.294 #830g
m_meleg = 0.406
# 134.4C meleg
r_hideg = 110.29
r_meleg = 134.45

c_v = 4178
t_hideg = (r_hideg - 100 - 1.7)/0.385
t_meleg = (r_meleg - 100 - 1.7)/0.385

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'adatok', '6_b_faladat.csv')

data = np.genfromtxt(filename, delimiter=',', skip_header=0)

time = data[:, 0]
resistance = data[:, 1]
temp = (resistance - 100 - 1.7)/0.385

print(f"Kezdeti mert homerseklet: {temp[0]:.2f} C, Vegso: {temp[-1]:.2f} C, t_meleg: {t_meleg:.2f} C, t_hideg: {t_hideg:.2f}")

t_kozos = temp[-1]
C = c_v * (m_meleg * (t_meleg - t_kozos) - m_hideg * (t_kozos - t_hideg)) / (t_kozos - t_hideg)

print( f"Termosz hokapacitas: {C:.1f} J/K" )

plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='b', label='homerseklet az ido fuggvenyeben')
plt.xlabel("Ido (s)")
plt.ylabel("Homerseklet (C)")
plt.title(f"6_feladat: Termosz hokapacitasanak merese")
plt.legend()
plt.tight_layout()
plt.savefig('6_2_graf.pdf')
plt.show()
