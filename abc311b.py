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

def solve(n, d, grid):
    # print(n)
    ans = 0
    last = -1
    for i in range(d):
        flag = True
        for j in range(n):
            if grid[j][i] == 'o':
                continue
            else:
                flag = False
                break
        if flag:
            if last == -1:
                last = i
            ans = max(ans, i - last + 1)
        else:
            last = -1
    print(ans)

    return


n,d = li()
grid = []
for _ in range(n):
    grid.append(input())
solve(n, d, grid)

