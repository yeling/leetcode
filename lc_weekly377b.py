
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
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.append(1)
        hFences.append(m)
        hFences.sort()
        vFences.append(1)
        vFences.append(n)
        vFences.sort()
        hSet = set()
        vSet = set()
        ans = -1
        for i in range(1,len(hFences)):
            s = hFences[i - 1]
            for j in range(i, len(hFences)):
                e = hFences[j]
                hSet.add(e - s)
        
        for i in range(1,len(vFences)):
            s = vFences[i - 1]
            for j in range(i, len(vFences)):
                e = vFences[j]
                vSet.add(e - s)
    
        # print(hSet, vSet)
        for v in hSet:
            if v in vSet:
                ans = max(ans, v)
        if ans != -1:
            ans = (ans * ans) %MOD
        return ans
    
m = 4
n = 3
hFences = [2,3]
vFences = [2]
# m = 6
# n = 7
# hFences = [2]
# vFences = [4]
sol = Solution()
print(sol.maximizeSquareArea(m,n,hFences, vFences))
