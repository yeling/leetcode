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

def main2(x, t):
    curr = x
    for _ in range(t + 1):
        curr = curr /sqrt(curr * curr + 1)
    print(curr)

    return 

def main3(x, t):
    curr = x /sqrt(x * x + 1)
    curr = curr * curr
    for _ in range(t):
        curr = curr /(curr + 1)
    print(sqrt(curr))

    return 

def main(x, t):
    curr = x /sqrt(x * x + 1)
    curr = curr * curr
    temp = sqrt(curr / (t*curr + 1))
    print(temp)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    x,t = li()
    # main2(x, t)
    main(x, t)
   
