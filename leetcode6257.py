
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
     def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        temp = 0
        for v in grid:
            v.sort(reverse=True)
        for i in range(n):
            temp = -1
            for j in range(m):
                temp = max(temp, grid[j][i])
            ans += temp
                    
        return ans
    
grid = [[1,2,4],[3,3,1]]
grid = [[10]]
sol = Solution()
print(sol.deleteGreatestValue(grid))
