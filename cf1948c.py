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

def solve(n, s1, s2):
    cache = [0] * 2
    s = [s1,s2]
    for i in range(2):
        cache[i] = [0] * n
        for j in range(n):
            cache[i][j] = [0,0]
    #0,1是否经过
    cache[0][0] = [1,0]
    stack = [(0,0)]
    step = 0
    dirs = [[1,0], [-1,0],[0,1],[0,-1]]
    while len(stack) > 0:
        next = []
        if step%2 == 0:
            for x,y in stack:
                for d in dirs:
                    dx = x + d[0]
                    dy = y + d[1]
                    if dx >= 0 and dx <= 1 and dy >= 0 and dy <= n - 1 and cache[dx][dy][(step + 1)%2] == 0:
                        next.append((dx,dy))
                        cache[dx][dy][(step + 1)%2] = 1
                    if dx == 1 and dy == n - 1:
                        print(YES)
                        return
        else:
            for x,y in stack:
                d = [0,0]
                if s[x][y] == '>':
                    d = [0,1]
                elif s[x][y] == '<':
                    d = [0, -1]
                dx = x + d[0]
                dy = y + d[1]
                if dx >= 0 and dx <= 1 and dy >= 0 and dy <= n - 1 and cache[dx][dy] == [0,0]:
                    next.append((dx,dy))
                    cache[dx][dy][(step + 1)%2] = 1
                if dx == 1 and dy == n - 1:
                    print(YES)
                    return
        stack = next
        step += 1
        # print(stack)
    print(NO)


    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s1 = input()
    s2 = input()
    solve(n, s1, s2)

   
