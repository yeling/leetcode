
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
    def canChange(self, start: str, target: str) -> bool:
        l = 0
        r = 0
        n = len(start)
        while l < len(start) and r < len(target):
            while l < len(start) and start[l] == '_':
                l += 1
            while r < len(target) and target[r] == '_':
                r += 1
            if l < len(start) and r < len(target):
                if start[l] == target[r] and ((start[l] == 'L' and l >= r) or (start[l] == 'R' and l <= r)):
                    l += 1
                    r += 1
                    continue
                else:
                    return False
        while l < len(start) and start[l] == '_':
                l += 1
        while r < len(target) and target[r] == '_':
            r += 1
        return l == n and r == n
    
start = "_L__R__R_"
target = "L______RR"
start = "R_L_"
target = "___RL"
sol = Solution()
print(sol.canChange(start, target))
