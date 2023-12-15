
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]
        for v in edges:
            g[v[0]].append(vals[v[1]])
            g[v[1]].append(vals[v[0]])
        ans = -INF
        for i,v in enumerate(g):
            v.sort(reverse=True)
            ts = vals[i]
            j = 0
            while j < len(v) and j < k:
                if v[j] < 0:
                    break
                ts += v[j]
                j += 1
            ans = max(ans, ts)
        
        return ans

vals = [1,2,3,4,10,-10,-20]
edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]]
k = 2
# vals = [-5]
# edges = []
# k = 0

# vals = [1,-8,0]
# edges = [[1,0],[2,1]]
# k = 2

sol = Solution()
print(sol.maxStarSum(vals, edges, k))

