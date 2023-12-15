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

mi = lambda: map(int, sys.stdin.buffer.readline().split())
li = lambda :list(mi())


def solve(n, m, grid):
    cache = [ [0] * (n + 1) for _ in range(n+1)]
    for i in range(m):
        for j in range(1,n):
            cache[grid[i][j-1]][grid[i][j]] = 1
    ans = 0
    # print(cache)
    for i in range(1,n+1):
        for j in range(i + 1,n+1):
            if cache[i][j] == 0 and cache[j][i] == 0:
                ans += 1 
    print(ans)



n,m = li()
grid = []
for _ in range(m):
    grid.append(li())

solve(n, m, grid)

