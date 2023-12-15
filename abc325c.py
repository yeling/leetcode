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

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


def solve(h, w, grid):
    dirs = [[1,0], [-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    # print(h)
    vis = [[False] * w for _ in range(h)]
    @bootstrap
    def dfs(x, y):
        vis[x][y] = True
        for d in dirs:
            dx = d[0] + x
            dy = d[1] + y
            if dx >= 0 and dx < h and dy >= 0 and dy < w:
                if grid[dx][dy] == "#" and vis[dx][dy] == False:
                    yield dfs(dx, dy)
        yield
    ans = 0
    for i in range(h):
        for j in range(w):
            if vis[i][j] == False and grid[i][j] == "#":
                # print(i, j, ans)
                ans += 1
                dfs(i, j)
    print(ans)
    return

h,w = li()
grid = []
for _ in range(h):
    grid.append(input())

solve(h, w, grid)

