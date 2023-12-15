
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
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for  i in range(limit + 1):
            left = n - i
            if left > 2 * limit or left < 0:
                continue
            else:
                l = max(0, left - limit)
                r = min(limit, left)
                ans += r - l + 1
            
        return ans
    
n = 1
limit = 3
sol = Solution()
print(sol.distributeCandies(n, limit))
