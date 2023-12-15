
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:   
        ans = num + 2 * t 
        return ans
    
num = 4
t = 1
num = 3
t = 2
sol = Solution()
print(sol.theMaximumAchievableX(num, t))
