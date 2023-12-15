
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
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        ans = 1
        dis = [[INF] * n for _ in range(n)]
        for u,v,w in roads:
            dis[v][u] = dis[u][v] = min(dis[u][v], w)
        


        return
    
n = 3
maxDistance = 5
roads = [[0,1,2],[1,2,10],[0,2,10]]
sol = Solution()
print(sol.numberOfSets(n, maxDistance, roads))
