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

def solve(n, m, grid):
    # U D L R
    # print(n, m, grid)
    row = [defaultdict(int) for _ in range(n)]
    col = [defaultdict(int) for _ in range(m)]
    for i in range(n):
        for j in range(m):
            row[i][grid[i][j]] += 1
            col[j][grid[i][j]] += 1
    for i in range(n):
        if row[i]['R'] == row[i]['L'] and (row[i]['U'] + row[i]['D'])%2 == 0:
            continue
        else:
            print(-1)
            return
    for j in range(m):
        if col[j]['U'] == col[j]['D'] and (col[j]['R'] + col[j]['L'])%2 == 0:
            continue
        else:
            print(-1)
            return
    # print(row, col)
    ans = [['.'] * m for _ in range(n)]
    # l r u p flag
    flag = False
    for i in range(n):
        flag = not flag
        for j in range(m):
            if grid[i][j] == 'L' or grid[i][j] == 'R':
                if flag:
                    if j%2 == 0:
                        ans[i][j] = 'W'
                    else:
                        ans[i][j] = 'B'
                else:
                    if j%2 == 0:
                        ans[i][j] = 'B'
                    else:
                        ans[i][j] = 'W'
            elif grid[i][j] == 'U' or grid[i][j] == 'D':
                if flag:
                    if j%2 == 0:
                        ans[i][j] = 'W'
                    else:
                        ans[i][j] = 'B'
                else:
                    if j%2 == 0:
                        ans[i][j] = 'B'
                    else:
                        ans[i][j] = 'W'
                              
    for i in range(n):
        print(''.join(ans[i]))
            




    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    grid = []
    for _ in range(n):
        grid.append(input())
    solve(n, m, grid)


   
