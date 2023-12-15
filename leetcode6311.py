
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
    def coloredCells(self, n: int) -> int:
        return (2*n - 1) * ( 2*n - 1) - (n - 1) * n * 2
    

n = 1
sol = Solution()
print(sol.coloredCells(n))
