
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
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        x = 0
        for i in range(0,n):
            ai = (a ^ (1 << i)) - a
            bi = (b ^ (1 << i)) - b
            if b * ai + a * bi + ai * bi  > 0:
                x |= (1<<i)
                a = a ^(1<<i)
                b = b ^(1<<i)
            # print(i, a, b, ai, bi)

        ans = a * b 
        return ans % MOD
    
    def check(self, a: int, b: int, n: int) -> int:
        ans = 0
        for  i in range(0, 2**n):
            curr = (i ^ a) * (i ^ b)
            print(i, curr)
            ans = max(ans, curr)
        print(ans)

a = 12
b = 5
n = 4
a = 6
b = 7 
n = 5
a = 1
b = 6
n = 3
sol = Solution()
# sol.check(a, b, n)
print(sol.maximumXorProduct(a, b, n))
