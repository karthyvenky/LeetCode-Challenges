#%%
def twosums(nums, target):
    # LC1 - Two Sums
    cursum = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            cursum = nums[i] + nums[j]
            if cursum == target:
                return([i, j])
    if cursum != target:
        return([0,0])

def fasttwosums(nums,target):
    for i in range(len(nums)):
        try:
            p = nums[i]
            q = nums[i+1:].index(target - nums[i]) + i+ 1
            print(i,q)
        except:
            pass

nums = [2, 7, 11, 15]
target = 9

# nums = [3,2,4]
# target = 6

# nums = [3,3]
# target = 6


# nums = [3,2,3]
# target = 6

fasttwosums(nums,target)
# %%
nums = [3,3]

def quick2sum(nums):
    target = 6
    res = set()
    d = dict((i,j) for i,j in enumerate(nums))
    for i in d.values():
        c = target - i
        if c in d.values() and d[i] != d[c]:
            res.add(tuple(sorted([d[i],d[target-i]])))
            return(res)
    return([])
        
# %%
print(quick2sum([3,3]))

# %%
