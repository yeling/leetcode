# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main2(n, m, a, b):
    stack = PriorityQueue()
    for v in a:
        stack.put(v)
    for i in range(m):
        curr = stack.get()
        stack.put(b[i])
    ans = 0
    while stack.empty() == False:
        ans += stack.get()
    print(ans)
    return 

def main(n, m, a, b):
    all = []
    for i in range(n):
        all.append(a[i])
    for i in range(m-1):
        all.append(b[i])
    all.sort(reverse=True)
    ans = b[m-1]
    for i in range(n-1):
        ans += all[i]
    print(ans)
    return 


caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    a = li()
    b = li()
    main(n, m, a, b)
   
