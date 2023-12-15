
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
   
def lcs(self, text1: str, text2: str) -> int:  
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j-1])

        return dp[m][n]

class Solution:
    # 先求出LCS序列，然后加上str1中，不同，str2中不同的
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
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
        # print(lc)
        i,j,k = 0,0,0
        res = ''
        while i < m or j < n or k < len(lc):
            if k == len(lc):
                res += str1[i:] + str2[j:]
                break
            while i < m and str1[i] != lc[k]:
                res += str1[i]
                i += 1
            while j < n and str2[j] != lc[k]:
                res += str2[j]
                j += 1
            res += lc[k]
            i += 1
            j += 1
            k += 1
        # print(res)             
        return res

str1 = "abac"
str2 = "cab"
sol = Solution()
print(sol.shortestCommonSupersequence(str1, str2))
