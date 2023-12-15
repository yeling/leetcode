
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
    # 63 / 744
    def maxScore(self, nums: List[int], x: int) -> int:  
        # 0 偶数， 1奇数
        dp = [0,0]
        for i,v in enumerate(nums):
            next = [0,0]
            if i == 0:
                dp[v%2] = v
                dp[v%2-1] = -INF
                continue
            if v%2 == 0:
                next[0] = max(dp[1] - x + v, dp[0] + v)
                next[1] = dp[1]
            else:
                next[0] = dp[0]
                next[1] = max(dp[0] - x + v, dp[1] + v)
            dp = next
            # print(dp)
        return max(dp)
    
nums = [2,3,6,1,9,2]
x = 5
nums = [2,4,6,8]
x = 3

nums = [38,92,23,30,25,96,6,71,78,77,33,23,71,48,87,77,53,28,6,20,90,83,42,21,64,95,84,29,22,21,33,36,53,51,85,25,80,56,71,69,5,21,4,84,28,16,65,7]
x = 52
#1545

sol = Solution()
print(sol.maxScore(nums, x))
