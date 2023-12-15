
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
    def subtractProductAndSum(self, n: int) -> int:
        m = 1
        s = 0
        while n > 0:
            s += n%10
            m *= n%10
            n = n//10
        
        return m - s
    

sol = Solution()
n = 234
print(sol.subtractProductAndSum(n))
