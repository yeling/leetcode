
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
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDis = 10 ** 5
        minIndex = -1
        for i,v in enumerate(points):
            dis = minDis
            if v[0] == x:
                dis = abs(v[1] - y)
            elif v[1] == y:
                dis = abs(v[0] - x)
            # print(dis)
            if dis < minDis:
                minDis = dis
                minIndex = i

        return minIndex   

x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]   
sol = Solution()
print(sol.nearestValidPoint(x,y,points))
