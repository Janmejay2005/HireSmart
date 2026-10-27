# HireSmart AI Tool & Prompt Governance Log
**Project:** HireSmart for TalentBridge  
**Lead Custodian:** Employer Brand & Tools Lead (*Amina Al-Mansoor*)  
**Governance Standard:** Section 3.4 & FR-5 Compliance  
**Source Dataset:** [`AI_Prompt_Log.csv`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/05_Prompt_Log/AI_Prompt_Log.csv)  

---

## 1. AI Governance & Prompt Integrity Policy
Under the HireSmart charter:
1. **Verifiable Calculations:** All analytical metrics and numbers must be derived deterministically via verified Python/Pandas logic and spreadsheet formulas. AI tools may not synthesize or hallucinate baseline numbers.
2. **Traceability:** Every prompt generating project documentation, summaries, or analytical frameworks must be logged with timestamp, tool, full prompt text, output summary, owner, and usage status.
3. **Privacy & Data Security:** No candidate personally identifiable information (PII) is ever submitted to AI models. Only anonymized, aggregated datasets are analyzed.

---

## 2. Master Prompt Register

| Date | Tool | Prompt Summary | Output Summary | Used / Discarded | Owner |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **2026-10-27** | Gemini 3.8 Flash | Draft executive project brief summary for HireSmart covering objectives, stakeholder analysis, budget constraints. | Generated structured 6-section brief summary with clear table layouts and success criteria. | **Used** | Elena Vance |
| **2026-10-27** | Gemini 3.8 Flash | Design 5-role RACI governance matrix and team workflow handoff specification for HireSmart Task 1. | Produced full RACI table across all 5 named roles with step-by-step handoff triggers. | **Used** | Elena Vance |
| **2026-10-27** | Gemini 3.8 Flash | Structure shared Google Drive and Notion task board architecture for HR project diagnostics adhering to strict RBAC. | Detailed folder blueprint (01 to 05) with permission matrix and Kanban lifecycle states. | **Used** | Amina Al-Mansoor |
| **2026-10-27** | Gemini 3.8 Flash | Generate audit protocol for raw applicant tracking data to detect anomalies, nulls, and formatting inconsistencies. | Formulated 7-step data hygiene framework covering duplicate checks, month consistency, and rate verification. | **Used** | David Chen |
| **2026-10-27** | Gemini 3.8 Flash | Write Python formulas for Offer Acceptance Rate, Early Exit Rate, Source Effectiveness, Recruiter Load, and Screening Burden. | Delivered verified mathematical functions and Pandas aggregation logic aligned with PRD Section 8. | **Used** | David Chen |
| **2026-10-27** | Gemini 3.8 Flash | Analyze correlation between recruiter workload (open reqs/applications) and time-to-hire delays. | Identified positive correlation (r=0.87) demonstrating that recruiter overload directly inflates screening duration. | **Used** | Marcus Brody |
| **2026-10-27** | Gemini 3.8 Flash | Synthesize qualitative candidate drop-off patterns and early exit drivers across sourcing channels. | Demonstrated that Job Board sourcing has highest early exit rate (26.4%) vs Referrals (4.3%) due to expectation mismatch. | **Used** | Sophia Rodriguez |
| **2026-10-27** | Gemini 3.8 Flash | Draft 1-page executive Hiring Data Insights Report synthesizing metrics, ranked bottlenecks, and Task 2 recommendations. | Synthesized headline, key metric summary table, 5 quantified findings, and prioritized bottleneck matrix. | **Used** | David Chen |
