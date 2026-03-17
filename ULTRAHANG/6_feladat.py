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
# kezdeti tavolsag 14.0cm (nagy bizonytalansag) csokkentettuk eredetileg 25nel volt
poz = np.array([25.0, 23.0, 21.0, 19.0, 17.0, 15.0, 13.0, 11.0, 9.0, 7.0, 5.0, 3.0, 1.0])
return_time_ms = np.array([0.916, 0.906, 0.896, 0.886, 0.874, 0.862, 0.850, 0.836, 0.828, 0.816, 0.804, 0.794, 0.782])

# Hangsebesség a 3. feladatból
v_hang = 346.64 # m/s
v_hang_mm_us = v_hang / 1000.0 # mm/us

# Tényleges távolság (kezdeti 14.0 cm = 140 mm, az orsó 25 mm-nél jelentett 0 csökkentést)
actual_dist_mm = 140.0 - (25.0 - poz)

# Becsült távolság az időből: d_est = (v * t) / 2
return_time_us = return_time_ms * 1000.0
estimated_dist_mm = (return_time_us * v_hang_mm_us) / 2.0

# --- LINEÁRIS ILLESZTÉS ---
m, b = np.polyfit(actual_dist_mm, estimated_dist_mm, 1)

print("--- Eredmenyek a linearis illesztesbol (6. feladat) ---")
print(f"Meredekseg (m): {m:.4f}")
print(f"Tengelymetszet (b): {b:.4f} mm")
print("-----------------------------------------------------")

# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 6))

plt.plot(actual_dist_mm, estimated_dist_mm, 'bo', label='Adatpontok', markersize=6, alpha=0.7)

x_fit = np.linspace(min(actual_dist_mm) - 2, max(actual_dist_mm) + 2, 100)
y_fit = m * x_fit + b
eq_str = f'Illesztett egyenes\n$d_{{est}} = {m:.3f} \\cdot d_{{act}} {"+" if b >= 0 else "-"} {abs(b):.1f}$'
plt.plot(x_fit, y_fit, 'k--', linewidth=2, label=eq_str)

plt.title('Becsült távolság a rögzített (tényleges) távolság függvényében')
plt.xlabel(r'Beállított tényleges távolság, $d_{act}$ [mm]')
plt.ylabel(r'Impulzus-időből becsült távolság, $d_{est}$ [mm]')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Kép mentése
plt.savefig('return_time_vs_poz.pdf')
print("A grafikon sikeresen lementve 'return_time_vs_poz.pdf' néven.")