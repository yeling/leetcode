
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
    def checkPowersOfThree(self, n: int) -> bool:
        t = n
        while t > 0:
            if t % 3 > 1:
                return False
            t = t // 3
        return True

n = 91
n = 31
sol = Solution()
print(sol.checkPowersOfThree(n))
