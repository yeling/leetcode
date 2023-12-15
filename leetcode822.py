
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cache = set()
        all = []
        for f,b in zip(fronts, backs):
            if f == b:
                cache.add(f)
            else:
                all.append(f)
                all.append(b)
        all.sort()
        for v in all:
            if v not in cache:
                return v
            
        return 0
    
fronts = [1,2,4,4,7]
backs = [1,3,4,1,3]
fronts = [1,2,7]
backs = [1,2,8]

sol = Solution()
print(sol.flipgame(fronts, backs))
