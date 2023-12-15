
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        sa = INF
        for v in nums2:
            if v in nums1:
                sa = min(v, sa)
        if sa != INF:
            return sa    
        
        mi = min(min(nums1),min(nums2))
        ma = max(min(nums1),min(nums2))
        return mi * 10 + ma
                

    
nums1 = [4,1,3]
nums2 = [5,7]
# nums1 = [3,5,2,6]
# nums2 = [3,1,7]
# nums1 = [6,4,3,7,2,1,8,5]
# nums2 = [6,8,5,3,1,7,4,2]
sol = Solution()
print(sol.minNumber(nums1, nums2))
