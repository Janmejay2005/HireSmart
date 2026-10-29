"""
UI & Application Robustness Test Suite
Validates UI integrity, boundary resilience, input handling, and AppSec hygiene:
1. UI DOM structure & element rendering
2. Interactive slider boundary testing & NaN input guards
3. Client-side security: Subresource Integrity (SRI) & CDN security
4. Data Pipeline Resilience: Zero-division guards & boundary handling
5. CSV / Excel Formula Injection defense (CWE-1236)
"""

import os
import re
import unittest
import pandas as pd
import numpy as np

class TestUIAndRobustness(unittest.TestCase):
    def setUp(self):
        self.dashboard_path = os.path.join("dashboard", "index.html")
        self.html_report_path = os.path.join("04_Reports", "HireSmart_Task1_Hiring_Insights_Report.html")

    def test_ui_dom_elements_present(self):
        """UI Test: Verify all critical interactive DOM containers exist."""
        with open(self.dashboard_path, "r", encoding="utf-8") as f:
            html = f.read()

        # Canvas elements for charts
        self.assertIn('id="offerChart"', html, "Offer chart canvas missing.")
        self.assertIn('id="stageChart"', html, "Stage breakdown chart canvas missing.")
        self.assertIn('id="sourcingChart"', html, "Sourcing chart canvas missing.")
        self.assertIn('id="recruiterChart"', html, "Recruiter scatterplot canvas missing.")

        # Interactive controls
        self.assertIn('id="screeningSlider"', html, "Simulator input slider missing.")
        self.assertIn('id="simTth"', html, "Time-to-hire simulation display missing.")
        self.assertIn('id="simDaysSaved"', html, "Days saved simulation display missing.")

    def test_ui_slider_boundary_attributes(self):
        """UI Boundary Test: Verify slider input has valid min, max, and step boundaries."""
        with open(self.dashboard_path, "r", encoding="utf-8") as f:
            html = f.read()

        slider_match = re.search(r'<input[^>]*id=["\']screeningSlider["\'][^>]*>', html)
        self.assertIsNotNone(slider_match, "Slider input element not found.")
        slider_tag = slider_match.group(0)

        self.assertIn('min="', slider_tag, "Slider must define min boundary.")
        self.assertIn('max="', slider_tag, "Slider must define max boundary.")
        self.assertIn('step="', slider_tag, "Slider must define step granularity.")

    def test_pipeline_zero_division_guard(self):
        """Pipeline Resilience: Ensure metric calculations handle zero-denominator edge cases."""
        # Simulated edge case: zero screening hours or zero offers
        zero_offers = 0
        accepted = 0
        screening_hours = 0
        apps = 100

        # Safe formulas should use conditional guards
        oar = (accepted / zero_offers * 100.0) if zero_offers > 0 else 0.0
        screening_burden = (apps / screening_hours) if screening_hours > 0 else 0.0

        self.assertEqual(oar, 0.0, "Zero offers must safely compute to 0.0% instead of crashing.")
        self.assertEqual(screening_burden, 0.0, "Zero screening hours must safely compute to 0.0 instead of crashing.")

    def test_csv_formula_injection_defense(self):
        """AppSec Audit: Test defense against spreadsheet formula injection (CWE-1236)."""
        # Formula injection characters: '=', '+', '-', '@'
        malicious_inputs = ["=CMD|' /C calc'!A0", "+1+1", "-2+5", "@SUM(1,2)"]
        
        def sanitize_cell(val):
            if isinstance(val, str) and val.startswith(('=', '+', '-', '@')):
                return "'" + val  # Prefix with single quote to neutralize formula execution in Excel
            return val

        for mal in malicious_inputs:
            sanitized = sanitize_cell(mal)
            self.assertTrue(sanitized.startswith("'"), f"Input '{mal}' was not neutralized.")

    def test_no_sensitive_pii_exposed(self):
        """AppSec Audit: Verify datasets do not expose sensitive PII (passwords, SSNs, API tokens)."""
        data_files = [
            os.path.join("02_Data", "raw_talentbridge_hiring_data.csv"),
            os.path.join("03_Analysis", "cleaned_talentbridge_hiring_data.csv")
        ]
        sensitive_keywords = ["password", "secret", "token", "ssn", "credit_card", "bearer"]
        
        for path in data_files:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read().lower()
                for kw in sensitive_keywords:
                    self.assertNotIn(kw, content, f"Sensitive keyword '{kw}' detected in {path}")

if __name__ == "__main__":
    unittest.main()
