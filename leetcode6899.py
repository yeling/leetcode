
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
    def maximumJumps(self, nums: List[int], target: int) -> int:    
        n = len(nums)
        dp = [0]*(n)
        dp[n - 1] = 0
        for i in range(n-1, -1, -1):
            if i != n - 1 and dp[i] == 0:
                continue 
            for j in range(0,i):
                if abs(nums[i] - nums[j]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
            # print(i,dp)
        if dp[0] == 0:
            dp[0] = -1
        return dp[0]
    
    
nums = [1,3,6,4,1,2]
target = 2
nums = [1,3,6,4,1,2]
target = 0
# nums = [1,2,0,3]
# target = 1

sol = Solution()
print(sol.maximumJumps(nums, target))
