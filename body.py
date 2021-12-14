from reportlab.platypus import Table


def genBodyTable(width, height):

    widthList = [
        width * 10 / 100,  # col 1 -
        width * 80 / 100,  # col 2 -
        width * 10 / 100,  # col 3 -

    ]

    heightList = [
        height * 10 / 100,  # linha 1 -
        height * 15 / 100,  # linha 2 -
        height * 35 / 100,  # linha 3 -
        height * 30 / 100,  # linha 4 -
        height * 10 / 100,  # linha 5 -
    ]

    res = Table([
        ['', 'Offer', ''],
        ['', '', ''],
        ['', '', ''],
        ['', '', ''],
        ['', '', ''],

    ],
        widthList,
        heightList
    )

    res.setStyle({
        ('GRID', (0, 0), (-1, -1), 1, 'red'),
    })

    return res
