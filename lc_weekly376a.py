
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
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cache = defaultdict(int)
        for i in range(n):
            for j in range(n):
                cache[grid[i][j]] += 1

        ans = [0,0]
        for i in range(1,n*n + 1):
            if cache[i] == 0:
                ans[1] = i
            elif cache[i] == 2:
                ans[0] = i
                

        return ans
    
grid = [[1,3],[2,2]]
sol = Solution()
print(sol.findMissingAndRepeatedValues(grid))
