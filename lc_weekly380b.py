
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
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        an = len(a)
        bn = len(b)
        ap = []
        bp = []
        for i in range(n):
            ta = s[i:i+an]
            if ta == a:
                ap.append(i)
            tb = s[i:i+bn]
            if tb == b:
                bp.append(i)
        ans = []
        for v in ap:
            p1 = bisect_right(bp, v + k)
            p2 = bisect_left(bp, v - k)
            # print(v, p1, p2)
            if p1 - p2 > 0:
                ans.append(v)
        # print(ap, bp)
        return ans
    
s = "isawsquirrelnearmysquirrelhouseohmy"
a = "my"
b = "squirrel"
k = 15
s = "abcd"
a = "a"
b = "a"
k = 4
sol = Solution()
print(sol.beautifulIndices(s, a, b, k))
