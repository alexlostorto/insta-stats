# Pretty tables
from src.lib.prettytables import PrettyTable


def createTable(title, rows):
    table = PrettyTable(['Username', 'Full Name'], title=title, padding=1, separator='curvy')
    table.add_rows(rows)

    return table
