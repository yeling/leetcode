
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
from datetime import *
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime(year, month, day).strftime("%A")
    
day = 15
month = 8
year = 2019
sol = Solution()
print(sol.dayOfTheWeek(year, month, day))
