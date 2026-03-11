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
# lehet fel mili hiba ha rosszul olvasom le a skalat

# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 6))

# Csak akkor ábrázoljuk és illesztünk, ha a tömbök mérete azonos és nem üresek
if len(distance_mm) == len(time_us_1) and len(distance_mm) > 0:
    # Mért adatok ábrázolása (távolság az x tengelyen, idő az y tengelyen)
    plt.plot(distance_mm, time_us_1, 'o', color='#1f77b4', markersize=6, label="1. Mérés")

    # Egyenes illesztése y = a*x + b alakban
    def linear_model(x, a, b):
        return a * x + b
    
    if len(distance_mm) > 1:
        # Illesztés a scipy.optimize.curve_fit fv-nyel
        popt, pcov = opt.curve_fit(linear_model, distance_mm, time_us_1)
        a, b = popt
        perr = np.sqrt(np.diag(pcov)) # a paraméterek hibája
        
        # Illesztett pontok generálása az ábrához
        d_fit = np.linspace(min(distance_mm), max(distance_mm), 100)
        t_fit = linear_model(d_fit, a, b)
        
        # Megformázzuk a hiba feliratot (opcionális, de hasznos)
        eq_label = f'Illesztett egyenes: $\Delta t = {a:.3f} \cdot s {b:+.3f}$'
        plt.plot(d_fit, t_fit, '-', color='#ff7f0e', label=eq_label)
        
        # Eredmény kiírása a konzolra
        print("--- Illesztés eredményei ---")
        print(f"Meredekség (a): {a:.4f} ± {perr[0]:.4f} us/mm")
        print(f"Y-metszet (b): {b:.4f} ± {perr[1]:.4f} us")
        if a != 0:
            # Sebesség [m/s]-ban. (1 mm/us = 1000 m/s)
            v_szamitott = (1.0 / a) * 1000
            error_perc = (perr[0] / abs(a)) * 100
            print(f"Számított sebesség (1/a): {v_szamitott:.2f} m/s (± {error_perc:.2f}%)")
        print("----------------------------")
else:
    print("Figyelem: A 'distance_mm' és 'time_us_1' tömbök mérete nem egyezik, vagy üresek.")
    print(f"distance_mm hossza: {len(distance_mm)}, time_us_1 hossza: {len(time_us_1)}. Kérlek töltsd ki az adatokat!")


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
