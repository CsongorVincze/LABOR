import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import os
import glob
import warnings

# Címtárak beállítása
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_dir = os.path.join(script_dir, '..', 'csv')
images_dir = os.path.join(script_dir, '..', 'images')
os.makedirs(images_dir, exist_ok=True)

# Összes 10-es feladathoz tartozó csv kikeresése
file_pattern = os.path.join(csv_dir, '10_*.csv')
files = glob.glob(file_pattern)

# (A modellt helyileg definiáljuk a cikluson belül, hogy az extrapolációhoz pontosan rögzítsük a t0 eltolást)

plt.rcParams.update({'font.size': 16})

for file in files:
    basename = os.path.basename(file)
    print(f"\n--- Fájl feldolgozása: {basename} ---")
    
    try:
        df = pd.read_csv(file)
        valid_data = ~df['Position'].isna() & ~df['Time'].isna()
        t_full = df.loc[valid_data, 'Time'].values
        pos_full = df.loc[valid_data, 'Position'].values
        
        if len(pos_full) < 100:
            print("Nincs elég adat a fájlban.")
            continue
            
        # 1. Lépés: Kezdeti becslés a TELJES ADATSORON, hogy legyen elég csúcsunk a frekvenciabecsléshez!
        peaks_all, _ = find_peaks(pos_full, distance=3, prominence=0.001)
        if len(peaks_all) < 10:
            print("Nem található elég csúcs.")
            continue
            
        t_peaks_all = t_full[peaks_all]
        pos_peaks_all = pos_full[peaks_all]
        t_max = t_full[peaks_all[np.argmax(pos_full[peaks_all])]]
        
        prom_guess = (np.max(pos_peaks_all) - np.min(pos_peaks_all)) * 0.2
        beat_maxima_idx, _ = find_peaks(pos_peaks_all, prominence=prom_guess, distance=10)
        
        if len(beat_maxima_idx) > 1:
            T_beat_guess = np.mean(np.diff(t_peaks_all[beat_maxima_idx]))
            f_beat_guess = 1.0 / T_beat_guess
        else:
            f_beat_guess = 0.5  # Tartalék becslés ha csak 1 lebegés van
            
        # 2. Lépés: Adatok megvágása (CSAK AZ ILLESZTÉSHEZ)
        # Az ablakot egy kicsit nagyobbra (12 mp) hagyjuk, hogy stabilabb legyen az illesztés
        window = (t_full >= t_max - 0.5) & (t_full <= t_max + 12.0)
        t_fit = t_full[window]
        pos_fit = pos_full[window]
        
        # A megvágott oszcilláció csúcsainak megkeresése (erre illesztünk)
        peaks, _ = find_peaks(pos_fit, distance=3, prominence=0.001)
        if len(peaks) < 5:
            print("Nem található elég csúcs a burkológörbéhez az ablakban.")
            continue
            
        t_peaks = t_fit[peaks]
        pos_peaks = pos_fit[peaks]
        
        # Modell definiálása rögzített t0-val
        t0 = t_peaks[0]
        def envelope_model_local(t, A, f_beat, phi, C, beta):
            t_shifted = t - t0
            return A * np.exp(-beta * t_shifted) * np.cos(2 * np.pi * f_beat * t + phi) + C
            
        C_guess = pos_peaks[-1] 
        A_guess = np.max(pos_peaks) - C_guess
        phi_guess = 0.0
        beta_guess = 0.5 
        
        # 3. Lépés: Görbeillesztés
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            popt, pcov = curve_fit(
                envelope_model_local, t_peaks, pos_peaks, 
                p0=[A_guess, f_beat_guess, phi_guess, C_guess, beta_guess],
                bounds=([0, 0, -np.inf, -np.inf, 0], [np.inf, np.inf, np.inf, np.inf, np.inf])
            )
                               
        A_fit, f_beat_fit, phi_fit, C_fit, beta_fit = popt
        
        # 4. Lépés: A feladatlap szerinti f_L és T_L kiszámítása
        # f_L = (f_1 - f_2) / 2.  A lebegés (buckák) frekvenciája f_beat = f_1 - f_2.
        # Tehát f_L = f_beat / 2
        f_L = f_beat_fit / 2.0
        T_L = 1.0 / f_L
        
        print(f"Lebegés csúcsainak sűrűsége (f_beat): {f_beat_fit:.4f} Hz")
        print(f"-> Burkoló szinuszgörbe frekvenciája (f_L) : {f_L:.4f} Hz")
        print(f"-> Burkoló szinuszgörbe periódusideje (T_L): {T_L:.4f} s")
        print(f"-> Amplitúdó (A)       : {A_fit:.5f} m")
        print(f"-> Állandósult szint(C): {C_fit:.5f} m")
        print(f"-> Fázis (phi)         : {phi_fit:.4f} rad")
        print(f"-> Csillapítás (beta)  : {beta_fit:.4f} 1/s")
        
        # 5. Lépés: Ábrázolás (2 részplotos ábra)
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)
        
        # --- FELSŐ ÁBRA: Eredeti jel és burkoló ---
        ax1.plot(t_full, pos_full, color='gray', alpha=0.4, label='Teljes mért jel (oszcilláció)')
        ax1.plot(t_peaks, pos_peaks, 'r.', markersize=8, label='Illesztéshez használt csúcsok')
        
        t_smooth = np.linspace(min(t_full), max(t_full), 2000)
        env_smooth = envelope_model_local(t_smooth, A_fit, f_beat_fit, phi_fit, C_fit, beta_fit)
        
        ax1.plot(t_smooth, env_smooth, 'b-', linewidth=2.5, 
                 label=fr'Illesztett burkoló ($f_L={f_L:.3f}$ Hz, $T_L={T_L:.2f}$ s)')
                 
        ax1.set_title(f'10. feladat - Lebegés vizsgálata ({basename})')
        ax1.set_ylabel('Pozíció [m]')
        ax1.legend(loc='upper right', fontsize=12)
        ax1.grid(True, linestyle='--', alpha=0.7)
        
        # --- ALSÓ ÁBRA: Az amplitúdó lecsengése (Decay of the amplitude) ---
        # Itt az állandósult szintet levonva csak a tiszta amplitúdót ábrázoljuk
        ax2.plot(t_peaks, pos_peaks - C_fit, 'r.', markersize=10, label='Csúcsok amplitúdója (Mért)')
        
        # A tiszta exponenciális lecsengés (decay)
        pure_decay = A_fit * np.exp(-beta_fit * (t_smooth - t0))
        ax2.plot(t_smooth, pure_decay, 'g--', linewidth=2.5, 
                 label=fr'Exponenciális lecsengés: $A={A_fit:.4f}$ m, $\beta={beta_fit:.4f}$ 1/s')
        
        ax2.set_xlabel('Idő [s]')
        ax2.set_ylabel('Amplitúdó [m]')
        ax2.legend(loc='upper right', fontsize=12)
        ax2.grid(True, linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        
        save_name = basename.replace('.csv', '_lebeges.png')
        save_path = os.path.join(images_dir, save_name)
        plt.savefig(save_path)
        print(f"Ábra elmentve: {save_path}")
        
    except Exception as e:
        print(f"Hiba történt a {basename} feldolgozása közben: {e}")

# Megjelenítjük a legenerált ábrákat a futás végén
plt.show()
