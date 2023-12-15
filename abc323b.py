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



def solve(n, grid):
    # print(n)
    cache = [(-v.count('o'), i) for i,v in enumerate(grid)]
    cache.sort()
    # print(cache)
    ans = [v[1] + 1 for v in cache]
    print(*ans)

    return


n = int(input())
grid = []
for _ in range(n):
    grid.append(input())
solve(n, grid)

