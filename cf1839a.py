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


def solve(n, k):
    if k == 1:
        print(n)
        return
    ans = n//k + 1
    if n%k > 1:
        ans += 1

    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    solve(n, k)
   
