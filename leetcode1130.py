
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
    #二维DP
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[INF] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for l in range(2,n+1):
            for i in range(n):
                if i + l > n:
                    break
                for j in range(1,l):
                    if i + j > n:
                        break
                    # print(i,j,l)
                    dp[i][i + l - 1] = min(dp[i][i + l - 1],max(arr[i:i+j]) * max(arr[i+j:i+l]) +  dp[i][i + j - 1] + dp[i + j][i + l - 1])
        # print(dp)
        return  dp[0][n-1]
    
# arr = [6,2,4]
# arr = [2,6,8,4]
arr = [15,13,5,3]
# arr = [7,12,8,10]
sol = Solution()
print(sol.mctFromLeafValues(arr))
