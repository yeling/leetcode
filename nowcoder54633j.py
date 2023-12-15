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

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(n, m, grid):
    #1,0开头的
    flag = True
    if grid[0][0] == 1:
        for i in range(n):
            for j in range(m):
                if (i + j)%2 == 0 and grid[i][j] == 1:
                    continue
                elif (i + j)%2 == 1 and grid[i][j] == 0:
                    continue
                else:
                    flag = False
                    break 
        if flag:
            print(0)
            return 
    #0,1
    ans = 0
    for i in range(n):
        for j in range(m):
            if (i + j)%2 == 0 and grid[i][j] == 1:
                ans += 1
            elif (i + j)%2 == 1 and grid[i][j] == 0:
                ans += 1
            # print(i, j, ans)
    print(ans)
    return 


n, m = li()
grid = []
for _ in range(n):
    grid.append([int(v) for v in input()])
main(n, m, grid)
   
