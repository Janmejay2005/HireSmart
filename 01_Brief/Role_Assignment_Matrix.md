# HireSmart Role Assignment & RACI Matrix
**Project:** HireSmart for TalentBridge  
**Phase:** Task 1 — Kickoff & Problem Analysis  
**Owner:** HR Project Lead  
**Document Version:** 1.0 (Confirmed)  

---

## 1. Project Team Roster & Ownership
The HireSmart project operates across five core functional roles. Every task, artifact, and review step is assigned to an accountable owner.

| Role | Named Owner | Department | Key Responsibility in Task 1 | Core Deliverable |
| :--- | :--- | :--- | :--- | :--- |
| **HR Project Lead** | *Elena Vance* | People Operations | Project governance, stakeholder alignment, timeline, task board orchestration, final QA and sign-off. | `Project_Brief_Summary.md`, Approved Final Insights Report |
| **People Data Analyst** | *David Chen* | People Analytics | Data audit, cleansing, quantitative metric formulas, trend modeling, statistical correlation, report drafting. | `cleaned_talentbridge_hiring_data.csv`, `hiring_metrics_summary.xlsx`, Draft 1-Page Report |
| **Talent Acquisition Lead** | *Marcus Brody* | Talent Acquisition | Sourcing channel performance audit, recruiter workload evaluation, screening bottleneck diagnosis. | Sourcing channel findings & Recruiter workload assessment |
| **Employer Brand & Tools Lead** | *Amina Al-Mansoor* | HR Tech & Operations | Workspace architecture, permission control, AI prompt logging governance, analytics tooling setup. | Configured Workspace, AI Tool Registry, `AI_Prompt_Log` |
| **Candidate Experience Lead** | *Sophia Rodriguez* | Employee Experience | Offer acceptance decline analysis, candidate journey friction mapping, early exit root-cause evaluation. | Candidate drop-off findings & Early exit review |

---

## 2. RACI Governance Matrix
* **R (Responsible):** The role that completes the work.
* **A (Accountable):** The single decision-maker who approves the work.
* **C (Consulted):** Key stakeholder providing inputs and validation.
* **I (Informed):** Updated on status and deliverables.

| Task / Deliverable | HR Project Lead | People Data Analyst | TA Lead | Tools Lead | Candidate Exp Lead |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **FR-1: Brief Summary** | **A / R** | C | C | I | C |
| **FR-2: Role Matrix & RACI** | **A / R** | C | C | C | C |
| **FR-3: Workspace & Permissions Setup** | A | I | I | **R** | I |
| **FR-4: Notion Task Board Management** | **A / R** | C | C | C | C |
| **FR-5: AI Prompt Log Governance** | A | C | C | **R** | C |
| **FR-6: Raw Data Cleaning & Verification** | A | **R** | C | I | I |
| **FR-7: Hiring Metric Calculations** | A | **R** | C | I | C |
| **FR-8: Trend Visualizations & Charts** | A | **R** | C | I | I |
| **FR-9: Bottleneck Ranking & Synthesis** | A | C | **R** | I | **R** |
| **FR-10: 1-Page Insights Report Draft** | A | **R** | C | I | C |
| **Final Executive Sign-Off** | **A / R** | I | I | I | I |

---

## 3. Workflow Handoff Protocol
The Task 1 operational pipeline relies on strict sequential and parallel handoffs:

```
[Elena: Brief & Roles] 
          │
          ▼
[Amina: Workspace Setup & Prompt Log Active]
          │
          ▼
[David: Data Intake, Cleaning & Metric Calculations]
          ├───────────────────────────────┐
          ▼                               ▼
[Marcus: Sourcing & Workload]    [Sophia: Offer Drop-off & Exits]
          │                               │
          └───────────────┬───────────────┘
                          ▼
            [David: Draft 1-Page Report]
                          │
                          ▼
         [Elena: Quality Audit & Executive Sign-off]
                          │
                          ▼
                  [Handoff to Task 2]
```

### Detailed Handoff Specifications:
1. **Brief & Setup → Data Ingestion:**
   - *Sender:* Tools Lead (Amina) & HR Lead (Elena)
   - *Recipient:* People Data Analyst (David)
   - *Artifact:* Operational folder structure (`01`–`05`), raw dataset in `02_Data`, active Notion board cards.
2. **Data Cleaning → Deep-Dive Leads:**
   - *Sender:* People Data Analyst (David)
   - *Recipients:* TA Lead (Marcus) & Candidate Experience Lead (Sophia)
   - *Artifact:* `cleaned_talentbridge_hiring_data.csv`, verified metrics sheet with clean timestamps and standardized categories.
3. **Domain Findings → Report Synthesis:**
   - *Senders:* TA Lead (Marcus) & Candidate Experience Lead (Sophia)
   - *Recipient:* People Data Analyst (David)
   - *Artifact:* Key bulleted observations on recruiter workload limits and source-driven exit rates.
4. **Report Draft → Final Approval:**
   - *Sender:* People Data Analyst (David)
   - *Recipient:* HR Project Lead (Elena)
   - *Artifact:* Complete 1-Page Hiring Insights Report (Markdown, HTML, DOCX) with all data fields populated.
