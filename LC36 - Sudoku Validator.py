#%%
nboard = \
    [[".",".",".",".","5",".",".","1","."],\
    [".","4",".","3",".",".",".",".","."],\
    [".",".",".",".",".","3",".",".","1"],\
    ["8",".",".",".",".",".",".","2","."],\
    [".",".","2",".","7",".",".",".","."],\
    [".","1","5",".",".",".",".",".","."],\
    [".",".",".",".",".","2",".",".","."],\
    [".","2",".","9",".",".",".",".","."],\
    [".",".","4",".",".",".",".",".","."]]

# nboard = [[".",".","4",".",".",".","6","3","."] \
#          ,[".",".",".",".",".",".",".",".","."] \
#          ,["5",".",".",".",".",".",".","9","."] \
#          ,[".",".",".","5","6",".",".",".","."],\
#           ["4",".","3",".",".",".",".",".","1"],\
#           [".",".",".","7",".",".",".",".","."],\
#           [".",".",".","5",".",".",".",".","."],\
#           [".",".",".",".",".",".",".",".","."],\
#           [".",".",".",".",".",".",".",".","."]]
board = \
[["5","3",".",".","7",".",".",".","."] \
,["6",".",".","1","9","5",".",".","."] \
,[".","9","8",".",".",".",".","6","."] \
,["8",".",".",".","6",".",".",".","3"] \
,["4",".",".","8",".","3",".",".","1"] \
,["7",".",".",".","2",".",".",".","6"] \
,[".","6",".",".",".",".","2","8","."] \
,[".",".",".","4","1","9",".",".","5"] \
,[".",".",".",".","8",".",".","7","9"]]

def checkboard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                board[i][j] = 0
            else:
                board[i][j] = int(board[i][j])

    return(checkrows(board) and checkcols(board) and checkgrid(board))

checkboard(nboard)

# %%
def checkline(row):
    for i in row:
        if i > 0:
            if i in row[row.index(i)+1:]:
                #print(row,"False")
                return False
    return True

def checkrows(board):
    for i in range(len(board)):
        if not checkline(board[i]):
            #print("row", board[i])
            return False
    return True

def checkcols(board):
    for j in range(len(board[0])):
        if not checkline([board[i][j] for i in range(len(board))]):
            #print("col", board[i])
            return False
    return True

def checkgrid(board):
    subgrids = []
    for box_i in range(3):
        for box_j in range(3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(board[3*box_i + i][3*box_j + j])
            subgrids.append(subgrid)
            #print(subgrid)
            if not checkline(subgrid):
                return False
    return True

checkgrid(nboard)
    
# %%

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # init data
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    boxes = [{} for i in range(9)]

    # validate a board
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                num = int(num)
                box_index = (i // 3 ) * 3 + j // 3
                
                # keep the current cell value
                rows[i][num] = rows[i].get(num, 0) + 1
                columns[j][num] = columns[j].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                
                # check if this value has been already seen before
                if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                    return False         
    return True

nboard = \
    [[".",".",".",".","5",".",".","1","."],\
    [".","4",".","3",".",".",".",".","."],\
    [".",".",".",".",".","3",".",".","1"],\
    ["8",".",".",".",".",".",".","2","."],\
    [".",".","2",".","7",".",".",".","."],\
    [".","1","5",".",".",".",".",".","."],\
    [".",".",".",".",".","2",".",".","."],\
    [".","2",".","9",".",".",".",".","."],\
    [".",".","4",".",".",".",".",".","."]]
    
print(isValidSudoku(nboard))
# %%
