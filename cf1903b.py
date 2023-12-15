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
    ans = [-1] * n
    if n == 1:
        print(YES)
        print(2)
        return 
    for i in range(n):
        curr = 2 ** 30 - 1
        for j in range(n):
            if i != j:
                curr &= grid[i][j]
        ans[i] = curr
    # print(ans)
    flag = True
    for i in range(n):
        curr = ans[i]
        for j in range(n):
            if i != j:
                if (ans[i] | ans[j]) == grid[i][j]:
                    
                    continue
                else:
                    
                    flag = False
                    break
    if flag:
        print(YES)
        print(*ans)
    else:
        print(NO)


    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(li())
    solve(n, grid)

   
