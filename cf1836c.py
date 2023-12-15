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
# if(path.exists('input.txt')):
#     sys.stdin = open("input.txt","r")
#     sys.stdout = open("output.txt","w")

# For fast I/O
# input = sys.stdin.buffer.readline
# input = sys.stdin.readline
# print = sys.stdout.write

# input = lambda: sys.stdin.readline().rstrip()
mi = lambda :map(int,input().split())
li = lambda :list(mi())

#Python3 TLE Py64 AC
def solve(a,b,c,k):
    av = [10 ** (a - 1), 10 ** a - 1]
    cv = [10**(c - 1), 10 ** c - 1]
    bv = [10**(b - 1), 10 ** b - 1]
    cnt = 0
    # if av[0] + bv[0] > cv[1]:
    #     print(-1)
    #     return
    # if (av[1] - av[0] + 1) * (bv[1] - bv[0] + 1) < k:
    #     print(-1)
    #     return
    # print(a,b,c,k)
    
    for i in range(av[0], av[1] + 1):
        maxb = min(bv[1], cv[1] - i)
        minb = max(bv[0], cv[0] - i)
        if minb > maxb:
            continue
        curr = maxb - minb + 1
        cnt += curr
        # print(cnt)
        if cnt >= k:
            print(i, "+", minb + (k - 1 - (cnt - curr)),"=", i + minb + (k - 1 - (cnt - curr)))
            return
    print(-1)

caseNum = int(input())
all = []
for i in range(0, caseNum):
    all.append(li())

for a,b,c,k in all:
    # solve2(a,b,c,k)
    solve(a,b,c,k)


   
