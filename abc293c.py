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


def main(h, w, grid):
    # print(grid)
    global ans 
    ans = 0
    def dfs(x,y,path:set):
        global ans 
        if x == h - 1 and y == w - 1:
            ans += 1
            # print(path)
            return 
        if x + 1 < h and grid[x+1][y] not in path:
            path.add(grid[x+1][y])
            dfs(x + 1, y, path)
            path.remove(grid[x+1][y])
        if y + 1 < w and grid[x][y + 1] not in path:
            path.add(grid[x][y + 1])
            dfs(x, y + 1, path)
            path.remove(grid[x][y + 1])
        return 
    path = set()
    path.add(grid[0][0])
    dfs(0,0,path)
    print(ans)
    return 
    # print(n)


h,w = li()
grid = []
for i in range(h):
    grid.append(li())

main(h,w, grid)
