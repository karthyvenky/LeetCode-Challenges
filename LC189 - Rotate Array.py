nums = [-1,-100,3,99]
k = 2

# nums = [1,2,3,4,5,6,7]
# k = 3

arrlen = len(nums)
if k > arrlen:
	k = k % arrlen
nums [:] = nums[-k:] + nums[0:-k]

print(nums)
