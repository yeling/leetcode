
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    #AC
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        g = [list() for _ in range(n + 1)]
        for u,v in paths:
            g[u].append(v)
            g[v].append(u)
        # print(g)
        
        def dfs(f, path):
            # print(f, path)
            left = set([1,2,3,4])
            for v in g[f]:
                if path[v] in left:
                    left.remove(path[v])
            # for v in left:
            path[f] = list(left)[0]
            for u in g[f]:
                if path[u] == 0:
                    dfs(u, path)             
            return  
        path = [0]*(n + 1)
        
        for i in range(1,n+1):
            if path[i] == 0:
                # print('begin ',i, path)
                dfs(i,path) 
            # print(path)

        return path[1:]
    
n = 3
paths = [[1,2],[2,3],[3,1]]
n = 4
paths = [[1,2],[3,4]]

n = 5
paths = [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]


# n = 4
# paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]

sol = Solution()
print(sol.gardenNoAdj(n, paths))
