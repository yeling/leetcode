# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(w,d,h,a,b,f,g):
    ans = INF
    ans = min(ans, h + g + b + abs(a - f))
    ans = min(ans, h + d - g + d - b + abs(a - f))
    ans = min(ans, h + f + a + abs(b - g))
    ans = min(ans, h + w - f + w - a + abs(b - g))
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    w, d, h = li()
    a, b, f, g = li()
    main(w,d,h,a,b,f,g)

   
