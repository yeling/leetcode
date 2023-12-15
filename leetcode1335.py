
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

def max(a,b):
    if a > b:
        return a
    else:
        return b
    
def min(a, b):
    if a < b:
        return a
    else:
        return b

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int: 
        n = len(jobDifficulty)
        if n < d:
            return -1
        # ma[i][j] i to j 的最大值
        ma = [[0]*n for _ in range(n)]
        dp = [[INF]*(d + 1) for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                temp = 0
                for k in range(i,j+1):
                    temp = max(temp, jobDifficulty[k])
                ma[i][j] = temp
        for i in range(n):
            dp[i][1] = ma[0][i]
            for k in range(2,d+1):
                for j in range(0,i):
                    dp[i][k] = min(dp[i][k], dp[j][k-1] + ma[j+1][i])
                
                    

        # print(ma)
        return dp[n-1][d]
    
jobDifficulty = [11,111,22,222,33,333,44,444]
d = 6
# jobDifficulty = [7,1,7,1,7,1]
# d = 3
sol = Solution()
print(sol.minDifficulty(jobDifficulty, d))
