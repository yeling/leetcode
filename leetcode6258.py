
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
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cache = set(nums)
        # vis = False * n
        ans = -1
        for _,v in enumerate(nums):
            temp = v
            tempLen = 1
            while temp * temp in cache:
                tempLen += 1
                temp = temp * temp
            if tempLen >= 2:
                ans = max(ans, tempLen)
        return ans
    
nums = [4,3,6,16,8,2]
nums = [2,3,5,6,7]
sol = Solution()
print(sol.longestSquareStreak(nums))
