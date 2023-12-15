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

def solve(n, s):
    cache = set()
    for i in range(1,n):
        cache.add(s[i-1:i+1])
        if i < n - 1:
            cache.add(s[i:i+2])
    print(len(cache))
        
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    solve(n, s)
   
