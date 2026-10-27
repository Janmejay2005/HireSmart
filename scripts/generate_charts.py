"""
HireSmart Data Visualization Engine
Generates publication-grade trend charts, funnel diagnostics,
and recruiter workload comparisons for 04_Reports/charts/
"""

import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np

# Ensure chart directory exists
chart_dir = os.path.join("04_Reports", "charts")
os.makedirs(chart_dir, exist_ok=True)

# Load data
df_monthly = pd.read_csv(os.path.join("03_Analysis", "cleaned_talentbridge_hiring_data.csv"))
df_sourcing = pd.read_csv(os.path.join("03_Analysis", "cleaned_talentbridge_sourcing_data.csv"))
df_recruiter = pd.read_csv(os.path.join("03_Analysis", "cleaned_talentbridge_recruiter_data.csv"))

# Calculate percentage columns
df_monthly["OAR"] = (df_monthly["Accepted"] / df_monthly["Offers"]) * 100.0
df_monthly["Exit_Rate"] = (df_monthly["Early_Exits_90d"] / df_monthly["Accepted"]) * 100.0
df_sourcing["Conversion_Pct"] = (df_sourcing["Hires"] / df_sourcing["Applications"]) * 100.0
df_sourcing["Exit_Pct"] = (df_sourcing["Early_Exits_90d"] / df_sourcing["Hires"]) * 100.0

# Styling
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
colors = {
    "primary": "#1E3A8A",      # Deep Navy
    "secondary": "#0284C7",    # Slate Blue
    "accent_red": "#DC2626",    # Crimson Red
    "accent_green": "#059669",  # Emerald Green
    "accent_amber": "#D97706",  # Amber
    "gray_dark": "#1F2937",
    "gray_light": "#F3F4F6",
}

# --- Chart 1: Monthly Offers Extended vs Accepted & Acceptance Rate Drop ---
fig, ax1 = plt.subplots(figsize=(10, 5.5), dpi=300)
x = np.arange(len(df_monthly))
width = 0.35

rects1 = ax1.bar(x - width/2, df_monthly["Offers"], width, label="Offers Extended", color="#93C5FD", edgecolor="#1D4ED8")
rects2 = ax1.bar(x + width/2, df_monthly["Accepted"], width, label="Offers Accepted (Hires)", color="#1D4ED8", edgecolor="#1E3A8A")

ax1.set_xlabel("Recruitment Month (2026)", fontsize=11, fontweight="bold", labelpad=10)
ax1.set_ylabel("Number of Offers", fontsize=11, fontweight="bold", color="#1E3A8A")
ax1.set_xticks(x)
ax1.set_xticklabels([m.split("-")[1] + " (M" + str(i+1) + ")" for i, m in enumerate(df_monthly["Month"])], rotation=0)
ax1.set_ylim(0, 65)

# Secondary axis for Offer Acceptance Rate %
ax2 = ax1.twinx()
line1 = ax2.plot(x, df_monthly["OAR"], color="#DC2626", marker="o", linewidth=2.8, markersize=7, label="Offer Acceptance Rate (%)")
ax2.set_ylabel("Offer Acceptance Rate (%)", fontsize=11, fontweight="bold", color="#DC2626")
ax2.set_ylim(40, 100)
ax2.yaxis.set_major_formatter(ticker.PercentFormatter())
ax2.grid(False)

# Annotate January and December
ax2.annotate(f"{df_monthly['OAR'].iloc[0]:.1f}%", xy=(0, df_monthly['OAR'].iloc[0]), xytext=(0, df_monthly['OAR'].iloc[0] + 5),
             ha="center", fontweight="bold", color="#DC2626", arrowprops=dict(arrowstyle="->", color="#DC2626"))
ax2.annotate(f"{df_monthly['OAR'].iloc[-1]:.1f}%\n(-29.5%)", xy=(11, df_monthly['OAR'].iloc[-1]), xytext=(11, df_monthly['OAR'].iloc[-1] + 8),
             ha="center", fontweight="bold", color="#DC2626", arrowprops=dict(arrowstyle="->", color="#DC2626"))

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right", frameon=True, facecolor="white", framealpha=0.95)

plt.title("TalentBridge: Widening Gap Between Offers Extended & Accepted (Jan–Dec 2026)\nAcceptance rate plunged 29.5 percentage points as recruitment lag expanded",
          fontsize=12, fontweight="bold", pad=15)
plt.tight_layout()
chart1_path = os.path.join(chart_dir, "offers_vs_acceptance_trend.png")
plt.savefig(chart1_path, dpi=300)
plt.close()
print(f"Generated: {chart1_path}")

# --- Chart 2: 48-Day Time-to-Hire Stage Breakdown ---
fig, ax = plt.subplots(figsize=(9, 4.8), dpi=300)
stages = ["Resume Screening & Triage", "Interviews (Recruiter & HM)", "Offer Formulation & Approvals", "Candidate Offer Decision"]
days = [df_monthly["Screening_Days"].mean(), df_monthly["Interview_Days"].mean(), df_monthly["Approval_Days"].mean(), df_monthly["Offer_Days"].mean()]
colors_stage = ["#EF4444", "#3B82F6", "#F59E0B", "#10B981"]

bars = ax.barh(stages[::-1], days[::-1], color=colors_stage[::-1], edgecolor="#374151", height=0.55)
ax.set_xlabel("Average Duration in Days (Total Benchmark: 48.0 Days)", fontsize=11, fontweight="bold")
ax.set_xlim(0, 22)

for bar in bars:
    w = bar.get_width()
    pct = (w / 48.0) * 100
    ax.text(w + 0.4, bar.get_y() + bar.get_height()/2, f"{w:.1f} Days ({pct:.1f}%)", va="center", ha="left", fontsize=10, fontweight="bold")

ax.axvline(10, color="gray", linestyle="--", alpha=0.6)
ax.text(10.2, 0.2, "Target Stage Max (10d)", color="gray", fontsize=8.5, fontstyle="italic")

plt.title("TalentBridge 48-Day Time-to-Hire Stage Deconstruction\nScreening is the #1 delay bottleneck, consuming 16.5 days (34.4% of total cycle)",
          fontsize=12, fontweight="bold", pad=15)
plt.tight_layout()
chart2_path = os.path.join(chart_dir, "time_to_hire_stage_breakdown.png")
plt.savefig(chart2_path, dpi=300)
plt.close()
print(f"Generated: {chart2_path}")

# --- Chart 3: Sourcing Effectiveness & Early Exits ---
fig, ax1 = plt.subplots(figsize=(10, 5), dpi=300)
x_src = np.arange(len(df_sourcing))
w_src = 0.38

rects_src1 = ax1.bar(x_src - w_src/2, df_sourcing["Conversion_Pct"], w_src, label="Hire Conversion Rate (%)", color="#10B981", edgecolor="#065F46")
rects_src2 = ax1.bar(x_src + w_src/2, df_sourcing["Exit_Pct"], w_src, label="90-Day Early Exit Rate (%)", color="#EF4444", edgecolor="#991B1B")

ax1.set_ylabel("Rate (%)", fontsize=11, fontweight="bold")
ax1.set_xticks(x_src)
ax1.set_xticklabels(df_sourcing["Source"], rotation=12, ha="right", fontsize=9.5)
ax1.set_ylim(0, 32)
ax1.yaxis.set_major_formatter(ticker.PercentFormatter())

for r in rects_src1:
    h = r.get_height()
    ax1.text(r.get_x() + r.get_width()/2, h + 0.6, f"{h:.1f}%", ha="center", fontsize=9, fontweight="bold", color="#065F46")

for r in rects_src2:
    h = r.get_height()
    ax1.text(r.get_x() + r.get_width()/2, h + 0.6, f"{h:.1f}%", ha="center", fontsize=9, fontweight="bold", color="#991B1B")

ax1.legend(loc="upper right", frameon=True)
plt.title("Sourcing Channel Quality: Conversion to Hire vs. 90-Day Early Exit Churn\nJob boards yield lowest conversion (1.9%) & highest churn (26.3%); Referrals deliver top ROI",
          fontsize=12, fontweight="bold", pad=15)
plt.tight_layout()
chart3_path = os.path.join(chart_dir, "sourcing_channel_effectiveness.png")
plt.savefig(chart3_path, dpi=300)
plt.close()
print(f"Generated: {chart3_path}")

# --- Chart 4: Recruiter Overload vs Time-to-Hire and Acceptance Rate ---
fig, ax1 = plt.subplots(figsize=(9.5, 5), dpi=300)
recruiters = df_recruiter["Recruiter"]
y_pos = np.arange(len(recruiters))

bar_reqs = ax1.barh(y_pos, df_recruiter["Open_Requisitions"], height=0.45, color="#6366F1", edgecolor="#3730A3", label="Open Requisitions")
ax1.set_xlabel("Open Requisitions per Recruiter", fontsize=11, fontweight="bold", color="#3730A3")
ax1.set_yticks(y_pos)
ax1.set_yticklabels(recruiters, fontsize=10, fontweight="bold")
ax1.set_xlim(0, 50)

for bar in bar_reqs:
    w = bar.get_width()
    ax1.text(w + 0.8, bar.get_y() + bar.get_height()/2, f"{int(w)} Reqs", va="center", ha="left", fontsize=9.5, fontweight="bold", color="#3730A3")

# Add text on right side showing TTH and Acceptance
for i, row in df_recruiter.iterrows():
    ax1.text(48, i, f"TTH: {row['Avg_TTH_Days']}d | OAR: {row['Accepted_Rate_Pct']:.1f}%",
             va="center", ha="right", fontsize=9, bbox=dict(boxstyle="round,pad=0.2", facecolor="#F3F4F6", edgecolor="#D1D5DB"))

ax1.axvline(25, color="#EF4444", linestyle="--", linewidth=1.5)
ax1.text(25.5, 4.2, "Optimal Workload Threshold (<=25 Reqs)", color="#EF4444", fontsize=8.5, fontweight="bold")

plt.title("Recruiter Workload Imbalance & Direct Impact on Outcomes (r = 1.00)\nOverburdened recruiters (>35 reqs) experience 54-56d time-to-hire & sub-58% offer acceptance",
          fontsize=11.5, fontweight="bold", pad=15)
plt.tight_layout()
chart4_path = os.path.join(chart_dir, "recruiter_workload_vs_tth.png")
plt.savefig(chart4_path, dpi=300)
plt.close()
print(f"Generated: {chart4_path}")

# --- Chart 5: 4-Panel Executive Overview Dashboard ---
fig, ((ax_a, ax_b), (ax_c, ax_d)) = plt.subplots(2, 2, figsize=(14, 10), dpi=300)

# Panel A: Monthly Trend
ax_a.plot(df_monthly["Month"].str.replace("2026-", "M"), df_monthly["Avg_TTH_Days"], marker="s", color="#DC2626", label="Avg Time-to-Hire (Days)", linewidth=2)
ax_a.set_ylabel("Days", color="#DC2626", fontweight="bold")
ax_a_twin = ax_a.twinx()
ax_a_twin.plot(df_monthly["Month"].str.replace("2026-", "M"), df_monthly["OAR"], marker="o", color="#2563EB", label="Offer Acceptance (%)", linewidth=2)
ax_a_twin.set_ylabel("Acceptance %", color="#2563EB", fontweight="bold")
ax_a.set_title("A. TTH Expansion vs Acceptance Rate Plunge", fontweight="bold", fontsize=10.5)
ax_a.grid(True, alpha=0.3)

# Panel B: Sourcing Conversion
ax_b.bar(df_sourcing["Source"].str.split(" ").str[0], df_sourcing["Conversion_Pct"], color="#10B981")
ax_b.set_ylabel("Conversion to Hire (%)", fontweight="bold")
ax_b.set_title("B. Hire Conversion by Sourcing Channel", fontweight="bold", fontsize=10.5)
for i, v in enumerate(df_sourcing["Conversion_Pct"]):
    ax_b.text(i, v + 0.3, f"{v:.1f}%", ha="center", fontsize=8.5, fontweight="bold")

# Panel C: Recruiter Workload
ax_c.scatter(df_recruiter["Open_Requisitions"], df_recruiter["Avg_TTH_Days"], s=180, color="#8B5CF6", edgecolors="black")
for i, txt in enumerate(df_recruiter["Recruiter"].str.split(" ").str[0]):
    ax_c.annotate(txt, (df_recruiter["Open_Requisitions"].iloc[i] + 0.8, df_recruiter["Avg_TTH_Days"].iloc[i]), fontsize=8.5)
ax_c.set_xlabel("Open Requisitions", fontweight="bold")
ax_c.set_ylabel("Time-to-Hire (Days)", fontweight="bold")
ax_c.set_title("C. Recruiter Requisition Load vs Time-to-Hire (r = 1.00)", fontweight="bold", fontsize=10.5)
ax_c.grid(True, alpha=0.3)

# Panel D: 90-Day Early Exits
ax_d.bar(df_monthly["Month"].str.replace("2026-", "M"), df_monthly["Early_Exits_90d"], color="#F97316")
ax_d.set_ylabel("Early Exits (90d)", fontweight="bold")
ax_d.set_title("D. Monthly Early Exits (Total: 76 Exits, 19.6% Rate)", fontweight="bold", fontsize=10.5)
for i, v in enumerate(df_monthly["Early_Exits_90d"]):
    ax_d.text(i, v + 0.15, str(v), ha="center", fontsize=8.5, fontweight="bold")

plt.suptitle("HireSmart Task 1: TalentBridge Executive Hiring Telemetry Dashboard", fontsize=14, fontweight="bold", y=0.99)
plt.tight_layout()
chart5_path = os.path.join(chart_dir, "executive_hiring_dashboard.png")
plt.savefig(chart5_path, dpi=300)
plt.close()
print(f"Generated: {chart5_path}")
