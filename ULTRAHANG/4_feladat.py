import numpy as np
import matplotlib.pyplot as plt

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
poz = np.array([24.34, 19.25, 15.42, 11.17, 6.12, 2.32])
amp = np.array([772.5, 799.0, 845.5, 868.5, 887.5, 931.5])

# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 6))
plt.plot(poz, amp, 'o', color='#d62728', markersize=8, label="Mért adatok")

plt.title('Amplitúdó a pozíció függvényében')
plt.xlabel(r'Pozíció, $x$ [mm]')
plt.ylabel(r'Amplitúdó csúcsértéke, $U_{pp}$ [mV]')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Kép mentése
plt.savefig('amp_vs_poz.pdf')
print("A grafikon sikeresen lementve 'amp_vs_poz.pdf' néven.")

plt.show()