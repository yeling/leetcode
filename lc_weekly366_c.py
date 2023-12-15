
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
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        pos = []
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                pos.append(i)
        c = len(pos)
        if c & 1 != 0:
            return -1
        # print(pos)
        # 元素个数
        dp = [INF] * (c + 1)
        dp[0] = 0
        for i in range(1,c+1):
            dp[i] = min(dp[i], dp[i - 1] + 0.5 * x)
            if i - 2 >= 0:
                dp[i] = min(dp[i], dp[i - 2] + pos[i - 1] - pos[i - 2])
    
        # print(dp)
        return int(dp[c])
    
s1 = "1100011000"
s2 = "0101001010"
x = 2
s1 = "10110"
s2 = "00011"
x = 4

s1 = "101101"
s2 = "000000"
x = 6
sol = Solution()
print(sol.minOperations(s1, s2, x))
