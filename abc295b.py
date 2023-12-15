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


def main(r, c, grid):
    for i in range(r):
        for j in range(c):
            if grid[i][j] != '.' and grid[i][j] != '#':
                dis = int(grid[i][j])
                for ri in range(-dis, dis + 1):
                    for ci in range(-dis, dis + 1):
                        if ri + i >= 0 and ri + i <= r - 1 and  ci + j >= 0 \
                            and ci + j <= c - 1 and abs(ri) + abs(ci) <= dis \
                            and grid[i + ri][j + ci] == '#':
                            grid[i + ri][j + ci] = '.'
                grid[i][j] = '.'
    for v in grid:
        print(''.join(v))
    return


r,c = li()
grid = []
for _ in range(r):
    s = input()
    grid.append([i for i in s])

main(r, c, grid)

