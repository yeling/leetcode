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
    # 9,100
    start = ['###.','###.','###.','....']
    end = ['....','.###','.###','.###']
    ans = []
    for i in range(0, n - 9 + 1):
        for j in range(0, m - 9 + 1):
            flag = True
            for ki in range(i, i + 4):
                for kj in range(j, j + 4):
                    if grid[ki][kj] == start[ki-i][kj-j]:
                        continue
                    else:
                        flag = False
                        break
            
            for ki in range(i + 5, i + 9):
                for kj in range(j + 5, j + 9):
                    if grid[ki][kj] == end[ki-i-5][kj-j-5]:
                        continue
                    else:
                        flag = False
                        break
            if flag:
                ans.append([i+1,j+1])
    ans.sort()    
    for v in ans:   
        print(*v)   

    return

n,m = li()
grid = []
for _ in range(n):
    grid.append(input())
solve(n, m, grid)

