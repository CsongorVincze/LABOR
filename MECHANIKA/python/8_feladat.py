import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import re
import warnings
from scipy.optimize import curve_fit

# Címtárak beállítása
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_dir = os.path.join(script_dir, '..', 'csv')

# Összes 8-as feladathoz tartozó csv kikeresése
file_pattern = os.path.join(csv_dir, '8_*.csv')
files = glob.glob(file_pattern)

frequencies_1 = []
amplitudes_1 = []
phases_1 = []

frequencies_2 = []
amplitudes_2 = []
phases_2 = []

illustration_done = False

for file in files:
    basename = os.path.basename(file)
    
    # A csillapítatlan / nem gerjesztett fájlt kihagyjuk
    if 'nemgerj' in basename:
        continue
        
    # Meghatározzuk, hogy melyik adatsorhoz tartozik
    is_dataset_2 = basename.startswith('8_2_')
    
    # Frekvencia kinyerése a fájlnévből
    if is_dataset_2:
        match = re.search(r'8_2_(\d+(?:\.\d+)?)', basename)
    else:
        match = re.search(r'8_(\d+(?:\.\d+)?)', basename)
        
    if match:
        freq_str = match.group(1)
        freq = float(freq_str)
        
        try:
            df = pd.read_csv(file)
            
            # Csak azokat a sorokat vesszük, ahol van pozíció és idő adat
            valid_pos = ~df['Position'].isna() & ~df['Time'].isna()
            t_pos = df.loc[valid_pos, 'Time'].values
            pos = df.loc[valid_pos, 'Position'].values
            
            if len(pos) < 10:
                continue
                
            # Hogy elkerüljük a kezdeti tranzienseket, az adatok második felét használjuk
            start_idx = len(pos) // 2
            pos_steady = pos[start_idx:]
            t_steady = t_pos[start_idx:]
            
            # Outlierek eltávolítása a szinusz illesztéshez (3 sigma szabály)
            median = np.median(pos_steady)
            std = np.std(pos_steady)
            valid_idx = np.abs(pos_steady - median) < 3 * std
            
            t_clean = t_steady[valid_idx]
            pos_clean = pos_steady[valid_idx]
            
            if len(pos_clean) < 10:
                continue
                
            # Számított paraméterek az illesztéshez
            f_rod = float(freq) / 6.4
            omega_force = 2 * np.pi * f_rod
            
            def sine_model(t, A, phi, C):
                return A * np.sin(omega_force * t + phi) + C
                
            # Kezdeti becslések a curve_fit számára
            A_guess = (np.max(pos_clean) - np.min(pos_clean)) / 2.0
            C_guess = np.mean(pos_clean)
            phi_guess = 0.0
            
            popt, _ = curve_fit(sine_model, t_clean, pos_clean, p0=[A_guess, phi_guess, C_guess])
            A_fit, phi_fit, C_fit = popt
            
            # Mindig pozitív amplitúdót használjunk
            if A_fit < 0:
                A_fit = -A_fit
                phi_fit = phi_fit + np.pi
                
            phi_fit = phi_fit % (2 * np.pi)
            amplitude = abs(A_fit)
            
            # Potential impulzusok keresése a fáziseltolódáshoz
            valid_pot = ~df['Potential'].isna() & ~df['Time'].isna()
            t_pot = df.loc[valid_pot, 'Time'].values
            pot = df.loc[valid_pot, 'Potential'].values
            
            # Impulzus: Potential < 1.5. Keresünk felfutó/lefutó éleket
            is_pulse = pot < 1.5
            pulse_edges = np.where(np.diff(is_pulse.astype(int)) == 1)[0]
            
            if len(pulse_edges) > 0:
                t_pulses = t_pot[pulse_edges]
                # A gerjesztés fázisa az impulzusok alapján
                phi_force_arr = (-omega_force * t_pulses) % (2 * np.pi)
                
                # Fáziseltolódás számítása (pozíció fázis - gerjesztés fázis)
                x = np.cos(phi_force_arr)
                y = np.sin(phi_force_arr)
                phi_force = np.arctan2(np.mean(y), np.mean(x))
                
                delta_phi = (phi_fit - phi_force) % (2 * np.pi)
                if delta_phi > np.pi:
                    delta_phi -= 2 * np.pi
                delta_phi_deg = np.degrees(delta_phi)
                
                # FÁZIS KICSOMAGOLÁSA (unwrapping) hogy ne ugorjon fel +180-ra
                if delta_phi_deg > 90:
                    delta_phi_deg -= 360
            else:
                delta_phi_deg = np.nan
                t_pulses = []
                
            # Illusztráció generálása az első sikeres fájlnál
            if not illustration_done:
                plt.rcParams.update({'font.size': 14})
                plt.figure(figsize=(12, 6))
                
                # Plotoljuk az illesztésre használt adatokat
                plt.plot(t_clean, pos_clean, 'k.', label='Szűrt pozíció adatok')
                
                # Sűrű időtengely az illesztett görbéhez
                t_smooth = np.linspace(min(t_clean), max(t_clean), 500)
                plt.plot(t_smooth, sine_model(t_smooth, A_fit, phi_fit, C_fit), 'r-', linewidth=2, label=f'Illesztett szinusz (A={amplitude:.4f} m)')
                
                # Plotoljuk a pulzusokat is vertical line-ként
                for p_idx, tp in enumerate(t_pulses):
                    if min(t_clean) <= tp <= max(t_clean):
                        label = 'Gerjesztő impulzus' if p_idx == 0 else ""
                        plt.axvline(x=tp, color='g', linestyle='--', alpha=0.6, label=label)
                
                if not np.isnan(delta_phi_deg):
                    plt.title(fr'Szinusz illesztés és impulzusok ({basename})\n$\Delta\phi = {delta_phi_deg:.1f}^\circ$')
                else:
                    plt.title(f'Szinusz illesztés illusztrációja ({basename})')
                plt.xlabel('Idő [s]')
                plt.ylabel('Pozíció [m]')
                plt.legend(loc='upper right')
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.margins(y=0.2)
                plt.tight_layout()
                
                images_dir = os.path.join(script_dir, '..', 'images')
                os.makedirs(images_dir, exist_ok=True)
                plt.savefig(os.path.join(images_dir, '8_sine_fit_illustration.png'))
                illustration_done = True
            
            if is_dataset_2:
                frequencies_2.append(f_rod)
                amplitudes_2.append(amplitude)
                phases_2.append(delta_phi_deg)
            else:
                frequencies_1.append(f_rod)
                amplitudes_1.append(amplitude)
                phases_1.append(delta_phi_deg)
        except Exception as e:
            print(f"Hiba a {basename} fájl feldolgozásakor: {e}")

# Segédfüggvény az adatok rendezésére és átlagolására
def process_dataset(freqs, amps, phs):
    if len(freqs) == 0:
        return np.array([]), np.array([]), np.array([])
    
    sorted_indices = np.argsort(freqs)
    freqs = np.array(freqs)[sorted_indices]
    amps = np.array(amps)[sorted_indices]
    phs = np.array(phs)[sorted_indices]

    unique_freqs = []
    avg_amps = []
    avg_phs = []
    for freq in np.unique(freqs):
        indices = np.where(freqs == freq)
        unique_freqs.append(freq)
        avg_amps.append(np.mean(amps[indices]))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            avg_phs.append(np.nanmean(phs[indices]))
        
    return np.array(unique_freqs), np.array(avg_amps), np.array(avg_phs)

u_freqs_1, avg_amps_1, avg_phs_1 = process_dataset(frequencies_1, amplitudes_1, phases_1)
u_freqs_2, avg_amps_2, avg_phs_2 = process_dataset(frequencies_2, amplitudes_2, phases_2)

# Globális betűméret beállítása
plt.rcParams.update({'font.size': 18})

plt.figure(figsize=(12, 8))

# Első adatsor ábrázolása
if len(u_freqs_1) > 0:
    plt.plot(u_freqs_1, avg_amps_1, marker='o', linestyle='-', color='b', label="1. mérés (8_...)")
    max_idx_1 = np.argmax(avg_amps_1)
    plt.plot(u_freqs_1[max_idx_1], avg_amps_1[max_idx_1], 'bo', markersize=10, label=f"Rezonancia 1: {u_freqs_1[max_idx_1]:.3f} Hz")

# Második adatsor ábrázolása
if len(u_freqs_2) > 0:
    plt.plot(u_freqs_2, avg_amps_2, marker='s', linestyle='-', color='g', label="2. mérés (8_2_...)")
    max_idx_2 = np.argmax(avg_amps_2)
    plt.plot(u_freqs_2[max_idx_2], avg_amps_2[max_idx_2], 'gs', markersize=10, label=f"Rezonancia 2: {u_freqs_2[max_idx_2]:.3f} Hz")

plt.title('8. feladat - Rezonanciagörbék')
plt.xlabel('Frekvencia [Hz]')
plt.ylabel('Amplitúdó [m]')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Kép mentése
images_dir = os.path.join(script_dir, '..', 'images')
os.makedirs(images_dir, exist_ok=True)
plt.savefig(os.path.join(images_dir, '8_feladat.png'))

# --- Fáziseltolódás Ábra ---
plt.figure(figsize=(12, 8))

if len(u_freqs_1) > 0:
    valid_1 = ~np.isnan(avg_phs_1)
    plt.plot(u_freqs_1[valid_1], avg_phs_1[valid_1], marker='o', linestyle='-', color='b', label="1. mérés (8_...)")

if len(u_freqs_2) > 0:
    valid_2 = ~np.isnan(avg_phs_2)
    plt.plot(u_freqs_2[valid_2], avg_phs_2[valid_2], marker='s', linestyle='-', color='g', label="2. mérés (8_2_...)")

plt.title('8. feladat - Fáziseltolódás a gerjesztéshez képest')
plt.xlabel('Frekvencia [Hz]')
plt.ylabel('Fáziseltolódás [fok]')
plt.yticks(np.arange(-360, 45, 45))
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(images_dir, '8_feladat_phase.png'))

plt.show()

# Konzolra kiírás
print("1. mérés (8_...) frekvencia-amplitúdó-fázis párok:")
for f, a, p in zip(u_freqs_1, avg_amps_1, avg_phs_1):
    print(f"{f:5.3f} Hz -> {a:.5f} m | Phase: {p:7.2f}°")

print("\n2. mérés (8_2_...) frekvencia-amplitúdó-fázis párok:")
for f, a, p in zip(u_freqs_2, avg_amps_2, avg_phs_2):
    print(f"{f:5.3f} Hz -> {a:.5f} m | Phase: {p:7.2f}°")
