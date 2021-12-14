from reportlab.lib import colors
from reportlab.platypus import Table


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

    res = Table([
        ['', 'Offer', ''],
        ['', _genContactsTable(widthList[1], heightList[1]), ''],
        ['', _genPriceListTable(widthList[1], heightList[2]), ''],
        ['', _genDescriptionParasTable(), ''],
        ['', _genAboutTable(widthList[1], heightList[4]), ''],

    ],
        widthList,
        heightList
    )

    color = colors.HexColor('#003363')

    res.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'red'),

        ('LINEBELOW', (1, 0), (1, 1), 5, color)
    ])

    return res


def _genContactsTable(width, height):

    return 'CONTACTS'

def _genPriceListTable(width, height):

    return 'PRICE LIST'

def _genDescriptionParasTable():

    return 'DESCRIPTION'

def _genAboutTable(width, height):

    return 'ABOUT'