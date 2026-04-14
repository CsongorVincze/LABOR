import os
import numpy as np
import matplotlib.pyplot as plt

m_jeg = 0.033
m_meleg = 0.477

c_v = 4178
C_termosz = 95


t_meleg = 93.24

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'adatok', '9_b_feladat.csv')

data = np.genfromtxt(filename, delimiter=',', skip_header=0)

time = data[3900:, 0] - data[3900, 0]
resistance = data[3900:, 1]
temp = (resistance - 100 - 1.7)/0.385

print(f"Kezdeti mert homerseklet: {temp[0]:.2f} C, Vegso: {temp[-1]:.2f} C, t_meleg: {t_meleg:.2f} C")

t_kozos = temp[-1]
L_j = (c_v*m_meleg*(t_meleg - temp[-1]) - c_v*m_jeg*temp[-1] + C_termosz*(t_meleg-temp[-1]))/(m_jeg*1000)

print( f"jeg_olvadasho: {L_j:.1f} kJ/kg" )

plt.rcParams.update({'font.size': 18})
plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='b', label='homerseklet az ido fuggvenyeben')
plt.xlabel("Ido (s)")
plt.ylabel("Homerseklet (C)")
plt.title(f"9_feladat: Jeg olvadasho")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(script_dir, '9_1_graf.pdf'))
plt.show()
