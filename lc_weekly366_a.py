
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n1 = 0
        n2 = 0
        for i in range(1, n + 1):
            if i%m != 0:
                n1 += i
            else:
                n2 += i
        
        return n1 - n2
    
n = 5
m = 6
sol = Solution()
print(sol.differenceOfSums(n, m))
