
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
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        mrow = 0
        mcol = 0
        hBars.sort()
        vBars.sort()
        curr = 2
        i = 0
        while i < len(hBars):
            curr = i
            while curr + 1 < len(hBars) and hBars[curr + 1] == hBars[curr] + 1:
                curr += 1
            mrow = max(mrow, curr - i + 2)
            i = curr + 1
        
        i = 0
        while i < len(vBars):
            curr = i
            while curr + 1 < len(vBars) and vBars[curr + 1] == vBars[curr] + 1:
                curr += 1
            mcol = max(mcol, curr - i + 2)
            i = curr + 1
        
        edge = min(mrow, mcol)
    
        return edge * edge
    
n = 2
m = 2
hBars = [2,3]
vBars = [2,3]
# n = 1
# m = 1
# hBars = [2]
# vBars = [2]
sol = Solution()
print(sol.maximizeSquareHoleArea(n, m, hBars, vBars))
