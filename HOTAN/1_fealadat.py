import numpy as np
import os
import matplotlib.pyplot as plt

# Replace 'data.csv' with your actual CSV file name!
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'adatok', '1_feladat.csv')
# Read the CSV file. 
# Notes:
# - 'delimiter' is set to ',' by default for CSV. Change to ';' if needed.
# - 'skip_header=1' skips the first row (e.g., column names). Set to 0 if there are no headers.
try:
    data = np.genfromtxt(filename, delimiter=',', skip_header=0)
except OSError:
    print(f"Error: The file '{filename}' was not found. Please provide the correct filename.")
    exit(1)

# Time is in the 1st column, Resistance is in the 2nd
time = data[:, 0]
resistance = data[:, 1]

# Filter out anomalously large resistance values (e.g., sensor errors like 9.9e+37)
valid_mask = resistance < 120
time = time[valid_mask]
resistance = resistance[valid_mask]

# Subtract 100 and divide by 0.385 
# This looks like you're calculating temperature for a Pt100 sensor!
calculated_values = (resistance - 100) / 0.425

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(time, calculated_values, marker='o', color='b', label='Temperature (Pt100)')
plt.title('Time vs Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature / Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('1_1_feladat.pdf')
plt.show()
