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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(n, k, grid, qs):
    g = [list() for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                g[i+1].append(j+1)
    #dij
    print(g)
    for s,t in qs:
        vis = [False]*(n + 1)
        dis = [INF] * (n + 1)
        stack = PriorityQueue()
        #(dis, pos)
        print('begin', s, t)
        s = s%n
        t = t%n
        if s == 0:
            s = n
        if t == 0:
            t = n
        
        stack.put((0,s))
        ans = -1
        while stack.empty() == False:
            curr = stack.get()
            print(curr, vis[curr[1]])
            if vis[curr[1]] == True:
                continue
            vis[curr[1]] = True
            for v in g[curr[1]]:
                print(v, t)
                if v == t:
                    ans = curr[0] + 1
                    break
                if v != curr[0] and vis[v] == False:
                    dis[v] = min(dis[v], curr[0] + 1)
                    stack.put((dis[v],v))
            
            if ans != -1:
                break
        print('ans' , s, t, ans)
    return 


n,k = li()
grid = []
for _ in range(n):
    grid.append(li())
    
q = int(input())
qs = []
for _ in range(q):
    qs.append(li())

main(n, k, grid, qs)
