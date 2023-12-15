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



def solve(n, m, nums, grid):
    # print(n)
    score = [(v,i) for i,v in enumerate(nums)]
    score.sort(reverse=True)
    # print(score)
    cache = [i + 1 for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'o':
                cache[i] += nums[j]
    dst = max(cache)
    # print(cache)
    for i in range(n):
        cnt = 0
        if cache[i] < dst:
            temp = cache[i]
            for v,j in score:
                if grid[i][j] == 'x':
                    temp += v
                    cnt += 1
                if temp >= dst:
                    break
        print(cnt)
    

    return

n,m = li()
nums = li()
grid = []
for _ in range(n):
    grid.append(input())

solve(n, m, nums, grid)

