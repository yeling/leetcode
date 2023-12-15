
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:   
        cache = defaultdict(int)
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for i in range(m):
            cache[tuple(matrix[i])] += 1
            temp = [0] * n
            for j in range(n):
                if matrix[i][j] == 0:
                    temp[j] = 1
            cache[tuple(temp)] += 1
        for k in cache:
            ans = max(ans, cache[k])
        return ans
    

matrix = [[0,0,0],[0,0,1],[1,1,0]]
sol = Solution()
print(sol.maxEqualRowsAfterFlips(matrix))
