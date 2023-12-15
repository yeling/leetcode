
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

# 1971. 寻找图中是否存在路径

class Solution:
    # 1. BFS
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vis = [False] * n
        g = [list() for _ in range(n)]
        for v0, v1 in edges:
            g[v0].append(v1)
            g[v1].append(v0)
        stack = deque()
        stack.append(source)
        while len(stack) > 0:
            curr = stack.pop()
            vis[curr] = True
            for v in g[curr]:
                if vis[v] == False:
                    stack.append(v)
        
        return vis[destination]
    
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

sol = Solution()
print(sol.validPath(n,edges, source, destination))
