# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def solve(n, m, nums):
    #BFS 1开始寻找M
    vis = [False] * n
    cache = [[] for _ in range(m+1)]
    for i,v in enumerate(nums):
        for j in v:
            cache[j].append(i)
    # print(cache)
    # print(nums)
    stack = set()
    depth = 0
    for v in cache[1]:
        stack.add(v)
        vis[v] = True
        if m in nums[v]:
            print(depth)
            return
    while len(stack) > 0:
        # print(stack)
        next = set()
        for curr in stack:
            # print('stack ' , curr, nums[curr])
            for v in nums[curr]:
                # print(v, m, cache[v])
                for k in cache[v]:
                    if vis[k] == False:
                        next.add(k)
                        vis[k] = True
                if v == m:
                    # print('find')
                    print(depth)
                    return
        stack = next
        depth += 1
    print(-1)
    return


n,m = li()
nums = []
for _ in range(n):
    a = int(input())
    nums.append(li())

solve(n, m, nums)


