
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import sys

MOD = 10 ** 9 + 7

EPS = 1e-6 #浮点数的运算补偿
def fequal(x, y):
    return abs(x - y) < EPS

class Solution:
    # 14 / 70
    # 17 / 70 
    # AC
    def mirrorReflection(self, p: int, q: int) -> int:
        if q == 0:
            return 0
        if q == p:
            return 1
        def cross(k,b,x,y):
            if x == -1:
                return ((y-b)/k, y)
            elif y == -1:
                return (x, k * x + b)
        #start 0,1,2,3
        x,y,x1,y1 = 0,0,p,q
        while True:
            # print(x, y, x1, y1)
            k = (y - y1)/(x - x1)
            b = y - k * x
            k1 = -k
            b1 = 2 * y1 - b
            #新的线与4条边的交点，在矩形内部的为准
            next = [(-1,0),(-1,p),(0,-1),(p,-1)]
            for v in next:
                t = cross(k1,b1,v[0],v[1])
                if x1 == v[0] or y1 == v[1]:
                    continue
                if t[0] == x or t[1] == y:
                    continue

                # print(t)
                if fequal(t[0],0) and fequal(t[1],p):
                    return 2
                elif fequal(t[0],p) and fequal(t[1],p):
                    return 1
                elif fequal(t[0],p) and fequal(t[1],0):
                    return 0
                elif t[0] <= p and t[0] >= 0 and t[1] <= p and t[1] >= 0:
                    x = x1
                    y = y1
                    x1 = t[0]
                    y1 = t[1]
                    
        return -1

p = 6
q = 5
sol = Solution()
print(sol.mirrorReflection(p,q))
print(sys.float_info)
t = 2e-5
print(t)
