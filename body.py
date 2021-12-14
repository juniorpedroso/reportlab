from reportlab.lib import colors
from reportlab.platypus import Table, Image
from reportlab.platypus import Table, Paragraph
from reportlab.lib.styles import ParagraphStyle


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
                dataList.append(line)  # problema 2

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

    res = Table(matrix, widthList, heightList)

    res.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'red'),
    ])

    return res


def _genPriceListTable(width, height):

    return 'PRICE LIST'


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
