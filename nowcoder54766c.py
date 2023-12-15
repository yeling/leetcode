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

def main(s):
    cache = set()
    ans = 0
    for v in s:
        if v not in cache:
            ans += 2
        else:
            ans += 1
        cache.add(v)
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    main(s)
   
