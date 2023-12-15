
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def minChanges(self, s: str) -> int:  
        n = len(s)
        dp = [[INF] * 2 for _ in range(n + 1)]
        dp[0][0] = 0
        dp[1][1] = 0
        for i in range(1,n):
            temp = s[i-1 : i + 1]
            if temp == '00':
                dp[i + 1][0] = min(dp[i - 1][1], dp[i - 1][0])
                dp[i + 1][1] = min(dp[i -1][1] + 2, dp[i - 1][0] + 2)
            elif temp == '01' or temp == '10':
                dp[i + 1][0] = min(dp[i - 1][1] + 1, dp[i - 1][0] + 1)
                dp[i + 1][1] = min(dp[i -1][1] + 1, dp[i - 1][0] + 1)
            elif temp == '11':
                 dp[i + 1][0] = min(dp[i - 1][1] + 2, dp[i - 1][0] + 2)
                 dp[i + 1][1] = min(dp[i -1][1], dp[i - 1][0])
            # print(dp)

        return min(dp[n][0], dp[n][1])
    
s = "0000"
# s = "10"
sol = Solution()
print(sol.minChanges(s))
