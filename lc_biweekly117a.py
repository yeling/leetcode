
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
            for j in range(limit + 1):
                for k in range(limit + 1):
                    # print(i, j, k, i + j + k)
                    if i + j + k == n:
                        ans += 1
            
        return ans
    
n = 15
limit = 8
sol = Solution()
print(sol.distributeCandies(n, limit))
