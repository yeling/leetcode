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

def solve2(n, m, k, a, b):
    ans = -1
    a.sort()
    b.sort()
    if k >= 1:
        if a[0] < b[-1]:
            ans = sum(a) - a[0] + b[-1]
            a[0],b[-1] = b[-1],a[0] 
        else:
            ans = sum(a)
    if k >= 2 and k % 2 == 0:
        if b[0] < a[-1]:
            ans = sum(a) - a[-1] + b[0]
            b[0],a[-1] = a[-1],b[0] 
        else:
            ans = ans

    if k >= 3 and k%2 == 1:
        if a[0] < b[-1]:
            ans = sum(a) - a[0] + b[-1]
            a[0],b[-1] = b[-1],a[0] 
        else:
            ans = sum(a)
    print(ans)
    return 
# AC 还是需要构造独特的数据结构
def solve(n, m, k, a, b):
    ans = -1
    a.sort()
    b.sort()
    for i in range(0, k%2 + 10):
        a.sort()
        b.sort()
        if (i + 1)%2 == 1 and a[0] < b[-1]:
            a[0],b[-1] = b[-1],a[0] 
        elif (i + 1)%2 == 0 and b[0] < a[-1]:
            b[0],a[-1] = a[-1],b[0] 
    print(sum(a))

    return
caseNum = int(input())
for i in range(0, caseNum):
    n,m, k = li()
    a = li()
    b = li()
    solve(n, m, k, a, b)

   
