import numpy as np
import matplotlib.pyplot as plt

# Beállítások
plt.rcParams.update({'font.size': 12})

# --- ADATOK ---
deltaT = np.array([3.6, 7.2, 11.4, 15.28, 19.0 ])
P = np.array([1.34, 4.05, 6.78, 9.34, 11.79])
V_peltier = np.array([96.3, 267.8, 444.4, 611.0, 774.0 ]) # Példa adatok (Volt)

# --- ILLESZTÉSEK (NUMPY) ---
# P = a1 * deltaT + b1
a1, b1 = np.polyfit(deltaT, P, 1)
# V_peltier = a2 * deltaT + b2
a2, b2 = np.polyfit(deltaT, V_peltier, 1)

print(f"Illesztés 1: P = {a1:.4f} * deltaT + {b1:.4f}")
print(f"Illesztés 2: V_peltier = {a2:.4f} * deltaT + {b2:.4f}")

# --- PLOT ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# 1. Grafikon: P vs deltaT
ax1.scatter(deltaT, P, color='darkblue', label='Mért P adatok')
deltaT_fit = np.linspace(min(deltaT), max(deltaT), 100)
ax1.plot(deltaT_fit, a1 * deltaT_fit + b1, color='red', label=f'Illesztés: {a1:.3f}x + {b1:.3f}')
ax1.set_xlabel('Hőmérséklet különbség, ΔT [K]')
ax1.set_ylabel('Teljesítmény, P [W]')
ax1.set_title('Peltier-cella: ΔT vs. P')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()

# 2. Grafikon: V_peltier vs deltaT
ax2.scatter(deltaT, V_peltier, color='darkgreen', label='Mért V_peltier adatok')
ax2.plot(deltaT_fit, a2 * deltaT_fit + b2, color='orange', label=f'Illesztés: {a2:.3f}x + {b2:.3f}')
ax2.set_xlabel('Hőmérséklet különbség, ΔT [K]')
ax2.set_ylabel('Peltier feszültség, V_peltier [V]')
ax2.set_title('Peltier-cella: ΔT vs. V_peltier')
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()

plt.tight_layout()
plt.savefig('1_feladat_plot_extended.png')
plt.show()
