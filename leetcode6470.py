
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
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mi = min(nums)
        ma = max(nums)
        for v in nums:
            if v != mi and v != ma:
                return v    
        return -1
    
nums = [1,2,4,5]
sol = Solution()
print(sol.findNonMinOrMax(nums))
