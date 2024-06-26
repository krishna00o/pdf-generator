import pandas
from fpdf import FPDF
import pandas as pd

# lines = [23,33,43,53,63,73,83,93,103,113,123,133,143,153,163,173,183
#         ,193,203,213,223,233,243,253,263,273]

pdf = FPDF(orientation='p', unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

dv = pd.read_csv("topics.csv")

for index, rows in dv.iterrows():
    pdf.add_page()

    # Add the header
    pdf.set_fill_color(254, 0, 0)
    pdf.set_font(family="Helvetica", style="B", size=25)
    pdf.cell(w=0, h=13, txt=rows["Topic"], ln=1, align='L')

    # Giving the co-ordinates of the line
    # pdf.line(10,23,200,23)

    # Add the footer
    pdf.ln(265)
    pdf.set_fill_color(180, 180, 180)
    pdf.set_font(family="Helvetica", style="I", size=10)
    pdf.cell(h=10, w=0, ln=1, align="R", txt=rows["Topic"])

    for y in range(23, 273, 10):
        pdf.line(10, y, 200, y)

    for i in range(rows['Pages'] - 1):
        pdf.add_page()

        for y in range(23, 273, 10):
            pdf.line(10, y, 200, y)

        # Add the footer
        pdf.ln(277)
        pdf.set_fill_color(180, 180, 180)
        pdf.set_font(family="Helvetica", style="I", size=10)
        pdf.cell(h=10, w=0, ln=1, align="R",txt=rows['Topic'])


pdf.output('output.pdf')


