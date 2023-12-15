
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
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [INF] *(n + 1)
        dp[0] = 0

        diff = [0] * n
        for i,v in enumerate(nums):
            diff[i] = max(0, k - v)
        # print(diff)
        for i in range(2):
            dp[i + 1] = diff[i]

        for i in range(2,n):
            for j in range(1,4):
                # print(i, i - j)
                dp[i + 1] = min(dp[i + 1], dp[i - j + 1] + diff[i])
        
        # print(dp)
        # return dp[n]
        return min(dp[n], dp[n - 1], dp[n - 2])

        
    
# nums = [2,3,0,0,2]
# k = 4
# nums = [0,1,3,3]
# k = 5
# nums = [1,1,2]
# k = 1

nums = [4,0,10,2,10,6]
k = 8
sol = Solution()
print(sol.minIncrementOperations(nums, k))
