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


# 
# Időkülönbségek (mért adatok) [us] - 3 független mérés
# kezdeti 9.4us 50mm
time_us_1 = np.array([0.0, 15.6, 21.6, 27.8, 33.8, 39.0, 44.6, 50.6, 56.6, 62.4, 68.4, 74.0, 79.4])
# lehet fel mili hiba ha rosszul olvasom le a skalat

# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 6))

# Mért adatok ábrázolása (távolság az x tengelyen, idő az y tengelyen)
plt.plot(distance_mm, time_us_1, 'o', color='#1f77b4', markersize=6, label="1. Mérés")


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
