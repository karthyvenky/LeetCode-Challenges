moves = [[0,0],[1,1]]
#moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
moves = [[1,1],[2,0],[0,2]]
moves = [[1,0],[2,2],[2,0],[0,1],[1,1]]
moves = [[2,2],[0,2],[1,0],[0,1],[2,0],[0,0]]
moves = [[0,0],[1,1]]
row = [[] for i in range(3)]
col = [[] for i in range(3)]
diag = [[] for i in range(2)]
A = True
for r,c in moves:
	row[r].append('X' if A is True else 'O')
	col[c].append('X' if A is True else 'O')
	if [r,c] in [[0,0],[1,1],[2,2]] :
		diag[0].append( 'X' if A is True else 'O')
	if [r,c] in [[0,2],[1,1],[2,0]] :
		diag[1].append('X' if A is True else 'O')
	A = not A
winner = "Draw"
i = 0
while winner == "Draw" and i < 3:
		winner = "A" if row[i] == ['X','X','X'] else "B" if  row[i] == ['O','O','O']  else "Draw"
		if winner == "Draw":
			winner = "A" if col[i] == ['X', 'X', 'X'] else "B" if col[i] == ['O', 'O', 'O']  else "Draw"
		if winner == "Draw" and i <2:
			winner = "A" if diag[i] == ['X', 'X', 'X'] else "B" if diag[i] == ['O', 'O', 'O']  else "Draw"
		i += 1
if winner == "Draw" and len(moves) < 9 :
		winner = "Pending"
print(winner)
