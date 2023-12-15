
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        i ,j = 0,0
        cache = set()
        temp = 0
        while temp <= bound:
            temp = x ** i
            j = 1
            next = temp + 1
            while next <= bound:
                cache.add(next)
                next = temp + (y ** j)
                j += 1
                if y == 1:
                    break
            i += 1
            if x == 1:
                break
            # print(i, cache)
        # cache.remove(0)


        return list(cache)
    
x = 3
y = 5
bound = 15
x = 2
y = 1
bound = 10
sol = Solution()
print(sol.powerfulIntegers(x,y, bound))
