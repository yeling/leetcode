
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
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[INF,INF] for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):
            dp[i + 1][1] = min(dp[i][0], dp[i][1]) + prices[i]
            end = min(i + 1 + i + 1, n)
            for j in range(i+1, end):
                dp[j + 1][0] = min(dp[j + 1][0], dp[i + 1][1])
            # print(i, dp)


        return min(dp[n])
    
prices = [3,1,2]
prices = [1,10,1,1]
sol = Solution()
print(sol.minimumCoins(prices))
