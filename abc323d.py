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
input = sys.stdin.buffer.readline
input = sys.stdin.readline
print = sys.stdout.write

input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve(n, grid):
    # print(n)
    cache = defaultdict(int)
    for s,c in grid:
        cache[s] += c
    
    ks = list(cache.keys())
    ks.sort()
    stack = deque(ks)
    # print(cache, stack)
    while len(stack) > 0:
        k = stack.popleft()
        if cache[k] >= 2:
            stack.append( k * 2)
            cache[k * 2] += cache[k]//2
            cache[k] = cache[k]%2
            if cache[k] == 0:
                del cache[k]
        elif cache[k] == 0:
            del cache[k]

        # print(k, cache)
    print(str(len(cache)) + "\n")
    return


n = int(input())
grid = []
for _ in range(n):
    grid.append(li())

solve(n, grid)

