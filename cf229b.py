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
    #dijk + t区间合并
    #[left,right]
    z = []
    for v in t:
        # print(v)
        temp = []
        i = 0
        left = right = -1
        while i < len(v):
            if i == 0:
                left = right = last = v[0]
            elif v[i] == last + 1:
                right = v[i]
                last = v[i]
            else:
                temp.append((left, right))
                left = right = last = v[i]
            i += 1
        if left != -1:
            temp.append((left, right))
        z.append(temp)
    # print(z)
    def findNext(target, arr):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left)//2
            if target < arr[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        
        next = target
        if right >= 0 and target <= arr[right][1]:
            next =  arr[right][1] + 1
        # print(target, arr, right, next)
        return next

    
    # next = findNext(3, z[2])
    # print(next)

    dis = [INF]*(1 + n)
    dis[1] = 0
    vis = [False] * (1 + n)
    # stack = PriorityQueue()
    #(index,w)
    g = [list() for _ in range(1 + n)]
    for v in edges:
        #print(v)
        g[v[0]].append((v[1],v[2]))
        g[v[1]].append((v[0],v[2]))
    #(dis,index)
    start = 0
    start = findNext(start, z[0])
    dis[1] = start
    # print('start ' , start, g)
    stack = [(start,1)]
    while stack:
        curr = heappop(stack)
        if vis[curr[1]] == True:
            continue
        if dis[curr[1]] < curr[0]:
            continue
        if curr[1] == n:
            break
        vis[curr[1]] = True
        # print("dis " , curr, dis)
        for v in g[curr[1]]:
            if v[0] != curr[1] and vis[v[0]] == False:
                tempDis = dis[curr[1]] + v[1]
                if v[0] != n:
                    tempDis = findNext(tempDis, z[v[0] - 1])
                dis[v[0]] = min(dis[v[0]], tempDis)
                # print(dis[v[0]], next)
                heappush(stack, (dis[v[0]], v[0]))
                # stack.put((dis[v[0]], v[0]))
    if dis[n] == INF:
        print(-1)
    else:
        print(dis[n]) 
    return 


def solve(n, m, edges, t):
    #dijk + t区间合并
    #[left,right]
    # z = []
    # for v in t:
    #     # print(v)
    #     temp = []
    #     i = 0
    #     left = right = -1
    #     while i < len(v):
    #         if i == 0:
    #             left = right = last = v[0]
    #         elif v[i] == last + 1:
    #             right = v[i]
    #             last = v[i]
    #         else:
    #             temp.append((left, right))
    #             left = right = last = v[i]
    #         i += 1
    #     if left != -1:
    #         temp.append((left, right))
    #     z.append(temp)
    # print(z)
    # def findNext(target, arr):
    #     left = 0
    #     right = len(arr) - 1
    #     while left <= right:
    #         mid = left + (right - left)//2
    #         if target < arr[mid][0]:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
        
    #     next = target
    #     if right >= 0 and target <= arr[right][1]:
    #         next =  arr[right][1] + 1
    #     # print(target, arr, right, next)
    #     return next

    dis = [INF]*(1 + n)
    dis[1] = 0
    vis = [False] * (1 + n)
    #(index,w)
    g = [list() for _ in range(1 + n)]
    for v in edges:
        #print(v)
        g[v[0]].append((v[1],v[2]))
        g[v[1]].append((v[0],v[2]))
    #(dis,index)
    start = 0
    # start = findNext(start, z[0])
    dis[1] = start
    # print('start ' , start, g)
    stack = PriorityQueue()
    # stack.put((start,1))
    stack = [(start,1)]
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
        # print("dis " , curr, dis)
        for v in g[curr[1]]:
            if v[0] != curr[1] and vis[v[0]] == False:
                tempDis = dis[curr[1]] + v[1]
                dis[v[0]] = min(dis[v[0]], tempDis)
                # print(dis[v[0]], next)
                # stack.put((dis[v[0]], v[0]))
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
solve(n, m, edges, t)

   
