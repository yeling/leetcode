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

def solve(n, a, b):
    sa = []
    for i in range(n):
        heappush(sa, (-(a[i] + b[i]), i))

    for i in range(n):
        curr = heappop(sa)
        if curr[0] == 0:
            break
        if i%2 == 0:
            a[curr[1]] -= 1
            b[curr[1]] = 0
        else:
            a[curr[1]] = 0
            b[curr[1]] -= 1
        # print(a, b)
    ans = 0
    # print(a, b)
    for i in range(n):
        ans += a[i] - b[i]
    print(ans)


    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = li()
    b = li()
    solve(n, a, b)

   
