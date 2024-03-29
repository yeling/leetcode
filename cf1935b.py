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
    # print(n, nums)
    n = len(nums)
    m = 0
    cache = defaultdict(int)
    for v in nums:
        cache[v ^ INF] = 1
        while cache[m ^ INF] != 0:
            m += 1
    l = n - 1
    lm = 0
    cachel = defaultdict(int)
    for i,v in enumerate(nums):
        cachel[v ^ INF] = 1
        while cachel[lm ^ INF] != 0:
            lm += 1
        if lm == m:
            l = i
            break
    
    r = 0
    rm = 0
    cacher = defaultdict(int)
    for i in range(n-1, -1, -1):
        cacher[nums[i] ^ INF] = 1
        while cacher[rm ^ INF] != 0:
            rm += 1
        if rm == m:
            r = i
            break

    # print(nums, m, lm, rm, l, r)
    if r <= l:
        print(-1)
    else:
        print(2)
        print(1, l + 1)
        print(l + 2, n)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
