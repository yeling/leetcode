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

def solve(p, a, b):
    def dis(x, y):
        return (x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1])
    a0 = dis(a, [0,0])
    b0 = dis(b, [0,0])
    pa = dis(p, a)
    pb = dis(p, b)
    ab = dis(a, b)
    if 4 * b0 < ab and 4 * pb < ab:
        ans = sqrt(max(b0, pb))
    elif 4 * a0 < ab and 4 * pa < ab:
        ans = sqrt(max(a0, pa))
    elif (4 * b0 < ab or 4 * a0 < ab) and (4 * pb < ab or 4 * pa < ab):
        ans = sqrt(ab)/2
    else:
        ans = sqrt(max(min(a0, b0), min(pa, pb)))

    print(ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    p = li()
    a = li()
    b = li()
    solve(p, a, b)


   
