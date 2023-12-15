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

# --------------------
# 手写栈模板
# 克服py栈太浅的问题
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
                    if not stack:break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
# --------------------
#函数头加上@bootstrap
#函数内部return改成yield



def solve(n, m, grid):
    dirs = [[1,0], [-1,0],[0,1],[0,-1]]
    global vis
    # 0,1,2,3
    vis = [[0] * m for _ in range(n)]
    @bootstrap
    def dfs(x,y,dir, index):
        # print(x, y, dir)
        global vis
        vis[x][y] |= (1 << (index))
        dx = x + dir[0]
        dy = y + dir[1]
        if dx >= 0 and dx < n and dy >= 0 and dy < m:
            if vis[dx][dy] & (1 << index) == 0:
                if grid[dx][dy] == '.':
                    yield dfs(dx, dy, dir, index)
                else:
                    for i,v in enumerate(dirs):
                        if vis[x][y] & (1<<i) == 0:
                            yield dfs(x, y, v, i)
        yield

    dfs(1,1, [0,1], 2)
    dfs(1,1, [1,0], 0)
    ans = 0
    for i in range(n):
        for j in range(m):
            if vis[i][j] != 0:
                ans += 1
    print(ans)

    
    return

n, m = li()
grid = []
for _ in range(n):
    grid.append(input())
solve(n, m, grid)

