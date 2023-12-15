
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
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:  
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
    

text1 = "abcde"
text2 = "ace" 
# text1 = "aa"
# text2 = "aaaa" 


sol = Solution()
print(sol.longestCommonSubsequence(text1,text2))
