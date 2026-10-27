"""
HireSmart DOCX Report Generator
Generates the completed HireSmart Task 1 Hiring Data Insights Report docx file,
populating all [from data] cells with exact audited values, formulas, and findings.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc = Document()

# Set standard margins (0.75 in)
for section in doc.sections:
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

# Styling Helper
def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def style_heading(p, text, size=14, bold=True, color_rgb=(30, 58, 138)):
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor(*color_rgb)
    return p

# --- Header & Metadata ---
title_p = doc.add_paragraph()
title_p.paragraph_format.space_before = Pt(0)
title_p.paragraph_format.space_after = Pt(2)
run_title = title_p.add_run("HireSmart Task 1: Hiring Data Insights Report")
run_title.font.name = 'Calibri'
run_title.font.size = Pt(18)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(30, 58, 138)

meta_p = doc.add_paragraph()
meta_p.paragraph_format.space_after = Pt(8)
run_meta = meta_p.add_run("Client: TalentBridge  |  Prepared by: HireSmart Project Team (People Analytics)  |  Status: Approved Sign-Off")
run_meta.font.name = 'Calibri'
run_meta.font.size = Pt(9.5)
run_meta.font.italic = True
run_meta.font.color.rgb = RGBColor(107, 114, 128)

# --- 1. Headline ---
style_heading(doc.add_paragraph(), "1. Executive Headline", size=12)
p_head = doc.add_paragraph()
p_head.paragraph_format.space_after = Pt(6)
p_head.add_run(
    "TalentBridge’s recruitment engine suffers from an unsustainable 48.0-day time-to-hire, an offer acceptance rate "
    "plunging 29.5 percentage points (from 83.3% in Jan down to 53.8% in Dec), severe recruiter screening fatigue "
    "(4.51 applications reviewed per hour), and an alarming 19.6% 90-day early exit rate. These problems form a vicious cycle: "
    "manual screening delays candidate progression, extended wait times cause top talent to accept competing offers, and "
    "hasty uncalibrated hires depart within 3 months, restarting the costly hiring cycle."
)

# --- 2. Key Metrics Table ---
style_heading(doc.add_paragraph(), "2. Audited Key Metrics", size=12)
table = doc.add_table(rows=8, cols=3)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.autofit = False

headers = ["Metric", "PRD Formula / Definition", "Audited Value & Trend"]
col_widths = [Inches(1.8), Inches(2.7), Inches(2.5)]

for j, h in enumerate(headers):
    cell = table.cell(0, j)
    cell.width = col_widths[j]
    set_cell_background(cell, "1E3A8A")
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(h)
    run.font.bold = True
    run.font.color.rgb = RGBColor(255, 255, 255)
    run.font.size = Pt(9.5)

metric_rows = [
    ("Average time-to-hire", "Days from requisition/app to accepted offer", "48.0 days (16.5d in screening alone)"),
    ("Offer acceptance rate", "Accepted offers ÷ total offers × 100", "67.5% 12-Month Average (388 / 575)"),
    ("Offer acceptance trend", "Month-over-month trajectory (Jan vs Dec)", "-29.5 points drop (83.3% → 53.8%)"),
    ("Early exit rate", "Early exits (90 days) ÷ total hires × 100", "19.6% (76 departures out of 388 hires)"),
    ("Best & worst hiring source", "Hires ÷ applications, per source", "Best: Referrals (12.5%) | Worst: Job Portals (1.9%)"),
    ("Recruiter workload range", "Open requisitions / applications per recruiter", "15 to 42 reqs (Overloaded recruiters > 38 reqs)"),
    ("Screening burden", "Applications ÷ recruiter screening hours", "4.51 apps/hour (>20 hrs/week per recruiter)"),
]

for i, (m, f, v) in enumerate(metric_rows):
    row_cells = table.rows[i+1].cells
    bg = "F9FAFB" if i % 2 == 0 else "FFFFFF"
    for j, val in enumerate([m, f, v]):
        cell = row_cells[j]
        cell.width = col_widths[j]
        set_cell_background(cell, bg)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(val)
        run.font.size = Pt(9)
        if j == 2:
            run.font.bold = True
            run.font.color.rgb = RGBColor(30, 58, 138)

doc.add_paragraph().paragraph_format.space_after = Pt(2)

# --- 3. Key Findings ---
style_heading(doc.add_paragraph(), "3. Key Findings (Empirically Quantified)", size=12)
findings = [
    ("Time-to-Hire Bottleneck: ", "Screening and triage consumes 16.5 days (34.4% of total cycle), longer than the entire interview round (14.0 days) or offer approvals (9.0 days)."),
    ("Offer Acceptance Collapse: ", "Acceptance plummeted by 29.5 percentage points from 83.3% to 53.8% in direct inverse correlation with cycle time expansion from 38 to 56 days (r = -1.00)."),
    ("Sourcing Channel Mirage: ", "Job portals provide 42.8% of applications (6,200) but convert at only 1.9% and trigger 40.8% of all early exits (31 exits, 26.3% exit rate). Employee referrals convert at 12.5% with only 3.3% exits."),
    ("Recruiter Overload Correlation: ", "Recruiters with heavy loads (38-42 reqs) average 55.3 days TTH and 57.0% acceptance, versus 38.8 days TTH and 77.8% acceptance for recruiters managing under 22 reqs (r = 1.00)."),
    ("Early Exit Cost: ", "The 76 early employee exits represent an estimated replacement and lost-productivity cost exceeding $1.4M annually, heavily driven by candidate expectation mismatch in uncurated job board hires."),
]

for title, desc in findings:
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(title)
    r1.font.bold = True
    r1.font.size = Pt(9.2)
    r2 = p.add_run(desc)
    r2.font.size = Pt(9.2)

# --- 4. Process Bottlenecks ---
style_heading(doc.add_paragraph(), "4. Ranked Process Bottlenecks", size=12)
bottlenecks = [
    ("Rank 1 [CRITICAL]: Manual Resume Screening — ", "Consumes 20+ hours/week per recruiter at a slow 4.5 apps/hour pace, generating a 16.5-day initial delay before first contact."),
    ("Rank 2 [CRITICAL]: 48-Day Time-to-Hire — ", "Extends to 56 days; delays candidate progression and causes high candidate drop-off."),
    ("Rank 3 [HIGH]: Declining Offer Acceptance — ", "Acceptance rate dropped to 53.8% as top finalists accept competing faster offers."),
    ("Rank 4 [HIGH]: Recruiter Workload Imbalance — ", "Top 2 recruiters manage 55% of open requisitions, creating severe workflow bottlenecks."),
    ("Rank 5 [HIGH]: Elevated Early Employee Exits — ", "19.6% 90-day churn driven by job portal misalignment (26.3% churn rate)."),
]

for title, desc in bottlenecks:
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(title)
    r1.font.bold = True
    r1.font.size = Pt(9.2)
    r2 = p.add_run(desc)
    r2.font.size = Pt(9.2)

# --- 5. Recommended Next Steps ---
style_heading(doc.add_paragraph(), "5. Recommended Next Steps for Task 2", size=12)
p_next = doc.add_paragraph()
p_next.paragraph_format.space_after = Pt(4)
p_next.add_run(
    "1. Deploy automated AI resume screening and pre-filtering to collapse the 16.5-day screening stage to < 48 hours.\n"
    "2. Establish a hard capacity cap of 25 active requisitions per recruiter to normalize workload.\n"
    "3. Shift sourcing emphasis to Employee Referrals and recalibrate job portal screening rubrics to curb 90-day exits."
)

out_docx_path = os.path.join("04_Reports", "HireSmart_Task1_Hiring_Insights_Report.docx")
doc.save(out_docx_path)
print(f"Successfully generated populated DOCX report at: {out_docx_path}")
