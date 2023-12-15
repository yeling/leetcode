
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
    def maxArrayValue(self, nums: List[int]) -> int:    
        n = len(nums)
        l = n - 1
        ans = nums[l]
        curr = nums[l]
        while l > 0:
            if curr >= nums[l - 1]:
                curr += nums[l - 1]
            else:
                curr = nums[l - 1]
            ans = max(ans, curr)
            l -= 1
        return ans
    
nums = [2,3,31,9,10]
# nums = [5,3,3]
sol = Solution()
print(sol.maxArrayValue(nums))
