
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
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def dis(x,y):
            dx = x[0] - y[0]
            dy = x[1] - y[1]
            return sqrt(dx * dx + dy * dy)
        
        n = len(points)
        ms = 0
        for i in range(n):
            for j in range(i + 1,n):
                for k in range(j+1,n):
                    a = dis(points[i],points[j])
                    b = dis(points[i],points[k])
                    c = dis(points[k],points[j])
                    p = (a + b + c)/2
                    s = (p*(p-a)*(p-b)*(p-c))
                    ms = max(ms,s)
        return sqrt(ms)

points = [[0,0],[0,1],[1,0],[0,2],[2,0]]   
sol = Solution()
print(sol.largestTriangleArea(points))
