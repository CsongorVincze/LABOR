import os
import numpy as np
import matplotlib.pyplot as plt

m_hideg = 0.464
m_meleg = 0.467

r_hideg = 110.4
r_meleg = 141.0

c_v = 4178
t_hideg = 

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'adatok', '6_feladat.csv')

data = np.genfromtxt(filename, delimiter=',', skip_header=0)

time = data[:, 0]
resistance = data[:, 1]
temp = (resistance - 100 - 1.7)/0.385

print(temp[0], temp[-1])

C = c_v * (m_meleg * (temp[-1] - temp[0]) + m_hideg * (temp[-1] - t_hideg))/(temp[-1] - temp[-1])

print( f"Termosz hokapacitas: {C}" )

plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='b', label='homerseklet az ido fuggvenyeben')
plt.xlabel("Ido (s)")
plt.ylabel("Homerseklet (C)")
plt.title(f"6_feladat: Termosz hokapacitasanak merese")
plt.legend()
plt.tight_layout()
plt.savefig('6_2_graf.pdf')
plt.show()
