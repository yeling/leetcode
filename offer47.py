
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
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                if j - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1] + grid[i][j])
                if i - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + + grid[i][j])
        return dp[m-1][n-1]
    
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
sol = Solution()
print(sol.maxValue(grid))
