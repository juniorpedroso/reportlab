from reportlab.platypus import Table, Image


def genHeaderTable(width, height):

    widthList = [
        width * 55 / 100,  # col 1 - Imagem da esquerda
        width * 45 / 100,  # col 2 - Imagem da direita
        0,
    ]

    leftImagePath = 'resources\paradiseHotel.jpg'
    leftImageWidth = widthList[0]
    leftImage = Image(leftImagePath, leftImageWidth, height)

    rightImagePath = 'resources\logoParadise.png'
    rightImageWidth = widthList[1]
    rightImage = Image(
        rightImagePath, rightImageWidth, height,
        kind='proportional')

    rightText = 'HOTEL'

    res = Table([
        [leftImage, rightImage, rightText]
    ],
        widthList, height)

    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),

        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),

        ('ALIGN', (1, 0), (1, 0), 'CENTER'),  # Alinhamento Horizontal
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),  # Alinhamento Vertical

        ('FONTSIZE', (2, 0), (2, 0), 20),
        # Isto faz com que a terceira coluna, com o texto HOTEL apareça
        ('LEFTPADDING', (2, 0), (2, 0), -widthList[1] + 98),
        ('BOTTOMPADDING', (2, 0), (2, 0), 40),

    ])
    return res
