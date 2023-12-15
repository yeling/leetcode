
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 1025 / 1027 
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        cache = []
        n = len(grid)
        for i in range(n):
            for j in range(n):
                cache.append((grid[i][j], i, j))
        if grid[0][0] != 0:
            return False
        cache.sort()
        # print(cache)
        for i in range(1, len(cache)):
            dx = abs(cache[i][1] - cache[i - 1][1])
            dy = abs(cache[i][2] - cache[i - 1][2])
            if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
                continue
            else:
                return False

        return True
    
grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
grid = [[0,3,6],[5,8,1],[2,7,4]]
grid = [[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]]
for v in grid:
    print(v)
sol = Solution()
print(sol.checkValidGrid(grid))
