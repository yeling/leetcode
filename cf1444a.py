# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main2(p, q):
    if p%q != 0:
        print(p)
        return
    ma = int(sqrt(p)) + 1
    # print(p, q, ma)
    while ma >= 1:
        if p%ma == 0 and ma % q != 0:
            print(ma)
            return
        ma -= 1
    return 


def main(p, q):
    if p%q != 0:
        print(p)
        return
    i = 2
    # print(p, q, ma)
    ans = 0
    while i * i <= q:
        if q%i != 0:
            i += 1
            continue
        x = p
        while x%q == 0:
            x //= i
        ans = max(ans, x)
        while q%i == 0:
            q//=i
        i += 1
    if q > 1:
        while p % q == 0:
            p //= q
        if p > ans:
            ans = p
    print(ans)
    return

caseNum = int(input())
for i in range(0, caseNum):
    p,q = li()
    main(p, q)
   
