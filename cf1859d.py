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
# from sortedcontainers import SortedList


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

# input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve(n, nums, q, qs):
    # print(n)
    cache = []
    for l,r,a,b in nums:
        cache.append([l,b])
    #合并
    cache.sort()
    l,r = cache[0]
    last = []
    for i,(a,b) in enumerate(cache):
        if r >= a:
            r = b
            continue
        else:
            last.append([l,r])
            l = a
            r = b
    last.append([l,r])
    # print(last)
    ans = []
    for q in qs:
        i = bisect_right(last, q, key=lambda e:e[1])
        if i < len(last) and last[i][0] <= q:
            ans.append(last[i][1])
        else:
            ans.append(q)
    print(*ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(li())
    q = int(input())
    qs = li()
    solve(n, nums, q, qs)

        

   
