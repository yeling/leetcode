
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
    def minimumScore2(self, str1: str, str2: str) -> int:
        m = len(str1)
        n = len(str2)
        # dp = [[0]*(n + 1) for _ in range(m + 1)]
        #(len, str)
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                dp[i][j] = [0,'']

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j][0] = dp[i-1][j-1][0] + 1
                    dp[i][j][1] = dp[i-1][j-1][1] + str1[i - 1]
                else:
                    if dp[i - 1][j][0] >= dp[i][j-1][0]:
                        dp[i][j][0] = dp[i - 1][j][0]
                        dp[i][j][1] = dp[i - 1][j][1]
                    else:
                        dp[i][j][0] = dp[i][j - 1][0]
                        dp[i][j][1] = dp[i][j - 1][1]
        lc = dp[m][n][1]
        if len(lc) == 0:
            return n
        print(lc)
        i,j = 0,0
        l = INF
        r = -INF
        res = ''
        while i < len(lc) and j < n:
            if lc[i] != str2[j]:
                l = min(l, j)
                r = max(r, j)
                j += 1
            else:
                i += 1
                j += 1
        if i == INF or r == -INF:
            return 0
        return r - l + 1
    def minimumScore(self, s: str, t: str) -> int:
        l = 0
        r = len(t) - 1
        
        return 
    
s = "abacaba"
t = "bzaa"
s = "cde"
t = "xxd"

s = "abecdebe"
t = "eaebceae"
sol = Solution()
print(sol.minimumScore(s,t))
