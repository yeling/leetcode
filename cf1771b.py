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

def main(n,m,ps):
    
    pair = [set() for _ in range(n)]
    for p in ps:
        pair[p[0] - 1].add(p[1] - 1)
        pair[p[1] - 1].add(p[0] - 1)
    
    ans = n
    left = 0
    right = 1
    cache = defaultdict(int)
    for v in pair[0]:
        cache[v] = 1

    while left < n:
        if right < n and cache[right] == 0:
            ans += 1
            for v in pair[right]:
                cache[v] += 1
            right += 1
        else:
            for v in pair[left]:
                cache[v] -= 1
            left += 1
            if left == right and left < n:
                for v in pair[left]:
                    cache[v] += 1
                right += 1
        # print(left , cache, ans)
    print(ans) 

def main2(n,m,ps):
    pair = [set() for _ in range(n)]
    for p in ps:
        pair[p[0] - 1].add(p[1] - 1)
        pair[p[1] - 1].add(p[0] - 1)
    ans = 0
    cache = set()
    for i in range(n):
        cache.clear()
        for j in range(i,n):
            if j not in cache:
                ans += 1
                for v in pair[j]:
                    cache.add(v)
            else:
                break
    print(ans) 
    
# n = 4
# m = 2
# pair = [[1,2], [2,3]]
# main(n,m,pair)

caseNum = int(input())
for i in range(0, caseNum):
    n,m  = li()
    ps = []
    for i in range(m):
        p = li()
        ps.append(p)
    main(n,m,ps)
        




   
