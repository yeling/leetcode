
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        a = None
        b = None
        if length >= 10 ** 4 or width >= 10**4 or height >= 10**4 or length * width * height >= 10 ** 9:
            a = "Bulky"
        if mass >= 100:
            b = "Heavy"
        ans = "Neither"
        if a and b:
            ans = "Both"
        elif a:
            ans = a
        elif b:
            ans = b
        return ans
        
    
length = 1000
width = 35
height = 700
mass = 300
length = 200
width = 50
height = 800
mass = 50

sol = Solution()
print(sol.categorizeBox(length, width, height, mass))
