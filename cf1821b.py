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

def main(n, a, b):
    l = 0
    r = n - 1 
    while l <= n - 1:
        if a[l] != b[l]:
            break
        l += 1
    while r >= 0:
        if a[r] != b[r]:
            break
        r -= 1
    
    temp = a[l:r+1]
    temp.sort()

    if l >= 1 and a[l - 1] <= temp[0]:
        while l >= 1 and a[l - 1] <= a[l]:
            l -= 1

    if r < n - 1 and a[r + 1] >= temp[-1]:
        while r < n - 1 and a[r + 1] >= a[r]:
            r += 1
    
    print(l + 1, r + 1)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = li()
    b = li()
    main(n, a, b)
   
