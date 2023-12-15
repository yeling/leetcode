
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
    def minimumCost(self, s: str) -> int:    
        n = len(s)
        ans = 0
        for i in range(1,n):
            if s[i] != s[i-1]:
                ans += min(i, n-i)

        return ans
    
s = "010101"
s = "01010"
sol = Solution()
print(sol.minimumCost(s))
