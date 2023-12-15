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
    for i in range(h):
        temp = ''
        for j in range(w):
            if grid[i][j] == 0:
                temp += '.'
            else:
                temp += chr(64 + grid[i][j])
        print(temp)

    return 


h,w = li()
grid = []
for i in range(h):
    grid.append(li())

main(h, w, grid)
