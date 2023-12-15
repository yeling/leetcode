# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(n, m):
    if n < m:
        print(NO)
        return
    if n == m:
        print(YES)
        return
    vis = defaultdict(int)
    stack = set()
    stack.add(n)
    vis[n] = 1
    while len(stack) > 0:
        next = set()
        for v in stack:
            if v%3 == 0:
                if vis[v//3] == 0 and v//3 > m:
                    vis[v//3] = 1
                    next.add(v//3)
                if vis[(v//3) * 2] == 0 and (v//3) * 2 > m:
                    vis[(v//3) * 2] = 1
                    next.add((v//3) * 2)
                if v//3 == m or (v//3) * 2 == m:
                    print(YES)
                    return 

        stack = next
    print(NO)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    main(n, m)
   
