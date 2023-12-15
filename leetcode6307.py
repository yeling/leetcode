
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
    def passThePillow(self, n: int, time: int) -> int:
        time = time%(2*(n - 1))
        ans = 0
        if time >= n - 1:
            ans = n - (time - (n - 1))
        else:
            ans = time + 1

        return ans
    
n = 3
time = 5
sol = Solution()
print(sol.passThePillow(n, time))
