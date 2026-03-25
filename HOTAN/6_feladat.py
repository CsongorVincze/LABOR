import os
import numpy as np
import matplotlib.pyplot as plt

m_hideg = 0.464
m_meleg = 0.467

r_hideg = 110.4
r_meleg = 141.0

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'adatok', '6_feladat.csv')

data = np.genfromtxt(filename, delimiter=',', skip_header=0)

time = data[:, 0]
resistance = data[:, 1]
temp = (resistance - 100 - 1.3)/0.425

print(temp[0], temp[-1])

plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='b', label='homerseklet az ido fuggvenyeben')
plt.xlabel("Ido (s)")
plt.ylabel("Homerseklet (C)")
plt.title(f"5_feladat: Termosz hokapacitasanak merese")
plt.legend()
plt.tight_layout()
plt.savefig('5_1_graf.pdf')
plt.show()
