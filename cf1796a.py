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

def getFB(n):
    ans = ''
    for i in range(1,n+1):
        if i%3 == 0:
            ans += 'F'
        if i%5 == 0:
            ans += 'B'
    
    return ans

all = getFB(60)
def main(n, s):
    if s in all:
        print('Yes')
    else:
        print('No')
    return 

# print(all, len(all))

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n, s)
