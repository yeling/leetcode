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

def main(n, m, s, t):
    # print(n, m, s, t)
    all = list(s)

    for i in range(len(t)):
        all.append(t[-i-1])
    diff = 0
    for i in range(1, len(all)):
        if all[i] == all[i-1]:
            diff += 1
        if diff > 1:
            print('No')
            return
    print('Yes')
    return 

caseNum = int(input())
# print(caseNum)
for i in range(0, caseNum):
    n, m = li()
    s = input()
    t = input()
    main(n, m, s, t)
    
   
