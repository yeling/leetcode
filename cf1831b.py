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

def solve(n, a, b):
    cacheA = defaultdict(int)
    cacheB = defaultdict(int)
    i = 0
    
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        cacheA[a[i]] = max(cacheA[a[i]],j - i)
        i = j
    i = 0
    while i < n:
        j = i
        while j < n and b[j] == b[i]:
            j += 1
        cacheB[b[i]] = max(cacheB[b[i]], j - i)
        i = j
    ans = 0
    # print(cacheA,cacheB)
   
    for k in cacheA:
        ans = max(ans, cacheA[k] + cacheB[k])
    
    for k in cacheB:
        ans = max(ans, cacheA[k] + cacheB[k])
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = li()
    b = li()
    solve(n, a, b)
   
