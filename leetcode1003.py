
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            print(s)
            i = len(s) - 1
            flag = False
            while i >= 2:
                if s[i-2:i+1] == 'abc':
                    s = s[0:i-2] + s[i+1:]
                    flag = True
                i -= 1
            if flag == False:
                break

        
        return len(s) == 0
    
s = "abcabcababcc"
# s = "abca"
sol = Solution()
print(sol.isValid(s))
