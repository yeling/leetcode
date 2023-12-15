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

# 95%
def solve(m, n, grid):
    vis = [[False] * n for _ in range(m)]
    dirs = [[1,0], [-1,0],[0,1],[0,-1]]
    # print(m)
    vis[0][0] = True
    grid[0][0] = 1
    stack = []
    stack.append([0,0])
    while len(stack) > 0:
        cnt = len(stack)
        for i in range(cnt):
            v = stack[i]
            for dir in dirs:
                dx = v[0] + dir[0]
                dy = v[1] + dir[1]
                if dx >= 0 and dx < m and dy >= 0 and dy < n:
                    if vis[dx][dy] == False and grid[dx][dy] == 0:
                        vis[dx][dy] = True
                        grid[dx][dy] = 1
                        stack.append([dx,dy])

        stack = stack[cnt:]
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2 or grid[i][j] == 0:
                ans += 1
    print(ans)
    return 

# 95% 行列无关
def solve2(m, n, grid):
    dirs = [[1,0], [-1,0],[0,1],[0,-1]]
    # print(m)
    grid[0][0] = 1
    def dfs(x,y):
        for dir in dirs:
            dx = x + dir[0]
            dy = y + dir[1]
            if dx >= 0 and dx < m and dy >= 0 and dy < n:
                if grid[dx][dy] == 0:
                    grid[dx][dy] = 1
                    dfs(dx, dy)
        return
    dfs(0, 0)
    # for g in grid:
    #     print(g)
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2 or grid[i][j] == 0:
                ans += 1
    print(ans)
    return 

m,n = li()
grid = []
for _ in range(n):
    grid.append(li())

solve2(m, n, grid)

   
