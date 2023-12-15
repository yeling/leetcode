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

def main(a,b):
    a = abs(a)
    b = abs(b)
    if a < b:
        a,b = b,a
    
    ans = 2 * b
    diff = a - b
    if diff > 0:
        ans += 1 + (diff - 1) * 2
    print(ans)
    return 

# main(4,1)

caseNum = int(input())
for i in range(0, caseNum):
    a,b = li()
    main(a,b)
   
