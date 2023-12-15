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

def main(n, x1, y1, x2, y2):
    
    def dis(x1,y1,n):
        c = (n+1)/2      
        return int(max(abs(c - x1), abs(c - y1)))
    
    p1 = dis(x1, y1, n)
    p2 = dis(x2, y2, n)
    print(abs(p1 - p2))
    # print(abs(p1 - p2), p1, p2)
    return 

# main(4, 3, 1, 4, 1)

caseNum = int(input())
for i in range(0, caseNum):
    n,x1,y1,x2,y2 = li()
    main(n, x1, y1, x2, y2)
   
