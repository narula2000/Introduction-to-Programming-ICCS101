import random
import pprint
pp = pprint.PrettyPrinter(indent=0)


def ranboard(n):
    con = [' ', '2', '4', '8', '16', '32']
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(con[random.randint(0, len(con)-1)])
        board.append(row)
    return board


pp.pprint(ranboard(4))
