
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

# 1278. 分割回文串 III
# 1.dp问题,前i个，k个子集
# move[i][j]为i到j为回文串时需要修改的字符个数
# dp[i][k] = min dp[j][k-1] + move[j+1][i]
# j 取值范围[k-1,i-1]

MOD = 10 ** 9 + 7

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        move = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                left = i
                right = j
                c = 0
                while left < right:
                    if s[left] != s[right]:
                        c += 1
                    left += 1
                    right -= 1
                move[i][j] = c
        # print(move)
        dp = [[n] * k for _ in range(n)]
        for i in range(k):
            dp[i][i] = 0
        
        for i in range(n):
            dp[i][0] = move[0][i]
            for j in range(1,k):
                for ji in range(j-1,i):
                    dp[i][j] = min(dp[i][j], dp[ji][j-1] + move[ji + 1][i])
        # print(dp)
        return dp[i][k-1]

s = "aabbc"
k = 3

s = "abc"
k = 2

s = "leetcode"
k = 8

sol = Solution()
print(sol.palindromePartition(s,k))
