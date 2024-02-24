
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
    def flowerGame(self, n: int, m: int) -> int:
        nodd = n//2 + n%2
        neven = n//2
        modd = m//2 + m%2
        meven = m//2
        ans = nodd * meven + neven * modd 
        return ans
    
n = 3
m = 2
n = 1
m = 1
sol = Solution()
print(sol.flowerGame(n,m))
