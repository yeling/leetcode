
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
    def getLucky(self, s: str, k: int) -> int:
        numStr = ''
        for v in s:
            numStr += str(ord(v) - 97 + 1)
        i = 0
        # print(numStr)
        while i < k and int(numStr) > 10:
            next = 0
            for v in numStr:
                next += int(v)
            numStr = str(next)
            i += 1
            # print(numStr)

        return int(numStr)
    
s = "leetcode"
k = 2
sol = Solution()
print(sol.getLucky(s,k))
