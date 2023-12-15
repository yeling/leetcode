
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
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inlist = [[] for _ in range(n)]
        for u,v in edges:
            inlist[v].append(u)
        ans = []
        for i in range(n):
            if len(inlist[i]) == 0:
                ans.append(i)
        if len(ans) == 1:
            return ans[0]
        return -1
    
n = 3
edges = [[0,1],[1,2]]
n = 4
edges = [[0,2],[1,3],[1,2]]
sol = Solution()
print(sol.findChampion(n, edges))
