import numpy as np
import os
import matplotlib.pyplot as plt

# Replace 'data.csv' with your actual CSV file name!
script_dir = os.path.dirname(os.path.abspath(__file__))
filename_f = os.path.join(script_dir, 'adatok', '1_feladat.csv')
filename_z = os.path.join(script_dir, 'adatok', '1_feladat_zold.csv')

# Read the CSV file. 
# Notes:
# - 'delimiter' is set to ',' by default for CSV. Change to ';' if needed.
# - 'skip_header=1' skips the first row (e.g., column names). Set to 0 if there are no headers.
try:
    data_f = np.genfromtxt(filename_f, delimiter=',', skip_header=0)
    data_z = np.genfromtxt(filename_z, delimiter=',', skip_header=0)
except OSError:
    print(f"Error: The file '{filename_f}' or '{filename_z}' was not found. Please provide the correct filename.")
    exit(1)

# Time is in the 1st column, Resistance is in the 2nd
time_f = data_f[:90, 0]
resistance_f = data_f[:90, 1]

time_z = data_z[:90, 0]
resistance_z = data_z[:90, 1]

# Subtract 100 and divide by 0.385 
# This looks like you're calculating temperature for a Pt100 sensor!
calculated_values_f = (resistance_f - 100) / 0.425
calculated_values_z = (resistance_z - 100) / 0.385


# Plot the results
plt.rcParams.update({'font.size': 14})

plt.figure(figsize=(10, 6))
plt.scatter(time_f, calculated_values_f, marker='o', color='black', label='Fekete termosz')
plt.scatter(time_z, calculated_values_z, marker='o', color='green', label='Zöld termosz')
plt.title('Pt100 szenzorokkal mért hőmérsékletek')
plt.xlabel('Idő (s)')
plt.ylabel('Hőmérséklet (°C)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('1_1_feladat.pdf')
plt.show()
