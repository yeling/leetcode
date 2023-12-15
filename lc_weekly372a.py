
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
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        i = 0
        while i < len(s1) and i < len(s2) and i < len(s3):
            if s1[i] == s2[i] == s3[i]:
                i += 1
                continue
            else:
                break 
        if i == 0:
            return -1
        
        return len(s1) + len(s2) + len(s3) - 3 * i
    
s1 = "abc"
s2 = "abb"
s3 = "ab"
s1 = "dac"
s2 = "bac"
s3 = "cac"
sol = Solution()
print(sol.findMinimumOperations(s1, s2, s3))
