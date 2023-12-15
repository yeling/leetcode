
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
    def tilingRectangle(self, n: int, m: int) -> int:  
        cnt = 0
        while n > 1 or m > 1:
            print(n, m)
            if n == m:
                break
            elif n > m:
                n = n - m
            elif n < m:
                m = m - n
            cnt += 1
        cnt += 1
        return cnt
    
n = 13
m = 11
sol = Solution()
print(sol.tilingRectangle(n, m))
