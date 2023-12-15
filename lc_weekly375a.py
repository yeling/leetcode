
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
    def countTestedDevices(self, batteryPercentages: List[int]) -> int: 
        ans = 0
        for v in batteryPercentages:
            if v - ans > 0:
                ans += 1   
        return ans
    
batteryPercentages = [1,1,2,1,3]
batteryPercentages = [0,1,2]
sol = Solution()
print(sol.countTestedDevices(batteryPercentages))
