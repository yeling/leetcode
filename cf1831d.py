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

#暴力
def solve2(n, a, b):
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]*a[j] == b[i] + b[j]:
                ans += 1
    print(ans)    
    return 
#TLE
def solve3(n, a, b):
    ans = 0
    cache = [(a[i],b[i]) for i in range(n)]
    cache.sort()
    # print(cache)
    for i in range(n):
        curr = cache[i][0]
        next = curr
        while curr * next <= 2*n:
            target = (next, curr * next - cache[i][1])
            l = bisect_left(cache, target, lo = i + 1)
            r = bisect_right(cache, target, lo = l)
            ans += r - l
            next += 1
        # print(cache[i], ans)
    print(ans)   
    return 

#MLE
def solve4(n, a, b):
    ans = 0
    cnt = defaultdict(int)
    for i in range(n):
        cnt[(a[i],b[i])] += 1
    # print(cache)
    allk = list(cnt.keys())
    allk.sort()
    # print(allk)
    for i in range(len(allk)):
        curr = allk[i][0]
        next = curr
        while curr * next <= 2*n:
            target = (next, curr * next - allk[i][1])
            if allk[i] == target:
                ans += (cnt[allk[i]] * (cnt[target] - 1))//2
            elif allk[i][0] != target[0] or target[1] > allk[i][1]:
                ans += cnt[allk[i]] * cnt[target]
            next += 1
            # print(allk[i], target, ans)
    print(ans)   
    return 

def solve(n, a, b):
    ans = 0
    cnt = Counter()
    for i in range(n):
        cnt[(a[i],b[i])] += 1
    # print(cache)
    allk = list(cnt.keys())
    allk.sort()
    # print(allk)
    for i in range(len(allk)):
        curr = allk[i][0]
        next = curr
        while curr * next <= 2*n:
            target = (next, curr * next - allk[i][1])
            if allk[i] == target:
                ans += (cnt[allk[i]] * (cnt[target] - 1))//2
            elif allk[i][0] != target[0] or target[1] > allk[i][1]:
                ans += cnt[allk[i]] * cnt[target]
            next += 1
            # print(allk[i], target, ans)
    print(ans)   
    return
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = li()
    b = li()
    # solve3(n, a, b)
    solve(n, a, b)
   
