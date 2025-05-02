import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Custom colors for rider types
custom_palette = {
    "casual": "#3598FE",  # blue
    "member": "#08CF96"   # green
}

# Load the cleaned data
df = pd.read_csv("cleaned_data/merged_cleaned.csv")

# Ensure 'day_of_week' is ordered correctly
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=days_order, ordered=True)

# --- 1. Boxplot: Ride length by user type and weekday ---
plt.figure(figsize=(12, 6))
sns.boxplot(
    data=df[df['ride_length'] < 60],
    x='day_of_week',
    y='ride_length',
    hue='member_casual',
    palette=custom_palette
)
plt.title('Ride Length by Day of Week (Under 60 min)')
plt.ylabel('Ride Length (min)')
plt.xlabel('Day of Week')
plt.legend(title='Rider Type')
plt.tight_layout()
plt.savefig("cleaned_data/boxplot_ride_length_by_day.png")
plt.close()

# --- 2. Hourly ride patterns ---
df['hour'] = pd.to_datetime(df['started_at']).dt.hour
hourly = df.groupby(['hour', 'member_casual']).size().reset_index(name='ride_count')

plt.figure(figsize=(12, 6))
sns.lineplot(
    data=hourly,
    x='hour',
    y='ride_count',
    hue='member_casual',
    palette=custom_palette
)
plt.title('Rides by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Number of Rides')
plt.xticks(range(0, 24))
plt.legend(title='Rider Type')
plt.tight_layout()
plt.savefig("cleaned_data/rides_by_hour.png")
plt.close()

# --- 3. Rideable type breakdown ---
ride_type = df.groupby(['rideable_type', 'member_casual']).size().reset_index(name='count')

plt.figure(figsize=(8, 6))
sns.barplot(
    data=ride_type,
    x='rideable_type',
    y='count',
    hue='member_casual',
    palette=custom_palette
)
plt.title('Rideable Type Usage by Rider Type')
plt.ylabel('Number of Rides')
plt.xlabel('Bike Type')
plt.legend(title='Rider Type')
plt.tight_layout()
plt.savefig("cleaned_data/rideable_type_by_user.png")
plt.close()

print("✅ Charts saved to cleaned_data/:")
print("- boxplot_ride_length_by_day.png")
print("- rides_by_hour.png")
print("- rideable_type_by_user.png")
