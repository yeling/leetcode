
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
    # 82 / 89
    # BFS
    def shortestPathBinaryMatrix2(self, grid: List[List[int]]) -> int:  
        n = len(grid)
        dirs = [[1,0], [-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        dp = [[INF]*n for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                for d in dirs:
                    dx = d[0] + i
                    dy = d[1] + j 
                    if dx >= 0 and dx < n and dy >= 0 and dy < n and grid[dx][dy] == 0:
                        dp[dx][dy] = min(dp[dx][dy], dp[i][j] + 1)
        ans = dp[n-1][n-1]
        if ans == INF:
            ans = -1
        return ans
    
    # BFS
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:  
        n = len(grid)
        dirs = [[1,0], [-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        dp = [[INF]*n for _ in range(n)]
        vis = [[False]*n for _ in range(n)]
        if grid[0][0] == 1:
            return - 1
        if n == 1 and grid[0][0] == 0:
            return 1
        
        dp[0][0] = 1
        stack = set()
        stack.add((0,0))
        depth = 1
        while len(stack) > 0:
            next = set()
            depth += 1
            for v in stack:
                for d in dirs:
                    dx = d[0] + v[0]
                    dy = d[1] + v[1]
                    if dx >= 0 and dx < n and dy >= 0 and dy < n and grid[dx][dy] == 0 and vis[dx][dy] == False:
                        dp[dx][dy] = min(dp[dx][dy], dp[v[0]][v[1]] + 1)
                        next.add((dx,dy))
                        if dx == n - 1 and dy == n - 1:
                            return depth
                vis[v[0]][v[1]] = True
            stack = next
        return -1
    
    
grid = [[0,0,0],[1,1,0],[1,1,0]]
grid = [[0,0,0],[1,1,0],[1,1,1]]
grid = [[0]]
sol = Solution()
print(sol.shortestPathBinaryMatrix(grid))
