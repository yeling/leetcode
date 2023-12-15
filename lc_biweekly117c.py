
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
    def stringCount(self, n: int) -> int:   
        # 
        if n < 4:
            return 0
        ans = 1
        ans *= (n) * (n - 1) * (n - 2) 
        ans //= 2
        for _ in range(n - 4):
            ans *= 26
            # ans %= MOD
    
        return ans
    
   
n = 10
sol = Solution()
# 526083947580
print(sol.stringCount(n))
