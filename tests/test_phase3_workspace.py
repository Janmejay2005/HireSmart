"""
Phase 3 Test Suite: Workspace, Notion Board, & Prompt Log Governance
Validates PRD Section 3.1-3.6, 6 (FR-3, FR-4, FR-5) and Phase 3 Exit Criteria.
"""

import os
import unittest
import pandas as pd

class TestPhase3Workspace(unittest.TestCase):
    def test_five_drive_folders_exist(self):
        """Phase 3.1 & FR-3: Ensure standard folder structure exists."""
        required_dirs = [
            "01_Brief",
            "02_Data",
            "03_Analysis",
            "04_Reports",
            "05_Prompt_Log"
        ]
        for d in required_dirs:
            self.assertTrue(os.path.isdir(d), f"Required workspace directory '{d}' is missing.")

    def test_workspace_permissions_guide(self):
        """Phase 3.2: Check that permissions guide is documented."""
        path = os.path.join("01_Brief", "Workspace_Setup_Guide.md")
        self.assertTrue(os.path.exists(path), "Workspace_Setup_Guide.md not found.")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Permission", content, "Permission matrix not documented.")

    def test_notion_board_csv_schema(self):
        """Phase 3.3 & FR-4: Validate Notion task board CSV schema and contents."""
        csv_path = os.path.join("01_Brief", "notion_board_tasks.csv")
        self.assertTrue(os.path.exists(csv_path), "notion_board_tasks.csv not found.")
        
        df = pd.read_csv(csv_path)
        required_cols = ["Task ID", "Title", "Owner", "Phase", "Priority", "Status", "Due Date", "Linked Deliverable", "Reviewer"]
        for col in required_cols:
            self.assertIn(col, df.columns, f"Notion CSV missing column: {col}")
        
        self.assertGreaterEqual(len(df), 10, "Notion board should have at least 10 tracked tasks.")
        self.assertTrue(set(df["Status"].unique()).issubset({"Backlog", "In Progress", "Review", "Done"}), "Invalid Notion task status.")

    def test_prompt_log_schema_and_integrity(self):
        """Phase 3.4 & FR-5: Validate AI Prompt Log CSV schema and records."""
        csv_path = os.path.join("05_Prompt_Log", "AI_Prompt_Log.csv")
        self.assertTrue(os.path.exists(csv_path), "AI_Prompt_Log.csv not found.")

        df = pd.read_csv(csv_path)
        required_cols = ["Date", "Tool", "Prompt", "Output summary", "Used or not", "Owner"]
        for col in required_cols:
            self.assertIn(col, df.columns, f"AI Prompt Log missing column: {col}")

        self.assertGreaterEqual(len(df), 5, "Prompt log must record all major AI interactions.")
        self.assertTrue(all(df["Used or not"].str.contains("Used|Discarded", case=False)), "Used or not must indicate usage status.")

    def test_prompt_log_documentation(self):
        """Phase 3.4: Verify markdown prompt governance document."""
        md_path = os.path.join("05_Prompt_Log", "AI_Prompt_Log.md")
        self.assertTrue(os.path.exists(md_path), "AI_Prompt_Log.md not found.")

if __name__ == "__main__":
    unittest.main()
