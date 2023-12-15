
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
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = nums1.count(0)
        s1 = sum(nums1)
        c2 = nums2.count(0)
        s2 = sum(nums2)
        ma = max(s1 + c1, s2 + c2)
        if c1 == 0 or c2 == 0:
            if c1 == 0 and s1 < ma:
                return -1
            elif c2 == 0 and s2 < ma:
                return -1
            else:
                return ma
        else:
            return ma

        return
    
nums1 = [3,2,0,1,0]
nums2 = [6,5,0]
nums1 = [2,0,2,0]
nums2 = [0,1,4]
nums1 = [0,17,20,17,5,0,14,19,7,8,16,18,6]
nums2 = [21,1,27,19,2,2,24,21,16,1,13,27,8,5,3,11,13,7,29,7]
sol = Solution()
print(sol.minSum(nums1, nums2))
