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

def solve(n, k, a, b):
    pair = [[v,i] for i,v in enumerate(a)]
    pair.sort()
    b.sort()
    ans = [0]*n
    for i in range(n):
        ans[pair[i][1]] = b[i]
    print(*ans)

   

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n, k = li()
    a = li()
    b = li()
    solve(n, k, a, b)
   
