
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
    # 1049 / 1055 个通过测试用例
    def minimumVisitedCells2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[INF] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if dp[i][j] != INF:
                    k = grid[i][j]
                    for p in range(k + 1):
                        if j + p < n:
                            dp[i][j+p] = min(dp[i][j+p], dp[i][j] + 1)
                        if i + p < m:
                            dp[i + p][j] = min(dp[i + p][j], dp[i][j] + 1)
                # print(i,j, dp)
        if dp[m - 1][n - 1] == INF:
            return -1
        else:
            return dp[m - 1][n - 1]
        return
    
    # 1037 / 1055 个通过测试用例
    # BFS + vis
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[False] * n for _ in range(m)]
        stack = set()
        stack.add((0,0))
        d = 1
        while len(stack) > 0:
            if (m-1,n-1) in stack:
                return d
            next = set()
            for v in stack:
                i,j = v[0],v[1]
                vis[i][j] = True
                k = grid[v[0]][v[1]]
                # print(vis)
                for p in range(1,k + 1):
                    if j + p < n and vis[i][j + p] == False:
                        next.add((i, j + p))
                    if i + p < m and vis[i + p][j] == False:
                        next.add((i + p, j))
            d += 1
            stack = next
        return -1
    
grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
grid = [[2,1,0],[1,0,0]]
sol = Solution()
print(sol.minimumVisitedCells(grid))
