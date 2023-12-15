
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
    def doesValidArrayExist(self, derived: List[int]) -> bool:  
        n = len(derived)
        s = 0
        for i in range(0,n):
            s ^= derived[i]
        return s == 0
    
derived = [1,1]
sol = Solution()
print(sol.doesValidArrayExist(derived))
