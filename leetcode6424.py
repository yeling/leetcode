
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:   
        l = -1
        r = -1
        n = len(nums)
        for i,v in enumerate(nums):
            if v == 1:
                l = i
            elif v == n:
                r = i
        ans = 0
        if l < r:
            ans = l + (n - 1 - r)
        else:
            ans = l + (n - 1 - r ) - 1
        
        return ans
    
nums = [2,1,4,3]
nums = [2,4,1,3]
nums = [1,3,4,2,5]
sol = Solution()
print(sol.semiOrderedPermutation(nums))
