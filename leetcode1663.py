
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
    def getSmallestString(self, n: int, k: int) -> str:
        left = k - n
        res = [1] * n
        r = n - 1
        while left > 0:
            if left > 25:
                left -= 25
                res[r] += 25
                r -= 1
            else:
                res[r] += left
                left = 0
                r -= 1
        ans = ''
        for i,v in enumerate(res):
            ans  += chr(96 + v)
        return ans
    
n = 5
k = 73
sol = Solution()
print(sol.getSmallestString(n, k))
