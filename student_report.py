from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import pandas as pd

df = pd.read_csv("student_marks.csv")

average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

doc = SimpleDocTemplate("student_report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []

elements.append(Paragraph("<b>Automated Student Performance Report</b>", styles["Title"]))
elements.append(Paragraph("This report is generated automatically using Python.", styles["Normal"]))

elements.append(Paragraph("<b>Summary Analysis</b>", styles["Heading2"]))
elements.append(Paragraph(f"Average Marks: {average_marks:.2f}", styles["Normal"]))
elements.append(Paragraph(f"Highest Marks: {highest_marks}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Marks: {lowest_marks}", styles["Normal"]))

elements.append(Paragraph("<b>Student Marks Table</b>", styles["Heading2"]))

table_data = [df.columns.tolist()] + df.values.tolist()
table = Table(table_data)

table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("GRID", (0,0), (-1,-1), 1, colors.black),
    ("ALIGN", (1,1), (-1,-1), "CENTER")
]))

elements.append(table)
doc.build(elements)

print("PDF Report Generated Successfully!")
