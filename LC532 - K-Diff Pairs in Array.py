
def getkdiff(arr, target):
	from collections import Counter
	d = Counter(arr)
	sol = 0
	for val in d :
		comp = val - target
		if target == 0 and d[val] > 1 :
			sol = sol + 1
		if target > 0 and comp in d:
			sol = sol + 1
	
	print(sol)


#getkdiff([3,1,4,1,5],2)
#getkdiff([-1,-2,-3], 1)
#getkdiff([1,2,4,4,3,3,0,9,2,3],  3)
#getkdiff([1,2,3,4,5],1)
getkdiff([1,3,1,5,4],0)
