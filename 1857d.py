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
    ans = []
    ma = 0
    pos = -1
    for i,v in enumerate(a):
        if v > ma:
            ma = v
            pos = i
    flag = True
    for i in range(n):
        if ma - a[i] >= b[pos] - b[i]:
            if ma - a[i] == b[pos] - b[i]:
                ans.append(i + 1)
            continue
        else:
            flag = False
            break
    ans.sort()
    if flag:
        print(len(ans))
        print(*ans)
    else:
        print(0)
    return 

def solve(n, a, b):
    diff = -INF
    for i,j in zip(a,b):
        diff = max(diff, i - j)
    ans = []
    for k,(i,j) in enumerate(zip(a,b)):
        if diff == i - j:
            ans.append(k + 1)
    print(len(ans))
    print(*ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = li()
    b = li()
    solve(n, a, b)

   
