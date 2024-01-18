
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
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        for v in nums:
            cache[v] += 1
        ans = 0
        f = max(cache.values())
        for v in cache.values():
            if v == f:
                ans += v
        return ans
    
nums = [1,2,2,3,1,4]
nums = [1,2,3,4,5]
sol = Solution()
print(sol.maxFrequencyElements(nums))
