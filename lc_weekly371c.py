
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
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int: 
        m1 = max(nums1)
        m2 = max(nums2)
        ma = max(m1, m2)
        n = len(nums1)
        if ma != nums1[-1] and ma != nums2[-1]:
            return -1
        sec = 0
        if ma == nums1[-1]:
            sec = nums2[-1]
        elif ma == nums2[-1]:
            sec = nums1[-1]
        for i in range(n):
            if nums1[i] <= sec or nums2[i] <= sec:
                continue
            else:
                return -1
        #2最大
        op1 = 0
        op2 = 0
        for i in range(n):
            if nums1[i] > sec:
                op1 += 1
            if nums2[i] > sec:
                op2 += 1
         
        return min(op1, op2)
    
nums1 = [1,2,7]
nums2 = [4,5,3]
nums1 = [2,3,4,5,9]
nums2 = [8,8,4,4,4]
sol = Solution()
print(sol.minOperations(nums1, nums2))
