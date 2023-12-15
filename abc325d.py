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


# AC 5 WA 42
def solve2(n, grid):
    #(s,t)
    cache = [(t, t + d) for t,d in grid]
    cache.sort(key = lambda x: x[1])
    # print(cache)
    ans = 0
    last = 0
    stack = []
    for v in cache:
        heappush(stack, v)
    i = 0
    while i < n:
        curr = cache[i][1]
        if curr > last:
            cnt = curr - last
            while len(stack) > 0:
                top = heappop(stack)
                if top[1] < curr:
                    continue
                else:
                    heappush(stack, top)
                    break
            tc = 0
            while len(stack) > 0:
                top = heappop(stack)
                if top[1] >= curr and tc < cnt:
                    tc += 1
                    continue
                else:
                    heappush(stack, top)
                    break
            ans += tc
        last = curr
        i += 1

    print(ans)
    return

def solve(n, grid):
    #(t,s)
    cache = [(t + d, t) for t,d in grid]
    cache.sort()
    # print(cache)
    ans = 0
    last = 0
    stack = []
    # t, s
    for v in cache:
        heappush(stack, v)
    i = 0
    while i < n:
        curr = cache[i][0]
        while i < n and curr == last:
            curr = cache[i][0]
            i += 1
            
        if curr > last:
            cnt = curr - last
            while len(stack) > 0:
                top = heappop(stack)
                if top[0] < curr:
                    continue
                else:
                    heappush(stack, top)
                    break
            tc = 0
            while len(stack) > 0:
                top = heappop(stack)
                if top[0] >= curr and tc < cnt:
                    tc += 1
                    continue
                else:
                    heappush(stack, top)
                    break
            ans += tc
        last = curr
        # print(curr, stack)
        i += 1

    print(ans)
    return

caseNum = int(input())
grid = []
for i in range(0, caseNum):
    grid.append(li())

solve2(caseNum, grid)

