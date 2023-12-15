
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
    def furthestDistanceFromOrigin(self, moves: str) -> int:  
        cnt = Counter(moves)

        return abs(cnt['L'] - cnt['R']) + cnt['_']
    
moves = "L_RL__R"
moves = "_______"
sol = Solution()
print(sol.furthestDistanceFromOrigin(moves))
