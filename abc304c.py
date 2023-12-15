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



def solve(n, d, nums):
    g = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(i+1, n):
            if (nums[i][0] - nums[j][0]) ** 2 + (nums[i][1] - nums[j][1]) ** 2 <= d * d:
                g[i + 1].append(j + 1)
                g[j + 1].append(i + 1)
    stack = []
    stack.append(1)
    vis = [False] * (n + 1)
    vis[1] = True
    # print(g)
    while len(stack) > 0:
        cnt = len(stack)
        for i in range(cnt):
            for v in g[stack[i]]:
                if vis[v] == False:
                    vis[v] = True
                    stack.append(v)
        stack = stack[cnt:]
    # print(vis)
    for i in range(1,n+1):
        if vis[i] == True:
            print(YES)
        else:
            print(NO)


n,d = li()
nums = []
for i in range(0, n):
    nums.append(li())

solve(n, d, nums)


