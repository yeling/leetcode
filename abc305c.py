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

# input = lambda: sys.stdin.readline().rstrip()
mi = lambda :map(int,input().split())
li = lambda :list(mi())


def solve(h, w, grid):
    #(cnt,r)
    row = [0]*h
    col = [0]*w
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                row[i] += 1
                col[j] += 1
    
    rows = [(v,i) for i,v in enumerate(row)]
    rows.sort()
    x = -1
    y = -1
    for i in range(h):
        if rows[i][0] != 0:
            x = rows[i][1]
            break

    cols = [(v,i) for i,v in enumerate(col)]
    cols.sort()
    for i in range(w):
        if cols[i][0] != 0:
            y = cols[i][1]
            break
    print(x+1, y + 1)

    return


h,w = li()
grid = []
for i in range(h):
    grid.append(input())

solve(h, w, grid)

