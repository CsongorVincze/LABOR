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
images_dir = os.path.join(script_dir, '..', 'images')
os.makedirs(images_dir, exist_ok=True)

# Összes 8-as feladathoz tartozó csv kikeresése
file_pattern = os.path.join(csv_dir, '8_*.csv')
files = glob.glob(file_pattern)

frequencies_1 = []
amplitudes_1 = []

frequencies_2 = []
amplitudes_2 = []

print("Adatok beolvasása és szinuszillesztés...")
for file in files:
    basename = os.path.basename(file)
    if 'nemgerj' in basename:
        continue
        
    is_dataset_2 = basename.startswith('8_2_')
    
    if is_dataset_2:
        match = re.search(r'8_2_(\d+(?:\.\d+)?)', basename)
    else:
        match = re.search(r'8_(\d+(?:\.\d+)?)', basename)
        
    if match:
        freq_str = match.group(1)
        freq = float(freq_str)
        f_rod = freq / 6.4
        omega_force = 2 * np.pi * f_rod
        
        try:
            df = pd.read_csv(file)
            valid_pos = ~df['Position'].isna() & ~df['Time'].isna()
            t_pos = df.loc[valid_pos, 'Time'].values
            pos = df.loc[valid_pos, 'Position'].values
            
            if len(pos) < 10:
                continue
                
            start_idx = len(pos) // 2
            pos_steady = pos[start_idx:]
            t_steady = t_pos[start_idx:]
            
            median = np.median(pos_steady)
            std = np.std(pos_steady)
            valid_idx = np.abs(pos_steady - median) < 3 * std
            
            t_clean = t_steady[valid_idx]
            pos_clean = pos_steady[valid_idx]
            
            if len(pos_clean) < 10:
                continue
                
            def sine_model(t, A, phi, C):
                return A * np.sin(omega_force * t + phi) + C
                
            A_guess = (np.max(pos_clean) - np.min(pos_clean)) / 2.0
            C_guess = np.mean(pos_clean)
            phi_guess = 0.0
            
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                popt, _ = curve_fit(sine_model, t_clean, pos_clean, p0=[A_guess, phi_guess, C_guess])
            
            A_fit = popt[0]
            amplitude = abs(A_fit)
            
            if is_dataset_2:
                frequencies_2.append(f_rod)
                amplitudes_2.append(amplitude)
            else:
                frequencies_1.append(f_rod)
                amplitudes_1.append(amplitude)
                
        except Exception as e:
            # Csak csendben kihagyjuk, hogy ne szemeteljük tele a konzolt
            pass

def process_dataset(freqs, amps):
    if len(freqs) == 0:
        return np.array([]), np.array([])
    sorted_indices = np.argsort(freqs)
    freqs = np.array(freqs)[sorted_indices]
    amps = np.array(amps)[sorted_indices]
    
    unique_freqs = []
    avg_amps = []
    for freq in np.unique(freqs):
        indices = np.where(freqs == freq)
        unique_freqs.append(freq)
        avg_amps.append(np.mean(amps[indices]))
        
    return np.array(unique_freqs), np.array(avg_amps)

f_1, A_1 = process_dataset(frequencies_1, amplitudes_1)
f_2, A_2 = process_dataset(frequencies_2, amplitudes_2)

# --- 9. FELADAT: Sebességamplitúdó illesztés és paraméterek számítása ---

def velocity_model(omega, omega_0, beta, C):
    """Sebességamplitúdó modell: v_A = (C*omega) / sqrt((omega_0^2 - omega^2)^2 + 4*beta^2*omega^2)"""
    return (C * omega) / np.sqrt((omega_0**2 - omega**2)**2 + 4 * beta**2 * omega**2)

def fit_and_extract_parameters(f_data, A_data, label_name):
    print(f"\n--- {label_name} eredményei ---")
    if len(f_data) == 0:
        print("Nincs elég adat az illesztéshez.")
        return None
        
    omega_data = 2 * np.pi * f_data
    v_A_data = A_data * omega_data
    
    # Kezdeti becslések a curve_fit számára
    max_idx = np.argmax(v_A_data)
    omega_0_guess = omega_data[max_idx]
    beta_guess = 0.5  # Kis csillapítás feltételezése kezdetnek
    C_guess = v_A_data[max_idx] * 2 * beta_guess # Mert a maximum C / (2*beta)
    
    try:
        popt, pcov = curve_fit(velocity_model, omega_data, v_A_data, 
                               p0=[omega_0_guess, beta_guess, C_guess],
                               bounds=([0, 0, 0], [np.inf, np.inf, np.inf]))
        
        omega_0, beta, C = popt
        errors = np.sqrt(np.diag(pcov))
        d_omega_0, d_beta, d_C = errors
        
        # Jósági tényező (Q) számítása hibaterjedéssel
        Q = omega_0 / (2 * beta)
        # Hibaterjedés Q-ra: dQ = Q * sqrt((d_omega_0/omega_0)^2 + (d_beta/beta)^2)
        dQ = Q * np.sqrt((d_omega_0 / omega_0)**2 + (d_beta / beta)**2)
        
        print(f"Saját körfrekvencia (omega_0): {omega_0:.3f} ± {d_omega_0:.3f} rad/s")
        print(f"Csillapítási tényező (beta)  : {beta:.3f} ± {d_beta:.3f} 1/s")
        print(f"C paraméter (F_0/m)          : {C:.4f} ± {d_C:.4f} m/s^2")
        print(f"Jósági tényező (Q)           : {Q:.2f} ± {dQ:.2f}")
        
        return omega_data, v_A_data, popt, errors, Q, dQ
    except Exception as e:
        print(f"Hiba történt az illesztés során: {e}")
        return None

res_1 = fit_and_extract_parameters(f_1, A_1, "1. Mérés (Kis csillapítás)")
res_2 = fit_and_extract_parameters(f_2, A_2, "2. Mérés (Nagy csillapítás)")

# --- Ábrázolás ---
plt.rcParams.update({'font.size': 16})
plt.figure(figsize=(12, 8))

if res_1 is not None:
    omega_1, v_A_1, popt_1, err_1, Q_1, dQ_1 = res_1
    omega_smooth_1 = np.linspace(min(omega_1)*0.9, max(omega_1)*1.1, 500)
    v_smooth_1 = velocity_model(omega_smooth_1, *popt_1)
    
    plt.plot(omega_1, v_A_1, 'bo', label="Mért adat (Kis csillapítás)")
    plt.plot(omega_smooth_1, v_smooth_1, 'b-', linewidth=2, 
             label=fr"Illesztés 1: $\beta={popt_1[1]:.2f}$, $Q={Q_1:.1f}$")

if res_2 is not None:
    omega_2, v_A_2, popt_2, err_2, Q_2, dQ_2 = res_2
    omega_smooth_2 = np.linspace(min(omega_2)*0.9, max(omega_2)*1.1, 500)
    v_smooth_2 = velocity_model(omega_smooth_2, *popt_2)
    
    plt.plot(omega_2, v_A_2, 'gs', label="Mért adat (Nagy csillapítás)")
    plt.plot(omega_smooth_2, v_smooth_2, 'g-', linewidth=2, 
             label=fr"Illesztés 2: $\beta={popt_2[1]:.2f}$, $Q={Q_2:.1f}$")

plt.title('9. feladat - Sebességamplitúdó rezonanciagörbék')
plt.xlabel('Körfrekvencia, $\omega$ [rad/s]')
plt.ylabel('Sebességamplitúdó, $A\omega$ [m/s]')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

save_path = os.path.join(images_dir, '9_feladat_velocity.png')
plt.savefig(save_path)
print(f"\nAz ábra sikeresen elmentve: {save_path}")

plt.show()
