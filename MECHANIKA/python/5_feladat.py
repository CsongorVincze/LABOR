import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Get the absolute path to the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, '..', 'csv', '5_feladat.csv')

try:
    df = pd.read_csv(filename, sep=r'\s+')
except Exception as e:
    print(f"Hiba a {filename} fájl beolvasásakor: {e}")
    exit(1)

angles = df['Angle'].values
cols = ['T_5cm_hegyes', 'T_5cm_tompa', 'T_2cm_hegyes', 'T_2cm_tompa']
labels = ['5 cm hegyesszög', '5 cm tompaszög', '2 cm hegyesszög', '2 cm tompaszög']
colors = ['r', 'orange', 'b', 'c']

plt.rcParams.update({'font.size': 14})
plt.figure(figsize=(10, 6))

for col, label, color in zip(cols, labels, colors):
    y = df[col].values
    valid = ~np.isnan(y)
    # Vonalak átlátszóan (alpha=0.3)
    plt.plot(angles[valid], y[valid], linestyle='-', color=color, alpha=0.3)
    # Pontok nem átlátszóan
    plt.scatter(angles[valid], y[valid], marker='o', color=color, label=label, zorder=5)

plt.title("Lengési idők a szögelfordulás függvényében (10 lengés)")
plt.xlabel("Szögelfordulás [°]")
plt.ylabel("Lengési idő (10 lengésre) [s]")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the plot
output_image = os.path.join(script_dir, '..', 'images', '5_feladat.png')
plt.savefig(output_image)
plt.show()

print(f"Az ábra elkészült és mentve lett: {output_image}")
