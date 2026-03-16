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
# kezdeti 0us 50mm
time_us_1 = np.array([0, 5.6, 12.0, 17.4, 23.0, 29.2, 34.8, 40.8, 46.6, 52.2, 57.8, 63.8, 69.2])
time_us_2 = np.array([0, 5.6, 11.8, 16.8, 22.8, 28.8, 34.4, 40.6, 45.8, 51.6, 57.8, 63.0, 69.0])
# lehet fel mili hiba ha rosszul olvasom le a skalat

# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 6))

valid_times = []
labels = []
colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd']
markers = ['o-', 's-', '^-', 'D-']

if len(distance_mm) == len(time_us_1) and len(distance_mm) > 1:
    valid_times.append(np.diff(time_us_1))
    labels.append("1. Mérés")

if len(distance_mm) == len(time_us_2) and len(distance_mm) > 1:
    valid_times.append(np.diff(time_us_2))
    labels.append("2. Mérés")

# X tengelyen az intervallumok végét (vagy elejét) is használhatjuk, itt a szakasz vége lesz:
x_dist = distance_mm[1:]

if len(valid_times) > 0:
    # Ábrázoljuk az egyes időkülönbségeket
    for i, diff_arr in enumerate(valid_times):
        plt.plot(x_dist, diff_arr, markers[i % len(markers)], color=colors[i % len(colors)], markersize=6, alpha=0.7, label=labels[i])
        
    # Átlag kiszámítása pontonként a különbségekre
    diff_avg = np.mean(valid_times, axis=0)
    plt.plot(x_dist, diff_avg, '--', color='black', linewidth=2, alpha=0.6, label="Átlagos időkülönbség")

    # Konzolos kiírás a számított átlagos sebességre
    mean_of_diffs = np.mean(diff_avg)
    std_of_diffs = np.std(diff_avg)
    print("--- Eredmények az időkülönbségekből ---")
    print(f"Átlagos időkülönbség 2 mm megtételére: {mean_of_diffs:.4f} ± {std_of_diffs:.4f} us")
    if mean_of_diffs != 0:
        # Sebesség = út / idő = 2 mm / mean_of_diffs us = (2 / mean) * 1000 [m/s]
        v_szamitott = (2.0 / mean_of_diffs) * 1000
        print(f"Számított átlagos sebesség: {v_szamitott:.2f} m/s")
    print("---------------------------------------")

else:
    print("Figyelem: A 'distance_mm' és az idő tömbök mérete nem egyezik, vagy nincsenek adatok megadva.")
    print(f"Kérlek töltsd ki az adatokat helyesen!")


plt.title('Hangsebesség meghatározása\n(Szomszédos mérési pontok időkülönbségei)')
plt.xlabel(r'Távolság (szakasz vége), $s$ [mm]')
plt.ylabel(r'Időkülönbség, $\Delta t_i - \Delta t_{i-1}$ [$\mu$s]')
plt.grid(True, linestyle='--', alpha=0.7)

# Y tengely beállítása úgy, hogy 0-tól induljon, ha akarjuk (de így jobban látszik a szórás)
plt.ylim(0, np.max(valid_times)*1.2 if len(valid_times)>0 else 10)

plt.legend()
plt.tight_layout()

# Kép mentése
plt.savefig('hangsebesseg_meres_diff.pdf')
print("A grafikon sikeresen lementve 'hangsebesseg_meres_diff.pdf' néven.")

plt.show()
