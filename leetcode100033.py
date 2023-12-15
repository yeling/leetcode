
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
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
        return
    
n = 3
k = 2
budget = 15
composition = [[1,1,1],[1,1,10]]
stock = [0,0,100]
cost = [1,2,3]
sol = Solution()
print(sol.maxNumberOfAlloys(n, k, budget, composition, stock, cost))
