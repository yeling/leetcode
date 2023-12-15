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

def main(n,x):
    ans = n
    m = n
    while ans >= x:
        ans &= m
        print('ans', ans)
        if ans == x:
            print(m)
            return
        m += 1
    print(-1)
    return 

def main2(n,x):
    ans = n
    m = n
    while ans >= x:
        ans &= m
        if ans == x:
            print(m)
            return
        m += 1
    print(-1)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,x = li()
    main(n,x)

   
