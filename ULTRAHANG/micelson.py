import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

# --- BEÁLLÍTÁSOK ---
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "axes.titlesize": 16,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "legend.fontsize": 12,
    "grid.linewidth": 0.5,
})

# --- ADATOK ---
# Távolságok a napló alapján [mm]
distance_mm = np.array([22, 18, 10, 5 ])

# Időkülönbségek (mért adatok) [us] - 3 független mérés
amp_mV_2 = np.array([3.4, 3.4, 3.6, 4.5,])
# init dist 13.9mm




# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 6))

# Mért adatok ábrázolása (távolság az x tengelyen, amplitúdó az y tengelyen)
plt.plot(distance_mm, amp_mV_1, 'o', color='#1f77b4', markersize=6, label="1. Mérés")
plt.plot(distance_mm, amp_mV_2, 's', color='#ff7f0e', markersize=6, label="2. Mérés", alpha=0.8)
plt.plot(distance_mm, amp_mV_3, '^', color='#2ca02c', markersize=6, label="3. Mérés", alpha=0.8)

plt.title('Amplitúdó - Távolság grafikon')
plt.xlabel(r'Távolság, $s$ [mm]')
plt.ylabel(r'Amplitúdó, $U$ [mV]')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Kép mentése
plt.savefig('amplitudo_meres.pdf')
print("A grafikon sikeresen lementve 'amplitudo_meres.pdf' néven.")

# --- MÁSODIK ÁBRA (Precízebb mérési pontok) ---
plt.figure(figsize=(8, 6))

plt.plot(prec_dist, prec_amp_mV, 'D', color='#d62728', markersize=6, label="Precíz mérés")

plt.title('Amplitúdó - Távolság grafikon (Precíz mérés)')
plt.xlabel(r'Távolság, $s$ [mm]')
plt.ylabel(r'Amplitúdó, $U$ [mV]')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Kép mentése
plt.savefig('amplitudo_preciz.pdf')
print("A grafikon sikeresen lementve 'amplitudo_preciz.pdf' néven.")

plt.show()
