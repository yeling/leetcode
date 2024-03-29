
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
    def minOperations(self, nums: List[int], k: int) -> int:
        cache = []
        ans = 0
        for v in nums:
            heappush(cache, v)
        while True:
            a = heappop(cache)
            # print(a)
            if a >= k:
                break
            b = heappop(cache)
            ans += 1
            heappush(cache, 2*a + b)
        



        return ans
    
nums = [2,11,10,1,3]
k = 10
nums = [1,1,2,4,9]
k = 20
sol = Solution()
print(sol.minOperations(nums, k))
