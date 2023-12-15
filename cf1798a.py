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

def main(n, a, b):
    ma = min(a[-1], b[-1])
    mb = max(a[-1], b[-1])
    for i in range(n):
        if min(a[i], b[i]) <= ma and max(a[i],b[i]) <= mb:
            continue
        else:
            print("No")
            return 
    print("Yes")
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = li()
    b = li()
    main(n, a, b)
   
