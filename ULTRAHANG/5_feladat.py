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
# az ado es a vevo tavolsaga 11.0cm
poz = np.array([25.0, 23.0, 21.0, 19.0, 17.0, 15.0, 13.0, 11.0, 9.0, 7.0, 5.0, 3.0, 1.0])
time_diff_1 = np.array([0.391, 0.386, 0.380, 0.374, 0.368, 0.362, 0.357, 0.351, 0.345, 0.339, 0.333, 0.327, 0.322])
time_diff_2 = np.array([0.391, 0.386, 0.380, 0.374, 0.368, 0.363, 0.357, 0.351, 0.345, 0.340, 0.334, 0.328, 0.322])


# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 6))

valid_times = []
labels = []
colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd']
markers = ['o', 's', '^', 'D']

if len(poz) == len(time_diff_1) and len(poz) > 0:
    valid_times.append(time_diff_1)
    labels.append("1. Mérés")

if len(poz) == len(time_diff_2) and len(poz) > 0:
    valid_times.append(time_diff_2)
    labels.append("2. Mérés")

if len(valid_times) > 0:
    # Ábrázoljuk az egyes méréseket
    for i, t_arr in enumerate(valid_times):
        plt.plot(poz, t_arr, markers[i % len(markers)], color=colors[i % len(colors)], markersize=6, alpha=0.7, label=labels[i])
        
    # Átlag kiszámítása pontonként
    time_avg = np.mean(valid_times, axis=0)

    # Egyenes illesztése y = a*x + b alakban
    def linear_model(x, a, b):
        return a * x + b
    
    if len(poz) > 1:
        # Illesztés a scipy.optimize.curve_fit fv-nyel az átlagra
        popt, pcov = opt.curve_fit(linear_model, poz, time_avg)
        a, b = popt
        perr = np.sqrt(np.diag(pcov)) # a paraméterek hibája
        
        # Illesztett pontok generálása az ábrához
        p_fit = np.linspace(min(poz), max(poz), 100)
        t_fit = linear_model(p_fit, a, b)
        
        # Megformázzuk a hiba feliratot
        if len(valid_times) > 1:
            eq_label = f'Illesztett egyenes (átlagra): $\Delta t = {a:.4f} \cdot s {b:+.4f}$'
        else:
            eq_label = f'Illesztett egyenes: $\Delta t = {a:.4f} \cdot s {b:+.4f}$'
            
        plt.plot(p_fit, t_fit, '-', color='#ff7f0e', linewidth=2, label=eq_label)
        
        # Eredmény kiírása a konzolra
        print(f"--- Illesztés eredményei ({len(valid_times)} mérés{' átlagára' if len(valid_times)>1 else ''}) ---")
        print(f"Meredekség (a): {a:.5f} ± {perr[0]:.5f} ms/cm (vagy s/m stb, mert az egység nem volt megadva)")
        print(f"Y-metszet (b): {b:.4f} ± {perr[1]:.4f}")
        
        # Sebesség számítása, ha a poz [cm]-ben és az idő [ms]-ben van:
        # v = 1/a -> cm/ms = 10 m/s szorzó, de a feladat egységei alapján érdemes megnézni
        if a != 0:
            # Tegyük fel játéknak: ha poz [cm] és idő [ms] -> 1 cm/ms = 10 m/s
            v_szamitott = abs((1.0 / a) * 10)
            error_perc = (perr[0] / abs(a)) * 100
            print(f"Számított sebesség (ha poz[cm], idő[ms]): {v_szamitott:.2f} m/s (± {error_perc:.2f}%)")
        print("----------------------------")
else:
    print("Figyelem: A 'poz' és az idő tömbök mérete nem egyezik, vagy üresek.")
    print(f"Kérlek töltsd ki az adatokat helyesen!")

plt.title('Idő a pozíció függvényében')
plt.xlabel(r'Pozíció, $x$ [cm / mm]')
plt.ylabel(r'Idő, $t$ [ms / $\mu$s]')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Kép mentése
plt.savefig('ido_vs_poz.pdf')
print("A grafikon sikeresen lementve 'ido_vs_poz.pdf' néven.")

plt.show()