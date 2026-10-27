"""
Phase 1 Test Suite: Understand the Brief & Problem Framing
Validates PRD Section 1, 2, 3, 4, 6 (FR-1) and Phase 1 Exit Criteria.
"""

import os
import unittest

class TestPhase1Brief(unittest.TestCase):
    def setUp(self):
        self.brief_file = os.path.join("01_Brief", "Project_Brief_Summary.md")

    def test_brief_file_exists(self):
        """FR-1: Verify that Project Brief Summary file exists and is populated."""
        self.assertTrue(os.path.exists(self.brief_file), "Project_Brief_Summary.md not found.")
        self.assertGreater(os.path.getsize(self.brief_file), 500, "Brief file content is too short.")

    def test_four_core_problems_captured(self):
        """Phase 1.2: Check that all four core problems are clearly articulated."""
        with open(self.brief_file, "r", encoding="utf-8") as f:
            content = f.read().lower()
        
        self.assertIn("48", content, "48-day time-to-hire problem not documented.")
        self.assertIn("offer acceptance", content, "Declining offer acceptance not documented.")
        self.assertIn("screening", content, "Manual resume screening problem not documented.")
        self.assertIn("exit", content, "Early employee exits problem not documented.")

    def test_user_stakeholders_analyzed(self):
        """Phase 1.3: Verify all 5 user and stakeholder groups are analyzed."""
        with open(self.brief_file, "r", encoding="utf-8") as f:
            content = f.read().lower()

        required_users = ["hr leadership", "recruiter", "hiring manager", "candidate", "project team"]
        for user in required_users:
            self.assertIn(user, content, f"Stakeholder group '{user}' not addressed in brief.")

    def test_budget_and_constraints(self):
        """Phase 1.4: Confirm zero-cost budget constraint and tooling requirements."""
        with open(self.brief_file, "r", encoding="utf-8") as f:
            content = f.read().lower()

        self.assertTrue("budget" in content or "zero-cost" in content or "$0" in content, "Budget constraint missing.")
        self.assertIn("prompt log", content, "Prompt log governance requirement missing.")

    def test_non_goals_explicitly_bounded(self):
        """Phase 1: Validate Non-Goals boundary conditions."""
        with open(self.brief_file, "r", encoding="utf-8") as f:
            content = f.read().lower()

        self.assertIn("non-goals", content, "Non-goals section must be explicit.")

    def test_phase1_exit_criteria(self):
        """Phase 1 Exit Criteria: Sign-off status confirmed."""
        with open(self.brief_file, "r", encoding="utf-8") as f:
            content = f.read().lower()

        self.assertTrue("sign-off" in content or "approved" in content, "Brief summary lacks approval sign-off.")

if __name__ == "__main__":
    unittest.main()
