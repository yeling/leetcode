
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
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1],x[2]))
        # print(trips) 
        #t n curr
        curr = 0
        cache = defaultdict(int)   
        for d, f, t in trips:
            for v in list(cache.keys()):
                if v <= f:
                    curr -= cache[v]
                    del cache[v]
            if curr + d > capacity:
                return False
            cache[t] += d
            curr += d
        return True

        return
    
trips = [[3,3,7],[2,1,5]]
capacity = 4
trips = [[2,1,5],[3,3,7]]
capacity = 5
sol = Solution()
print(sol.carPooling(trips, capacity))
