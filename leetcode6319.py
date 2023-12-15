
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
    def evenOddBit(self, n: int) -> List[int]:
        ns = bin(n)
        ns = ns[2:]
        ans = [0,0]
        # print(ns)
        for i in range(len(ns)):
            if ns[-1-i] == '1':
                ans[i%2] += 1

        return ans
    
n = 17
n = 2
sol = Solution()
print(sol.evenOddBit(n))
