
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
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1,n + 1):
            temp = bin(i)[2:]
            # print(temp)
            if temp not in s:
                return False
            
        return True
    
s = "0110"
n = 3
sol = Solution()
print(sol.queryString(s, n))
