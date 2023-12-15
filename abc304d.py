# auther yeling
import sys
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from heapq import *
import string


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

# mi = lambda: map(int, sys.stdin.buffer.readline().split())
mi = lambda :map(int,input().split())
li = lambda :list(mi())


def solve2(w,h, nums, anums, bnums):
    cache = Counter()
    miv = INF
    mav = 0
    anums = [0] + anums + [w]
    bnums = [0] + bnums + [h]
    # print(anums, bnums)

    for p,q in nums:
        pi = bisect_left(anums, p)
        qi = bisect_right(bnums, q)
        cache[(pi,qi)] += 1
        #miv 可能一直是1，同一个key最后只计算了第一次，所以要最后求min
        miv = min(miv, cache[(pi,qi)])
        mav = max(mav, cache[(pi,qi)])
    
    if len(cache.keys()) < (len(anums) - 1) * (len(bnums) - 1):
        miv = 0

    print(miv, mav)

def solve(w,h, nums, anums, bnums):
    cache = Counter()
    mi = INF
    ma = 0
    anums = [0] + anums + [w]
    bnums = [0] + bnums + [h]
    # print(anums, bnums)

    for p,q in nums:
        pi = bisect_left(anums, p)
        qi = bisect_right(bnums, q)
        cache[(pi,qi)] += 1

    mi = min(cache.values())
    ma = max(cache.values())
    if len(cache.keys()) < (len(anums) - 1) * (len(bnums) - 1):
        mi = 0

    print(mi, ma)

# cache = Counter()
# mav = 0
# miv = INF
# for i in range(10):
#     cache[(i,i)] += i
#     miv = min(miv, cache[(i,i)])
#     mav = max(mav, cache[(i,i)])
# print(cache, miv, mav)

w,h = li()
n = int(input())
nums = []
for i in range(0, n):
    nums.append(li())

a = int(input())
anums = li()

b = int(input())
bnums = li()

solve(w,h, nums, anums, bnums)
# solve2(w,h, nums, anums, bnums)


