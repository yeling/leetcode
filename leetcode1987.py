
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
    #1987. 不同的好子序列数目
    #1.
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        n = len(binary)
        dp = [0] * (n + 1)
        pre = [-1, -1]
        for i, v in enumerate(binary):
            v = int(v)
            if pre[v] == -1:
                if v == 1:
                    dp[i + 1] = dp[i] + dp[i] + 1
                else:
                    dp[i + 1] = dp[i] + dp[i]
            else:
                dp[i+1] = dp[i] + dp[i] - dp[pre[v + 1 - 1]]
            pre[v] = i
            # print(i, dp)
        if pre[0] != -1:
            dp[n] += 1
        return dp[n]%MOD


binary = "101"
sol = Solution()
print(sol.numberOfUniqueGoodSubsequences(binary))
