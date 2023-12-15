
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for q in queries:
            s = 0
            for p in points:
                dx = q[0] - p[0]
                dy = q[1] - p[1]
                if dx * dx + dy * dy <= q[2] * q[2]:
                    s += 1
            res.append(s)
        return res
    
    
points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]

sol = Solution()
print(sol.countPoints(points, queries))

