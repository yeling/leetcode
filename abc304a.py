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


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

# mi = lambda: map(int, sys.stdin.buffer.readline().split())
mi = lambda :map(int,input().split())
li = lambda :list(mi())


def solve(arr):
    yong = INF
    pos = -1

    for i,(n,s) in enumerate(arr):
        if n < yong:
            yong = n
            pos = i
    ans = arr[pos:] + arr[:pos]
    for n,s in ans:
        print(s)



caseNum = int(input())
arr = []
for i in range(0, caseNum):
    s, n = input().split()
    n = int(n)
    arr.append((n,s))
solve(arr)

