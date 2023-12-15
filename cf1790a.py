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

pi = '314159265358979323846264338327'
def main(n):
    for i,v in enumerate(n):
        if pi[i] != v:
            print(i)
            return
    print(len(n))
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = input()
    main(n)
   
