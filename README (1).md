# Cyclistic Case Study 🚲

End-to-End Data Analytics Project | Google Data Analytics Capstone

This project analyzes 12 months of Cyclistic bike-share data to uncover differences in behavior between casual riders and annual members. Using Python and real-world data wrangling techniques, I identified key usage patterns and generated strategic marketing recommendations to support the company’s growth goals.

---

## 📌 Business Task

How do annual members and casual riders use Cyclistic bikes differently?
Goal: Help the marketing team identify how to convert more casual riders into annual members.

---

## 🧰 Tools & Skills Used

* Python (pandas, matplotlib, seaborn)
* Tableau Public (interactive dashboard)
* Data wrangling & cleaning
* Exploratory data analysis (EDA)
* Google Data Analytics Certificate methodology

---

## 🗂️ Project Structure

```
Cyclistic-Case-Study/
├── raw_data/                   # 12 monthly CSV files (2023)
├── cleaned_data/              # Cleaned dataset with over 5.7M rows
│   └── merged_cleaned.csv
├── scripts/                   # Python scripts
│   ├── merge_and_clean.py
│   ├── analyze.py
│   └── analyze_more.py
├── visuals/                   # Charts & plots
│   ├── rides_per_weekday.png
│   ├── boxplot_ride_length_by_day.png
│   ├── rides_by_hour.png
│   └── rideable_type_by_user.png
└── README.md
```

---

## 📊 Key Insights

* Casual riders average 28.3 minutes per trip; members average 12.5
* Casuals ride mostly on weekends; members ride more consistently on weekdays
* Members ride during commute hours; casuals ride mid-day/evenings
* Casuals prefer docked and electric bikes more than members

---

## 📈 Visualizations

1. Rides per Weekday by Rider Type
2. Ride Length Boxplot (under 60 minutes)
3. Rides by Hour of Day
4. Bike Type Usage by Rider Type

---

## 📊 Interactive Dashboard

Explore the live dashboard on Tableau Public → \[Insert Tableau link here]

---

## 💡 Recommendations

1. Weekend Explorer Pass – promote trial weekend memberships
2. Electric Bike Bonus – offer e-bike incentives to new members
3. Weekday Commuter Targeting – convert casuals who ride during the week

---

## 📚 Framework Applied

I followed the 6-step Google Data Analytics process:

* Ask → Prepare → Process → Analyze → Share → Act

---

## 📬 Contact

Let’s connect! Reach out via GitHub or LinkedIn for collaboration, feedback, or questions.

───────────────────────────────   
📘 Cyclistic\_Case\_Study\_Portfolio\_Report (for Docs/PDF)
───────────────────────────────

Title: Cyclistic Case Study – Converting Casual Riders to Annual Members
Author: \[Your Name]
Date: May 2025
Tools: Python, pandas, seaborn, matplotlib, Tableau Public

────────────────────────────

Executive Summary

Cyclistic, a Chicago-based bike-share company, wants to increase annual memberships. Using 12 months of ride data from 2023, this case study analyzes how casual and member riders behave differently. Over 5.7 million rows of data were cleaned and analyzed using Python. Following the six-step Google Data Analytics process, I developed three data-driven recommendations to improve membership conversions.

────────────────────────────

1. Ask: Business Task

Main question:
How do annual members and casual riders use Cyclistic bikes differently?

Business goal:
Support marketing efforts by uncovering patterns that encourage casual riders to upgrade.

────────────────────────────

2. Prepare & Process: Data Cleaning

Data source: 12 monthly CSV files (January to December 2023)

Steps taken:

* Combined files using Python
* Cleaned and standardized timestamps
* Calculated ride\_length in minutes
* Extracted day of week and hour
* Removed invalid and negative-duration records
* Filtered to include only “member” and “casual” riders

Final dataset size: 5,718,608 rides

────────────────────────────

3. Analyze: Key Insights

🕒 Ride Duration
Casuals ride 28.3 minutes on average; members ride 12.5 minutes

📅 Day of Week
Casuals ride mostly on weekends; members ride more consistently throughout the week

⏰ Time of Day
Members ride during rush hours; casuals prefer midday and evening

🚲 Rideable Type
Casuals use electric and docked bikes more than members

────────────────────────────

4. Share: Visual Evidence

(Figure 1) Rides per Day of Week — Casuals peak on weekends
(Figure 2) Ride Length Boxplot — Casuals ride longer on all days
(Figure 3) Rides by Hour — Members ride during commute hours
(Figure 4) Bike Type Usage — Casuals prefer electric & docked

Visuals are available in the /visuals folder.

────────────────────────────

5. Act: Recommendations

6. Weekend Explorer Pass
   Offer a weekend-only membership to target casual weekend users

7. Electric Bike Bonus
   Incentivize casual riders with free electric bike time for new memberships

8. Weekday Commuter Campaign
   Identify and convert casuals who ride on weekdays with commuter-focused offers

────────────────────────────

6. Google Data Analytics Process Applied

I followed the six-step process from the certificate:

* Ask – Defined a clear business challenge
* Prepare – Collected and structured 12 months of data
* Process – Cleaned and transformed the data using Python
* Analyze – Discovered meaningful trends and patterns
* Share – Communicated findings with visuals and summaries
* Act – Proposed specific, targeted marketing strategies

This case study showcases my ability to combine business context with data analysis using Python and Tableau.

────────────────────────────

7. Interactive Dashboard

Explore the dashboard here → [Cyclistic Case Study By Moses Oni](https://public.tableau.com/views/CyclisticDashboard2023/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)




