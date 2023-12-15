
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
    def minimumMoves(self, s: str) -> int:
        ans = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == 'X':
                ans += 1
                i += 3
            else:
                i += 1
        return ans
    
s = "XXOX"
s = "XXX"
s = "OOOO"
sol = Solution()
print(sol.minimumMoves(s))
