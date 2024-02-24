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

def solve(n, q, nums, grid):
    # print(n, q)
    pre = [0] * (n + 1)
    pone = [0] * (n + 1)
    for i,v in enumerate(nums):
        pre[i + 1] = pre[i] + v
        pone[i + 1] = pone[i]
        if v == 1:
            pone[i + 1] += 1

    for l,r in grid:
        if l == r:
            print(NO)
        else:
            l -= 1
            r -= 1
            t = r - l + 1 - (pone[r + 1] - pone[l])
            more = pre[r + 1] - pre[l] - ((pone[r + 1] - pone[l])) - 2 * t
            if t + more >= pone[r + 1] - pone[l]:
                print(YES)
            else:
                print(NO)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,q= li()
    nums = li()
    grid = []
    for _ in range(q):
        grid.append(li())
    solve(n, q, nums, grid)

   
