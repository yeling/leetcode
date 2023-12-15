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

def solve(n, m):
    if m == 1:
        print(0)
    else:
        if n < m:
            print(n + 1)
        else:
            print(m)
    offset = min(n, m - 1)
    start = list(range(0,m)) + list(range(0,m))
    for i in range(offset):
        print(*start[i: i + m])
    for i in range(offset, n):
        print(*start[0: m])



    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    solve(n, m)

   
