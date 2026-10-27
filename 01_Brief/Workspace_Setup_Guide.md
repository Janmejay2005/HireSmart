# HireSmart Workspace & Governance Setup Guide
**Project:** HireSmart for TalentBridge  
**Owner:** Employer Brand & Tools Lead (*Amina Al-Mansoor*)  
**Scope:** Phase 3 Infrastructure & Environment Configuration  
**Status:** Completed & Operational  

---

## 1. Directory & Google Drive Architecture
The workspace is structured into 5 standard operational directories mapped to the project lifecycle:

```text
HireSmart-Task1/
├── 01_Brief/          # Project charter, PRD, role allocations, Notion task schema
├── 02_Data/           # Raw intake records, uncleaned CSV/Excel datasets, cleaning logs
├── 03_Analysis/       # Cleaned datasets, metric calculation engines, formulas, models
├── 04_Reports/        # Final 1-page reports, executive briefings, visualizations
│   └── charts/        # High-resolution PNG visualizations (trends, sources, workloads)
├── 05_Prompt_Log/     # Standardized prompt governance logs (Markdown and CSV)
├── scripts/           # Python automation scripts (cleaning, analytics, chart generators)
└── dashboard/         # Interactive executive web dashboard
```

---

## 2. Access Control & Permission Matrix (Google Drive & Notion)
To balance security, compliance, and velocity, role-based access control (RBAC) is enforced:

| Workspace Area | HR Project Lead | People Data Analyst | TA Lead | Tools Lead | Candidate Exp Lead | Executive Stakeholders |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **01_Brief** | Admin / Edit | View | View | Edit | View | View Only |
| **02_Data (Raw)** | View | Edit / Lock | View | View | View | No Access |
| **03_Analysis** | View | Admin / Edit | View | View | View | View Only |
| **04_Reports** | Admin / Edit | Edit | Edit | Edit | Edit | View / Comment |
| **05_Prompt_Log** | View | Edit | Edit | Admin / Edit | Edit | View Only |
| **Notion Board** | Admin / Manage | Full Edit | Full Edit | Full Edit | Full Edit | View / Comment |

---

## 3. Approved AI Tooling & Governance Protocol
Under budget requirements (FR-5), all AI integrations use compliant, zero-cost / free-tier tools:

1. **Google Gemini / OpenAI ChatGPT Free Tiers:** Used strictly for text synthesis, drafting summaries, and role play testing.
2. **Google Sheets / Python with Pandas:** Primary statistical and metric computation engine to eliminate hallucinations.
3. **Matplotlib & Seaborn:** Generation of publication-grade charts.
4. **Prompt Log Enforcement:** Every team member must record their AI interactions into `05_Prompt_Log/AI_Prompt_Log.csv` before outputs can be cited in final reports.
