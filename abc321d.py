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



def solve(n, m, p, a, b):
    a.sort()
    b.sort()
    pre = [0] * (m + 1)
    for i,v in enumerate(b):
        pre[i + 1] = pre[i] + v
    ans = 0
    for i in range(n):
        pos = bisect_right(b, p - a[i])
        ans += (m - pos) * p + pre[pos] + pos*a[i]
    print(ans)
    return

n,m,p = li()
a = li()
b = li()
solve(n, m, p, a, b)

