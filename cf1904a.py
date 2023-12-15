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

def solve(a,b, xk, yk, xq, yq):
    dirs = [[1,1], [1,-1],[-1,1],[-1,-1]]
    sk = set()
    sq = set()
    for d in dirs:
        sk.add((xk + d[0]*a, yk + d[1]*b))
        sk.add((xk + d[0]*b, yk + d[1]*a))
        sq.add((xq + d[0]*a, yq + d[1]*b))
        sq.add((xq + d[0]*b, yq + d[1]*a))
    ans = 0
    for v in sk:
        if v in sq:
            ans += 1
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    a,b = li()
    xk, yk = li()
    xq, yq = li()
    solve(a,b, xk, yk, xq, yq)

   
