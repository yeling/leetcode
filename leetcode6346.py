
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
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * k for i in range(n)]
        for i in range(k):
            for j in range(n):
                
        return
    
nums = [2,7,9,3,1]
k = 2
sol = Solution()
print(sol.minCapability(nums, k))
