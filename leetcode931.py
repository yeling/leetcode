
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
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[INF] * n for _ in range(n)]
        dp[0] = matrix[0]
        dirs = [[-1,-1], [-1,0],[-1,1]]
                
        for i in range(1,n):
            for j in range(n):
                for k in dirs:
                    dx = i + k[0]
                    dy = j + k[1]
                    if 0 <= dx < n and  0 <= dy < n:
                        dp[i][j] = min(dp[i][j], matrix[i][j] + dp[dx][dy])
        # print(dp)
        ans = min(dp[-1])
        return ans
    
matrix = [[2,1,3],[6,5,4],[7,8,9]]
sol = Solution()
print(sol.minFallingPathSum(matrix))
