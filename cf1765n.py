# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

def main(n,k):
    #数字降序移动第一个，升序移动最后一个
    start = 0
    nstr = [int(v) for v in str(n)]
    i = 0 
    while i < k:
        dst = start
        while dst < len(nstr) - 1 and nstr[dst] <= nstr[dst + 1]:
            dst += 1
        if dst == start and dst < len(nstr) - 1 and nstr[dst + 1] == 0:
            start += 1
            continue
        i += 1
        nstr = nstr[0:dst] + nstr[dst+1:]
    print(*nstr,sep='')

# main(10000,4)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    k = int(input())
    main(n,k)

   
