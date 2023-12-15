
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
    # 918 / 1072
    def repairCars(self, ranks: List[int], cars: int) -> int:
        stack = []
        #(sum, num, unit)
        for v in ranks:
            heappush(stack, (v,1,v))

        ans = 0
        for i in range(cars):
            temp = heappop(stack)
            ans, num, unit = temp
            heappush(stack, (unit * (num + 1) * (num + 1), num + 1, unit))
            # print(temp)
        # print(stack)
        return ans
    
ranks = [4,2,3,1]
cars = 10
ranks = [4,3,1,4,3,4,6,3,6,6,4,6,1,3,5,1,1,1,4,6,6,3,1,7,4,5,4,5,7,2,2,3,1,2,6,5,3,2,6,3,7,7,2,4]
cars = 35
sol = Solution()
print(sol.repairCars(ranks, cars))
