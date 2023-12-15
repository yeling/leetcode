
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
    def countWays(self, ranges: List[List[int]]) -> int:
        # print(ranges)
        ranges.sort()
        # print(ranges)
        cur = ranges[0]
        ans = 2
        for s,e in ranges:
            if cur[1] < s:
                ans *= 2
                ans %= MOD
                cur = [s,e]
            else:
                cur[1] = max(cur[1],e)

        return ans%MOD
    
ranges = [[1,3],[10,20],[2,5],[4,8]]
# ranges = [[6,10],[5,15]]
sol = Solution()
print(sol.countWays(ranges))
