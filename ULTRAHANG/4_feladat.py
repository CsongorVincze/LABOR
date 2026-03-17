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

# Rendezzük sorba távolság szerint (maximumok sorszámozásához)
poz_sorted = np.sort(poz)
n_max = np.arange(1, len(poz_sorted) + 1)

# --- LINEÁRIS ILLESZTÉS ---
# Távolság = m * (maximum sorszáma) + b, ahol m adja meg a félhullámhosszt (lambda / 2)
p, cov_matrix = np.polyfit(n_max, poz_sorted, 1, cov=True)
m, b = p

err_m = np.sqrt(cov_matrix[0, 0])
err_b = np.sqrt(cov_matrix[1, 1])

f_rez = 40.81  # Később a jegyzőkönyv szerint: rezonanciafrekvencia 40.81 kHz
err_f_rez = 0.01 # Becsült leolvasási hibája a függvénygenerátornak

lambda_mm = 2 * m
err_lambda = 2 * err_m

v_ms = lambda_mm * f_rez 
# Hibaterjedés: (Delta v / v)^2 = (Delta lambda / lambda)^2 + (Delta f / f)^2
err_v_ms = v_ms * np.sqrt((err_lambda / lambda_mm)**2 + (err_f_rez / f_rez)**2)

print("--- Eredmenyek a linearis illesztesbol (4. feladat) ---")
print(f"Meredekseg (lambda/2): {m:.4f} +/- {err_m:.4f} mm")
print(f"Hullamhossz (lambda): {lambda_mm:.4f} +/- {err_lambda:.4f} mm")
print(f"Kiszamitott hangsebesseg (f = {f_rez} +/- {err_f_rez} kHz eseten): {v_ms:.2f} +/- {err_v_ms:.2f} m/s")
print("-----------------------------------------------------")

# --- 1. ÁBRÁZOLÁS: Amplitúdó - Pozíció ---
plt.figure(figsize=(7, 5))
plt.plot(poz, amp, 'o', color='#d62728', markersize=8, label="Mért adatok")
plt.title('Amplitúdó a pozíció függvényében')
plt.xlabel(r'Pozíció, $x$ [mm]')
plt.ylabel(r'Amplitúdó csúcsértéke, $U_{pp}$ [mV]')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('amp_vs_poz.pdf')
plt.close()

# --- 2. ÁBRÁZOLÁS: Pozíció - Maximum sorszáma ---
plt.figure(figsize=(7, 5))
plt.plot(n_max, poz_sorted, 'bo', label='Mért pozíciók', markersize=8, alpha=0.7)

n_fit = np.linspace(0, np.max(n_max) + 1, 100)
poz_fit = m * n_fit + b
eq_str = f'Illesztett egyenes\n$x = {m:.3f} \\cdot n {"+" if b >= 0 else "-"} {abs(b):.3f}$'
plt.plot(n_fit, poz_fit, 'k--', linewidth=2, label=eq_str)

plt.title('Maximumhelyek pozíciója az állóhullámban')
plt.xlabel('Maximum sorszáma, $n$')
plt.ylabel(r'Pozíció, $x$ [mm]')
plt.xticks(n_max)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('poz_vs_n_max.pdf')
plt.close()

print("A grafikonok sikeresen lementve 'amp_vs_poz.pdf' és 'poz_vs_n_max.pdf' néven.")