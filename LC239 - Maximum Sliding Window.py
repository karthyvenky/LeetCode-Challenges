
def maxSlidingWindow(nums, k):
	from collections import deque
	q = deque()
	l = r = 0
	arrlen = len(nums)
	maxnums = []
	while r < arrlen:
		while q and nums[q[-1]] < nums[r]:
			q.pop()
		q.append(r)
		
		if r - l + 1 == k:
			#got window
			maxnums.append(nums[q[0]])
			l = l + 1
			if q[0] < l :
				q.popleft()
			
		r = r +1
	return(maxnums)
	

#print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7],  3))
# print(maxSlidingWindow([9,11],  2))
print(maxSlidingWindow([5,-1,4,3,5], 3))

def maxWindow(nums,k):
	output = []
	from collections import  deque
	q = deque()  # store indexes
	l = r = 0
	
	while r < len(nums):
		# pop smaller values from q
		while q and nums[q[-1]] < nums[r]:
			q.pop()
		q.append(r)
		
		# remove element outside of window range
		if l > q[0]:
			q.popleft()
		
		# ensure window is size k
		if (r + 1) >= k:
			output.append(nums[q[0]])
			l += 1
		r += 1
	
	return output


