
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        return len(t) - j
        
        

s = "coaching"
t = "coding"
s = "abcde"
t = "a"
s = "z"
t = "abcde"
sol = Solution()
print(sol.appendCharacters(s,t))
