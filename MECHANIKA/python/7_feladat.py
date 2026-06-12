import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

def process_and_plot(files, time_cutoffs, titles, colors, save_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, '..', 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    plt.rcParams.update({'font.size': 14})
    plt.figure(figsize=(12, 10))
    
    periods_list = []
    
    for i, (file_base, t_cut, title, color) in enumerate(zip(files, time_cutoffs, titles, colors)):
        filename = os.path.join(script_dir, '..', 'csv', file_base)
        try:
            df = pd.read_csv(filename)
        except Exception as e:
            print(f"Hiba a fájl beolvasásakor ({file_base}): {e}")
            continue
            
        if 'Time' in df.columns:
            df = df[df['Time'] >= t_cut]
            time = df['Time'].values
            pos = df['Position'].values
        else:
            print(f"Nincs 'Time' oszlop a fájlban: {file_base}")
            continue
        
        # Mintavételi idő (dt) becslése, hogy az időbeli távolság alapján szűrjünk
        dt = np.mean(np.diff(time))
        # Legalább 0.3 másodperc legyen két csúcs között (a legkisebb periódusidő ~0.46s)
        min_distance = max(5, int(0.3 / dt))
        
        peaks, _ = find_peaks(pos, distance=min_distance, prominence=0.01)
        if len(peaks) > 1:
            period = np.mean(np.diff(time[peaks]))
        else:
            period = np.nan
        periods_list.append(period)
            
        print(f"{file_base} periódusideje: {period:.4f} s")
        
        plt.subplot(2, 1, i + 1)
        plt.plot(time, pos, label=f'Adat ({file_base})', color=color)
        
        if len(peaks) > 0:
            if not np.isnan(period):
                plt.plot(time[peaks], pos[peaks], "rx", markersize=8, label=f'Csúcsok (T = {period:.3f} s)')
            else:
                plt.plot(time[peaks], pos[peaks], "rx", markersize=8, label='Csúcsok')
                
        if not np.isnan(period):
            plt.title(f"{title} (T = {period:.4f} s)")
        else:
            plt.title(title)
        plt.xlabel('Idő [s]')
        plt.ylabel('Pozíció [m]')
        plt.legend(loc='upper right')
        plt.margins(y=0.25)
        plt.grid(True)
        
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, save_name))
    plt.show(block=False)
    return periods_list

if __name__ == '__main__':
    # 1. ábra
    p1 = process_and_plot(
        files=['7_feladat.csv', '7_feladat_2.csv'],
        time_cutoffs=[7.5, 2.0],
        titles=['Külső csillapítás nélküli rezgés rézkorong nélkül - 1. mérés', 'Külső csillapítás nélküli rezgés rézkorong nélkül - 2. mérés'],
        colors=['darkblue', 'deepskyblue'],
        save_name='7_feladat_1.png'
    )

    # 2. ábra
    p2 = process_and_plot(
        files=['7_feladat_b_1.csv', '7_feladat_b_2.csv'],
        time_cutoffs=[2.5, 2.5],
        titles=['Külső csillapítás nélküli rezgés egy rézkoronggal - 1. mérés', 'Külső csillapítás nélküli rezgés egy rézkoronggal - 2. mérés'],
        colors=['darkgreen', 'limegreen'],
        save_name='7_feladat_2.png'
    )

    # 3. ábra
    p3 = process_and_plot(
        files=['7_feladat_b_3.csv', '7_feladat_b_4.csv'],
        time_cutoffs=[2.5, 2.5],
        titles=['Külső csillapítás nélküli rezgés két rézkoronggal - 1. mérés', 'Külső csillapítás nélküli rezgés két rézkoronggal - 2. mérés'],
        colors=['darkred', 'lightcoral'],
        save_name='7_feladat_3.png'
    )

    # 4. ábra: Körfrekvencia a tömeg függvényében
    # Tömeg értékek: 50g (0 korong), 100g (1 korong), 150g (2 korong)
    masses = [0.050, 0.100, 0.150]
    
    # Átlagos periódusidők az egyes állapotokhoz
    T_avg = [np.nanmean(p1), np.nanmean(p2), np.nanmean(p3)]
    
    # Körfrekvencia számítása: omega = 2 * pi / T
    omegas = [2 * np.pi / t for t in T_avg]
    
    plt.figure(figsize=(10, 6))
    plt.plot(masses, omegas, 'bo-', markersize=10, linewidth=2, label=r"Mért $\omega$")
    plt.title("Körfrekvencia a tömeg függvényében")
    plt.xlabel("Tömeg [kg]")
    plt.ylabel(r"Körfrekvencia, $\omega$ [rad/s]")
    
    # Értékek feliratozása
    for m, o in zip(masses, omegas):
        plt.text(m, o + 0.1, f'{o:.2f}', ha='center', va='bottom', fontsize=12)
        
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.margins(0.15)
    plt.legend()
    plt.tight_layout()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, '..', 'images')
    plt.savefig(os.path.join(images_dir, '7_feladat_omega_vs_mass.png'))
    
    # 5. ábra: Körfrekvencia az 1/sqrt(m) függvényében
    inv_sqrt_m = [1 / np.sqrt(m) for m in masses]
    
    # Lineáris illesztés (y = ax + b)
    p = np.polyfit(inv_sqrt_m, omegas, 1)
    a, b = p
    
    # Illesztett egyenes x pontjainak generálása a vonalhoz
    x_fit = np.linspace(min(inv_sqrt_m)*0.9, max(inv_sqrt_m)*1.1, 100)
    y_fit = a * x_fit + b
    
    plt.figure(figsize=(10, 6))
    plt.plot(inv_sqrt_m, omegas, 'ko', markersize=10, label=r"Mért $\omega$")
    plt.plot(x_fit, y_fit, 'r-', linewidth=2, label=f"Illesztett egyenes: y = {a:.3f}x + {b:.3f}")
    
    plt.title(r"Körfrekvencia az $1/\sqrt{m}$ függvényében")
    plt.xlabel(r"$1/\sqrt{m}$ [1/$\sqrt{kg}$]")
    plt.ylabel(r"Körfrekvencia, $\omega$ [rad/s]")
    
    # Értékek feliratozása
    for x, y in zip(inv_sqrt_m, omegas):
        plt.text(x, y + 0.1, f'{y:.2f}', ha='center', va='bottom', fontsize=12)
        
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.margins(0.15)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, '7_feladat_omega_vs_inv_sqrt_m.png'))
    
    plt.show()
