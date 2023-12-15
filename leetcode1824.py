
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
    
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        dp = [[INF]*(n + 1) for _ in range(3)]
        dp[1][0] = 0
        for j in range(1,4):
            if j != 2 and obstacles[0] != j:
                dp[j - 1][0] = 1
    
        for i in range(1,n + 1):
            curr = INF
            for j in range(1,4):
                if obstacles[i] != j:
                    curr = min(curr, dp[j-1][i-1])
                    dp[j-1][i] = dp[j-1][i-1]
            for j in range(1,4):
                if obstacles[i] != j and dp[j-1][i] > curr:
                    dp[j-1][i] = curr + 1
            # print(dp)

        return min(dp[0][n-1], dp[1][n-1], dp[2][n-1])
    
obstacles = [0,1,2,3,0]
sol = Solution()
print(sol.minSideJumps(obstacles))
