"""
HireSmart - TalentBridge Hiring Data Generator and Cleansing Engine
Generates raw dataset with intentional real-world anomalies, logs cleaning steps,
and produces the verified cleaned dataset meeting all PRD specifications.
"""

import os
import pandas as pd
import numpy as np

# Ensure directories exist
os.makedirs("02_Data", exist_ok=True)
os.makedirs("03_Analysis", exist_ok=True)

# 1. Generate Raw 12-Month Recruitment Telemetry
raw_monthly_data = [
    {"Month": "2026-01", "Applications": 950, "Screening_Hours": 210, "Screened": 920, "Interviews": 140, "Offers": 42, "Accepted": 35, "Early_Exits_90d": 5, "Avg_TTH_Days": 38.0, "Screening_Days": 11.5, "Interview_Days": 12.0, "Approval_Days": 7.5, "Offer_Days": 7.0},
    {"Month": "2026-02", "Applications": 1020, "Screening_Hours": 225, "Screened": 980, "Interviews": 150, "Offers": 44, "Accepted": 36, "Early_Exits_90d": 6, "Avg_TTH_Days": 40.5, "Screening_Days": 12.5, "Interview_Days": 12.5, "Approval_Days": 8.0, "Offer_Days": 7.5},
    {"Month": "2026-03", "Applications": 1150, "Screening_Hours": 250, "Screened": 1100, "Interviews": 165, "Offers": 48, "Accepted": 37, "Early_Exits_90d": 6, "Avg_TTH_Days": 42.0, "Screening_Days": 13.5, "Interview_Days": 13.0, "Approval_Days": 8.0, "Offer_Days": 7.5},
    {"Month": "2026-04", "Applications": 1200, "Screening_Hours": 260, "Screened": 1150, "Interviews": 170, "Offers": 46, "Accepted": 34, "Early_Exits_90d": 7, "Avg_TTH_Days": 45.0, "Screening_Days": 15.0, "Interview_Days": 13.5, "Approval_Days": 8.5, "Offer_Days": 8.0},
    {"Month": "2026-05", "Applications": 1280, "Screening_Hours": 280, "Screened": 1210, "Interviews": 180, "Offers": 50, "Accepted": 35, "Early_Exits_90d": 7, "Avg_TTH_Days": 47.0, "Screening_Days": 16.0, "Interview_Days": 14.0, "Approval_Days": 8.5, "Offer_Days": 8.5},
    {"Month": "2026-06", "Applications": 1350, "Screening_Hours": 295, "Screened": 1260, "Interviews": 185, "Offers": 52, "Accepted": 35, "Early_Exits_90d": 8, "Avg_TTH_Days": 48.5, "Screening_Days": 17.0, "Interview_Days": 14.0, "Approval_Days": 9.0, "Offer_Days": 8.5},
    {"Month": "2026-07", "Applications": 1220, "Screening_Hours": 270, "Screened": 1180, "Interviews": 175, "Offers": 47, "Accepted": 31, "Early_Exits_90d": 6, "Avg_TTH_Days": 49.0, "Screening_Days": 17.5, "Interview_Days": 14.0, "Approval_Days": 9.0, "Offer_Days": 8.5},
    {"Month": "2026-08", "Applications": 1180, "Screening_Hours": 265, "Screened": 1140, "Interviews": 168, "Offers": 45, "Accepted": 29, "Early_Exits_90d": 6, "Avg_TTH_Days": 50.5, "Screening_Days": 18.0, "Interview_Days": 14.5, "Approval_Days": 9.5, "Offer_Days": 8.5},
    {"Month": "2026-09", "Applications": 1310, "Screening_Hours": 290, "Screened": 1240, "Interviews": 182, "Offers": 49, "Accepted": 30, "Early_Exits_90d": 7, "Avg_TTH_Days": 52.0, "Screening_Days": 18.5, "Interview_Days": 14.5, "Approval_Days": 10.0, "Offer_Days": 9.0},
    {"Month": "2026-10", "Applications": 1400, "Screening_Hours": 310, "Screened": 1320, "Interviews": 195, "Offers": 53, "Accepted": 31, "Early_Exits_90d": 8, "Avg_TTH_Days": 53.5, "Screening_Days": 19.0, "Interview_Days": 15.0, "Approval_Days": 10.0, "Offer_Days": 9.5},
    {"Month": "2026-11", "Applications": 1250, "Screening_Hours": 285, "Screened": 1200, "Interviews": 178, "Offers": 47, "Accepted": 27, "Early_Exits_90d": 5, "Avg_TTH_Days": 54.0, "Screening_Days": 19.5, "Interview_Days": 15.0, "Approval_Days": 10.0, "Offer_Days": 9.5},
    {"Month": "2026-12", "Applications": 1190, "Screening_Hours": 275, "Screened": 1150, "Interviews": 172, "Offers": 52, "Accepted": 28, "Early_Exits_90d": 5, "Avg_TTH_Days": 56.0, "Screening_Days": 20.0, "Interview_Days": 15.5, "Approval_Days": 10.5, "Offer_Days": 10.0},
]

df_monthly = pd.DataFrame(raw_monthly_data)

# Introduce realistic real-world dirty data points for raw file to test cleaning pipeline:
# 1. Inconsistent date format ("2026/06" vs "2026-06")
# 2. String representation in numerical column ("1,250")
# 3. Trailing whitespace in month name
# 4. Duplicate row inserted at the end
df_raw = df_monthly.copy()
df_raw.loc[5, "Month"] = "2026/06 "
df_raw["Applications"] = df_raw["Applications"].astype(str)
df_raw.loc[10, "Applications"] = "1,250"
# Add a duplicate row
duplicate_row = df_raw.iloc[[3]].copy()
df_raw = pd.concat([df_raw, duplicate_row], ignore_index=True)

raw_path = os.path.join("02_Data", "raw_talentbridge_hiring_data.csv")
df_raw.to_csv(raw_path, index=False)
print(f"Created Raw Dataset: {raw_path} with {len(df_raw)} records (including simulated dirty entries).")

# 2. Sourcing Channel Dataset
sourcing_data = [
    {"Source": "Employee Referrals", "Applications": 480, "Screened": 420, "Interviews": 180, "Offers": 68, "Hires": 60, "Early_Exits_90d": 2, "Cost_Per_Hire_USD": 1200, "Avg_Days_To_Offer": 28.0},
    {"Source": "LinkedIn Recruiter", "Applications": 3800, "Screened": 3450, "Interviews": 580, "Offers": 160, "Hires": 122, "Early_Exits_90d": 22, "Cost_Per_Hire_USD": 3400, "Avg_Days_To_Offer": 44.5},
    {"Source": "Job Portals (Indeed/Monster)", "Applications": 6200, "Screened": 5800, "Interviews": 720, "Offers": 175, "Hires": 118, "Early_Exits_90d": 31, "Cost_Per_Hire_USD": 2100, "Avg_Days_To_Offer": 52.0},
    {"Source": "Direct Careers Website", "Applications": 2450, "Screened": 2300, "Interviews": 390, "Offers": 85, "Hires": 58, "Early_Exits_90d": 13, "Cost_Per_Hire_USD": 850, "Avg_Days_To_Offer": 46.0},
    {"Source": "Staffing Agencies", "Applications": 650, "Screened": 610, "Interviews": 140, "Offers": 37, "Hires": 22, "Early_Exits_90d": 4, "Cost_Per_Hire_USD": 8500, "Avg_Days_To_Offer": 36.5},
]
df_sourcing = pd.DataFrame(sourcing_data)
sourcing_raw_path = os.path.join("02_Data", "raw_talentbridge_sourcing_data.csv")
df_sourcing.to_csv(sourcing_raw_path, index=False)

# 3. Recruiter Workload Dataset
recruiter_data = [
    {"Recruiter": "Sarah Jenkins", "Open_Requisitions": 18, "Apps_Assigned": 2150, "Monthly_Screening_Hours": 48, "Avg_TTH_Days": 39.5, "Offers_Made": 115, "Offers_Accepted": 92, "Accepted_Rate_Pct": 80.0, "Screening_Hours_Per_Week": 12.0},
    {"Recruiter": "Mike Ross", "Open_Requisitions": 38, "Apps_Assigned": 3800, "Monthly_Screening_Hours": 78, "Avg_TTH_Days": 54.0, "Offers_Made": 128, "Offers_Accepted": 74, "Accepted_Rate_Pct": 57.8, "Screening_Hours_Per_Week": 19.5},
    {"Recruiter": "Lisa Wong", "Open_Requisitions": 22, "Apps_Assigned": 2450, "Monthly_Screening_Hours": 52, "Avg_TTH_Days": 42.0, "Offers_Made": 108, "Offers_Accepted": 82, "Accepted_Rate_Pct": 75.9, "Screening_Hours_Per_Week": 13.0},
    {"Recruiter": "James Cooper", "Open_Requisitions": 42, "Apps_Assigned": 4100, "Monthly_Screening_Hours": 85, "Avg_TTH_Days": 56.5, "Offers_Made": 135, "Offers_Accepted": 76, "Accepted_Rate_Pct": 56.3, "Screening_Hours_Per_Week": 21.2},
    {"Recruiter": "Chloe Patel", "Open_Requisitions": 15, "Apps_Assigned": 1850, "Monthly_Screening_Hours": 42, "Avg_TTH_Days": 38.0, "Offers_Made": 74, "Offers_Accepted": 56, "Accepted_Rate_Pct": 75.7, "Screening_Hours_Per_Week": 10.5},
]
df_recruiter = pd.DataFrame(recruiter_data)
recruiter_raw_path = os.path.join("02_Data", "raw_talentbridge_recruiter_data.csv")
df_recruiter.to_csv(recruiter_raw_path, index=False)

# 4. Clean and Normalize Data
print("\n--- Executing Cleaning & Normalization Pipeline ---")
# De-duplicate
initial_rows = len(df_raw)
df_clean = df_raw.drop_duplicates().copy()
dedup_count = initial_rows - len(df_clean)

# Clean Month strings
df_clean["Month"] = df_clean["Month"].str.strip().str.replace("/", "-")

# Clean numerical strings
df_clean["Applications"] = df_clean["Applications"].astype(str).str.replace(",", "").astype(int)

# Sort chronologically
df_clean = df_clean.sort_values("Month").reset_index(drop=True)

# Save Cleaned Datasets
clean_monthly_path = os.path.join("03_Analysis", "cleaned_talentbridge_hiring_data.csv")
df_clean.to_csv(clean_monthly_path, index=False)
print(f"Cleaned Monthly Data saved to: {clean_monthly_path} (Deduplicated: {dedup_count} rows, Standardized Month & Types)")

clean_sourcing_path = os.path.join("03_Analysis", "cleaned_talentbridge_sourcing_data.csv")
df_sourcing.to_csv(clean_sourcing_path, index=False)

clean_recruiter_path = os.path.join("03_Analysis", "cleaned_talentbridge_recruiter_data.csv")
df_recruiter.to_csv(clean_recruiter_path, index=False)

print("Data generation and cleaning completed successfully.")
