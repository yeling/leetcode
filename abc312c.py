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

def solve2(n, m, a, b):
    # print(n)
    a.sort()
    b.sort()
    l = 0
    r = 0
    if a[0] > b[-1]:
        print(b[-1] + 1)
        return
    while l < n:
        while r < m and b[r] < a[l]:
            r += 1
        if l + 1 >= m - r:
            print(a[l])
            return
        l += 1
    return
# 33 WA 11
def solve(n, m, a, b):
    # print(n)
    a.sort()
    b.sort()
    l = 0
    r = 0
    ans = INF
    if a[0] > b[-1]:
        print(b[-1] + 1)
        return
    
    for i,v in enumerate(a):
        ai = bisect_left(b,v)
        if i + 1 >= m - ai:
            ans = v
            break

    for i,v in enumerate(b):
        ai = bisect_left(a,v)
        if ai + 1 >= m - i:
            ans = min(ans, v)
            break
    print(ans)


    return

n,m = li()
a = li()
b = li()
solve2(n, m, a, b)
solve(n, m, a, b)

