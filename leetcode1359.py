
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
    def countOrders(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = (i * (2*i - 1)) * dp[i - 1]
            dp[i] %= MOD 
        return dp[n] % MOD 
    
n = 3
sol = Solution()
print(sol.countOrders(n))
