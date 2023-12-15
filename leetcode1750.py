
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
    # 98 / 100 
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                dst = s[l]
                l += 1
                r -= 1
                while l <= r and s[l] == dst:
                    l += 1
                while r >= l and s[r] == dst: 
                    r -= 1
            else:
                break

        return r - l + 1
    
s = "cabaabac"
s = "cac"
s = "aabccabba"
s = "abbbbbbbbbbbbbbbbbbba"
sol = Solution()
print(sol.minimumLength(s))
