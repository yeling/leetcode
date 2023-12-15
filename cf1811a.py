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

def main(n, d, s):
    s = list(s)
    for i,v in enumerate(s):
        if d > int(v):
            ans = s[0:i] + [str(d)] + s[i:]
            print(''.join(ans))
            return 
    ans = s[:] + [str(d)]
    print(''.join(ans))
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,d = li()
    s = input()
    main(n, d, s)
   
