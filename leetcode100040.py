
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
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        if nums[0] > 0:
            ans += 1
        for i,v in enumerate(nums):
            if i + 1 > v and (i + 1 == n or i + 1 < nums[i + 1]):
                ans += 1

        return ans
    
nums = [6,0,3,3,6,7,2,7]
# nums = [1,1]
nums = [1,1,0,1]
sol = Solution()
print(sol.countWays(nums))
