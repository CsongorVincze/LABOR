import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Read the CSV file
data = pd.read_csv(os.path.join(script_dir, 'Csongi_8_feladat.csv'))

# Fit a line to the data
x = data['Teljesítmény (W)'].values
y = data['Hőm.küli. (°C)'].values
coeffs = np.polyfit(x, y, 1)
poly = np.poly1d(coeffs)
y_fit = poly(x)

# Calculate x-intercept (where y=0)
x_intercept = -coeffs[1] / coeffs[0]
print(f"X-axis intersection point: ({x_intercept:.4f}, 0)")
print(f"Line equation: y = {coeffs[0]:.4f}x + {coeffs[1]:.4f}")

# Create the plot: Hőm.küli. vs Teljesítmény
plt.figure(figsize=(10, 6))
plt.scatter(data['Teljesítmény (W)'], data['Hőm.küli. (°C)'], marker='o', s=100, color='steelblue', label='Adatok')
plt.plot(x, y_fit, color='red', linewidth=2, label=f'Illesztés: y={coeffs[0]:.2f}x+{coeffs[1]:.2f}')
plt.xlabel('Teljesítmény (W)', fontsize=12)
plt.ylabel('Hőm.küli. (°C)', fontsize=12)
plt.title('8. Feladat - Peltier: Külső hőmérséklet vs Teljesítmény', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('8_feladat_plot.png', dpi=150, bbox_inches='tight')
plt.show()
