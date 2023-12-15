
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
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        n = len(types)
        dp = [0] * (target + 1)
        next = dp[:]
        for count, mask in types:
            next = dp[:]
            #0
            for j in range(1, count + 1):
                if j * mask <= target:
                    next[j * mask] += 1
                    next[j * mask] %=MOD
                else:
                    break
            # > 0
            # print(next)
            for i in range(1,target):
                if dp[i] == 0:
                    continue
                for j in range(1, count + 1):
                    if i + j * mask <= target:
                        next[i + j * mask] += dp[i]
                        next[i + j * mask] %=MOD
                    else:
                        break
            dp = next[:]
            # print(dp)

        # print(dp)

        return dp[target]%MOD
    
target = 18
types = [[6,1],[3,2],[2,3]]

target = 6
types = [[6,1],[3,2],[2,3]]

# target = 5
# types = [[50,1],[50,2],[50,5]]

sol = Solution()
print(sol.waysToReachTarget(target, types))
