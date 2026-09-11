import pandas as pd

# Load the population data
file_path = "/Users/liz/Library/CloudStorage/OneDrive2-Personal/Desktop/arteeri-master/results/149/1999/data/species_global_ts_prey_population.csv"

df = pd.read_csv(file_path, header=None)

# Name the column
df.columns = ["Population"]

# Remove the first 1000 time steps (transient period)
df = df.iloc[1000:].reset_index(drop=True)

# Calculate mean population size
mean_population = df["Population"].mean()

minimum_population = df["Population"].min()

maximum_population = df["Population"].max()

population_range = maximum_population - minimum_population

print(f"Maximum population size: {maximum_population:.4f}")

print(f"Minimum population size: {minimum_population:.4f}")

print(f"Mean population size: {mean_population:.4f}")

print(f"Range population size: {population_range:.4f}")

# PATCH OCCUPANCY

file_path_2 = "/Users/liz/Library/CloudStorage/OneDrive2-Personal/Desktop/arteeri-master/results/149/1999/data/species_global_ts_prey_patches_occupied.csv"

df = pd.read_csv(file_path_2, header=None)

# Name the column
df.columns = ["Occupancy"]

# Remove the first 1000 time steps (transient period)
df = df.iloc[1000:].reset_index(drop=True)

mean_occupancy = df["Occupancy"].mean()

minimum_occupancy = df["Occupancy"].min()
maximum_occupancy = df["Occupancy"].max()
range_occupancy = maximum_occupancy - minimum_occupancy
print(f"Maximum occupancy size: {maximum_occupancy:.4f}")
print(f"Minimum occupancy size: {minimum_occupancy:.4f}")
print(f"range occupancy size: {range_occupancy:.4f}")
print(f"Mean occupancy size:{mean_occupancy: 4f}")

# PROBABILITY OF EXTINCTION

file_path_3 = "/Users/liz/Library/CloudStorage/OneDrive2-Personal/Desktop/arteeri-master/results/149/1999/data/species_global_ts_prey_patches_extinct.csv"
df = pd.read_csv(file_path_3, header=None)

df.columns = ["Extinctions"]

# Remove the first 1000 transient time steps
df = df.iloc[1000:].reset_index(drop=True)

# Number of habitat patches
total_patches = 64

# Total number of extinction events
total_extinctions = df["Extinctions"].sum()

# Number of time steps analysed
number_of_time_steps = len(df)

# Local extinction event rate
extinction_rate = total_extinctions / (
    total_patches * number_of_time_steps
)

print(f"Total extinction events: {total_extinctions:.0f}")
print(f"Time steps analysed: {number_of_time_steps}")
print(f"Extinction event rate: {extinction_rate:.6f}")
print(f"Extinction event rate (%): {extinction_rate * 100:.4f}%")