import os
import numpy as np
import matplotlib.pyplot as plt

m_hideg = 0.464
m_meleg = 0.467

r_hideg = 110.4
r_meleg = 141.0

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'adatok', '6_feladat.csv')

c_v = 4178
t_hideg = (r_hideg - 100 - 1.3) / 0.425
t_meleg = (r_meleg - 100 - 1.3) / 0.425

data = np.genfromtxt(filename, delimiter=',', skip_header=0)

time = data[:, 0]
resistance = data[:, 1]
temp = (resistance - 100 - 1.3)/0.425

print(f"Kezdeti mert homerseklet: {temp[0]:.2f} C, Vegso: {temp[-1]:.2f} C, t_hideg: {t_hideg:.2f} C, t_meleg: {t_meleg:.2f} C")

t_kozos = temp[-1]
# Termosz hokapacitas (Q_le = Q_fel_v + Q_fel_t)
# m_meleg * c_v * (t_meleg - t_kozos) = m_hideg * c_v * (t_kozos - t_hideg) + C * (t_kozos - t_hideg)
C = c_v * (m_meleg * (t_meleg - t_kozos) - m_hideg * (t_kozos - t_hideg)) / (t_kozos - t_hideg)

print( f"Termosz hokapacitas: {C:.1f} J/K" )

# Thideg = 21.41C
# c_termosz = -163.85
# FIXME: you had issues here before
plt.figure(figsize=(10, 6))
plt.scatter(time, temp, marker='o', color='b', label='homerseklet az ido fuggvenyeben')
plt.xlabel("Ido (s)")
plt.ylabel("Homerseklet (C)")
plt.title(f"6_feladat: Termosz hokapacitasanak merese")
plt.legend()
plt.tight_layout()
plt.savefig('6_1_graf.pdf')
plt.show()