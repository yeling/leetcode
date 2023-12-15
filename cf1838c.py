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

input = lambda: sys.stdin.readline().rstrip()
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve(n, m):
    grid = [[0]*m for _ in range(n)]
    if n == 4:
        curr = 1
        for j in range(m):
            for i in range(n):
                grid[i][j] = curr 
                curr += 1
    else:
        curr = 1
        for i in range(0,n,2):
            for j in range(m):
                grid[i][j] = curr 
                curr += 1
        for i in range(1,n,2):
            for j in range(m):
                grid[i][j] = curr 
                curr += 1
    for i in range(n):
        print(*grid[i])
    print()

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    solve(n, m)

   
