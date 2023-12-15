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

def main(n, k, nums):
    hasl = False
    hasr = False
    for l,r in nums:
        if l == k:
            if hasr:
                print('Yes')
                return 
            hasl = True    
        if r == k:
            if hasl:
                print('Yes')
                return 
            hasr = True
    print('No')
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k  = li()
    nums = []
    for j in range(n):
        nums.append(li())
    main(n, k, nums)

   
