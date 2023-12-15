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

def Exp(a, n, mod):
    ans = 1
    while n != 0:
        if n & 1 != 0:
            ans = ans * a %mod
        a = a * a % mod
        n >>= 1
    return ans

def Inv(a, p):
    return Exp(a, p-2, p)

def main(n):
    # ans = (n * (n+1) * (2 *n+1)/3)%MOD + MOD - (n * ( n + 1) / 2)%MOD
    ans = (n * (n+1) * (2 *n+1) * Inv(3, MOD))%MOD + MOD - (n * ( n + 1) * Inv(2,MOD))%MOD
    ans = (ans * 2022)%MOD 
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n )
   
