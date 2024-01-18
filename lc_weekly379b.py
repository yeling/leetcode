
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
    # 663 / 737 个通过测试用例
    # 728 / 737 个通过测试用例
    # 731 / 737 个通过测试用例
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:    
        ans = 2
        if (c + d)%2 == (e + f)%2:
            ans = min(ans, 2)
        if a == e:
            if a != c:
                ans = 1
            elif (b < d and f < d) or (b > d and f > d):
                ans = min(ans,1)
            else:
                ans = min(ans, 3)
        elif b == f:
            if b != d:
                ans = 1
            elif (a < c and e < c) or (a > c and e > c):
                ans = min(ans,1)
            else:
                ans = min(ans, 3)
        else:
            ans = 2
        # dir = [[1,1], [1, -1], [-1,1],[-1,-1]]
        if abs(c - e) == abs(d - f):
            if d != f and b != f and (c - e) /(d - f) == (a - e)/(b - f):
                if (c < a and e < a) or (c > a and e > a):
                    ans = 1
            else:
                ans = 1
        return ans
    
a = 6
b = 8
c = 6
d = 6
e = 6
f = 3
# 6
# 8
# 6
# 6
# 6
# 3

sol = Solution()
print(sol.minMovesToCaptureTheQueen(a,b,c,d,e,f))
