import matplotlib.pyplot as plt
import numpy as np

# --- BEÁLLÍTÁSOK ---
# Opcionálisan beállíthatunk szép, magyar nyelvű és tudományos kinézetű grafikonokat
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

# --- 1. MÉRÉS: Széles frekvenciasáv mérése ---
# Adatok az 1. táblázatból
freq_1 = np.array([1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 51.9, 55, 60, 65, 70, 75, 80, 85, 90, 93.5, 95, 100])
amp_1 = np.array([0, 0, 0, 0, 0, 0, 0, 3, 183, 15, 12, 19, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1])

# --- 2. MÉRÉS: Rezonanciafrekvencia körüli sűrűbb mérés ---
# Adatok a 2. táblázatból
freq_2 = np.array([38.0, 39.0, 39.2, 39.4, 39.6, 39.8, 40.0, 40.2, 40.23, 40.25, 40.26, 40.27, 40.28, 40.29, 40.3, 40.4, 40.5, 41.0])
amp_2 = np.array([32.8, 70.2, 82.1, 99.0, 121.3, 148.4, 160.2, 176.6, 173.3, 178.8, 178.3, 179.1, 178.6, 179.0, 176.6, 174.4, 16.3, 152.4])


# --- ÁBRÁZOLÁS ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 1. Grafikon: Széles sáv
ax1.plot(freq_1, amp_1, 'o', color='#1f77b4', markersize=6, label="Mért pontok")
ax1.set_title('Átviteli karakterisztika (Széles tartomány)')
ax1.set_xlabel('Frekvencia [kHz]')
ax1.set_ylabel('Amplitúdó [mV]')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()

# 2. Grafikon: Rezonancia körül
ax2.plot(freq_2, amp_2, 'rs', markersize=6, label="Mért pontok")
# Megjegyzés: A 40.5 kHz-nél lévő 16.3 mV valószínűleg egy elírás a naplóban (pl. 163 helyett).
ax2.set_title('Átviteli karakterisztika (Rezonancia körül)')
ax2.set_xlabel('Frekvencia [kHz]')
ax2.set_ylabel('Amplitúdó [mV]')
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()

plt.tight_layout()

# Mentés PDF formátumban (kiváló a LaTeX-be történő beillesztéshez)
plt.savefig('atviteli_karakterisztika.pdf')
print("A grafikon sikeresen lementve 'atviteli_karakterisztika.pdf' néven.")

# Eredmény megjelenítése
plt.show()

