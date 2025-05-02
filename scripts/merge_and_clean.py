# Import the necessary libraries
import pandas as pd          # pandas = data manipulation and analysis
import os                    # os = helps interact with the file system (folders/files)

# Define the folder where your raw CSV files are stored
data_folder = "raw_data"     # Folder containing all 12 months of ride data

# List all files in the folder that end with .csv
all_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

# Create an empty list to store each CSV as a DataFrame
dfs = []

# Loop through each file and read it into a pandas DataFrame
for file in all_files:
    file_path = os.path.join(data_folder, file)  # Create full path to file
    df = pd.read_csv(file_path)                  # Read the CSV into a DataFrame
    dfs.append(df)                               # Add the DataFrame to our list

# Combine all DataFrames into one giant table
df_all = pd.concat(dfs, ignore_index=True)       # ignore_index=True resets row numbers

# Convert string timestamps into actual datetime objects
df_all['started_at'] = pd.to_datetime(df_all['started_at'])  # Start time of ride
df_all['ended_at'] = pd.to_datetime(df_all['ended_at'])      # End time of ride

# Create a new column: ride_length in **minutes**
df_all['ride_length'] = (df_all['ended_at'] - df_all['started_at']).dt.total_seconds() / 60

# Create another column: day_of_week (like 'Monday', 'Tuesday', etc.)
df_all['day_of_week'] = df_all['started_at'].dt.day_name()

# Clean the data — remove any rides that are invalid or junk

# 1. Filter out rides that are zero or negative in duration
df_all = df_all[df_all['ride_length'] > 0]

# 2. Keep only rows where user type is 'member' or 'casual'
df_all = df_all[df_all['member_casual'].isin(['member', 'casual'])]

# Save the cleaned and combined data to a new CSV file in the cleaned_data folder
df_all.to_csv("cleaned_data/merged_cleaned.csv", index=False)

# Print a final message with the number of rows
print(f"✅ Done! Combined rows: {len(df_all)}")
