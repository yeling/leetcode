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

def main2(n, s1, s2, nums):
    ans = INF
    for i in range(n+1):
        temp = max(s1*i, (n -i) * s2)
        ans = min(ans, temp)
    a = []
    b = []
    for i in range(1,n + 1):
        if i <= ans:
            a.append(i)
        else:
            b.append(i)
    print(len(a), *a)
    print(len(b), *b)
    return 

def main(n, s1, s2, nums):
    ans = INF
    for i in range(n+1):
        temp = max(s1*i, (n -i) * s2)
        ans = min(ans, temp)
    a = []
    b = []
    for i in range(1,n + 1):
        if i <= ans:
            a.append(i)
        else:
            b.append(i)
    print(len(a), *a)
    print(len(b), *b)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n, s1, s2 = li()
    nums = li()
    main(n, s1, s2, nums)
   
