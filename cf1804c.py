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

def main2(n, x, p):
    for i in range(1,p + 1):
        temp = (i + 1) * i //2
        if temp%n == (n - x)%n:
            print('Yes')
            return 
    print('No')
    return 

def main(n, x, p):
    s = 1
    if p > n:
        s = 0
    # p = min(p,n)
    for i in range(1,2*n):
        temp = (i + 1) * i //2
        if temp%n == (n - x)%n:
            print('Yes')
            return 
    print('No')
    return 


# for i in range(5,20):
# main(2, 0, 5)
# main2(2,0,5)

caseNum = int(input())
for i in range(0, caseNum):
    n,x,p = li()
    main(n, x, p)
   
