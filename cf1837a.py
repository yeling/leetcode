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

def solve(x, k):
    if x % k != 0:
        print(1)
        print(x)
    else:
        print(2)
        print(x - 1, 1)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    x,k = li()
    solve(x, k)
   
