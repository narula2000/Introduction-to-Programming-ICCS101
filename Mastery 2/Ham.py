board=[['O','O','H'],
       ['T','O','O'],
       ['O','O','O']]
def computeMove(board):
    hp=[]
    tp=[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'H':
                hp.append(i)
                hp.append(j)
            if board[i][j] =='T':
                tp.append(i)
                tp.append(j)
    dist= (hp[1]-tp[1])-(hp[0]-tp[0])
    return dist
print(computeMove(board))
    