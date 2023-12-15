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
# li = lambda :list(mi())

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve(n, m, h, k, s, cache):
    curr = (0,0)
    ch = h 
    # print(cache)
    for v in s:
        # print(curr, ch)
        ch -= 1
        if v == 'R':
            curr = (curr[0] + 1, curr[1])
        elif v == 'L':
            curr = (curr[0] - 1, curr[1])
        elif v == 'U':
            curr = (curr[0], curr[1] + 1)
        elif v == 'D':
            curr = (curr[0], curr[1] - 1)
        
        if ch < 0:
            print(NO)
            return
        
        if curr in cache and ch < k:
            # print(cache)
            cache.remove(curr)
            # print(cache)
            ch = k
    
    print(YES)
    return



n,m,h,k = li()
s = input()

cache = set()
for _ in range(m):
    # temp = li()
    # print(temp)
    cache.add(tuple(li()))
solve(n, m, h, k, s, cache)


