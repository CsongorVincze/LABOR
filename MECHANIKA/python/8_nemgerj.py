import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import os

# Fájl elérési útjának beállítása
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, '..', 'csv', '8_nemgerj.csv')

try:
    df = pd.read_csv(filename)
except Exception as e:
    print(f"Hiba a fájl beolvasásakor: {e}")
    exit(1)

# Üres mezők kiszűrése
df = df.dropna(subset=['Time', 'Position'])

# Az első 4 másodperc levágása
df = df[df['Time'] >= 4.0]

time = df['Time'].values
pos = df['Position'].values

# Csúcsok (lokális maximumok) megkeresése
# prominence: minimális kiemelkedés a zaj kiszűrésére
peaks, _ = find_peaks(pos, distance=5, prominence=0.002)

if len(peaks) > 1:
    periods = np.diff(time[peaks])
    avg_period = np.mean(periods)
    eigenfrequency = 1.0 / avg_period
else:
    avg_period = np.nan
    eigenfrequency = np.nan

print(f"Mért átlagos periódusidő: {avg_period:.5f} s")
print(f"Számított sajátfrekvencia: {eigenfrequency:.5f} Hz")

if len(peaks) > 2:
    t_peaks = time[peaks]
    pos_peaks = pos[peaks]
    t_shifted = t_peaks - t_peaks[0]
    
    def exp_decay(t, A0, beta, C):
        return A0 * np.exp(-beta * t) + C
        
    C_guess = np.mean(pos) # Az egyensúlyi helyzet a jel átlaga környékén van
    A0_guess = pos_peaks[0] - C_guess
    beta_guess = 0.5
    
    try:
        popt, pcov = curve_fit(exp_decay, t_shifted, pos_peaks, p0=[A0_guess, beta_guess, C_guess])
        A0_fit, beta_fit, C_fit = popt
        omega_0 = 2 * np.pi * eigenfrequency
        Q_fit = omega_0 / (2 * beta_fit)
        
        print(f"Csillapítási tényező (beta): {beta_fit:.5f} 1/s")
        print(f"Jósági tényező (Q): {Q_fit:.2f}")
    except Exception as e:
        print(f"Hiba a burkológörbe illesztésekor: {e}")
        beta_fit = None
else:
    beta_fit = None

# Globális betűméret beállítása
plt.rcParams.update({'font.size': 18})

plt.figure(figsize=(12, 6))

plt.plot(time, pos, label="Szabad rezgés", color='b')
if len(peaks) > 1:
    plt.plot(time[peaks], pos[peaks], "rx", markersize=8, label=f"Csúcsok (f_saját = {eigenfrequency:.3f} Hz)")
else:
    plt.plot(time[peaks], pos[peaks], "rx", markersize=8, label="Csúcsok")

if 'beta_fit' in locals() and beta_fit is not None:
    t_plot = np.linspace(min(time), max(time), 500)
    env_plot = exp_decay(t_plot - t_peaks[0], A0_fit, beta_fit, C_fit)
    plt.plot(t_plot, env_plot, 'g--', linewidth=2, label=fr"Burkológörbe ($\beta = {beta_fit:.3f}$, $Q = {Q_fit:.1f}$)")

plt.title('8. feladat - Szabad rezgés vizsgálata')
plt.xlabel('Idő [s]')
plt.ylabel('Pozíció [m]')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Kép mentése
images_dir = os.path.join(script_dir, '..', 'images')
os.makedirs(images_dir, exist_ok=True)
plt.savefig(os.path.join(images_dir, '8_nemgerj.png'))

plt.show()
