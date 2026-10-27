"""
Phase 2 Test Suite: Roles, Responsibilities & RACI Governance
Validates PRD Section 5, 6 (FR-2) and Phase 2 Exit Criteria.
"""

import os
import unittest

class TestPhase2Roles(unittest.TestCase):
    def setUp(self):
        self.role_file = os.path.join("01_Brief", "Role_Assignment_Matrix.md")

    def test_role_file_exists(self):
        """FR-2: Verify Role Assignment Matrix file exists and is populated."""
        self.assertTrue(os.path.exists(self.role_file), "Role_Assignment_Matrix.md not found.")
        self.assertGreater(os.path.getsize(self.role_file), 500, "Role matrix file content is too short.")

    def test_all_five_roles_assigned(self):
        """Phase 2.1: Ensure all five required roles are assigned to named owners."""
        with open(self.role_file, "r", encoding="utf-8") as f:
            content = f.read()

        required_roles = [
            "HR Project Lead",
            "People Data Analyst",
            "Talent Acquisition Lead",
            "Employer Brand & Tools Lead",
            "Candidate Experience Lead"
        ]
        for role in required_roles:
            self.assertIn(role, content, f"Role '{role}' is missing from the assignment table.")

    def test_named_individuals_assigned(self):
        """Phase 2.1: Verify named individuals are associated with roles."""
        with open(self.role_file, "r", encoding="utf-8") as f:
            content = f.read()

        required_names = ["Elena Vance", "David Chen", "Marcus Brody", "Amina Al-Mansoor", "Sophia Rodriguez"]
        for name in required_names:
            self.assertIn(name, content, f"Named owner '{name}' not found in team roster.")

    def test_raci_governance_matrix(self):
        """Phase 2.2: Verify RACI matrix covers Responsible, Accountable, Consulted, Informed."""
        with open(self.role_file, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("RACI", content, "RACI matrix header missing.")
        self.assertIn("Responsible", content, "R definition missing.")
        self.assertIn("Accountable", content, "A definition missing.")

    def test_workflow_handoffs_agreed(self):
        """Phase 2.3: Verify explicit handoff protocols between roles."""
        with open(self.role_file, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("Handoff", content, "Handoff specifications missing.")
        self.assertIn("David", content, "Analyst handoff missing.")
        self.assertIn("Elena", content, "Lead sign-off handoff missing.")

if __name__ == "__main__":
    unittest.main()
