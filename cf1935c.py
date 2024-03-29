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

def solve2(n, l, grid):
    # print(n, l, grid)
    grid.sort(key=lambda x: x[1])
    ans = 0
    for i in range(n):
        ct = 0
        maxB = 0
        minB = INF
        for j in range(i,n):
            ct += grid[j][0]
            maxB = max(maxB, grid[j][1])
            minB = min(minB, grid[j][1])
            if ct + maxB - minB <= l:
                ans = max(ans, j - i + 1)

    print(ans)
    return 

def solve(n, l, grid):
    # print(n, l, grid)
    ans = 0
    cache = [0] * n
    for i in range(n):
        currSum = grid[i][0]
        if currSum > l:
            continue 

        cache = [0] * n
        cache[i] = 1
        last = i
        ct = 1
        while True:
            curr = INF
            currPos = -1
            for j in range(n):
                if cache[j] == 1:
                    continue
                t = grid[j][0] + abs(grid[j][1] - grid[last][1])
                if t <= curr:
                    curr = t
                    currPos = j
            if curr == INF or currSum + curr > l:
                break
            else:
                last = currPos
                cache[currPos] = 1
                currSum += curr
                ct += 1
            # print(i, currPos, currSum)
        ans = max(ans, ct)



    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,l = li()
    grid = []
    for _ in range(n):
        grid.append(tuple(li()))
    solve(n, l, grid)

   
