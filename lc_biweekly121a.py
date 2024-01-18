
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
    def missingInteger(self, nums: List[int]) -> int:
        dst = nums[0]
        n = len(nums)
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            dst += nums[i]
            i += 1
        ret = dst
        while True:
            if ret not in nums:
                return ret
            else:
                ret += 1


        return
    
nums = [1,2,3,2,5]
nums = [3,4,5,1,12,14,13]
sol = Solution()
print(sol.missingInteger(nums))
