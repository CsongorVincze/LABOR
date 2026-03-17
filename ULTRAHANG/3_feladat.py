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
distance_mm = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

time_us_1 = np.array([0, 5.6, 12.0, 17.4, 23.0, 29.2, 34.8, 40.8, 46.6, 52.2, 57.8, 63.8, 69.2])
time_us_2 = np.array([0, 5.6, 11.8, 16.8, 22.8, 28.8, 34.4, 40.6, 45.8, 51.6, 57.8, 63.0, 69.0])

# Egyesítjük az adatokat az illesztéshez (minden pontot felhasználunk)
x_all = np.concatenate((distance_mm, distance_mm)) # Távolság a vízszintes (X) tengelyen [mm]
y_all = np.concatenate((time_us_1, time_us_2))   # Idő a függőleges (Y) tengelyen [us]

# --- LINEÁRIS ILLESZTÉS ---
# y = m*x + b, ahol m a meredekség [us/mm], b a tengelymetszet [us]
p, cov_matrix = np.polyfit(x_all, y_all, 1, cov=True)
m, b = p

# Szórások (hibák) a kovarianciamátrix főátlójából
err_m = np.sqrt(cov_matrix[0, 0])
err_b = np.sqrt(cov_matrix[1, 1])

# Sebesség kiszámítása: v = 1 / m (és konverzió mm/us-ről m/s-ra -> szorzás 1000-rel)
v_ms = (1.0 / m) * 1000

# Hibaterjedés: Delta v = | 1000 / m^2 | * err_m
err_v = abs(1000.0 / (m**2)) * err_m

print("--- Eredmenyek a linearis illesztesbol ---")
print(f"Meredekseg (m): {m:.4f} ± {err_m:.4f} us/mm")
print(f"Tengelymetszet (b): {b:.4f} ± {err_b:.4f} us")
print(f"Hangsebesseg (v): {v_ms:.2f} ± {err_v:.2f} m/s")
print("---------------------------------------")

# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 6))

# Mért adatpontok plotolása
plt.plot(distance_mm, time_us_1, 'bo', label='1. Mérés', markersize=6, alpha=0.7)
plt.plot(distance_mm, time_us_2, 'rs', label='2. Mérés', markersize=6, alpha=0.7)

# Illesztett egyenes plotolása
x_fit = np.linspace(0, np.max(x_all), 100)
y_fit = m * x_fit + b
eq_str = f'Illesztett egyenes\n$t = {m:.3f} \\cdot s {"+" if b >= 0 else "-"} {abs(b):.3f}$'
plt.plot(x_fit, y_fit, 'k--', linewidth=2, label=eq_str)

plt.title('Hangsebesség meghatározása\n(Idő-távolság grafikon)')
plt.xlabel(r'Távolság, $s$ [mm]')
plt.ylabel(r'Idő, $t$ [$\mu$s]')
plt.grid(True, linestyle='--', alpha=0.7)

plt.legend()
plt.tight_layout()

# Kép mentése
plt.savefig('hangsebesseg_meres.pdf')
print("A grafikon sikeresen lementve 'hangsebesseg_meres.pdf' néven.")

# Opcionálisan: plt.show()
