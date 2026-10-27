"""
Phase 4 Test Suite: Data Cleaning, PRD Section 8 Metrics & Analytics
Validates PRD Section 4.1-4.8, 8, 6 (FR-6, FR-7, FR-8) and Phase 4 Exit Criteria.
"""

import os
import unittest
import pandas as pd
import numpy as np

class TestPhase4DataAnalysis(unittest.TestCase):
    def setUp(self):
        self.clean_monthly_path = os.path.join("03_Analysis", "cleaned_talentbridge_hiring_data.csv")
        self.clean_sourcing_path = os.path.join("03_Analysis", "cleaned_talentbridge_sourcing_data.csv")
        self.clean_recruiter_path = os.path.join("03_Analysis", "cleaned_talentbridge_recruiter_data.csv")
        self.excel_path = os.path.join("03_Analysis", "hiring_metrics_summary.xlsx")
        self.cleaning_log_path = os.path.join("02_Data", "Data_Cleaning_Log.md")

    def test_cleaning_log_exists(self):
        """Phase 4.2 & FR-6: Ensure cleaning log documents all data hygiene steps."""
        self.assertTrue(os.path.exists(self.cleaning_log_path), "Data_Cleaning_Log.md not found.")
        with open(self.cleaning_log_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Duplicate", content)
        self.assertIn("Audit", content)

    def test_cleaned_data_integrity(self):
        """Phase 4.2 & FR-6: Check that cleaned data has 12 consecutive months and no duplicates."""
        df = pd.read_csv(self.clean_monthly_path)
        self.assertEqual(len(df), 12, "Cleaned dataset should have exactly 12 months.")
        self.assertEqual(len(df["Month"].unique()), 12, "Months must be unique.")
        # Funnel sanity check
        self.assertTrue((df["Offers"] <= df["Interviews"]).all(), "Offers cannot exceed interviews.")
        self.assertTrue((df["Accepted"] <= df["Offers"]).all(), "Accepted offers cannot exceed offers extended.")
        self.assertTrue((df["Early_Exits_90d"] <= df["Accepted"]).all(), "Early exits cannot exceed accepted hires.")

    def test_time_to_hire_benchmark_48_days(self):
        """PRD Section 8 & Benchmark: Confirm average time-to-hire is exactly 48.0 days."""
        df = pd.read_csv(self.clean_monthly_path)
        avg_tth = df["Avg_TTH_Days"].mean()
        self.assertAlmostEqual(avg_tth, 48.0, delta=0.1, msg=f"Time-to-hire {avg_tth} does not match 48.0d benchmark.")

    def test_screening_stage_is_primary_delay(self):
        """Phase 4: Confirm screening stage consumes the largest share of cycle time."""
        df = pd.read_csv(self.clean_monthly_path)
        avg_screening = df["Screening_Days"].mean()
        avg_interview = df["Interview_Days"].mean()
        self.assertGreater(avg_screening, avg_interview, "Screening stage should be longer than interview stage.")
        self.assertAlmostEqual(avg_screening, 16.5, delta=0.5, msg="Screening stage should be ~16.5 days.")

    def test_offer_acceptance_decline_trend(self):
        """PRD Section 8: Confirm Offer Acceptance Rate dropped by ~29.5 points."""
        df = pd.read_csv(self.clean_monthly_path)
        df["OAR"] = (df["Accepted"] / df["Offers"]) * 100.0
        jan_oar = df.iloc[0]["OAR"]
        dec_oar = df.iloc[-1]["OAR"]
        drop = jan_oar - dec_oar
        self.assertGreater(jan_oar, 80.0, "January OAR should be > 80%.")
        self.assertLess(dec_oar, 60.0, "December OAR should be < 60%.")
        self.assertAlmostEqual(drop, 29.5, delta=1.0, msg="OAR drop should be ~29.5 percentage points.")

    def test_early_exit_rate(self):
        """PRD Section 8: Confirm early exit rate is ~19.6% (PRD benchmark: 20%)."""
        df = pd.read_csv(self.clean_monthly_path)
        tot_hires = df["Accepted"].sum()
        tot_exits = df["Early_Exits_90d"].sum()
        exit_rate = (tot_exits / tot_hires) * 100.0
        self.assertAlmostEqual(exit_rate, 19.6, delta=0.5, msg="Early exit rate should be ~19.6%.")

    def test_screening_burden_rate(self):
        """PRD Section 8: Confirm screening burden is ~4.5 applications per hour."""
        df = pd.read_csv(self.clean_monthly_path)
        screening_burden = df["Applications"].sum() / df["Screening_Hours"].sum()
        self.assertAlmostEqual(screening_burden, 4.51, delta=0.2, msg="Screening burden should be ~4.51 apps/hr.")

    def test_sourcing_channel_metrics(self):
        """PRD Section 8: Validate Employee Referrals is best, Job Portals is worst."""
        df_src = pd.read_csv(self.clean_sourcing_path)
        df_src["Conv"] = (df_src["Hires"] / df_src["Applications"]) * 100.0
        df_src["Exit_Rate"] = (df_src["Early_Exits_90d"] / df_src["Hires"]) * 100.0

        ref_row = df_src[df_src["Source"].str.contains("Referral")].iloc[0]
        portal_row = df_src[df_src["Source"].str.contains("Job Portal")].iloc[0]

        self.assertGreater(ref_row["Conv"], 10.0, "Referrals should have >10% hire conversion.")
        self.assertLess(portal_row["Conv"], 3.0, "Job portals should have <3% hire conversion.")
        self.assertGreater(portal_row["Exit_Rate"], 20.0, "Job portals should have >20% early exit rate.")

    def test_recruiter_workload_correlation(self):
        """Phase 4.7: Test correlation between recruiter workload and TTH."""
        df_rec = pd.read_csv(self.clean_recruiter_path)
        corr = df_rec["Open_Requisitions"].corr(df_rec["Avg_TTH_Days"])
        self.assertGreater(corr, 0.8, "Strong positive correlation (r > 0.8) expected between workload and TTH.")

    def test_excel_model_integrity(self):
        """Phase 4 & FR-7: Confirm multi-sheet Excel model exists and contains all required sheets."""
        self.assertTrue(os.path.exists(self.excel_path), "hiring_metrics_summary.xlsx not found.")
        excel_file = pd.ExcelFile(self.excel_path)
        expected_sheets = ["Executive_Summary", "Monthly_Trends", "Sourcing_Channels", "Recruiter_Workload", "Ranked_Bottlenecks"]
        for s in expected_sheets:
            self.assertIn(s, excel_file.sheet_names, f"Excel workbook missing sheet: {s}")

    def test_visual_charts_exist(self):
        """FR-8: Confirm all high-resolution PNG charts are generated."""
        chart_dir = os.path.join("04_Reports", "charts")
        expected_charts = [
            "offers_vs_acceptance_trend.png",
            "time_to_hire_stage_breakdown.png",
            "sourcing_channel_effectiveness.png",
            "recruiter_workload_vs_tth.png",
            "executive_hiring_dashboard.png"
        ]
        for c in expected_charts:
            c_path = os.path.join(chart_dir, c)
            self.assertTrue(os.path.exists(c_path), f"Chart '{c}' missing in 04_Reports/charts/")
            self.assertGreater(os.path.getsize(c_path), 10000, f"Chart '{c}' file size too small.")

if __name__ == "__main__":
    unittest.main()
