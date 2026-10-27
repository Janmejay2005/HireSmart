# HireSmart Notion Task Board Tracking System
**Project:** HireSmart for TalentBridge — Task 1  
**Managed by:** HR Project Lead (*Elena Vance*)  
**Source Dataset:** [`notion_board_tasks.csv`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/01_Brief/notion_board_tasks.csv)  

---

## 1. Kanban Board State Architecture
The Notion workspace enforces a 4-stage pipeline transition:
* **Backlog:** Tasks scoped and prioritized with clear success criteria.
* **In Progress:** Actively underway by assigned owner.
* **Review:** Work completed and deliverable file linked; awaiting reviewer QA.
* **Done:** Formally approved by reviewer with zero open defects.

---

## 2. Live Task Board Status Snapshot

### 🟢 Completed (Done)
| Task ID | Card Title | Owner | Phase | Priority | Linked Deliverable | Reviewer |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TSK-01** | Digest Project Brief & Define Success Targets | Elena Vance | Phase 1 | Must | [Project_Brief_Summary.md](file:///c:/Users/HP/Desktop/Python%20File/Task%201/01_Brief/Project_Brief_Summary.md) | Elena Vance |
| **TSK-02** | Establish Role Matrix & RACI Governance | Elena Vance | Phase 2 | Must | [Role_Assignment_Matrix.md](file:///c:/Users/HP/Desktop/Python%20File/Task%201/01_Brief/Role_Assignment_Matrix.md) | Elena Vance |
| **TSK-03** | Configure Drive Folders & Access Permissions | Amina Al-Mansoor | Phase 3 | Must | [Workspace_Setup_Guide.md](file:///c:/Users/HP/Desktop/Python%20File/Task%201/01_Brief/Workspace_Setup_Guide.md) | Elena Vance |
| **TSK-04** | Initialize Notion Kanban Board & Prompt Log | Amina Al-Mansoor | Phase 3 | Must | [AI_Prompt_Log.md](file:///c:/Users/HP/Desktop/Python%20File/Task%201/05_Prompt_Log/AI_Prompt_Log.md) | Elena Vance |
| **TSK-05** | Data Ingestion & Integrity Auditing | David Chen | Phase 4 | Must | [raw_talentbridge_hiring_data.csv](file:///c:/Users/HP/Desktop/Python%20File/Task%201/02_Data/raw_talentbridge_hiring_data.csv) | Elena Vance |
| **TSK-06** | Execute Data Cleansing & Normalization | David Chen | Phase 4 | Must | [cleaned_talentbridge_hiring_data.csv](file:///c:/Users/HP/Desktop/Python%20File/Task%201/03_Analysis/cleaned_talentbridge_hiring_data.csv) | Elena Vance |
| **TSK-07** | Compute Core Hiring Metrics & Formulas | David Chen | Phase 4 | Must | [hiring_metrics_summary.xlsx](file:///c:/Users/HP/Desktop/Python%20File/Task%201/03_Analysis/hiring_metrics_summary.xlsx) | Elena Vance |
| **TSK-08** | Sourcing Channel Effectiveness Analysis | Marcus Brody | Phase 4 | Must | [hiring_metrics_summary.xlsx](file:///c:/Users/HP/Desktop/Python%20File/Task%201/03_Analysis/hiring_metrics_summary.xlsx) | David Chen |
| **TSK-09** | Recruiter Workload & Screening Burden Audit | Marcus Brody | Phase 4 | Must | [hiring_metrics_summary.xlsx](file:///c:/Users/HP/Desktop/Python%20File/Task%201/03_Analysis/hiring_metrics_summary.xlsx) | David Chen |
| **TSK-10** | Offer Acceptance Drop-Off & Exit Root Cause | Sophia Rodriguez | Phase 4 | Must | [hiring_metrics_summary.xlsx](file:///c:/Users/HP/Desktop/Python%20File/Task%201/03_Analysis/hiring_metrics_summary.xlsx) | David Chen |
| **TSK-11** | Generate High-Res Trend Visualizations | David Chen | Phase 4 | Should | [charts/](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/charts/) | Elena Vance |
| **TSK-12** | Rank Bottlenecks & Synthesize Findings | Working Group | Phase 4 | Must | [HireSmart_Task1_Hiring_Insights_Report.md](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/HireSmart_Task1_Hiring_Insights_Report.md) | Elena Vance |
| **TSK-13** | Draft 1-Page Executive Insights Report | David Chen | Phase 5 | Must | [HireSmart_Task1_Hiring_Insights_Report.md](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/HireSmart_Task1_Hiring_Insights_Report.md) | Elena Vance |
| **TSK-14** | Executive QA Sign-off & Task 2 Handoff | Elena Vance | Phase 5 | Must | [HireSmart Task 1 Hiring Data Insights Report.docx](file:///c:/Users/HP/Desktop/Python%20File/Task%201/04_Reports/HireSmart_Task1_Hiring_Insights_Report.docx) | Elena Vance |

---

## 3. Notion Board Integration Instructions
1. Open your team Notion Workspace.
2. Select **Import** -> **CSV** -> Choose [`01_Brief/notion_board_tasks.csv`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/01_Brief/notion_board_tasks.csv).
3. Switch view to **Board View** grouped by `Status` (`Backlog`, `In Progress`, `Review`, `Done`).
4. Apply card filters for `Owner` and `Priority`.
