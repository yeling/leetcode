
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
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        i  = 0
        while i * cost1 <= total:
            ans += (total - i * cost1)//cost2 + 1
            i += 1
            # print(i, ans)
        return ans
    
total = 20
cost1 = 10
cost2 = 5
sol = Solution()
print(sol.waysToBuyPensPencils(total, cost1, cost2))
