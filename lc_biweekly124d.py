
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
    def maxSelectedElements2(self, nums: List[int]) -> int: 
        n = len(nums)
        nums.sort()
        ans = 1
        dp = [0] * (10 ** 6 + 1)
        next = [0] * (10 ** 6 + 1)
        for i,v in enumerate(nums):
            next = dp[:]
            next[v + 1] = max(dp[v] + 1, dp[v + 1], 1)
            next[v] = max(dp[v], dp[v - 1] + 1 , 1)
            ans = max(ans, next[v], next[v + 1])
            dp = next
            # print(i, v, dp)

        return ans
    
    def maxSelectedElements(self, nums: List[int]) -> int: 
        n = len(nums)
        nums.sort()
        ans = 1
        dp = defaultdict(int)
        next = defaultdict(int)
        for i,v in enumerate(nums):
            next = dp
            next[v + 1] = max(dp[v] + 1, dp[v + 1], 1)
            next[v] = max(dp[v], dp[v - 1] + 1 , 1)
            ans = max(ans, next[v], next[v + 1])
            dp = next
            # print(i, v, dp)

        return ans
    
nums = [2,1,5,1,1]
# nums = [1,4,7,10]
# nums = [2,9,7,16,11,9,18,7,11,12,6,15,4,10]
sol = Solution()
print(sol.maxSelectedElements(nums))
