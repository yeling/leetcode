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

def solve(s):
    n = len(s)
    pre = ['0'] * (n + 1)
    for i in range(len(s)):
        if s[i] != '?':
            pre[i + 1] = s[i]
        else:
            pre[i + 1] = pre[i]
    ans = pre[1:]
    print(''.join(ans))
    
    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    solve(s)

   
