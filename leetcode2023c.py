
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:

        def pointInRect(x,y, x1, y1, r):
            ans = False
            if x <= x1 + r and x >= x1 - r and y <= y1 + r and y >= y1 - r:
                ans = True
            # print(x,y,x1,y1, r, ans)
            return ans

        cache = set()
        n = len(forceField)
        #放大两倍，避免0.5
        for i in range(n):
            forceField[i] = [forceField[i][0]*2,forceField[i][1]*2, forceField[i][2]]
        
        #正方形求交点
        for i in range(n):
            for j in range(i+1,n):
                x1,y1,r1 = forceField[i]
                x2,y2,r2 = forceField[j]
                #
                if abs(x1 - x2) + abs(y1 - y2) <= r1 + r2:
                    points1 = [(x1 - r1, y1 - r1),(x1 - r1, y1 + r1),(x1 + r1, y1 - r1),(x1 + r1, y1 + r1)]
                    points2 = [(x2 - r2, y2 - r2),(x2 - r2, y2 + r2),(x2 + r2, y2 - r2),(x2 + r2, y2 + r2)]
                    for v in points1:
                        if pointInRect(v[0],v[1],x1,y1,r1) and pointInRect(v[0],v[1],x2,y2,r2):
                            cache.add(v)
                    for v in points2:
                        if pointInRect(v[0],v[1],x1,y1,r1) and pointInRect(v[0],v[1],x2,y2,r2):
                            cache.add(v)
        #交点求最值
        print(cache)

                

        return
    
forceField = [[4,4,6],[7,5,3],[1,6,2],[5,6,3]]
forceField = [[0,0,1],[1,0,1]]
sol = Solution()
print(sol.fieldOfGreatestBlessing(forceField))
