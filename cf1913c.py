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
YES="YES"
NO="NO"


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

def solve(m, grid):
    cache = [0] * 32
    for t,v in grid:
        if t == 1:
            cache[v] += 1
        elif t == 2:
            temp = v
            tc = cache[:]
            i = 0
            flag = True
            while temp > 0:
                if temp%2 == 1:
                    if tc[i] > 0:
                        tc[i + 1] += (tc[i]-1)//2
                        i += 1
                    else:
                        flag = False
                        break
                else:
                    tc[i + 1] += tc[i]//2
                    i += 1
                temp = temp//2
            if flag:
                print(YES)
            else:
                print(NO)


    return 

m = int(input())
grid = []
for i in range(0, m):
    grid.append(li())

solve(m, grid)

   
