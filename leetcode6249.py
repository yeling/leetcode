
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            return n // 2
        else:
            return n

n = 4
sol = Solution()
print(sol.numberOfCuts(n))
