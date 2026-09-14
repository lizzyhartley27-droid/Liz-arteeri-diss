import pandas as pd

# Load the population data
file_path = "/Users/liz/Library/CloudStorage/OneDrive2-Personal/Desktop/arteeri-master/results/142/1999/data/species_global_ts_prey_population.csv"

df = pd.read_csv(file_path, header=None)

# Name the column
df.columns = ["Population"]

# Remove the first 1000 time steps (transient period)
df = df.iloc[1000:].reset_index(drop=True)

# Calculate mean population size
mean_population = df["Population"].mean()

minimum_population = df["Population"].min()

maximum_population = df["Population"].max()

standard_deviation = df["Population"].std()

cv = standard_deviation / mean_population

cv_percent = cv * 100

population_range = maximum_population - minimum_population

print(f"Maximum population size: {maximum_population:.4f}")

print(f"Minimum population size: {minimum_population:.4f}")

print(f"Mean population size: {mean_population:.4f}")

print(f"Range population size: {population_range:.4f}")

print(f"Standard deviation: {standard_deviation:.4f}")

print(f"Coefficient of variation: {cv:.4f}")

print(f"Coefficient of variation (%): {cv_percent:.2f}%")

# PATCH OCCUPANCY

file_path_2 = "/Users/liz/Library/CloudStorage/OneDrive2-Personal/Desktop/arteeri-master/results/142/1999/data/species_global_ts_prey_patches_occupied.csv"

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

file_path_3 = "/Users/liz/Library/CloudStorage/OneDrive2-Personal/Desktop/arteeri-master/results/142/1999/data/species_global_ts_prey_patches_extinct.csv"
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



# Load recolonisation data
file_path = "/Users/liz/Library/CloudStorage/OneDrive2-Personal/Desktop/arteeri-master/results/142/1999/data/species_global_ts_prey_patches_colonised.csv"

df = pd.read_csv(file_path, header=None)
df.columns = ["Recolonisations"]

# Remove first 1000 transient time steps
df = df.iloc[1000:].reset_index(drop=True)

# Number of habitat patches
total_patches = 64

# Number of time steps analysed
number_of_time_steps = len(df)

# Total recolonisation events
total_recolonisations = df["Recolonisations"].sum()

# Recolonisation rate per patch per time step
recolonisation_rate = total_recolonisations / (
    total_patches * number_of_time_steps
)

print(f"Total recolonisation events: {total_recolonisations:.0f}")
print(f"Time steps analysed: {number_of_time_steps}")
print(f"Recolonisation rate: {recolonisation_rate:.6f}")
print(f"Recolonisation rate (%): {recolonisation_rate * 100:.4f}%")
