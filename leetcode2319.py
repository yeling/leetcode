
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
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if (i + j == n - 1 or i == j) and grid[i][j] == 0:
                    return False
                if i + j != n - 1 and i != j and grid[i][j] != 0:
                    return False
        return True
    
grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
grid = [[5,7,0],[0,3,1],[0,5,0]]
sol = Solution()
print(sol.checkXMatrix(grid))
