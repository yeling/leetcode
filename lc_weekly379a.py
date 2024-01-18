
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
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int: 
        cache = defaultdict(int)
        for u,v in dimensions:
            temp = u * u + v * v
            if temp not in cache:
                cache[temp] = u * v
            else:
                cache[temp] = max(cache[temp], u * v)
         
        return cache[max(cache.keys())]
    
dimensions = [[9,3],[8,6]]
dimensions = [[2,6],[5,1],[3,10],[8,4]]

sol = Solution()
print(sol.areaOfMaxDiagonal(dimensions))
