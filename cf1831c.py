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

def solve2(n, edges):
    depth = 0
    vis = [False]*(n + 1)
    vis[1] = True
    while len(edges) > 0:
        next = []
        depth += 1
        for u,v in edges:
            if vis[u] == True or vis[v] == True:
                vis[u] = True
                vis[v] = True
            else:
                next.append([u,v])
        edges = next
    print(depth)
         
    return 

#BFS变种
def solve(n, edges):
    depth = 0
    #(v,order)
    g = [set() for _ in range(n+1)]
    for i,(u,v) in enumerate(edges):
        g[u].add((v,i))
        g[v].add((u,i))
    stack = []
    stack.append((1,-1))
    vis = [False]*(n + 1)
    # print(g)
    while len(stack) > 0:
        curr = stack[:]
        depth += 1
        left = []
        while len(curr) > 0:
            # print(curr)
            next = []
            for v,vr in curr:
                vis[v] = True
                for u,ur in g[v]:
                    if vr < ur and u != v:
                        next.append((u,ur))
                    elif vr > ur:
                        left.append((u,ur))
            curr = next
        # print('left ',left)
        stack = left

    print(depth)
         
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    edges = []
    for _ in range(1,n):
        edges.append(li())
    solve(n, edges)
   
