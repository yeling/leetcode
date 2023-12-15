
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
    def checkStrings(self, s1: str, s2: str) -> bool:   
        cache1 = [[]*2 for _ in range(2)]
        cache2 = [[]*2 for _ in range(2)]

        n = len(s1)
        for i in range(n):
            cache1[i%2].append(s1[i])
            cache2[i%2].append(s2[i])
        cache1[0].sort()
        cache1[1].sort()
        cache2[0].sort()
        cache2[1].sort()
        if cache1[0] == cache2[0] and cache1[1] == cache2[1]:
            return True
        else:
            return False

    
s1 = "abcdba"
s2 = "cabdab"
s1 = "abe"
s2 = "bea"
sol = Solution()
print(sol.checkStrings(s1,s2))
