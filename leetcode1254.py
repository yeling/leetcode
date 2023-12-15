
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 30 / 47 
    # 7 4 
    def closedIsland(self, grid: List[List[int]]) -> int:   
        n = len(grid)
        m = len(grid[0])
        vis = [[False] * m for _ in range(n)]
        ans = 0
        dirs = [[1,0], [-1,0],[0,1],[0,-1]]
                
        for i in range(n):
            for j in range(m):
                if vis[i][j] == False and grid[i][j] == 0:
                    stack = []
                    vis[i][j] = True
                    stack.append((i,j))
                    flag = True
                    while len(stack) > 0:
                        cnt = len(stack)
                        for si in range(cnt):
                            curr = stack[si]
                            for k in dirs:
                                dx = curr[0] + k[0]
                                dy = curr[1] + k[1]
                                if dx == -1 or dx == n or dy == -1 or dy == m:
                                    flag = False
                                elif vis[dx][dy] == False and grid[dx][dy] == 0:
                                    stack.append((dx,dy))
                                    vis[dx][dy] = True
                        stack = stack[cnt:]
                        
                    if flag:
                        # print(i,j, ans)
                        ans += 1

        return ans
    
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]

grid = [[1,1,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,0,1,1,1],[1,0,1,0,0,0,1,0,1,0],[1,1,1,1,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,0],[0,0,0,0,1,1,0,0,0,0],[1,0,1,0,0,0,0,1,1,0],[1,1,0,0,1,1,0,0,0,0],[0,0,0,1,1,0,1,1,1,0],[1,1,0,1,0,1,0,0,1,0]]

sol = Solution()
print(sol.closedIsland(grid))
