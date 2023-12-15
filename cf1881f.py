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

def solve2(n, k, ks, grid):
    # print(grid)
    marked = [0] * (n + 1)
    for v in ks:
        marked[v] = 1
    g = [[] for _ in range(n + 1)]
    for u,v in grid:
        g[u].append(v)
        g[v].append(u)
    depth = [0]*(n + 1)
    def dfs1(root, father):
        nonlocal depth, marked
        for v in g[root]:
            if v != father:
                dfs1(v, root)
                if depth[v] > 0:
                    depth[root] = max(depth[root], depth[v] + 1)
                elif marked[v] == 1:
                    depth[root] = max(depth[root], 1)
                
    
    dfs1(1, 0)
    # print(depth)
    f = depth[:]
    def dfs2(root, father):
        nonlocal depth, marked
        for v in g[root]:
            if v != father:
                f[v] = max(f[v], f[root] + 1)
                dfs2(v, root)
    dfs2(1, 0)
    print(depth, f)
    print(min(f[1:]))
    return 

def solve(n, k, ks, grid):
    # print(grid)
    marked = [0] * (n + 1)
    for v in ks:
        marked[v] = 1
    g = [[] for _ in range(n + 1)]
    for u,v in grid:
        g[u].append(v)
        g[v].append(u)
    depth = [0]*(n + 1)
    def dfs1(root, father):
        nonlocal depth, marked
        for v in g[root]:
            if v != father:
                dfs1(v, root)
                if depth[v] > 0:
                    depth[root] = max(depth[root], depth[v] + 1)
                elif marked[v] == 1:
                    depth[root] = max(depth[root], 1)
                
    
    dfs1(1, 0)
    # print(depth)
    f = depth[:]
    def dfs2(root, father):
        nonlocal depth, marked
        for v in g[root]:
            if v != father:
                f[v] = max(f[v], f[root] + 1)
                dfs2(v, root)
    dfs2(1, 0)
    print(depth, f)
    print(min(f[1:]))

    

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    ks = li()
    grid = []
    for _ in range(n - 1):
        grid.append(li())
    solve(n, k, ks, grid)



   
