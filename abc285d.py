# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(n, grid):
    g = [-1] * n
    print(grid)
    cache = defaultdict(int)
    for i in range(n):
        cache[grid[i][0]] = i + 1
    
    vis = [False]*n
    for i in range(n):
        if vis[i] == True:
            continue
        t = grid[i][1]
        print(t)
        while cache[t] != 0:
            if vis[cache[t] - 1] == True:
                print(NO)
                return
            else:
                t = grid[cache[t] - 1]
        vis[i] = True
    print(YES)
    return


caseNum = int(input())
grid = []
for i in range(0, caseNum):
    grid.append((input()).split(' '))
main(caseNum, grid)

