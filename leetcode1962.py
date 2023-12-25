
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
    def minStoneSum(self, piles: List[int], k: int) -> int:
        cache = [-v for v in piles]
        heapify(cache)
        for _ in range(k):
            curr = -heappop(cache)
            curr = curr - curr//2
            heappush(cache, -curr)
        return -sum(cache)
    
piles = [5,4,9]
k = 2
piles = [4,3,6,7]
k = 3
sol = Solution()
print(sol.minStoneSum(piles, k))
