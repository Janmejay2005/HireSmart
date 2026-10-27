# HireSmart for TalentBridge — Task 1: Project Kickoff & Hiring Problem Analysis

[![Status: Completed](https://img.shields.io/badge/Status-Completed-success.svg)](#)
[![Phase: Task 1](https://img.shields.io/badge/Phase-Task%201%20Kickoff-blue.svg)](#)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](#)
[![Deliverable: 1--Page Report](https://img.shields.io/badge/Deliverable-1--Page%20Report-purple.svg)](#)

---

## 1. Project Overview & Context
**TalentBridge** is experiencing critical friction across its talent acquisition ecosystem:
- **Extended Time-to-Hire:** Stretched to **48.0 days average** (industry benchmark: 28–32 days).
- **Collapsing Offer Acceptance:** Plunged **29.5 percentage points** (from 83.3% down to 53.8%).
- **Manual Resume Screening Burden:** Recruiters review candidates at only **4.51 applications/hour**, spending >20 hours/week on first-pass triage.
- **High Early Employee Attrition:** **19.6% (76 of 388 new hires)** depart within their first 90 days, largely driven by mismatching job board sourcing.

**HireSmart Task 1** establishes the foundational governance, workspace infrastructure, prompt registry, 12-month data audit, statistical metric calculations, bottleneck ranking, and a sign-off ready **1-Page Hiring Data Insights Report** that serves as the factual foundation for Task 2 solution engineering.

---

## 2. Methodology & End-to-End Process
The project follows a 5-phase sequential and parallel delivery flow:

```
Phase 1: Brief Understanding ──► Phase 2: Role Allocation ──► Phase 3: Workspace & Tooling
                                                                        │
┌───────────────────────────────────────────────────────────────────────┘
▼
Phase 4: Data Cleansing & Metric Modeling
  ├── Data Hygiene Audit (deduplication, normalization, validation)
  ├── PRD Section 8 Formula Execution (TTH, Acceptance, Exits, Sourcing, Workload)
  ├── Statistical Correlation Modeling (TTH vs OAR: r = -1.00, Workload vs TTH: r = 1.00)
  └── High-Resolution Chart Generation (PNGs in 04_Reports/charts/)
│
▼
Phase 5: Insights Report & Executive Dashboard
  ├── 1-Page Markdown Briefing (`04_Reports/HireSmart_Task1_Hiring_Insights_Report.md`)
  ├── Print-Ready Executive HTML Report (`04_Reports/HireSmart_Task1_Hiring_Insights_Report.html`)
  ├── Completed Formal Word Document (`04_Reports/HireSmart_Task1_Hiring_Insights_Report.docx`)
  └── Interactive Executive Web Dashboard (`dashboard/index.html`)
```

---

## 3. Deliverables vs. PRD Functional Requirements

| PRD Req | Deliverable Name | File Location | Responsible Owner |
| :--- | :--- | :--- | :--- |
| **FR-1** | Project Brief Summary | [`01_Brief/Project_Brief_Summary.md`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/01_Brief/Project_Brief_Summary.md) | Elena Vance (*HR Project Lead*) |
| **FR-2** | Role Assignment & RACI Matrix | [`01_Brief/Role_Assignment_Matrix.md`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/01_Brief/Role_Assignment_Matrix.md) | Elena Vance (*HR Project Lead*) |
| **FR-3** | Workspace Architecture & RBAC | [`01_Brief/Workspace_Setup_Guide.md`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/01_Brief/Workspace_Setup_Guide.md) | Amina Al-Mansoor (*Tools Lead*) |
| **FR-4** | Notion Task Board System | [`01_Brief/Notion_Task_Board.md`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/01_Brief/Notion_Task_Board.md) & [`notion_board_tasks.csv`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/01_Brief/notion_board_tasks.csv) | Elena Vance (*HR Project Lead*) |
| **FR-5** | Centralized AI Prompt Log | [`05_Prompt_Log/AI_Prompt_Log.md`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/05_Prompt_Log/AI_Prompt_Log.md) & [`AI_Prompt_Log.csv`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/05_Prompt_Log/AI_Prompt_Log.csv) | Amina Al-Mansoor (*Tools Lead*) |
| **FR-6** | Cleaned Hiring Dataset & Log | [`02_Data/Data_Cleaning_Log.md`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/02_Data/Data_Cleaning_Log.md) & [`03_Analysis/cleaned_talentbridge_hiring_data.csv`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/03_Analysis/cleaned_talentbridge_hiring_data.csv) | David Chen (*People Data Analyst*) |
| **FR-7** | Core Hiring Metrics Model | [`03_Analysis/hiring_metrics_summary.xlsx`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/03_Analysis/hiring_metrics_summary.xlsx) & [`metrics_calculation_engine.py`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/03_Analysis/metrics_calculation_engine.py) | David Chen (*People Data Analyst*) |
| **FR-8** | Trend & Diagnostic Visualizations | [`04_Reports/charts/`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/charts/) | David Chen (*People Data Analyst*) |
| **FR-9** | Ranked Bottleneck Matrix | [`04_Reports/HireSmart_Task1_Hiring_Insights_Report.md`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/HireSmart_Task1_Hiring_Insights_Report.md) | Working Group Lead Team |
| **FR-10** | 1-Page Insights Executive Report | [`04_Reports/HireSmart_Task1_Hiring_Insights_Report.md`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/HireSmart_Task1_Hiring_Insights_Report.md) / [HTML](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/HireSmart_Task1_Hiring_Insights_Report.html) / [DOCX](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/HireSmart_Task1_Hiring_Insights_Report.docx) | David Chen & Elena Vance |

---

## 4. Key Metrics Summary Scorecard

| Metric | Calculation Formula | Audited Value | Status / Takeaway |
| :--- | :--- | :---: | :--- |
| **Average Time-to-Hire** | Days from app to accepted offer | **48.0 Days** | **16.5 days lost in screening alone (34.4% of cycle)** |
| **Offer Acceptance Rate** | Accepted ÷ Total Offers × 100 | **67.5% Avg** | Plunged from 83.3% (Jan) down to 53.8% (Dec) |
| **Offer Acceptance Trend** | Trajectory across 12 months | **-29.5 pts** | Inverse correlation with time-to-hire ($r = -1.00$) |
| **90-Day Early Exit Rate** | Early Exits ÷ Hires × 100 | **19.6%** | **76 of 388 hires** quit early ($1.4M replacement cost) |
| **Screening Burden** | Applications ÷ Recruiter Screening Hours | **4.51 apps/hr** | Recruiters spend >20 hrs/week on manual resume review |
| **Top Sourcing Channel** | Hires ÷ Applications by Source | **Referrals (12.5%)** | Lowest early exit rate (**3.3%**) |
| **Worst Sourcing Channel** | Hires ÷ Applications by Source | **Job Portals (1.9%)** | Highest early exit rate (**26.3%**) |
| **Recruiter Load Imbalance** | Active requisitions per recruiter | **15 – 42 Reqs** | Overloaded recruiters (>35 reqs) average **55.3d TTH** |

---

## 5. Directory Architecture

```
Task 1/
├── 01_Brief/
│   ├── Project_Brief_Summary.md       # FR-1: Executive brief, objectives, constraints
│   ├── Role_Assignment_Matrix.md      # FR-2: 5 named owners & RACI governance
│   ├── Workspace_Setup_Guide.md       # FR-3: Drive architecture & permission levels
│   ├── Notion_Task_Board.md           # FR-4: Markdown Kanban board
│   └── notion_board_tasks.csv         # FR-4: Direct CSV import for Notion
├── 02_Data/
│   ├── raw_talentbridge_hiring_data.csv    # Raw 12-month recruitment dataset
│   ├── raw_talentbridge_sourcing_data.csv  # Sourcing channel breakdown
│   ├── raw_talentbridge_recruiter_data.csv # Recruiter capacity telemetry
│   └── Data_Cleaning_Log.md           # FR-6: 5-point data hygiene audit log
├── 03_Analysis/
│   ├── cleaned_talentbridge_hiring_data.csv # FR-6: Sanitized normalized dataset
│   ├── cleaned_talentbridge_sourcing_data.csv
│   ├── cleaned_talentbridge_recruiter_data.csv
│   ├── hiring_metrics_summary.xlsx    # FR-7: 5-sheet automated Excel model
│   └── metrics_calculation_engine.py  # FR-7: Reusable Python analytical logic
├── 04_Reports/
│   ├── HireSmart_Task1_Hiring_Insights_Report.md   # FR-10: 1-page executive markdown report
│   ├── HireSmart_Task1_Hiring_Insights_Report.html # FR-10: Print-ready executive HTML report
│   ├── HireSmart_Task1_Hiring_Insights_Report.docx # FR-10: Formatted Word document
│   └── charts/
│       ├── offers_vs_acceptance_trend.png          # FR-8: Widening offer gap
│       ├── time_to_hire_stage_breakdown.png        # FR-8: 16.5d screening bottleneck
│       ├── sourcing_channel_effectiveness.png      # FR-8: Conversion vs churn
│       ├── recruiter_workload_vs_tth.png           # FR-8: Workload imbalance vs SLA
│       └── executive_hiring_dashboard.png          # FR-8: 4-panel executive overview
├── 05_Prompt_Log/
│   ├── AI_Prompt_Log.csv              # FR-5: Master AI prompt registry
│   └── AI_Prompt_Log.md               # FR-5: Tool governance documentation
├── dashboard/
│   └── index.html                     # Interactive Web Dashboard with Task 2 Simulator
├── scripts/
│   ├── generate_and_clean_data.py     # Data synthesis & normalization script
│   ├── metrics_engine.py              # Statistical calculation engine
│   ├── generate_charts.py             # Matplotlib publication chart generator
│   └── generate_docx_report.py        # Python-docx report compiler
├── run_pipeline.py                    # Master one-click execution pipeline
└── README.md                          # Comprehensive project documentation
```

---

## 6. How to Run & Verify the Project

### Execute Master Pipeline:
```powershell
python run_pipeline.py
```
This automatically runs data ingestion, cleaning, formula calculation, Excel generation, chart exports, and Word document compilation.

### Open the Interactive Analytics Dashboard:
Double-click [`dashboard/index.html`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/dashboard/index.html) or open it in any web browser to explore interactive charts, recruiter SLA scatterplots, and the **Task 2 Automated Screening Simulator**.

### Open the Executive 1-Page Report:
- **Print-ready HTML:** [`04_Reports/HireSmart_Task1_Hiring_Insights_Report.html`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/HireSmart_Task1_Hiring_Insights_Report.html)
- **Word Document:** [`04_Reports/HireSmart_Task1_Hiring_Insights_Report.docx`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/HireSmart_Task1_Hiring_Insights_Report.docx)
- **Markdown:** [`04_Reports/HireSmart_Task1_Hiring_Insights_Report.md`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/HireSmart_Task1_Hiring_Insights_Report.md)

---

## 7. Handoff to Task 2 (Solution Engineering)
With Task 1 complete, the primary bottleneck has been empirically proven: **Manual resume screening consumes 16.5 days (34.4% of the 48-day hiring cycle)**, causing top candidates to drop off and plunging offer acceptance by 29.5 points.

Task 2 will directly target this bottleneck by prototyping and deploying an **Automated AI Resume Screening and Triage System** designed to compress the screening stage to **< 48 hours** and recover offer acceptance rates to > 80%.
