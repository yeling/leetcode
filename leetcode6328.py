
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
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        val = [-2000] * 26
        for i,v in enumerate(chars):
            val[ord(v) - ord('a')] = vals[i]
        # print(val)
        sval = [0]*(len(s))
        for i,v in enumerate(s):
            if val[ord(v) - ord('a')] == -2000:
                sval[i] = ord(v) - ord('a') + 1
            else:
                sval[i] = val[ord(v) - ord('a')]
        # print(sval)
        l = 0
        r = 0
        total = 0
        ans = 0
        while r < len(s):
            if total >= 0:
                total += sval[r]
                r += 1
            else:
                total -= sval[l]
                l += 1
            ans = max(ans, total)
            # print(l, r, ans)

        return ans
    

s = "adaaaddaaaaaa"
chars = "d"
vals = [-2]
# s = "abc"
# chars = "abc"
# vals = [-1,-1,-1]
sol = Solution()
print(sol.maximumCostSubstring(s, chars, vals))
