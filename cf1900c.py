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

# --------------------
# 手写栈模板
# 克服py栈太浅的问题
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
# --------------------
#函数头加上@bootstrap
#函数内部return改成yield

def solve(n, s, grid):
    ans = n
    @bootstrap
    def dfs(root, pre):
        l,r = 0,0
        nonlocal ans
        if grid[root - 1][0] == 0 and grid[root - 1][1] == 0:
            ans = min(ans, pre)

        if grid[root - 1][0] != 0:
            if s[root - 1] != 'L':
                l = 1
            yield dfs(grid[root - 1][0], pre + l)
        if grid[root - 1][1] != 0:
            if s[root - 1] != 'R':
                r = 1
            yield dfs(grid[root - 1][1], pre + r)
        yield 
    dfs(1, 0)
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    grid = []
    for _ in range(n):
        grid.append(li())
    solve(n, s, grid)

   
