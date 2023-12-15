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

def solve(grid):
    col = [0] * (10)
    for i in range(9):
        col = [0] * (10)
        row = [0] * (10)
        for j in range(9):
            col[grid[i][j]] += 1
            row[grid[j][i]] += 1
        for ki in range(1,10):
            if col[ki] == 1:
                continue
            else:
                print(NO)
                return
        for ki in range(1,10):
            if row[ki] == 1:
                continue
            else:
                print(NO)
                return
    for i in range(3):
        for j in range(3):
            sub = [0] * (10)
            for ki in range(3):
                for kj in range(3):
                    sub[grid[i*3 + ki][j*3 + kj]] += 1
            for ki in range(1,10):
                if sub[ki] == 1:
                    continue
                else:
                    print(NO)
                    return
    print(YES)
    return

grid = []
for i in range(9):
    grid.append(li())
solve(grid)

