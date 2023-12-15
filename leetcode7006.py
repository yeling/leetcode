
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
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort()
        dp = [0]*(n + 1)
        i = 0
        j = 0
        ans = 0
        while i < n and j < len(offers):
            while i < offers[j][0]:
                dp[i + 1] = max(dp[i], dp[i + 1])
                i += 1
            dp[offers[j][1] + 1] = max(dp[offers[j][1] + 1], dp[i] + offers[j][2])
            j += 1
            # print(dp)
        return max(dp)
    
n = 5
offers = [[0,0,1],[0,2,2],[1,3,2]]
n = 5
offers = [[0,0,1],[0,2,10],[1,3,2]]
sol = Solution()
print(sol.maximizeTheProfit(n, offers))
