import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Read the CSV file
data = pd.read_csv(os.path.join(script_dir, 'Csongi_7_feladat.csv'), header=None, names=['X', 'Y'])

# Print first and last datapoints
print("First datapoint:")
print(data.iloc[0])
print("\nLast datapoint:")
print(data.iloc[-1])

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(data['X'], data['Y'], marker='o', linestyle='-', markersize=4, linewidth=1.5)
plt.xlabel('Eltelt idő (s)')
plt.ylabel('Mért ellenállás (ohm)')
plt.title('7. Feladat - Peltier effektus hűtési folyamata')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('7_feladat_plot.png', dpi=150, bbox_inches='tight')
plt.show()
