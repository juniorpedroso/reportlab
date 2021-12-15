from reportlab.lib import colors
from reportlab.platypus import Table, Image
from reportlab.platypus import Table, Paragraph
from reportlab.lib.styles import ParagraphStyle
import csv


def genBodyTable(width, height):

    widthList = [
        width * 10 / 100,  # col 0 - Left Padding
        width * 80 / 100,  # col 1 - Valores
        width * 10 / 100,  # col 2 - Right Padding

    ]

    heightList = [
        height * 10 / 100,  # linha 0 - offer
        height * 15 / 100,  # linha 1 - contacts
        height * 35 / 100,  # linha 2 - price list
        height * 30 / 100,  # linha 3 - description
        height * 10 / 100,  # linha 4 - about table
    ]

    leftPadding = 20
    tablesWidth = widthList[1] - leftPadding

    res = Table([
        ['', 'Offer', ''],
        ['', _genContactsTable(tablesWidth, heightList[1]), ''],
        ['', _genPriceListTable(tablesWidth, heightList[2]), ''],
        ['', _genDescriptionParasTable(), ''],
        ['', _genAboutTable(widthList[1], heightList[4]), ''],

    ],
        widthList,
        heightList
    )

    color = colors.HexColor('#003363')

    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),

        # Linhas separando as grades
        ('LINEBELOW', (1, 0), (1, 1), 1, color),
        ('LINEBELOW', (1, 3), (1, 3), 1, color),

        # Colocando uma margem dentro das células
        ('LEFTPADDING', (1, 0), (1, 3), leftPadding),

        # Ao aumentar a fonte da palavra OFFER, ela aumenta para baixo
        # sendo necessário criar um bottompadding com o mesmo tamanho do aumento
        ('FONTSIZE', (1, 0), (1, 0), 30),
        ('BOTTOMPADDING', (1, 0), (1, 0), 30),

        # Ajustando o bottompadding das linhas 1 e 2, sem padding
        ('BOTTOMPADDING', (1, 1), (1, 2), 0),
        # Ajustando o bottompadding da linha 3, com padding
        ('BOTTOMPADDING', (1, 3), (1, 3), 40),
        # Ajustando o bottompadding da linha 4, sem padding
        ('BOTTOMPADDING', (1, 4), (1, 4), 0),
        ('LEFTPADDING', (1, 4), (1, 4), 0),

    ])

    return res


def _genContactsTable(width, height):

    widthList = [
        width * 30 / 100,  # col 0 -
        width * 30 / 100,  # col 1 -
        width * 20 / 100,  # col 2 -
        width * 20 / 100,  # col 3 -
    ]

    heightList = [
        height * 25 / 100,  # linha 0 -
        height * 25 / 100,  # linha 1 -
        height * 25 / 100,  # linha 2 -
        height * 25 / 100,  # linha 3 -
    ]

    dataList = []
    with open(r'resources\tabledata.txt', 'r') as file:  # problema 1
        for line in file:
            if line != '\n':
                dataList.append(line.replace('\n', ''))  # problema 2

    matrix = [
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''],
    ]

    idx = 0
    for ridx, row in enumerate(matrix):
        for cidx, col in enumerate(row):
            matrix[ridx][cidx] = dataList[idx]
            idx += 1

            if idx == len(dataList):
                break
        if idx == len(dataList):
            break

    res = Table(matrix, widthList, heightList)

    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),

        ('ALIGN', (3, 0), (3, 3), 'RIGHT'),
        ('RIGHTPADDING', (3, 0), (3, 3), 20),

        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

    ])

    return res


def _genPriceListTable(width, height):

    titleStyle = ParagraphStyle('titleStyle')
    titleStyle.fontSize = 20
    titleStyle.fontName = 'Helvetica-Bold'
    titleStyle.spaceAfter = 15

    titlePara = Paragraph('Detais', titleStyle)

    pricesTable = _genPricesTable(width, height * 70 / 100)

    elementsList = [titlePara, pricesTable]

    res = Table([[elementsList]], width, height)

    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),

        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),

    ])

    return res


def _genPricesTable(width, height):

    matrix = []

    with open(r'resources\pricesTable.csv') as file:
        matrix = list(csv.reader(file))

    if len(matrix) < 2 or len(matrix[0]) != 6:
        return Table([['no data']])

    widthList = [
        width * 20 / 100,
        width * 20 / 100,
        width * 25 / 100,
        width * 15 / 100,
        width * 10 / 100,
        width * 10 / 100,
    ]

    rowCount = len(matrix)
    res = Table(matrix, widthList, height / rowCount)

    # r - red (vermelho)
    # g - green (verde)
    # b - blue (azul)
    # a - alpha (opacity) - Transparente ou não
    color = colors.toColor('rgba(0, 115, 153, 0.9)')

    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, 'grey'),  # Contornos internos

        ('BACKGROUND', (0, 0), (-1, 0), color),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),

        ('ALIGN', (1, 0), (-1, 0), 'CENTER'),

        ('ALIGN', (1, 1), (2, -1), 'CENTER'),

        ('ALIGN', (5, 1), (5, -1), 'RIGHT'),

        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

        # ('BACKGROUND', (0, 0), (-1, -1), color),
        # ('TEXTCOLOR', (0, 0), (-1, -1), 'white'),

    ])

    for i in range(1, rowCount):
        if i % 2 == 0:
            bc = colors.antiquewhite

        else:
            bc = colors.beige

        res.setStyle([
            ('BACKGROUND', (0, i), (-1, i), bc)
        ])

    return res


def _genDescriptionParasTable():

    result = []

    para1Style = ParagraphStyle('para1d')
    para1Style.fontSize = 10
    para1Style.spaceAfter = 15
    para1Style.textColor = colors.HexColor('#003363')

    # Este comando inicia um negrito -> <b> e este termina -> </b>
    para1 = Paragraph('''
    <b>
    Thank you very much for using the servides from us at Palms. 
    Here at Palms Hotel we have living rooms and well-equipped 
    meeting rooms of all sizes with a capacity from 8 - 300 people,
    so that we will be well prepared for most needs you way have.
    </b>
    ''', para1Style)

    para2Style = ParagraphStyle('para2d')
    para2Style.fontSize = 10

    # Este comando inicia o texto em itálico -> <i> e este termina -> </i>
    para2 = Paragraph('''
    <i>
    Palms Hotel is also known for  cuisine and good service, 
    therefore you can fell confident that your needs and desires 
    will be well taken care of, whether you choose to use our 
    beatiful Restaurant Palms of other living rooms, 
    we guarantee a <u>good experience with us.</u>
    </i>
    ''', para2Style)

    result.append(para1)
    result.append(para2)

    return result


def _genAboutTable(width, height):

    widthList = [
        width * 20 / 100,   # Coluna 0 - Imagem
        width * 80 / 100,   # Coluna 1 - Parágrafos
    ]

    img = Image(
        'resources\logoParadise.png',
        widthList[0],
        height,
        kind='proportional',
    )

    para1Style = ParagraphStyle('para1')
    para1Style.fontSize = 14
    para1Style.spaceAfter = 15
    para1 = Paragraph('Palms Hotels', para1Style)

    para2Style = ParagraphStyle('para2')
    para2Style.fontSize = 8
    para2 = Paragraph('''
    Ever since 2004, Palms Hotel has received accomodation and
    dining guests. The hotel and the restaurants has been run
    and owned by the Dubai SGPS.
    ''', para2Style)

    paras = [para1, para2]

    res = Table([
        [img, paras],
    ],
        widthList,
        height,
    )

    res.setStyle([
        # ('GRID', (0, 0), (1, 0), 1, 'red'),


        ('ALIGN', (0, 0), (0, 0), 'CENTER'),  # Alinhamento Horizontal
        ('VALIGN', (0, 0), (1, 0), 'MIDDLE'),  # Alinhamento Vertical

        ('BOTTOMPADDING', (0, 0), (1, 0), 0),
        ('LEFTPADDING', (0, 0), (0, 0), 0),

    ])

    return res
