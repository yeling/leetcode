
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
    def maxMoves(self, grid: List[List[int]]) -> int:   
        m = len(grid)
        n = len(grid[0]) 
        dp = [[0]*n for _ in range(m)]
        dirs = [[0,1], [1,1],[-1,1]]
        ans = 0
        last = 0
        for j in range(n):
            last = ans
            for i in range(m):
                for k in dirs:
                    dx = i + k[0]
                    dy = j + k[1]
                    if 0 <= dx < m and  0 <= dy < n and grid[dx][dy] > grid[i][j]:
                        dp[dx][dy] = max(dp[dx][dy], dp[i][j] + 1)
                        ans = max(ans,dp[dx][dy])
                # print(dp)
            if last == ans:
                break
        return ans
    
grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
# grid = [[3,2,4],[2,1,9],[1,1,7]]
grid = [[187,167,209,251,152,236,263,128,135],[267,249,251,285,73,204,70,207,74],[189,159,235,66,84,89,153,111,189],[120,81,210,7,2,231,92,128,218],[193,131,244,293,284,175,226,205,245]]
sol = Solution()
print(sol.maxMoves(grid))
