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

#MLE
def solve(n, grid):
    # print(grid)
    cnt = 1
    ops = defaultdict(deque)
    for i in range(n):
        if grid[i][0] == 1:
            cnt += 1
        elif grid[i][0] == 2:
            ops[grid[i][1]].append([grid[i][2], cnt])
    # print(ops)
    
    ans = [0] * (cnt + 1)
    g = [[] for _ in range(cnt + 1)]
    cnt = 1
    for i in range(n):
        if grid[i][0] == 1:
            cnt += 1
            g[grid[i][1]].append(cnt)
        elif grid[i][0] == 2:
            ans[grid[i][1]] += grid[i][2]
        
    # print(father)
    def dfs(root):
        # print(root, ops[root], ans)
        for v in g[root]:
            for q in ops[root]:
                if q[1] >= v:
                    ans[v] += q[0]
                    if q[1] > v:
                        ops[v].append([q[0], q[1]])
            dfs(v)
        return
    dfs(1)
    print(*ans[1:])
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(li())
    solve(n, grid)

   
