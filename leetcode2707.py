
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
    def minExtraChar2(self, s: str, dictionary: List[str]) -> int:  
        cache = set(dictionary)
        # print(cache)
        n = len(s)
        dp = [[n]*n for _ in range(n)]
        for i in range(n):
            if s[0:i+1] in cache:
                dp[0][i] = 0
            else:
                dp[0][i] = i + 1
            
        # print(dp)
        for i in range(n):
            for j in range(n):
                for k in range(j,n):
                    if s[j+1:k+1] in cache:
                        dp[i][k] = min(dp[i][k], dp[i][j])
                    else:
                        dp[i][k] = min(dp[i][k], dp[i][j] + k - j)
        # print(dp)
        return dp[0][n-1]
    
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:  
        cache = set(dictionary)
        # print(cache)
        n = len(s)
        dp = [[n]*n for _ in range(n)]
        for i in range(n):
            if s[0:i+1] in cache:
                dp[0][i] = 0
            else:
                dp[0][i] = i + 1
        vis = [[False] * (n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(i,n+1):
                if s[i:j] in cache:
                    vis[i][j] = True
        # print(dp)
        for i in range(n):
            for j in range(n):
                for k in range(j,n):
                    if vis[j+1][k+1]:
                        dp[i][k] = min(dp[i][k], dp[i][j])
                    else:
                        dp[i][k] = min(dp[i][k], dp[i][j] + k - j)
        # print(dp)
        return dp[0][n-1]
    
s = "leetscode"
dictionary = ["leet","code","leetcode"]
s = "sayhelloworld"
dictionary = ["hello","world"]

sol = Solution()
print(sol.minExtraChar(s, dictionary))
print(sol.minExtraChar2(s, dictionary))
