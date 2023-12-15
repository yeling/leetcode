
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
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]: 
        m = len(grid)
        n = len(grid[0])
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                topLeft = set()
                ti = i - 1
                tj = j - 1
                while ti >= 0 and tj >= 0:
                    topLeft.add(grid[ti][tj])
                    ti -= 1
                    tj -= 1

                bottomRight = set()
                ti = i + 1
                tj = j + 1
                while ti < m and tj < n:
                    bottomRight.add(grid[ti][tj])
                    ti += 1
                    tj += 1
                ans[i][j] = abs(len(bottomRight) - len(topLeft))




        return ans
    
grid = [[1,2,3],[3,1,5],[3,2,1]]
grid = [[1]]
sol = Solution()
print(sol.differenceOfDistinctValues(grid))
