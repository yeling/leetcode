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

def solve(n, m, a, b):
    a = [1] + a
    a.sort()
    b.sort()
    # print(a, b)
    pos = -1
    for i,v in enumerate(a):
        pos = bisect_right(b, v, lo = pos + 1)
        # print(v, pos)
        if pos == n:
            print(n - i)
            return
        # print(pos)
    print(0)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    a = li()
    b = li()
    solve(n, m, a, b)

   
