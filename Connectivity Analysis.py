import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

# 1. Load your data
try:
    # header=None tells pandas that your file has no column title at the top
    df = pd.read_csv("/Users/liz/Library/CloudStorage/OneDrive2-Personal/Desktop/arteeri-master/results/127/1999/data/species_global_ts_prey_population.csv", header=None)

    # Rename the single column to make the code clean
    df.columns = ['Overall_Count']

    # Dropping the first 1 thousand time-steps
    df = df.iloc[1000:].reset_index(drop=True)

    # Create an artificial 'Time' column based on row numbers (0, 1, 2, 3...)
    df['Time'] = df.index

    print("--- Data Preview ---")
    print(df.head(), "\n")

except FileNotFoundError:
    print("Error: '/Users/liz/Library/CloudStorage/OneDrive2-Personal/Desktop/arteeri-master/results/127/1999/data/species_global_ts_prey_population.csv' not found. Check your file path!")
    exit()

# 2. Visualise the Population Trend over sequential rows
plt.figure(figsize=(10, 5))
sns.set_theme(style="whitegrid")

# Plot actual population line
sns.lineplot(data=df, x='Time', y='Overall_Count', color='darkgreen', linewidth=2, label='Population Count')

# Plot linear trend line to see if it drifts down or up over time
sns.regplot(data=df, x='Time', y='Overall_Count', scatter=False, color='red',
            line_kws={"linestyle": "--", "linewidth": 1.5}, label='Long-term Trend')

plt.title("Population Dynamics under Low Connectivity (p = 0.1)", fontsize=14)
plt.xlabel("Sequential Data Points (Time Steps)", fontsize=12)
plt.ylabel("Overall Population Count", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()

# 3. Fit an Autoregressive (ARIMA) Model
print("--- ARIMA Model Summary ---")
model = ARIMA(df['Overall_Count'], order=(1, 0, 0))
model_fitted = model.fit()
print(model_fitted.summary())

# 4. Check for Extinction Drift (Augmented Dickey-Fuller Test)
print("\n--- Stationarity / Drift Test ---")
adf_result = adfuller(df['Overall_Count'])

print(f"ADF Statistic: {adf_result[0]:.4f}")
print(f"p-value: {adf_result[1]:.4f}")
print("Critical Values:")
for key, value in adf_result[4].items():
    print(f"   {key}: {value:.4f}")

# Interpret the p-value
if adf_result[1] < 0.05:
    print("\nConclusion: The population is Stationary (fluctuates around a stable mean).")
else:
    print("\nConclusion: The population is Non-Stationary (exhibiting long-term upward or downward drift).")


