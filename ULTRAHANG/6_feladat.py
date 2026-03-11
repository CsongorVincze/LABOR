import numpy as np
import matplotlib.pyplot as plt
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
# kezdeti tavolsag 14.0cm (nagy bizonytalansag) csokkentettuk eredetileg 25nel volt
poz = np.array([25.0, 23.0, 21.0, 19.0, 17.0, 15.0, 13.0, 11.0, 9.0, 7.0, 5.0, 3.0, 1.0])
return_time = np.array([0.916, 0.906, 0.896, 0.886, 0.874, 0.862, 0.850, 0.836, 0.828, 0.816, 0.804, 0.794, 0.782])

# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 6))

if len(poz) == len(return_time) and len(poz) > 0:
    # Ábrázoljuk a mérést
    plt.plot(poz, return_time, 'o', color='#1f77b4', markersize=6, label="Mért adat (Impulzus-visszhang)")
    
    # Egyenes illesztése y = a*x + b alakban
    def linear_model(x, a, b):
        return a * x + b
    
    if len(poz) > 1:
        # Illesztés a scipy.optimize.curve_fit fv-nyel
        popt, pcov = opt.curve_fit(linear_model, poz, return_time)
        a, b = popt
        perr = np.sqrt(np.diag(pcov)) # a paraméterek hibája
        
        # Illesztett pontok generálása az ábrához
        p_fit = np.linspace(min(poz), max(poz), 100)
        t_fit = linear_model(p_fit, a, b)
        
        # Megformázzuk a hiba feliratot
        eq_label = rf'Illesztett egyenes: $t = {a:.4f} \cdot x {b:+.4f}$'
        plt.plot(p_fit, t_fit, '-', color='#ff7f0e', linewidth=2, label=eq_label)
        
        # Eredmény kiírása a konzolra
        print(f"--- Illesztés eredményei (Impulzus-visszhang) ---")
        print(f"Meredekség (a): {a:.5f} ± {perr[0]:.5f} ms/cm (?) (A pontos SI átváltás a feladat egységeitől függ)")
        print(f"Y-metszet (b): {b:.4f} ± {perr[1]:.4f}")
        
        if a != 0:
            # Impulzus visszhangnál az út 2*x, tehát a sebesség: v = 2 * (x / t) => v = 2 * (1 / a)
            # Tegyük fel játéknak: ha poz [cm] és idő [ms] -> 1 cm/ms = 10 m/s => v = 2 / a * 10 [m/s]
            v_szamitott = abs((2.0 / a) * 10)
            error_perc = (perr[0] / abs(a)) * 100
            print(f"Számított sebesség impulzus-visszhangra (ha poz[cm], idő[ms]): {v_szamitott:.2f} m/s (± {error_perc:.2f}%)")
        print("----------------------------")
else:
    print("Figyelem: A 'poz' és a 'return_time' tömbök mérete nem egyezik, vagy üresek.")
    print(f"Kérlek ellenőrizd az adatokat!")


plt.title('Visszaérkezési idő a pozíció függvényében (Impulzus-visszhang)')
plt.xlabel(r'Pozíció, $x$ [cm / mm]')
plt.ylabel(r'Visszaérkezési idő, $t$ [ms / $\mu$s]')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Kép mentése
plt.savefig('return_time_vs_poz.pdf')
print("A grafikon sikeresen lementve 'return_time_vs_poz.pdf' néven.")

plt.show()