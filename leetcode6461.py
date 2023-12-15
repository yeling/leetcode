
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
from heapq import *
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def isFascinating(self, n: int) -> bool:
        temp = ''
        temp += str(n) + str(2*n) + str(3*n)
        arr = []
        for v in temp:
            arr.append(v)
        # print(arr)
        for i in range(0,10):
            if i == 0:
                if arr.count(str(i)) != 0:
                    return False
            elif arr.count(str(i)) != 1:
                return False
                
        return True
    

n = 192
n = 100
sol = Solution()
print(sol.isFascinating(n))
