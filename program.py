# aprendendo reportlab com Hugo Ferro, canal AllTech

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table

from header import genHeaderTable
from body import genBodyTable
from footer import genFooterTable


pdf = canvas.Canvas('report.pdf', pagesize=A4)
pdf.setTitle('Palms Hotel')

width, height = A4

heightList = [

    height * 20 / 100,  # header
    height * 77 / 100,  # body
    height * 3 / 100,   # footer
]

mainTable = Table([
    [genHeaderTable(width, heightList[0])],
    [genBodyTable(width, heightList[1])],
    [genFooterTable(width, heightList[2])],
],
    colWidths=width,
    rowHeights=heightList
)

mainTable.setStyle([
    # ('GRID', (0, 0), (-1, -1), 1, 'red'),

    ('LEFTPADDING', (0, 0), (0, 2), 0),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),

])

mainTable.wrapOn(pdf, 0, 0)
mainTable.drawOn(pdf, 0, 0)

pdf.showPage()

pdf.save() 
