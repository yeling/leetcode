
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

def max(a,b):
    if a > b:
        return a
    else:
        return b
    
def min(a, b):
    if a < b:
        return a
    else:
        return b

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        mh = 0
        for i in range(1, len(horizontalCuts)):
            mh = max(mh, horizontalCuts[i] - horizontalCuts[i - 1])
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        mw = 0
        for i in range(1, len(verticalCuts)):
            mw = max(mw, verticalCuts[i] - verticalCuts[i - 1])
        
        return (mw * mh)%MOD
    
h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]
sol = Solution()
print(sol.maxArea(h, w, horizontalCuts, verticalCuts))
