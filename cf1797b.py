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

def main(n, k, grid):
    ans = 0
    # print(n, k)
    for i in range((n + 1)//2):
        lenj = n
        if n%2 == 1 and i == (n//2):
            lenj = (n + 1)//2
        for j in range(lenj):
            # print(i, j, grid[i][j])
            if grid[i][j] != grid[n-1-i][n-1-j]:
                ans += 1
    # print(ans, k)
    if ans > k:
        print('No')
    elif ans <= k:
        if n%2 == 1:
            print('Yes')
        elif n%2 == 0 and (k - ans)%2 == 0:
            print('Yes')
        else:
            print('No')
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    grid = []
    for _ in range(n):
        grid.append(li())
    main(n, k, grid)
   
