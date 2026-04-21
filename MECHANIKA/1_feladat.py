import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import argparse
import sys
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set up basic argument parsing in case we want to pass the CSV filename
    parser = argparse.ArgumentParser(description='Plot data from a CSV file and fit a line.')
    parser.add_argument('-f', '--file', type=str, default=os.path.join(script_dir, '1_feladat.csv'), help='Path to the CSV file')
    args = parser.parse_args()
    
    csv_file = args.file
    
    # If a specific CSV file isn't provided or doesn't exist, try to find one in the script directory
    if not os.path.exists(csv_file):
        csv_files = [f for f in os.listdir(script_dir) if f.endswith('.csv')]
        if len(csv_files) == 1:
            csv_file = os.path.join(script_dir, csv_files[0])
            print(f"Found {csv_files[0]}, using it as data source.")
        elif len(csv_files) > 1:
            print(f"Multiple CSV files found. Please specify one using '-f'. Available: {csv_files}")
            sys.exit(1)
        else:
            print("No CSV file found. Please provide a CSV file.")
            sys.exit(1)

    # Read the data from the CSV file
    try:
        # Assumes a common format standard with ',' separator. Can be changed if needed.
        df = pd.read_csv(csv_file)
        print("Data loaded successfully. Columns found:", list(df.columns))
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")
        sys.exit(1)
        
    # Assume the first two columns contain the X and Y data respectively to keep it general
    if len(df.columns) < 2:
        print("CSV file must have at least two columns containing data.")
        sys.exit(1)
        
    x_col = df.columns[0]
    y_col = df.columns[1]
    
    # Drop any NaNs
    df = df.dropna(subset=[x_col, y_col])
    
    x = df[x_col].values
    y = df[y_col].values
    
    # Perform a linear regression (line fitting)
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Generate the points for the fitted line
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = slope * x_fit + intercept
    
    # Create the plot
    plt.figure(figsize=(8, 6))
    
    # Plot the original datapoints
    plt.scatter(x, y, color='blue', label='Data points', zorder=3)
    
    # Plot the fitted line
    plt.plot(x_fit, y_fit, color='red', label=f'Fit: y = {slope:.4f}x {intercept:+.4f}\n$R^2$ = {r_value**2:.4f}', zorder=2)
    
    # Formatting the plot
    plt.xlabel(x_col, fontsize=12)
    plt.ylabel(y_col, fontsize=12)
    plt.title(f'{y_col} vs {x_col}', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7, zorder=1)
    plt.legend()
    
    # Save and show the plot
    plt.tight_layout()
    plt.savefig('1_feladat.png')
    plt.show()

if __name__ == "__main__":
    main()
