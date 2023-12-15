
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
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int: 
        ans = 0
        for v in hours:
            if v >= target:
                ans += 1   
        return ans
    
hours = [0,1,2,3,4]
target = 2
sol = Solution()
print(sol.numberOfEmployeesWhoMetTarget(hours, target))
