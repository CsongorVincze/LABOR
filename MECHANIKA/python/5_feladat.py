import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Keresgéljük meg a gyökeret
script_dir = os.path.dirname(os.path.abspath(__file__))

# 1. k* és theta automatikus számítása a 4_feladat.csv-ből
df_4 = pd.read_csv(os.path.join(script_dir, '..', 'csv', '4_feladat.csv'), header=None, sep=r'\s+', names=['R', 'T10'])
x_4 = df_4['R'].values**2
y_4 = (df_4['T10'].values / 10.0)**2
m_4, c_4 = np.polyfit(x_4, y_4, 1)

m_disk = 0.05142 # 4. feladatban használt korong tömege (kg)
k_star = 4 * np.pi**2 * m_disk / m_4
theta_table = m_disk * c_4 / m_4 - 1.6e-5

print(f"--- 4. FELADATBÓL ÁTVETT PARAMÉTEREK ---")
print(f"Torziós direkciós nyomaték (k*): {k_star:.5e} N m")
print(f"Torziós asztal tehetetlensége (theta): {theta_table:.5e} kg m^2\n")


# 2. 5. Feladat adatainak feldolgozása
filename = os.path.join(script_dir, '..', 'csv', '5_feladat.csv')
try:
    df = pd.read_csv(filename, sep=r'\s+')
except Exception as e:
    print(f"Hiba a {filename} fájl beolvasásakor: {e}")
    exit(1)

# Minta tömege kg-ban. EZT ÁT KELL ÍRNI A MÉRLEGEN MÉRT ÉRTÉKRE!
m_sample = 0.0387 # Példaérték: 88 gramm (Kérlek írd át!)
print(f"FIGYELEM! A minta tömege (m_sample) jelenleg {m_sample*1000} g-ra van beállítva a kódban.")
print(f"Kérlek nyisd meg az 5_feladat.py fájlt, és írd át az 'm_sample' változót a laboron mért pontos tömegre!\n")

angles_deg = df['Angle'].values
gamma = np.radians(angles_deg)

cols = ['T_5cm_hegyes', 'T_5cm_tompa', 'T_2cm_hegyes', 'T_2cm_tompa']
labels = ['5 cm (hegyes furat)', '5 cm (tompa furat)', '2 cm (hegyes furat)', '2 cm (tompa furat)']
radii = [0.05, 0.05, 0.02, 0.02]
colors = ['r', 'orange', 'b', 'c']

def cosine_model(g, A, B, gamma0):
    return A + B * np.cos(g - gamma0)

plt.rcParams.update({'font.size': 14})
plt.figure(figsize=(12, 7))

for col, label, color, r0 in zip(cols, labels, colors, radii):
    y_raw = df[col].values
    valid = ~np.isnan(y_raw)
    
    g_valid = gamma[valid]
    g_deg_valid = angles_deg[valid]
    
    # A feladatlap szerint a lengésidő NÉGYZETÉT (T'^2) kell ábrázolni
    T_squared = (y_raw[valid] / 10.0)**2
    
    # Görbeillesztés paramétereinek becslése
    A_guess = np.mean(T_squared)
    B_guess = (np.max(T_squared) - np.min(T_squared)) / 2.0
    gamma0_guess = g_valid[np.argmax(T_squared)]
    
    try:
        popt, _ = curve_fit(cosine_model, g_valid, T_squared, p0=[A_guess, B_guess, gamma0_guess])
        A_fit, B_fit, gamma0_fit = popt
        
        # B mindig pozitív legyen a fizikai jelentés miatt
        if B_fit < 0:
            B_fit = -B_fit
            gamma0_fit += np.pi
            
    except Exception as e:
        print(f"Illesztés sikertelen: {col} -> {e}")
        continue
        
    # --- Fizikai paraméterek számítása (III.1.5 egyenlet alapján) ---
    # B = 4pi^2 / k* * 2 * m * r0 * r1
    r1 = (B_fit * k_star) / (8 * np.pi**2 * m_sample * r0)
    
    # A = 4pi^2 / k* * (theta_table + theta_x + m(r0^2 + r1^2))
    theta_x = (A_fit * k_star) / (4 * np.pi**2) - theta_table - m_sample * (r0**2 + r1**2)
    
    print(f"--- {label} ---")
    print(f"  Illesztett A = {A_fit:.4f} s^2,  B = {B_fit:.4f} s^2")
    print(f"  Súlypont távolsága (r1)      : {r1*1000:.2f} mm")
    print(f"  Saját tehetetl. nyom. (th_x) : {theta_x*1e6:.2f} kg*mm^2")
    
    # Adatpontok ábrázolása
    plt.scatter(g_deg_valid, T_squared, marker='o', s=80, color=color, label=f'{label} (Mért)')
    
    # Illesztett görbe ábrázolása
    g_smooth = np.linspace(0, 2*np.pi, 200)
    T2_smooth = cosine_model(g_smooth, A_fit, B_fit, gamma0_fit)
    plt.plot(np.degrees(g_smooth), T2_smooth, linestyle='-', linewidth=2.5, color=color, alpha=0.6,
             label=fr'Illesztett ($A={A_fit:.3f}$, $B={B_fit:.3f}$)')

plt.title("Lengési idők négyzete ($T'^2$) a szögelfordulás függvényében")
plt.xlabel(r"Szögelfordulás, $\gamma$ [°]")
plt.ylabel(r"Lengési idő négyzete, $T'^2$ [s$^2$]")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

output_image = os.path.join(script_dir, '..', 'images', '5_feladat.png')
plt.savefig(output_image)
print(f"\nAz ábra elkészült és mentve lett: {output_image}")

