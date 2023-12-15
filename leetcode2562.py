
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
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            if l != r:
                ans += int(str(nums[l]) + str(nums[r]))
            else:
                ans += nums[l]
            l += 1
            r -= 1 
        return ans
    
nums = [2]
sol = Solution()
print(sol.findTheArrayConcVal(nums))
