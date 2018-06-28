# Assignment 06, Task 05
# Name: Vikrom Narula
# Collaborators: 1409
# Time Spent: 8:00 hrs
# ----------------------------------


# Checks whether a given board has any 
# possible move left. If no more moves,  
# return True. Otherwise return False.
def isGameOver(board):
    for r in range(len(board)):
        for c in range(len(board[0])-1):
            if board[r][c+1]==' ' or board[r][c]==' ':
                return False
            elif board[r][c]==board[r][c+1]:
                return False
    for r in range(len(board)-1):
        for c in range(len(board[0])):
            if board[r+1][c]==' ' or board[r+1][c]==' ':
                return False
            elif board[r][c]==board[r+1][c]:
                return False
    return True

# Returns a tuple (changed, new_board) 
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Up' key.
def doKeyUp(board):
    checker=[]
    for cop in board:
        checker.append(cop[:])
    for times in range(len(checker)): #shif all up
        for r in range(len(checker)-1):
            for c in range(len(checker[0])):
                if checker[r][c]==' ':
                    checker[r][c]=checker[r+1][c]
                    checker[r+1][c]=' '
    for r in range(len(checker)-1,0,-1): # Add same num
        for c in range(len(checker[0])):
            if checker[r][c]==checker[r-1][c] and checker[r][c]!=' ':
                checker[r][c]=str(int(checker[r][c])*2)
                checker[r-1][c]=' '        
    for times in range(len(checker)):
        for r in range(len(checker)-1):  #Shift up once
            for c in range(len(checker[0])): 
                if checker[r][c]==' ':
                    checker[r][c]=checker[r+1][c]
                    checker[r+1][c]=' '
    return ((board!=checker),checker)

# Returns a tuple (changed, new_board) 
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Down' key.
def doKeyDown(board):
    checker=[]
    for cop in board:
        checker.append(cop[:])
    for times in range(len(checker)): #shif all up
        for r in range(len(checker)-1,0,-1):
            for c in range(len(checker[0])):
                if checker[r][c]==' ':
                    checker[r][c]=checker[r-1][c]
                    checker[r-1][c]=' '
    for r in range(len(checker)-1): # Add same num
        for c in range(len(checker[0])):
            if checker[r][c]==checker[r+1][c] and checker[r][c]!=' ':
                checker[r][c]=str(int(checker[r][c])*2)
                checker[r+1][c]=' '        
    for times in range(len(checker)): #shif all up
        for r in range(len(checker)-1,0,-1):
            for c in range(len(checker[0])):
                if checker[r][c]==' ':
                    checker[r][c]=checker[r-1][c]
                    checker[r-1][c]=' '
    return ((board!=checker),checker)

# Returns a tuple (changed, new_board) 
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Left' key.
def doKeyLeft(board):
    checker=[]
    for cop in board:
        checker.append(cop[:])
    for times in range(len(checker[0])): #shif all up
        for r in range(len(checker)):
            for c in range(len(checker[0])-1):
                if checker[r][c]==' ':
                    checker[r][c]=checker[r][c+1]
                    checker[r][c+1]=' '
    for r in range(len(checker)): # Add same num
        for c in range(len(checker[0])-1):
            if checker[r][c]==checker[r][c+1] and checker[r][c]!=' ':
                checker[r][c]=str(int(checker[r][c])*2)
                checker[r][c+1]=' '        
    for times in range(len(checker[0])): #shif all up
        for r in range(len(checker)):
            for c in range(len(checker[0])-1):
                if checker[r][c]==' ':
                    checker[r][c]=checker[r][c+1]
                    checker[r][c+1]=' '
    return ((board!=checker),checker)


# Returns a tuple (changed, new_board) 
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Right' key.
def doKeyRight(board):
    checker=[]
    for cop in board:
        checker.append(cop[:])
    for times in range(len(checker[0])): #shif all up
        for r in range(len(checker)):
            for c in range(len(checker[0])-1,0,-1):
                if checker[r][c]==' ':
                    checker[r][c]=checker[r][c-1]
                    checker[r][c-1]=' '
    for r in range(len(checker)): # Add same num
        for c in range(len(checker[0])-1,0,-1):
            if checker[r][c]==checker[r][c-1] and checker[r][c]!=' ':
                checker[r][c]=str(int(checker[r][c])*2)
                checker[r][c-1]=' '        
    for times in range(len(checker[0])): #shif all up
        for r in range(len(checker)):
            for c in range(len(checker[0])-1,0,-1):
                if checker[r][c]==' ':
                    checker[r][c]=checker[r][c-1]
                    checker[r][c-1]=' '
    return ((board!=checker),checker)


# Returns a list of tuples (row, col)
# indicating where the empty spots are
def emptyPos(board):
    lst=[]
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]==' ':
                lst.append((r, c))
    return lst


# Returns a dictionary mapping each tile 
# value on the board to its count (i.e.,
# how many times it appears on the board)
def hist(board):
    di=dict()
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]!=' ':
                if board[r][c] not in di:
                    di[board[r][c]]=1
                else:
                    di[board[r][c]]+=1
    return di

