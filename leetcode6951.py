
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
    # 983 / 1035 个通过测试用例
    def maximumSafenessFactor2(self, grid: List[List[int]]) -> int:  
        n = len(grid)
        dp = [[INF]*n for _ in range(n)]
        cache = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    cache.append([i,j])
        for i in range(n):
            for j in range(n):
                for v in cache:
                    dp[i][j] = min(dp[i][j], abs(v[0] - i) + abs(v[1] - j))
        # bfs
        
        dirs = [[1,0], [-1,0],[0,1],[0,-1]]
        ans = [[0]*n for _ in range(n)]
        ans[0][0] = dp[i][j]
        for i in range(n):
            for j in range(n):
                for dir in dirs:
                    dx = i + dir[0]
                    dy = j + dir[1]
                    if dx >= 0 and dx < n and dy >= 0 and dy < n:
                        ans[i][j] = max(ans[i][j], ans[dx][dy])
                ans[i][j] = min(ans[i][j], dp[i][j])
        # print(ans)   
        print('bb')   
        for v in ans:
            print(*v)    
        return ans[-1][-1]
    
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:  
        n = len(grid)
        dp = [[INF]*n for _ in range(n)]
        cache = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    cache.append([i,j])
        for i in range(n):
            for j in range(n):
                for v in cache:
                    dp[i][j] = min(dp[i][j], abs(v[0] - i) + abs(v[1] - j))
        # bfs
        print('cc')   
        for v in dp:
            print(*v)  

        dirs = [[1,0], [-1,0],[0,1],[0,-1]]
        ans = [[0]*n for _ in range(n)]
        ans[0][0] = dp[i][j]
        vis = [[False]*n for _ in range(n)]
        stack = []
        stack.append([0,0])
        while len(stack) > 0:
            next = []
            for curr in stack:
                for dir in dirs:
                    dx = curr[0] + dir[0]
                    dy = curr[1] + dir[1]
                    if dx >= 0 and dx < n and dy >= 0 and dy < n:
                        ans[dx][dy] = min(dp[dx][dy],max(ans[curr[0]][curr[1]], ans[dx][dy]))
                        next.append([dx,dy])

        

        for i in range(n):
            for j in range(n):
                for dir in dirs:
                    dx = i + dir[0]
                    dy = j + dir[1]
                    if dx >= 0 and dx < n and dy >= 0 and dy < n:
                        ans[i][j] = max(ans[i][j], ans[dx][dy])
                ans[i][j] = min(ans[i][j], dp[i][j])
        # print(ans)   
        print('bb')   
        for v in ans:
            print(*v)    
        return ans[-1][-1]
    
grid = [[0,0,0],[0,1,0],[0,0,0]]
# grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
# 2
grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]]
sol = Solution()
for v in grid:
    print(*v)
print(sol.maximumSafenessFactor(grid))
