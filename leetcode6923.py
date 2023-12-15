
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
    def minimumBeautifulSubstrings(self, s: str) -> int:
        cache = set([bin(5**i)[2:] for i in range(8)])
        # print(cache)
        n = len(s)
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(i+1):
                # print(s[j:i+1])
                if s[j:i + 1] in cache: 
                    dp[i + 1] = min(dp[i + 1], dp[j] + 1)
        # print(dp)
        if dp[n] == INF:
            return - 1
        return dp[n]
    
s = "100111"
sol = Solution()
print(sol.minimumBeautifulSubstrings(s))
