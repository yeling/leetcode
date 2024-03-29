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
from os import path

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"


# for I/O for local system
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    # sys.stdout = open("output.txt","w")

# For fast I/O
# input = sys.stdin.buffer.readline
# input = sys.stdin.readline
# print = sys.stdout.write

input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve(n, m, x, grid):
    cache = [0] * n
    cache[x - 1] = 1
    for v in grid:
        t = v.split()
        r = int(t[0])
        next = [0] * n
        if t[1] == '0':
            for i in range(n):
                if cache[i] != 0:
                    next[(i + r)%(n)] = 1
            # clock
        elif t[1] == '1':
            for i in range(n):
                if cache[i] != 0:         
                    next[(i + n - (r%n))%(n)] = 1
        else:
            for i in range(n):
                if cache[i] != 0:
                    next[(i + r)%n] = 1
                    # print((i + n - (r%n))%n)
                    next[(i + n - (r%n))%(n)] = 1
        # print(v, cache, next)
        cache = next
        # print(1, cache)

    ans = []
    for i,v in enumerate(cache):
        if v > 0:
            ans.append(i + 1)
    print(len(ans))
    print(*ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m,x = li()
    grid = []
    for _ in range(m):
        grid.append(input())
    solve(n, m, x, grid)

   
