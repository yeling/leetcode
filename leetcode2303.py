
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
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        s = 0
        ans = 0
        for i,(upper,percent) in enumerate(brackets):
            percent /= 100
            if income >= upper:
                if i == 0:
                    ans += upper * percent
                else:
                    ans += (upper - brackets[i-1][0]) * percent
            else:
                if i == 0:
                    ans += income * percent
                else:
                    ans += (income - brackets[i-1][0]) * percent
                break
        return ans
    
brackets = [[3,50],[7,10],[12,25]]
income = 10
brackets = [[1,0],[4,25],[5,50]]
income = 2
sol = Solution()
print(sol.calculateTax(brackets, income))
