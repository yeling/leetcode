
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
    # 75 / 96 
    def maximumScore(self, a: int, b: int, c: int) -> int:
        all = [a,b,c]
        all.sort()
        a,b,c = all
        ans = 0
        if a + b <= c:
            ans = a + b
        else:
            if (c + b - a)%2 == 0:
                ans = c + b - (c + b - a)//2 
            else:
                ans = c + b - (c + b - a)//2  - 1
        return ans
    
a = 2
b = 4
c = 6
a = 24
b = 19
c = 24
sol = Solution()
print(sol.maximumScore(a,b,c))
