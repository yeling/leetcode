
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
    # TLE 38 / 52
    def maxSumAfterPartitioning2(self, arr: List[int], k: int) -> int:
        n = len(arr)
        ma = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                for ik in range(i,j+1):
                    ma[i][j] = max(ma[i][j], arr[ik])
        # print(ma)

        dp = [0] * (n+1)
        for i in range(n):
            begin = max(0, i - k + 1)
            for j in range(begin, i + 1):
                dp[i + 1] = max(dp[i + 1], dp[j] + ma[j][i] * (i - j + 1))
        # print(dp)

        return dp[n]
    
    #TLE
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        ma = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                ma[i][j] = max(ma[i][j - 1], arr[j])
        # print(ma)

        dp = [0] * (n+1)
        for i in range(n):
            begin = max(0, i - k + 1)
            for j in range(begin, i + 1):
                dp[i + 1] = max(dp[i + 1], dp[j] + ma[j][i] * (i - j + 1))
        # print(dp)

        return dp[n]
    
arr = [1,4,1,5,7,3,6,1,9,9,3]
arr = [1,4,1,5]
k = 4
# arr = [1,15,7,9,2,5,10]
# k = 3
sol = Solution()
print(sol.maxSumAfterPartitioning(arr,k))
