# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(n, m, a, b, q, qs):
    grid = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            grid[i][j] = a[i]*b[j]
    pre = [[0]*(m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            pre[i + 1][j + 1] = grid[i][j] + pre[i + 1][j] + pre[i][j + 1] - pre[i][j]
 

    # print(pre)
    for x1,y1,x2,y2 in qs:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        # print(x1, y1, x2, y2)
        ans = pre[x2 + 1][y2 + 1] - pre[x1][y2 + 1] - pre[x2 + 1][y1] + pre[x1][y1]
        print(ans)

    

    # print(n)



n,m = li()
a = li()
b = li()
q = int(input())
qs = []
for _ in range(q):
    qs.append(li())
main(n, m, a, b, q, qs)

