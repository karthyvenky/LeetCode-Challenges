#%%

nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    arrlen = len(nums)
    if arrlen <=2:
        return []
    leftpoi = 0
    rightpoi = arrlen-1
    cursum = 0
    target = 0
    nums = sorted(nums)
    arr = []
    
    for i in range(arrlen):
        leftpoi = i+1
        rightpoi = arrlen-1
        while leftpoi < rightpoi:
            cursum = nums[i] + nums[leftpoi] + nums[rightpoi]
            if cursum == target:
                triplet = [nums[i],nums[leftpoi],nums[rightpoi]]
                if triplet not in arr:
                    arr.append(triplet)
                leftpoi += 1
            elif cursum < target:
                leftpoi += 1
            else:
                rightpoi -= 1
    print(arr)

threeSum(nums)      
               
# %%

def newthreeSum( nums) :
    
    from collections import Counter
    import bisect
    counter = Counter(nums)
    nums = sorted(counter)
    output = []
    
    print(counter)
    print(nums)
    
    # (0,0,0)
    if 0 in counter:
        if counter[0] >= 3:
            output.append([0,0,0])
                    
    print(output)
    
    # (-2,1,1)
    for num in counter:
        if num != 0 and counter[num] >= 2 and -2*num in counter:
            output.append(sorted([-2*num,num,num]))
            
    print(output)
    
    # (-3,1,2)
    for i, num in enumerate(nums):
        if num < 0:
            opposite = -num
            left = bisect.bisect_left(nums, opposite - nums[-1], i + 1)
            right = bisect.bisect_right(nums, opposite / 2, left)
            for a in nums[left:right]:
                b = opposite - a
                if b in counter and a != b:
                    output.append([num,a,b])
    
    return output

nums = [-1,0,1,2,-1,-4]
newthreeSum(nums)