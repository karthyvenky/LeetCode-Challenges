#%%
a = [1,1]
b = [1,2]
s = sorted(a+b)

# %%
med = 0
if len(s)%2 != 0:
    med = s[len(s)//2]
else:
    med = (s[(len(s)//2) -1 ] + s[(len(s)//2) ])/2
print(med)
# %%
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = sorted(nums1 + nums2)
        med = 0
        if len(s)%2 != 0:
            med = s[len(s)//2]
        else:
            med = (s[(len(s)//2) -1 ] + s[(len(s)//2) ])/2
        return(med)