# Combined Analysis & Visualization Script for Cyclistic Data
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

# --- Descriptive Summary ---
print("🔍 DATA SUMMARY")
print("Total rides:", len(df))
print("\nSummary of ride length (in minutes):")
print(df['ride_length'].describe())

# Average ride length by user type
avg_ride = df.groupby("member_casual")["ride_length"].mean()
print("\n📊 Average ride length by user type:")
print(avg_ride)

# --- Prepare Categorical Ordering ---
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=days_order, ordered=True)

# --- 1. Ride Count by Weekday ---
ride_counts = df.groupby(["day_of_week", "member_casual"]).size().reset_index(name="ride_count")
ride_counts = ride_counts.sort_values("day_of_week")

plt.figure(figsize=(10, 6))
sns.barplot(
    data=ride_counts,
    x="day_of_week",
    y="ride_count",
    hue="member_casual",
    palette=custom_palette
)
plt.title("Number of Rides per Weekday by Rider Type", fontsize=14, weight='bold')
plt.ylabel("Number of Rides")
plt.xlabel("Day of Week")
plt.xticks(rotation=45)
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles=handles, labels=['Casual', 'Member'], title='User Type')
plt.tight_layout()
plt.savefig("cleaned_data/rides_per_weekday_customcolors.png", dpi=300)
plt.close()
print("📈 Rides per weekday plot saved.")

# --- 2. Median Ride Length by Day (Bar Chart) ---
median_by_day = (
    df[df['ride_length'] < 60]
    .groupby(['day_of_week', 'member_casual'])['ride_length']
    .median()
    .reset_index()
)

plt.figure(figsize=(12, 6))
sns.barplot(
    data=median_by_day,
    x='day_of_week',
    y='ride_length',
    hue='member_casual',
    palette=custom_palette
)
plt.title('Median Ride Length by Day of Week (Under 60 min)')
plt.ylabel('Median Ride Length (min)')
plt.xlabel('Day of Week')
plt.legend(title='Rider Type')
plt.tight_layout()
plt.savefig("cleaned_data/median_ride_length_by_day.png")
plt.close()
print("📊 Median ride length bar chart saved.")

# --- 3. Hourly Ride Patterns ---
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
print("⏰ Hourly ride pattern saved.")

# --- 4. Bike Type Usage ---
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
print("🚲 Rideable type plot saved.")

print("✅ All charts and summaries completed.")
