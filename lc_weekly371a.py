
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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(n):
                if abs(nums[i] - nums[j]) <= min(nums[i],nums[j]):
                    ans = max(ans, nums[i]^nums[j])    
        return ans
    
nums = [1,2,3,4,5]
nums = [5,6,25,30]
sol = Solution()
print(sol.maximumStrongPairXor(nums))
