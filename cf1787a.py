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

def main(n):
    if n%2 == 0:
        print(1, n//2)
    else:
        print(-1)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
