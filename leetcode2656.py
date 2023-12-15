
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
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans = 0
        stack = []
        for v in nums:
            heappush(stack, -v)
        # print(stack)
        for _ in range(k):
            curr = heappop(stack)
            ans += -curr
            heappush(stack, curr - 1)
        return ans
    
nums = [1,2,3,4,5]
k = 3
sol = Solution()
print(sol.maximizeSum(nums, k))
