
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
    def minimumCost(self, nums: List[int]) -> int:
        ans = INF
        n = len(nums)
        for i in range(1,n - 1):
            for j in range(i + 1, n):
                ans = min(ans, nums[0] + nums[i] + nums[j])    
        return ans
    
nums = [1,2,3,12]
nums = [10,3,1,1]
sol = Solution()
print(sol.minimumCost(nums))
