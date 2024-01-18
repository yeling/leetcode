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

def solve(n, grid):
    # print(n)
    l = 1
    r = 10 ** 9
    ans = 0
    for a,x in grid:
        if a == 1:
            l = max(l, x)
        elif a == 2:
            r = min(r, x)
    ans = r - l + 1
    if ans < 0:
        ans = 0
        print(ans)
        return
    
    cache = set()
    for a,x in grid:
        if a == 3 and l <= x <= r and x not in cache:
            ans -= 1
            cache.add(x)
    print(ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(li())
    solve(n, grid)

   
