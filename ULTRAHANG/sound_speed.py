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
distance_mm = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

# Időkülönbségek (mért adatok) [us] - 3 független mérés
time_us_1 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
time_us_2 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
time_us_3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 6))

# Mért adatok ábrázolása (távolság az x tengelyen, idő az y tengelyen)
plt.plot(distance_mm, time_us_1, 'o', color='#1f77b4', markersize=6, label="1. Mérés")
plt.plot(distance_mm, time_us_2, 's', color='#ff7f0e', markersize=6, label="2. Mérés", alpha=0.8)
plt.plot(distance_mm, time_us_3, '^', color='#2ca02c', markersize=6, label="3. Mérés", alpha=0.8)

plt.title('Hangsebesség meghatározása\n(Távolság - Idő grafikon)')
plt.xlabel(r'Távolság, $s$ [mm]')
plt.ylabel(r'Időkülönbség, $\Delta t$ [$\mu$s]')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Kép mentése
plt.savefig('hangsebesseg_meres.pdf')
print("A grafikon sikeresen lementve 'hangsebesseg_meres.pdf' néven.")

plt.show()
