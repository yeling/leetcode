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
    l = 0
    r = len(s) - 1
    diff = -1
    while l < r:
        if s[l] != s[r]:
            if diff == -1 or diff == l - 1:
                diff = l
            else:
                print('No')
                return
        l += 1
        r -= 1 
    print('Yes')
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n, s)
