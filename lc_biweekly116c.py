
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
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        for v in nums:
            for i in range(target, -1, -1):
                if i - v > 0 and dp[i - v] > 0:
                    dp[i] = max(dp[i], dp[i - v] + 1)
                elif i - v == 0:
                    dp[i] = max(dp[i], 1)
        if dp[target] == 0:
            return -1
        else:
            return dp[target]
                    
                
        return
    
nums = [1,2,3,4,5]
target = 9
nums = [4,1,3,2,1,5]
target = 7
nums = [1,1,5,4,5]
target = 3
sol = Solution()
print(sol.lengthOfLongestSubsequence(nums, target))
