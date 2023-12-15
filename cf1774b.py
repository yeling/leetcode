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

def main2(n,m,k,colors):
    ans = True
    if m < k:
        ans = False
    mc = max(colors) 
    if mc > (n + k - 1)//k:
        ans = False
    if mc == (n + k - 1)//k and colors.count(mc) > n%k:
        ans = False

    if ans:
        print("Yes")
    else:
        print("No")
   
    return 

def main(n,m,k,colors):
    ans = True
    if m < k:
        ans = False
    mc = max(colors) 
    # print(colors.count(mc))
    if mc > (n + k - 1)//k:
        ans = False
    if mc == (n + k - 1)//k and colors.count(mc) > n%k:
        ans = False

    if ans:
        print("Yes")
    else:
        print("No")
   
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m,k = li()
    colors = li()
    main(n,m,k,colors)

   
