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


def main(n, m, ops):
    # R = 0 B = 1
    cache = [[0]*2 for _ in range(n+1)]
    # print(cache) 
    for a,b,c,d in ops:
        a = int(a)
        c = int(c)
        # print(a,b,c,d)
        if b == 'R':
            cache[a][0] = c
        else:
            cache[a][1] = c
        if d == 'R':
            cache[c][0] = a
        else:
            cache[c][1] = a
    x = 0 #cycle
    y = 0 #other
    vis = [False] * (n + 1)
    # print(cache)
    for i in range(1,n+1):
        if vis[i] == True:
            continue
        vis[i] = True
        temp = cache[i]
        # R == B
        # if temp[0] == temp[1] and temp[1] != 0:
        #     x += 1
        #     vis[i] = True
        #     vis[temp[0]] = True
        #     continue
        path = set()
        path.add(i)
        isCycle = False
        # R
        parent = i
        curr = temp[0]
        # print(i, curr)
        while curr != 0:
            vis[curr] = True
            if curr in path:
                # print('R')
                isCycle = True
                break
            path.add(curr)
            if cache[curr][0] == parent:
                parent = curr
                curr = cache[curr][1]
            elif cache[curr][1] == parent:
                parent = curr
                curr = cache[curr][0]
        
        # B
        parent = i
        curr = temp[1]
        while curr != 0:
            vis[curr] = True
            if curr in path:
                isCycle = True
                # print('B')
                break
            path.add(curr)
            # print(path, curr, cache[curr])
            if cache[curr][0] == parent:
                parent = curr
                curr = cache[curr][1]
            elif cache[curr][1] == parent:
                parent = curr
                curr = cache[curr][0]
            # print(curr)
        
        if isCycle:
            x += 1
        else:
            y += 1
        # print(i, vis, path, isCycle)
    print(x, y) 
    return 


n,m = li()
ops = []
for i in range(m):
    ops.append(input().split())

main(n,m,ops)

