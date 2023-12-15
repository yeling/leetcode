
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
    def minimumMoves(self, grid: List[List[int]]) -> int:
        vis = [[False] * 3 for _ in range(3)]
        zero = set
        one = defaultdict(int)
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    zero.add((i,j))
                else:
                    one[(i,j)] = grid[i][j]

        ans = 0
        
        def dfs(zero : set,one: defaultdict):
            nonlocal ans
            for v in zero:
                for k in one:
                    #choose
                    zero.remove


            return
        dfs(zero, one)


        
        return
    
grid = [[1,3,0],[1,0,0],[1,0,3]]
sol = Solution()
print(sol.minimumMoves(grid))
