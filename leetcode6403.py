
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        #查找father
        def find(father, u):
            if father[u] != u:
                father[u] = find(father,father[u])
            return father[u]
        #合并
        def join(father, u, v):
            fu = find(father,u)
            fv = find(father,v)
            if fu != fv:
                father[fu] = fv
        
        father = list(range(n*m))
        vis = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and vis[i][j] == False:
                    dirs = [[1,0], [-1,0],[0,1],[0,-1]]
                    for k in dirs:
                        dx = i + k[0]
                        dy = j + k[1]
                        if 0 <= dx < m and  0 <= dy < n and vis[dx][dy] == False and grid[dx][dy] > 0:
                            join(father, i * n + j, dx * n + dy)
                            vis[i][j] = True
                vis[i][j] = True

        rootMap = defaultdict(int)
        ans = 0
        for i in range(len(father)):
            fa = find(father, father[i])
            rootMap[fa] += grid[i//n][i%n]
            ans = max(ans, rootMap[fa])
        
        # print(father)
        # print(rootMap)
            


        return ans
    
grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
grid = [[9,10]]
sol = Solution()
print(sol.findMaxFish(grid))
