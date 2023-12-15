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

def main2(n):
    ans = 26
    for i in range(5,n+1):
        ans += 2*i + 1
    print(ans) 

    return 

def main(n):
    ans = 26 + (n - 4) * ( n + 6)
    print(ans) 

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
    # main2(n)
   
