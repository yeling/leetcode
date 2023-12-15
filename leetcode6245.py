
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
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n+1):
            if (1 + i)*i == (i + n)* (n - i + 1):
                return i
        return -1

n = 15
sol = Solution()
print(sol.pivotInteger(n))
