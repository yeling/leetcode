
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
    #TLE
    # 293 / 1008 
    def numOfBurgers2(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        for i in range(cheeseSlices + 1):
            if 4 * i + 2 * (cheeseSlices - i) == tomatoSlices:
                return [i, cheeseSlices - i]    
        return []
    
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        a = tomatoSlices - 2 * cheeseSlices
        if a < 0 or a%2 == 1:
            return []
        a = a//2
        b = cheeseSlices - a 
        if b < 0:
            return []
        return [a, b]
    
tomatoSlices = 16
cheeseSlices = 7
sol = Solution()
print(sol.numOfBurgers(tomatoSlices, cheeseSlices))
