
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
    def canSplitArray(self, nums: List[int], m: int) -> bool:  
        n = len(nums)
        if n == 1 or n == 2:
            return True
        for i in range(1,n):
            if nums[i] + nums[i - 1] >= m:
                return True 
        return False
    
nums = [2, 2, 1]
m = 5
nums = [2, 3, 3, 2, 3]
m = 6
sol = Solution()
print(sol.canSplitArray(nums, m))
