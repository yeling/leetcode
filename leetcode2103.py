
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
    def countPoints(self, rings: str) -> int:  
        cnt = [set() for _ in range(10)] 
        for i in range(len(rings)//2):
            cnt[int(rings[2*i + 1])].add(rings[2*i])
        ans = 0
        # print(cnt)
        for v in cnt:
            if len(v) == 3:
                ans += 1
        return ans
    
rings = "B0B6G0R6R0R6G9"
rings = "B0R0G0R9R0B0G0"
rings = "G4"
sol = Solution()
print(sol.countPoints(rings))
