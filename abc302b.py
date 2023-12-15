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


def solve(h, w, arr):
    dirs = [[1,0], [-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    dst = "snuke"
    for i in range(h):
        for j in range(w):
            if arr[i][j] == dst[0]:
                for d in dirs:
                    curr = [[i,j]]
                    flag = True
                    for k in range(1,5):
                        dx = d[0]*k + i
                        dy = d[1]*k + j
                        # print(dx, dy, dst[k] )
                        if dx >= 0 and dx < h and dy >= 0 and dy < w and arr[dx][dy] == dst[k]:
                            curr.append([dx,dy])
                            continue
                        else:
                            flag = False
                            break
                    # print(curr)
                    if flag == True:
                        for v in curr:
                            print(v[0] + 1, v[1] + 1)
                        return





    return 



h,w = li()
arr = []
for _ in range(h):
    arr.append(input())

solve(h, w, arr)

