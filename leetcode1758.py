
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    def minOperations(self, s: str) -> int:
        c0,c1 = 0,0
        for i,v in enumerate(s):
            if i%2 == 0:
                if v == '1':
                    c0 += 1
                else:
                    c1 += 1
            else:
                if v == '1':
                    c1 += 1
                else:
                    c0 += 1

        return min(c0,c1)

s = "0100"
s = "1111"
sol = Solution()
print(sol.minOperations(s))
