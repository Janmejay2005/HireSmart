"""
HireSmart Master Multi-Phase Test Runner
Executes comprehensive regression and functional test suites across all 5 project phases:
- Phase 1: Understand the Brief & Problem Framing
- Phase 2: Roles, Responsibilities & RACI Governance
- Phase 3: Workspace Architecture, Notion Board & Prompt Log
- Phase 4: Data Cleansing, Metric Formulas & Statistical Analysis
- Phase 5: 1-Page Insights Report, Word Document, HTML & Dashboard
"""

import os
import sys
import unittest
import time

# Ensure current workspace root is in python path
current_dir = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Reconfigure stdout for utf-8 if supported
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def run_phase_tests(suite_name, test_module_name):
    print(f"\n{'='*75}")
    print(f">> EXECUTING: {suite_name.upper()}")
    print(f"{'='*75}")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(test_module_name)
    runner = unittest.TextTestRunner(verbosity=2)
    start_time = time.time()
    result = runner.run(suite)
    elapsed = time.time() - start_time
    
    status = "PASSED" if result.wasSuccessful() else "FAILED"
    passed_count = result.testsRun - len(result.failures) - len(result.errors)
    print(f"--- {suite_name} {status} in {elapsed:.2f}s ({result.testsRun} tests run, {len(result.failures)} failures, {len(result.errors)} errors) ---\n")
    return result.wasSuccessful(), passed_count, result.testsRun

if __name__ == "__main__":
    print("\n***************************************************************************")
    print("        HIRESMART TASK 1: MULTI-PHASE SYSTEM VERIFICATION SUITE           ")
    print("***************************************************************************")

    phases = [
        ("Phase 1: Project Brief & Problem Framing", "test_phase1_brief"),
        ("Phase 2: Roles, Responsibilities & RACI", "test_phase2_roles"),
        ("Phase 3: Workspace, Notion & Prompt Log", "test_phase3_workspace"),
        ("Phase 4: Data Cleansing & Metric Modeling", "test_phase4_data_analysis"),
        ("Phase 5: Insights Report & Delivery Formats", "test_phase5_reports"),
        ("Phase 6: UI Resilience & Application Security", "test_ui_and_robustness"),
    ]

    total_passed = 0
    total_run = 0
    all_passed = True
    summary_results = []

    for name, module in phases:
        passed, passed_count, run_count = run_phase_tests(name, module)
        total_passed += passed_count
        total_run += run_count
        summary_results.append((name, passed, passed_count, run_count))
        if not passed:
            all_passed = False

    print("\n" + "="*75)
    print("                   MULTI-PHASE TEST EXECUTION SUMMARY                      ")
    print("="*75)
    for name, passed, passed_count, run_count in summary_results:
        badge = "[PASS]" if passed else "[FAIL]"
        print(f" {badge} {name:<45} : {passed_count}/{run_count} Tests Passed")
    print("-" * 75)
    print(f" TOTAL TESTS EXECUTED: {total_run} | PASSED: {total_passed} | STATUS: {'ALL PHASES PASSED 100%' if all_passed else 'SOME TESTS FAILED'}")
    print("="*75 + "\n")

    sys.exit(0 if all_passed else 1)
