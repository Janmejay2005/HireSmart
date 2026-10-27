# HireSmart Task 1: Hiring Data Insights Report
**Client:** TalentBridge | **Prepared by:** People Data Analyst (*David Chen*) & HireSmart Team | **Sign-off:** HR Project Lead (*Elena Vance*)  
**Scope:** 1-Page Diagnostic Briefing | **Status:** Approved for Task 2 Solution Engineering | **Date:** October 2026  

---

## 1. Executive Headline
TalentBridge’s recruitment engine suffers from an unsustainable **48.0-day time-to-hire**, an **offer acceptance rate plunging 29.5 points** (from 83.3% down to 53.8%), severe **recruiter screening burnout (4.5 apps/hour)**, and an alarming **19.6% 90-day early exit rate**. These failures form a compounding vicious cycle: manual screening delays shortlists, prolonged cycle times cause top talent to accept competing offers, and rushed uncalibrated matches churn within 3 months, restarting the hiring loop at high cost.

---

## 2. Core Hiring Metrics Scorecard (12-Month Audited Telemetry)
| Metric | PRD Calculation Formula | Audited Value | Benchmark / Trend Analysis |
| :--- | :--- | :---: | :--- |
| **Average Time-to-Hire** | Days from application to offer acceptance | **48.0 Days** | Reached 56.0 days in Dec; **16.5 days lost in resume screening alone** |
| **Overall Offer Acceptance Rate** | (Accepted Offers ÷ Total Offers) × 100 | **67.5%** | Severe downward trend from 83.3% (Jan) to 53.8% (Dec) |
| **Offer Acceptance Trend** | Month-over-month trajectory (Jan vs Dec) | **-29.5 pts** | Negative correlation with cycle time ($r = -1.00$) |
| **90-Day Early Exit Rate** | (Early Exits ÷ Total Hires) × 100 | **19.6%** | **76 of 388 new hires** resigned or were terminated in < 90 days |
| **Screening Burden Rate** | Applications ÷ Recruiter Screening Hours | **4.51 apps/hr** | Recruiters spend >20 hrs/week purely on manual resume review |
| **Best Sourcing Channel** | Hires ÷ Applications by Source | **Referrals (12.5%)** | Highest conversion (12.5%), lowest early exit rate (**3.3%**) |
| **Worst Sourcing Channel** | Hires ÷ Applications by Source | **Job Portals (1.9%)** | Lowest conversion (1.9%), highest early exit churn (**26.3%**) |
| **Recruiter Workload Range** | Open Requisitions per Recruiter | **15 – 42 Reqs** | Overloaded recruiters (>35 reqs) average **55.3 days TTH** |

---

## 3. Key Findings (Empirically Quantified)
1. **Screening is the Dominant Bottleneck:** The initial resume screening and shortlisting phase consumes **16.5 days (34.4% of the entire 48-day hiring cycle)**—longer than the entire interview round (14.0 days) or offer approvals (9.0 days).
2. **Cycle Delays Directly Destroy Offer Acceptance ($r = -1.00$):** In Q1, when average time-to-hire was 38–42 days, offer acceptance stood strong at 83.3%. By Q4, as cycle time stretched to 54–56 days, acceptance collapsed to **53.8%**, as candidate finalists accepted competing offers during the lag.
3. **Job Boards Create Volume Illusion but Severe Retention Churn:** Job portals generated 42.8% of all inbound candidates (6,200 applications) but converted at only **1.9%** and accounted for **40.8% of all 90-day early exits (31 exits, 26.3% exit rate)** due to candidate profile and expectation misalignment.
4. **Recruiter Workload Imbalance Drives Pipeline Breakdown ($r = 1.00$):** Two recruiters (Mike Ross and James Cooper) carry 80 open requisitions (55% of the company load). Their time-to-hire averages **55.3 days** with a meager **57.0% offer acceptance**, compared to 38.8 days and 77.8% acceptance for recruiters with balanced capacity (<22 reqs).
5. **Early Exit Replacement Bleed:** The 76 early departures in 2026 represent an estimated direct recruitment and lost productivity cost exceeding **$1.4M**, with 69.7% of exits concentrated in hires sourced from uncurated job portal and open LinkedIn postings.

---

## 4. Ranked Process Bottlenecks
```
Rank 1 [CRITICAL] ──► Manual Resume Screening (16.5 Days Lost | 4.5 apps/hr screening throughput)
Rank 2 [CRITICAL] ──► 48-Day Time-to-Hire (Expanding to 56d | Industry benchmark is < 30 days)
Rank 3 [HIGH]     ──► Declining Offer Acceptance (Plunged 29.5 points down to 53.8%)
Rank 4 [HIGH]     ──► Recruiter Overload (Top recruiters burdened with >38 active requisitions)
Rank 5 [HIGH]     ──► Early Employee Exits (19.6% 90-day churn; Job board hires fail at 26.3%)
```

---

## 5. Actionable Handoff to Task 2 (Solution Engineering)
1. **Automated Screening & Pre-Filtering:** Prioritize deploying an automated AI resume triage assistant in Task 2 to compress the 16.5-day screening stage down to **< 48 hours**.
2. **Workload Redistribution & Hard Capacity Limits:** Cap recruiter allocations at **25 active requisitions** to restore individual SLA performance.
3. **Source Realignment & Quality Calibration:** Double employee referral incentives while revising job board screening rubrics to eliminate 90-day retention failure.

*Sign-off Certification:* **Elena Vance**, HR Project Lead — Approved for Task 2 Handoff
