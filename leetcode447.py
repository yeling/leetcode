
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
    def numberOfBoomerangs2(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k:
                        d1 = (points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + (points[i][1] - points[j][1]) *  (points[i][1] - points[j][1])
                        d2 = (points[i][0] - points[k][0]) * (points[i][0] - points[k][0]) + (points[i][1] - points[k][1]) *  (points[i][1] - points[k][1])
                        if d1 == d2:
                            ans += 1

        return ans
    
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n):
            cache = defaultdict(int)
            for j in range(n):
                if i != j:
                    d1 = (points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + (points[i][1] - points[j][1]) *  (points[i][1] - points[j][1])
                    if d1 in cache:
                        ans += cache[d1]
                    cache[d1] += 2

        return ans
    
    
points = [[0,0],[1,0],[2,0]]
sol = Solution()
print(sol.numberOfBoomerangs2(points))
print(sol.numberOfBoomerangs(points))
