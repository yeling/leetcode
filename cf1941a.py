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

def solve(n, m, k, bn, cn):
    ans = 0
    for v1 in bn:
        for v2 in cn:
            if v1 + v2 <= k:
                ans += 1
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m,k = li()
    bn = li()
    cn = li()
    solve(n, m, k, bn, cn)

   
