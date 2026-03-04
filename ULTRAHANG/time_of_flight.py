import matplotlib.pyplot as plt
import numpy as np

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

# init dist 16.4mm
# 25mm
# Távolság módosítás [mm]
distance_mm = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

# Repülési idő (Time of flight) [ms]
time_ms_1 = np.array([0.565, 0.571, 0.578, 0.582, 0.588, 0.594, 0.600, 0.606, 0.611, 0.617, 0.623, 0.629, 0.634])
time_ms_2 = np.array([0.564, 0.571, 0.577, 0.582, 0.587, 0.592, 0.599, 0.605, 0.610, 0.616, 0.623, 0.628, 0.633 ])

# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 6))

if len(distance_mm) > 0:
    if len(time_ms_1) == len(distance_mm):
        plt.plot(distance_mm, time_ms_1, 'o', color='#1f77b4', markersize=8, label="1. Mérés")
    if len(time_ms_2) == len(distance_mm):
        plt.plot(distance_mm, time_ms_2, 's', color='#ff7f0e', markersize=8, label="2. Mérés", alpha=0.8)

plt.title('Repülési idő a relatív távolság függvényében')
plt.xlabel(r'Relatív távolság, $\Delta s$ [mm]')
plt.ylabel(r'Repülési idő, $t$ [ms]')
plt.grid(True, linestyle='--', alpha=0.7)

# Csak akkor jelenítjük meg a jelmagyarázatot, ha van mit
if (len(time_ms_1) == len(distance_mm)) or (len(time_ms_2) == len(distance_mm)):
    plt.legend()

plt.tight_layout()

# Kép mentése
plt.savefig('time_of_flight.pdf')
print("A grafikon lementve 'time_of_flight.pdf' néven.")

plt.show()
