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

def main(n, t, a, b):
    left = t
    ans = 0
    pos = -1
    for i in range(n):
        if left >= a[i] and ans < b[i]:
            ans = b[i]
            pos = i + 1
        left -= 1
        if left == 0:
            break
    print(pos)
    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,t = li()
    a = li()
    b = li()
    main(n, t, a, b)
   
