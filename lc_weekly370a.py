
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
    def findChampion(self, grid: List[List[int]]) -> int: 
        ans = 0
        n = len(grid)
        for i in range(n):
            curr = grid[i].count(1)
            if curr == n - 1:
                return i   
        return 0
    
grid = [[0,0,1],[1,0,1],[0,0,0]]
grid = [[0,1],[0,0]]
sol = Solution()
print(sol.findChampion(grid))
