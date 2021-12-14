from reportlab.platypus import Table
from reportlab.lib import colors


def genFooterTable(width, height):

    text = 'Root 66, 8543 Dubai - Tlf.: +43 78 11 41 00 - ' + \
            'Email: palmsbeach@palms.com - www.palmshotel.com'

    color = colors.HexColor('#003363')

    res = Table([[text]], width, height)

    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

        ('BACKGROUND', (0, 0), (-1, -1), color),
        ('TEXTCOLOR', (0, 0), (-1, -1), 'white'),

    
    ])

    return res
