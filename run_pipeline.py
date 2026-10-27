"""
HireSmart Master Pipeline Runner
Executes all Task 1 modules sequentially:
1. Data generation & cleaning (FR-6)
2. Metric calculation & Excel model generation (FR-7)
3. Publication-grade chart generation (FR-8)
4. Completed DOCX report generation (FR-10)
"""

import subprocess
import sys
import os

def run_step(step_name, command):
    print(f"\n{'='*70}")
    print(f"STEP: {step_name}")
    print(f"COMMAND: {command}")
    print(f"{'='*70}")
    result = subprocess.run([sys.executable] + command.split()[1:], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FAILED: {step_name}")
        print("STDERR:\n", result.stderr)
        sys.exit(1)
    else:
        print(result.stdout)
        print(f"SUCCESS: {step_name} completed.")

if __name__ == "__main__":
    print("\nStarting HireSmart Task 1 Master Pipeline...\n")
    run_step("1. Data Cleansing & Ingestion", "python scripts/generate_and_clean_data.py")
    run_step("2. Hiring Metric Engine & Excel Generation", "python scripts/metrics_engine.py")
    run_step("3. High-Resolution Visualizations", "python scripts/generate_charts.py")
    run_step("4. Final DOCX Insights Report Generation", "python scripts/generate_docx_report.py")
    print(f"\n{'*'*70}")
    print("ALL HIRESMART TASK 1 DELIVERABLES SUCCESSFULLY COMPILED & VERIFIED!")
    print(f"{'*'*70}\n")
