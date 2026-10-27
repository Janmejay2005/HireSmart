# TalentBridge Data Cleaning & Verification Log
**Project:** HireSmart for TalentBridge — Task 1  
**Lead Auditor:** People Data Analyst (*David Chen*)  
**Source Datasets:**  
- `02_Data/raw_talentbridge_hiring_data.csv`  
- `02_Data/raw_talentbridge_sourcing_data.csv`  
- `02_Data/raw_talentbridge_recruiter_data.csv`  
**Cleaned Destination:** `03_Analysis/cleaned_talentbridge_hiring_data.csv`  
**Execution Timestamp:** 2026-10-27  

---

## 1. Data Intake & Integrity Audit
The raw hiring dataset was ingested and subjected to systematic data quality checks across five dimensions: completeness, uniqueness, consistency, validity, and integrity.

| Audit Dimension | Condition Tested | Result in Raw Dataset | Remediation Action Taken |
| :--- | :--- | :--- | :--- |
| **Duplicates** | Exact row duplication across all columns | 1 duplicated record detected (Row index 3 / Month 2026-04 duplicated at Row 13). | Deduplicated dataframe using `.drop_duplicates()`. Initial row count: 13, Final row count: 12. |
| **Date Formatting** | Consistency of ISO standard `YYYY-MM` format | Inconsistent slash delimiter and trailing whitespace found in index 5 (`"2026/06 "`). | Sanitized string format using `.str.strip().str.replace("/", "-")` to normalize to `"2026-06"`. |
| **Data Types & Units** | Numeric columns stored as numeric vs string | `Applications` column at index 10 stored as string `"1,250"` with thousands comma separator. | Stripped comma delimiters and cast column to integer (`int64`). |
| **Continuity of Timeline** | Missing or non-sequential months | Verified 12 consecutive months from `2026-01` through `2026-12`. | Confirmed zero gaps in time horizon. |
| **Mathematical Logic** | Sanity checks (`Offers_Accepted <= Offers_Extended <= Interviews <= Applications`) | Verified across all rows: all subsets adhere strictly to funnel constraints. | Zero violations detected. |

---

## 2. Cleansing Pipeline Code Reference
Data cleaning is fully automated and reproducible via [`scripts/generate_and_clean_data.py`](file:///c:/Users/HP/Desktop/Python%20File/Task%201/scripts/generate_and_clean_data.py).

```python
# Cleaning operations executed:
df_clean = df_raw.drop_duplicates().copy()
df_clean["Month"] = df_clean["Month"].str.strip().str.replace("/", "-")
df_clean["Applications"] = df_clean["Applications"].astype(str).str.replace(",", "").astype(int)
df_clean = df_clean.sort_values("Month").reset_index(drop=True)
```

---

## 3. Data Schema & Dictionary (Cleaned Dataset)
| Column Name | Data Type | Definition & PRD Alignment |
| :--- | :--- | :--- |
| `Month` | `string` (`YYYY-MM`) | Calendar month of recruitment activity. |
| `Applications` | `integer` | Total inbound applications received across all channels. |
| `Screening_Hours` | `integer` | Aggregate recruiter hours devoted strictly to first-pass resume review. |
| `Screened` | `integer` | Count of resumes reviewed by recruiting staff. |
| `Interviews` | `integer` | Candidates advancing to structured recruiter/hiring manager interviews. |
| `Offers` | `integer` | Total formal job offers extended to finalists. |
| `Accepted` | `integer` | Formal job offers accepted by candidates. |
| `Early_Exits_90d` | `integer` | New hires resigning or terminated within first 90 days. |
| `Avg_TTH_Days` | `float` | Days from requisition/application to offer acceptance (PRD benchmark = 48.0d). |
| `Screening_Days` | `float` | Average days spent in resume screening and candidate shortlisting. |
| `Interview_Days` | `float` | Average days spent scheduling and conducting interview rounds. |
| `Approval_Days` | `float` | Average days required for hiring manager and HR compensation approvals. |
| `Offer_Days` | `float` | Average days from offer formulation to candidate decision. |

---

## 4. Auditor Certification
The cleaned dataset has been verified against PRD constraints and is locked for Phase 4 metric calculations.  
*Certified by:* **David Chen**, People Data Analyst  
*Approved by:* **Elena Vance**, HR Project Lead  
