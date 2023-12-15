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

# mi = lambda :map(int,input().split())
mi = lambda: map(int, sys.stdin.buffer.readline().split())
li = lambda :list(mi())

def solve2(n, m, edges, t):
    dis = [INF]*(1 + n)
    dis[1] = 0
    vis = [False] * (1 + n)
    #(index,w)
    g = [list() for _ in range(1 + n)]
    for v in edges:
        #print(v)
        g[v[0]].append((v[1],v[2]))
        g[v[1]].append((v[0],v[2]))
    
    stack = PriorityQueue()
    stack.put((0,1))
    # stack = [(0,1)]
    while not stack.empty():
        curr = stack.get()
        # curr = heappop(stack)

        if vis[curr[1]] == True:
            continue
        if dis[curr[1]] < curr[0]:
            continue
        if curr[1] == n:
            break
        vis[curr[1]] = True
        # next = findNext(curr[0],z[curr[1]-1])
        next = curr[0]
        pos = bisect_left(t[curr[1]-1], next)
        while pos != len(t[curr[1]-1]) and t[curr[1]-1][pos] == next:
            next += 1
            pos = bisect_left(t[curr[1]-1], next)
            
        dis[curr[1]] = next
        for v in g[curr[1]]:
            if v[0] != curr[1] and vis[v[0]] == False:
                dis[v[0]] = min(dis[v[0]], dis[curr[1]] + v[1])
                # heappush(stack, (dis[v[0]], v[0]))
                stack.put((dis[v[0]], v[0]))
    if dis[n] == INF:
        print(-1)
    else:
        print(dis[n]) 
    return 

def solve(n, m, edges, t):
    dis = [INF]*(1 + n)
    dis[1] = 0
    vis = [False] * (1 + n)
    #(index,w)
    g = [list() for _ in range(1 + n)]
    for v in edges:
        #print(v)
        g[v[0]].append((v[1],v[2]))
        g[v[1]].append((v[0],v[2]))
    
    # stack = PriorityQueue()
    # stack.put((start,1))
    stack = [(0,1)]
    while stack:
        curr = heappop(stack)
        if vis[curr[1]] == True:
            continue
        if dis[curr[1]] < curr[0]:
            continue
        if curr[1] == n:
            break
        vis[curr[1]] = True
        # next = findNext(curr[0],z[curr[1]-1])
        next = curr[0]
        pos = bisect_left(t[curr[1]-1], next)
        while pos != len(t[curr[1]-1]) and t[curr[1]-1][pos] == next:
            next += 1
            pos = bisect_left(t[curr[1]-1], next)

        dis[curr[1]] = next
        for v in g[curr[1]]:
            if v[0] != curr[1] and vis[v[0]] == False:
                dis[v[0]] = min(dis[v[0]], dis[curr[1]] + v[1])
                heappush(stack, (dis[v[0]], v[0]))
    if dis[n] == INF:
        print(-1)
    else:
        print(dis[n]) 
    return 

    
n,m = li()
edges = []
for _ in range(m):
    edges.append(li())
t = []
for _ in range(n):
    t.append(li()[1:])
# solve(n, m, edges, t)
solve2(n, m, edges, t)

   
