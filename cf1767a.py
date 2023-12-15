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

def main(p1,p2,p3):
    c = 0
    if p1[0] == p2[0] or p2[0] == p3[0] or p1[0] == p3[0]:
        c += 1
    if p1[1] == p2[1] or p2[1] == p3[1] or p1[1] == p3[1]:
        c += 1
    if c > 1:
        print("No")
    else:
        print("YES")

    return 

caseNum = int(input())
for i in range(0, caseNum):
    input()
    p1 = li()
    p2 = li()
    p3 = li()
    main(p1,p2,p3)
    
