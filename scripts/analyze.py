import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual theme
sns.set(style="whitegrid")

# Custom colors
colors = {
    'casual': '#3598FE',
    'member': '#08CF96'
}

# Load the cleaned data
df = pd.read_csv("cleaned_data/merged_cleaned.csv")

# --- Descriptive Stats ---
print("Total rides:", len(df))
print("Summary of ride length (in minutes):")
print(df['ride_length'].describe())

# --- Average ride length by user type ---
avg_ride = df.groupby("member_casual")["ride_length"].mean()
print("\nAverage ride length by user type:")
print(avg_ride)

# --- Number of rides per weekday ---
ride_counts = df.groupby(["day_of_week", "member_casual"]).size().reset_index(name="ride_count")
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
ride_counts['day_of_week'] = pd.Categorical(ride_counts['day_of_week'], categories=days_order, ordered=True)
ride_counts = ride_counts.sort_values("day_of_week")

# --- Plot: Number of rides per weekday ---
plt.figure(figsize=(10, 6))
sns.barplot(
    data=ride_counts,
    x="day_of_week",
    y="ride_count",
    hue="member_casual",
    palette=[colors['member'], colors['casual']]
)

plt.title("Number of Rides per Weekday by Rider Type", fontsize=14, weight='bold')
plt.ylabel("Number of Rides")
plt.xlabel("Day of Week")
plt.xticks(rotation=45)
plt.legend(title='User Type', labels=['Member', 'Casual'])
plt.tight_layout()
plt.savefig("cleaned_data/rides_per_weekday_customcolors.png", dpi=300)
plt.show()
