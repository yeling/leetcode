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

def main(n, s):
    res = ''
    total = int(s[0])
    
    for i in range(1,n):
        if int(s[i]) == 0:
            res += '+'
        elif total == 1:
            res += '-'
            total = 0
        else:
            res += '+'
            total = 1
    print(res)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n,s)
   
