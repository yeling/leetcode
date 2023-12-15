
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
    def countHomogenous(self, s: str) -> int:
        ans = 0
        c = 0
        last = None
        for v in s:
            if v == last:
                c += 1
            else:
                c = 1
                last = v

            ans += c
            ans = ans%MOD
        return ans
    
s = "abbcccaa"
# s = "abb"
s = "zzzzz"
sol = Solution()
print(sol.countHomogenous(s))
