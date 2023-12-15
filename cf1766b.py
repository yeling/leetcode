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

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(n,s):
    dst = []
    lower = string.ascii_lowercase
    for i in range(26):
        for j in range(26):
            dst.append(lower[i] + lower[j])

    for v in dst:
        if s.count(v) >= 2:
            print('YES')
            return 
    print('NO')
    return 

# main(10,'laaaacaba')


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n,s)
