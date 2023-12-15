
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
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        isBulky = False
        isHeavy = False
        if length >= 10000 or width >= 10000 or height >= 10000:
            isBulky = True
        if length * width * height >= 10 ** 9:
            isBulky = True
        if mass >= 100:
            isHeavy = True
        
        if isBulky and isHeavy:
            return "Both"
        elif isBulky:
            return "Bulky"
        elif isHeavy:
            return "Heavy"
        else:
            return "Neither"
        

        return
    
length = 1000
width = 35
height = 700
mass = 300
sol = Solution()
print(sol.categorizeBox(length, width, height, mass))
