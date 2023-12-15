
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
    def secondHighest2(self, s: str) -> int:
        first = -1
        second = -1
        for v in s:
            uni = ord(v) - 48
            if uni >= 0 and uni <= 9:
                if uni > first:
                    second = first
                    first = uni
                elif uni == first:
                    continue
                elif uni > second:
                    second = uni
                
        return second
    
    def secondHighest(self, s: str) -> int:
        first = -1
        second = -1
        for v in s:
            if v.isdigit() == False:
                continue
            uni = int(v)
            if uni >= 0 and uni <= 9:
                if uni > first:
                    second = first
                    first = uni
                elif first > uni > second:
                    second = uni
                
        return second
    
s = "dfa12321afd"
s = "abc1111"
sol = Solution()
print(sol.secondHighest(s))
