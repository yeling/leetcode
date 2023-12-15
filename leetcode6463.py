
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
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:  
        m = len(grid)
        n = len(grid[0])
        #(hash, index  + 1)
        cache = defaultdict(int)
        for i,v in enumerate(grid):
            #
            temp = 0
            for j in range(n):
                if v[-1-j] != 0:
                    temp += (1 << j)
            # print(temp)
            if temp == 0:
                return [i]
            for j in range(2**n):
                if j & temp == 0 and j in cache:
                    return [cache[j] - 1, i]
            cache[temp] = i + 1
        
        return []
    
grid = [[1,1,1,0,0,0],[1,0,0,1,1,0],[0,1,0,1,0,1],[0,0,1,0,1,1]]

# 11100 0
# 10011 0
# 01010 1
# 00101 1
# 过不了这个啊
# grid = [[1,1,1],[1,1,1]]
# grid = [[0]]
sol = Solution()
print(sol.goodSubsetofBinaryMatrix(grid))
