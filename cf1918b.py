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

def solve2(n, a, b):
    # print(n)
    ra = []
    rb = []
    la = []
    for i in range(n):
        if a[i] == b[i]:
            la.append(a[i])
        else:
            ra.append(a[i])
            rb.append(b[i])
    la.sort()
    ra += la
    rb += la
    print(*ra)
    print(*rb)
    return 

def solve(n, a, b):
    # print(n)
    pa = [(v,i) for i,v in enumerate(a)]
    pa.sort()
    ra = list(range(1,n + 1))
    rb = [b[v[1]] for v in pa]
    print(*ra)
    print(*rb)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = li()
    b = li()
    solve(n, a, b)

   
