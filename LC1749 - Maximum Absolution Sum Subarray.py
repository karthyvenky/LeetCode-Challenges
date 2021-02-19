#super fast 
from itertools import accumulate
import operator
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        z = list(accumulate(nums,initial = 0))
        return abs(max(z) - min(z))