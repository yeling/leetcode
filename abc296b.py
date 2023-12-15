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


def main(grid):
    for i in range(8):
        for j in range(8):
            if grid[i][j] == '*':
                ans = chr(97 + j) + str(7 - i + 1)
                print(ans)
                return 


# print(chr(97))

grid = []
for _ in range(8):
    grid.append(input())

main(grid)

