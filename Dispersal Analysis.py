import pandas as pd

# Load the population data
file_path = "/results/142/1999/data/species_global_ts_prey_population.csv"

df = pd.read_csv(file_path, header=None)

# Name the column
df.columns = ["Population"]

# Remove the first 1000 time steps (transient period)
df = df.iloc[1000:].reset_index(drop=True)

# Calculate mean population size
mean_population = df["Population"].mean()

minimum_population = df["Population"].min()

maximum_population = df["Population"].max()

print(f"Maximum population size: {maximum_population:.4f}")

print(f"Minimum population size: {minimum_population:.4f}")

print(f"Mean population size: {mean_population:.4f}")