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

def solve(n):
    ans = list(range(1,n+1))
    ans[0] += n - sum(ans)%n
    print(*ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    solve(n)
   
