
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
    def equalPairs(self, grid: List[List[int]]) -> int:    
        n = len(grid)
        cache = defaultdict(int)
        for v in grid:
            cache[tuple(v)] += 1
        cnt = 0
        for j in range(n):
            temp = []
            for i in range(n):
                temp.append(grid[i][j])
                cnt += cache[tuple(temp)]
            

        return cnt
    
grid = [[3,2,1],[1,7,6],[2,7,7]]
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
sol = Solution()
print(sol.equalPairs(grid))
