
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
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(fx - sx)
        dy = abs(fy - sy)
        dis = max(dx,dy) 
        if dis == 0 and t == 1:
            return False
        
        if dis <= t:
            return True
        else:
            return False
        return
    
sx = 2
sy = 4
fx = 7
fy = 7
t = 6
# sx = 3
# sy = 1
# fx = 7
# fy = 3
# t = 3
sol = Solution()
print(sol.isReachableAtTime(sx, sy, fx, fy, t))
