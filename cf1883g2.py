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

#TLE 3
def solve2(n, m, a, b):
    # 排序后，分类讨论，数据结构
    a.sort()
    b.sort()
    # print(a, b)
    pos = -1
    vis = [False] * (n + 1)
    curr = 0
    last = 0
    for i,v in enumerate(a):
        pos = bisect_right(b, v, lo = pos + 1)
        vis[pos] = True
        last = pos
        # print(v, pos)
        if pos == n:
            curr = n - 1 - i
            break
        # print(pos)
    #后面是否有空位置
    suffix = [False] * (n + 2)
    #如果是刚好的n - 1个，最后一位是可以给被人用的
    if last == n - 2:
        suffix[n - 1] = True

    for i in range(pos, -1, -1):
        suffix[i] |= suffix[i + 1]
        if vis[i] == False:
            suffix[i] = True
    # print(vis, suffix)
    ans = 0
    for i in range(1, m + 1):
        pos = bisect_right(b, i)
        if suffix[pos] == True:
            ans += curr
        else:
            ans += curr + 1
        # print(i, ans)
    print(ans)
    return 

def solve(n, m, a, b):
    # 排序后，分类讨论，数据结构
    a.sort()
    b.sort()
    # print(a, b)
    pos = -1
    vis = [False] * (n + 1)
    curr = 0
    last = 0
    for i,v in enumerate(a):
        pos = bisect_right(b, v, lo = pos + 1)
        vis[pos] = True
        last = pos
        # print(v, pos)
        if pos == n:
            curr = n - 1 - i
            break
        # print(pos)
    #后面是否有空位置
    suffix = [False] * (n + 2)
    #如果是刚好的n - 1个，最后一位是可以给被人用的
    if last == n - 2:
        suffix[n - 1] = True

    for i in range(pos, -1, -1):
        suffix[i] |= suffix[i + 1]
        if vis[i] == False:
            suffix[i] = True
    # print(vis, suffix)
    ans = 0
    pre = 1
    i = 0
    while i < n and b[i] <= m:
        while i < n and b[i] == pre:
            i += 1
        cnt = 0
        if i < n:
            cnt = min(m + 1, b[i]) - pre
        else:
            cnt = min(m + 1, b[-1] + 1) - pre
        
        if suffix[i] == True:
            ans += cnt * curr
        else:
            ans += cnt * (curr + 1)
        # print(i, ans, cnt, curr)
        if i < n:
            pre = b[i]
        
    # print(suffix, vis, a, b)
    if m < b[0]:
        cnt = m
        if suffix[0] == True:
            ans += cnt * curr
        else:
            ans += cnt * (curr + 1)
    elif m >= b[n-1] + 1:
        cnt = m - b[n-1]
        ans += cnt * (curr + 1)

    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    a = li()
    b = li()
    solve(n, m, a, b)

   
