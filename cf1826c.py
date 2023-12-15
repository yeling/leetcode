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

def main2(n, m):
    if n == 1:
        print(YES)
        return 
    while m > 1:
        if n%m == 0:
            print(NO)
            return
        else:
            m -= 1
    print(YES)
    return 

def main(n, m):
    if n == 1:
        print(YES)
        return 
    if n <= m:
        print(NO)
        return 
    t = 2
    ma = int(sqrt(n))+1 
    while t <= ma:
        if n%t == 0 and t <= m:
            print(NO)
            return
        else:
            t += 1
    print(YES)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    main(n, m)
   
