
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
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0]*n
        # -1 , 1
        #二分染色法
        def dfs(i:int, c: int)->bool:
            color[i] = c
            for v in graph[i]:
                if i != v and color[v] == c:
                    return False
                elif color[v] == 0 and not dfs(v, -c):
                    return False
            return True
        for i,v in enumerate(color):
            # print(color)
            if v == 0 and not dfs(i,1):
                return False
        return True

# graph = [[1,3],[0,2],[1,3],[0,2]]
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
sol = Solution()
print(sol.isBipartite(graph))
