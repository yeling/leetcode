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

def solve(n, nums):
    cache = [(v,i) for i,v in enumerate(nums)]
    cache.sort()
    pre = [0] * (n + 1)
    ans = [0] * n
    # print(cache)
    for i in range(n):
        pre[i + 1] = pre[i] + cache[i][0]
    l = 0
    r = 1
    while l < n:
        r = max(l + 1, r)
        while r < n and pre[r] >= cache[r][0]:
            r += 1
        ans[cache[l][1]] = max(l,r - 1)
        # print(l, r, ans[cache[l][1]])
        l += 1

    print(*ans)
        





    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
