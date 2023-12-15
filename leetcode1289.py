
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
    def minFallingPathSum2(self, grid: List[List[int]]) -> int:    
        n = len(grid)
        for i in range(1,n):
            for j in range(n):
                temp = grid[i - 1][0:j] + grid[i - 1][j+1:]
                grid[i][j] += min(temp)
        # print(grid)
        return min(grid[-1])

    def minFallingPathSum(self, grid: List[List[int]]) -> int:    
        n = len(grid)
        for i in range(1,n):
            temp = grid[i - 1][:]
            temp.sort()
            for j in range(n):
                if grid[i - 1][j] == temp[0]:
                    grid[i][j] += temp[1]
                else:
                    grid[i][j] += temp[0]
        # print(grid)
        return min(grid[-1])
    
grid = [[1,2,3],[4,5,6],[7,8,9]]
# grid = [[7]]
sol = Solution()
print(sol.minFallingPathSum(grid))
