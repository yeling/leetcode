
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
from heapq import *
import string
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:    
        ans = [0,0]
        for v in nums1:
            if v in nums2:
                ans[0] += 1
        for v in nums2:
            if v in nums1:
                ans[1] += 1
        return ans
    
nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
sol = Solution()
print(sol.findIntersectionValues(nums1, nums2))
