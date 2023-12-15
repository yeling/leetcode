
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
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
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
        m = len(grid)
        n = len(grid[0])
        father = list(range(m*n))
        for i in range(m):
             for j in range(n):
                if i == 0 and j == 0:
                    continue
                if grid[i][j] == 1 and i + 1 < m and grid[i + 1][j] == 1:
                    join(father, i*m + j, (i + 1) * j)
                if grid[i][j] == 1 and j + 1 < n and grid[i][j + 1] == 1:
                    join(father, i*m + j, i * (j + 1))
        
        if find(father,1) == find(father, m*n - 1) and find(father,n) == find(find,m*n - 1):
            return False
        else:
            return True
        return
    
grid = [[1,1,1],[1,0,0],[1,1,1]]
grid = [[1,1,1],[1,0,1],[1,1,1]]
sol = Solution()
print(sol.isPossibleToCutPath(grid))
