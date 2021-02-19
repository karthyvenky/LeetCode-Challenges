
def get_deque_Winner(arr,k):
	from collections import deque
	arrlen = len(arr)
	d = deque(arr)
	winner = 0
	wincnt = 0
	while wincnt < k:
		x,y = d.popleft(), d.popleft()
		if y > x:
			if winner != y:
				winner = y
				wincnt = 1
			else:
				wincnt += 1
			d.append(x)
			d.appendleft(y)
		if x > y:
			if winner != x:
				winner = x
				wincnt = 1
			else:
				wincnt += 1
			d.append(y)
			d.appendleft(x)
	return(winner)
	

def getWinner(arr, k):
	cnt = 0
	maxnum = -(1<<31)
	l = arr[0]
	for r in arr[1: ] :
		if l > r:
			if maxnum != l:
				maxnum = l
				cnt = 1
			else:
				cnt += 1
		else:
			#r > l
			if maxnum != r:
				maxnum = r
				cnt = 1
			else:
				cnt += 1
			if cnt == k:
				return(maxnum)
			l = r
	return(maxnum)
	
	
		
	
#print(getWinner([1,11,22,33,44,55,66,77,88,99], 1000000000))
print(getWinner([2,1,3,5,4,6,7], 2))
