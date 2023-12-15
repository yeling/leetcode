
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
    # 115. 不同的子序列
    #1.dp问题
    # j == 0 and i == j dp[i][j] = dp[i-1][j] + 1
    # i == j dp[i][j] = dp[i-1][j] + dp[i-1][j-1] 
    # i != j dp[i][j] = dp[i-1][j]
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    if j- 1 == 0:
                        dp[i][j] = dp[i-1][j] + 1
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-1] 
                else:
                    dp[i][j] = dp[i-1][j]
            # print(i, *dp, sep='\n')
        return dp[m][n]


s = "rabbbit"
t = "rabbit"
# s = "rab"
# t = "rab"
s = "babgbag"
t = "bag"
sol = Solution()
print(sol.numDistinct(s, t))
