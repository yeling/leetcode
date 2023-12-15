
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
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:  
        l = 0
        r = 0
        while l < len(str1) and r < len(str2):
            if str1[l] == 'z':
                next = 'a'
            else:
                next = chr(ord(str1[l]) + 1)
            if str1[l] == str2[r] or next == str2[r]:
                l += 1
                r += 1
            else:
                l += 1

            if r == len(str2):
                return True  
        return False
    
str1 = "abc"
str2 = "ad"
str1 = "zc"
str2 = "ad"
str1 = "ab"
str2 = "d"
sol = Solution()
print(sol.canMakeSubsequence(str1, str2))
