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


def solve2(n, s):
    curr = 0
    cache = set()
    cache.add(curr)
    ma = curr
    mi = curr
    for v in s:
        if v == '>':
            curr -= 1
        elif v == '<':
            curr += 1
        ma = max(ma, curr)
        mi = min(mi, curr)
        
    print(ma - mi + 1)
    return 

def solve(n, s):
    curr = 0
    cache = set()
    cache.add(curr)
    ans = 1
    #curr存储的是连续 < > 符号的个数
    curr = 1
    for i in range(1,n):
        if s[i] == s[i-1]:
            curr += 1
            ans = max(ans, curr)
        else:
            curr = 1
    #最终元素个数，是符号的个数+1
    print(ans + 1)
    return 


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    solve(n, s)
   
