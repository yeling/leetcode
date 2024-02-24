
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
    def maxOperations(self, nums: List[int]) -> int:
        s = nums[0] + nums[1]
        n = len(nums)
        ans = 1
        for i in range(2, len(nums), 2):
            if i + 1 < n and nums[i] + nums[i + 1] == s:
                ans += 1
            else:
                break
        return ans
    
nums = [3,2,1]
sol = Solution()
print(sol.maxOperations(nums))
