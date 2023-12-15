
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
    def canBeEqual2(self, s1: str, s2: str) -> bool:
        n = len(s1)
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            elif i + 2 < n and s1[i + 2] == s2[i] and s1[i] == s2[i + 2]:
                continue
            else:
                return False
            
        return True
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        temp =  s1[2] + s1[1] + s1[0] + s1[3]
        if temp == s2:
            return True
        temp =  s1[2] + s1[3] + s1[0] + s1[1] 
        if temp == s2:
            return True
        temp =  s1[0] + s1[3] + s1[2] + s1[1] 
        if temp == s2:
            return True
        return False
        
            
    
s1 = "abcd"
s2 = "cdab"
s1 = "abcd"
s2 = "dacb"
sol = Solution()
print(sol.canBeEqual(s1,s2))
