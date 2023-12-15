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

def main(n, m, ns, ms):
    cache = list(zip(ns,range(n)))
    cache.sort()
    mi = cache[0]
    ma = cache[-1]
    for a,b,c in ms:
        if (b - mi[0]) * (b - mi[0]) >= 4 * a * c:
            print('Yes')
            print(mi[1])
        elif (b - ma[0]) * (b - ma[0]) >= 4 * a * c:
            print('Yes')
            print(ma[1])
        else:
            print('No')
        
    # print(cache)
    return 

nums = [1,2,3,4]
pos = bisect(nums, -1) 
print(pos)

# caseNum = int(input())
# for i in range(0, caseNum):
#     n,m = li()
#     ns = []
#     for _ in range(n):
#         ns.append(int(input()))
#     ms = []
#     for _ in range(m):
#         ms.append(li())
#     main(n, m, ns, ms)

   
