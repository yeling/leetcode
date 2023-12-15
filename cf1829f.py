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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main2(n, m, edges):
    grid = [[] for _ in range(n+1)]
    for u,v in edges:
        grid[u].append(v)
        grid[v].append(u)
    cache = defaultdict(int)
    for i,v in enumerate(grid):
        if i > 0:
            # print(i, v, len(v))
            cache[len(v)] += 1
    kind = []
    # print(cache)
    for k in cache:
        kind.append(cache[k])
    # print(kind)
    kind.sort()
    x = kind[1]
    y = max(kind)//x
    print(x, y)
    

    return 

def main(n, m, edges):
    grid = defaultdict(int)
    for u,v in edges:
        grid[u] += 1
        grid[v] += 1
    cache = defaultdict(int)
    for v in grid:
        cache[grid[v]] += 1
    kind = []
    # print(cache)
    x = 0
    for k in cache:
        if cache[k] == 1:
            x = k
        kind.append(cache[k])
    # print(kind)
    kind.sort()
    if x > 0:
        y = max(kind)//x
    else:
        y = kind[0] - 2
        x = max(kind)//y
    print(x, y)
    
    return 



caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    edges = []
    for _ in range(m):
        edges.append(li())
    main(n, m, edges)
   
