
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
    def minimumSteps(self, s: str) -> int:
        cache = [int(v) for v in s]
        l = r = len(s) - 1
        ans = 0
        while l > 0:
            while r >= 0 and cache[r] == 1:
                r -= 1
            if l > r:
                l = r
            while l >= 0 and cache[l] == 0:
                l -= 1
            if r >= 0 and l >= 0:
                cache[l] = 0
                cache[r] = 1
                ans += r - l
        # print(cache)
        return ans
    
s = "10101"
sol = Solution()
print(sol.minimumSteps(s))
