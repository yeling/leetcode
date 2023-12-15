
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
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int: 
        ans = sum(values) - values[0]
        n = len(values)
        g = [[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        ret = 0
        def dfs(u, p):
            nonlocal ret
            curr = 0
            for v in g[u]:
                if v != p:
                    curr += dfs(v, u)
            if curr == 0:
                return values[u]
            # print(u, values[u], curr)
            if values[u] >= curr:
                ret += values[u]
                return curr
            else:
                ret += curr
                return values[u]
        dfs(0, -1)
        ans = max(ans, ret )

        return ans
    
edges = [[0,1],[0,2],[0,3],[2,4],[4,5]]
values = [5,2,5,2,1,1]

# edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
# values = [20,10,9,7,4,3,5]

sol = Solution()
print(sol.maximumScoreAfterOperations(edges,values))
