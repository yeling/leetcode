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
MOD = 998244353

def main(l, r):
    ma = 1
    temp = l
    while temp * 2 <= r:
        ma += 1
        temp = temp * 2
    ans = 0
    for i in range(l, r//(int)(pow(2,ma-1)) + 1):
        if ma >= 2 and i * pow(2, ma-2) * 3 <= r:
            ans += ma
        elif i * pow(2, ma-1) <= r:
            ans += 1
        ans = ans%MOD
    
    print(ma, ans%MOD)

caseNum = int(input())
for i in range(0, caseNum):
    l,r = li()
    main(l, r)
   
