
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        ans = [0] * m
        for i in range(n):
            for j in range(m):
                ans[j] = max(ans[j], len(str(grid[i][j])))
        return ans
    
grid = [[1],[-2322],[-333]]
sol = Solution()
print(sol.findColumnWidth(grid))
