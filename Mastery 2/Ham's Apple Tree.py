def computeMove(board):
    hor=0
    ver=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='T':
                hor+=j
                ver+=i
            if board[i][j]=='H':
                hor-=j
                ver-=i
    return abs(hor)+abs(ver)

assert(computeMove([['H','O','O','O'],['O','O','O','O'],['O','O','O','O'],['O','O','O','T']])==6)
assert(computeMove([['H','O','O'],['O','O','T'],['O','O','O']])==3)
print('Pass')
