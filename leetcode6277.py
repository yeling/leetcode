
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        res = [[0] * n for _ in range(m)]
        #(0,1)的个数
        rows = [[0,0] for _ in range(m)]
        cols = [[0,0] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    rows[i][0] += 1
                    cols[j][0] += 1
                elif grid[i][j] == 1:
                    rows[i][1] += 1
                    cols[j][1] += 1
        for i in range(m):
            for j in range(n):
                res[i][j] = rows[i][1] + cols[j][1] - rows[i][0] - cols[j][0]
                
        return res

grid = [[0,1,1],[1,0,1],[0,0,1]]
grid = [[1,1,1],[1,1,1]]
sol = Solution()
print(sol.onesMinusZeros(grid))
