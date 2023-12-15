
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
    def maximumCount(self, nums: List[int]) -> int:
        b,s = 0, 0
        for v in nums:
            if v > 0:
                b += 1
            elif v < 0:
                s += 1
                
        return max(b,s)
    
nums = [-3,-2,-1,0,0,1,2]
sol = Solution()
print(sol.maximumCount(nums))
