
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
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        dirs = [[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]
        pos = [0,0]
        start = 0
        while grid[pos[0]][pos[1]] == start and start < n * n - 1:
            find = False
            # print(pos, start)
            for x,y in dirs:
                if pos[0] + x >= 0 and pos[0] + x <= n - 1 and pos[1] + y >= 0 and pos[1] + y <= n-1:
                    if grid[pos[0] + x ][pos[1] + y] == start + 1:
                        pos[0] = pos[0] + x
                        pos[1] = pos[1] + y
                        start = start + 1
                        find = True
                        break
            if find == False:
                return False

        return start == n * n - 1
    
grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
# grid = [[0,3,6],[5,8,1],[2,7,4]]

# grid = [[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]]

sol = Solution()
print(sol.checkValidGrid(grid))
