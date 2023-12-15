
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
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time = [0] * n
        for i,(d,s) in enumerate(zip(dist, speed)):
            time[i] = (d - 1)//s + 1
        time.sort()
        # print(time)
        for i in range(0,n):
            if time[i] < i + 1:
                return i
        
        return n
    
# dist = [3,2,4]
# speed = [5,3,2]
dist = [4,2,3]
speed = [2,1,1]
sol = Solution()
print(sol.eliminateMaximum(dist, speed))
