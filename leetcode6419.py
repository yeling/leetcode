
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.ans = 0
        def dfs(curr):
            # print(curr, self.ans)
            if 2 * curr + 1 > n:
                return
            dfs(2* curr)
            dfs(2* curr + 1)
            self.ans += abs(cost[2*curr - 1] - cost[2*curr])
            cost[curr - 1] += max(cost[2*curr - 1], cost[2*curr])
            
            
        dfs(1)
        return self.ans
    
n = 7
cost = [1,5,2,2,3,3,3]
n = 3
cost = [5,3,3]
# n = 15
# cost = [764,1460,2664,764,2725,4556,5305,8829,5064,5929,7660,6321,4830,7055,3761]
sol = Solution()
print(sol.minIncrements(n, cost))
# 15735
