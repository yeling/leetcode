
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
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1 = set(nums1)
        r1 = n - len(s1)
        s2 = set(nums2)
        r2 = n - len(s2)
        n = len(nums1)
        s1 = set(nums1)
        r1 = n - len(s1)
        s2 = set(nums2)
        r2 = n - len(s2)

        s = set(list(s1) + list(s2))
        ans = len(s)
        s11 = s1.copy()
        for v in s1:
            if r1 >= n//2:
                break
            if v in s2:
                r1 += 1 
                s11.remove(v)
        for v in s2:
            if r2 >= n//2:
                break
            if v in s11:
                r2 += 1
        
        if r1 < n//2:
            ans -= n//2 - r1
        if r2 < n//2:
            ans -= n//2 - r2
            
        
        return ans
    
nums1 = [1,2,1,2]
nums2 = [1,1,1,1]
nums1 = [1,2,3,4,5,6]
nums2 = [2,3,2,3,2,3]
nums1 = [10,8,7,9]
nums2 = [7,9,9,5]
sol = Solution()
print(sol.maximumSetSize(nums1, nums2))
