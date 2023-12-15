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

def solve(n, nums):
    minEven = INF
    minOdd = INF
    for v in nums:
        if v%2 == 0:
            minEven = min(minEven, v)
        else:
            minOdd = min(minOdd, v)
    mi = min(minEven, minOdd)
    even = mi%2 == 0
    for v in nums:
        if even:
            if v%2 == 0:
                continue
            elif v%2 == 1:
                print(NO)
                return
        else:
            if v%2 == 1:
                continue
            elif v%2 == 0 and v > minOdd:
                continue
            else:
                print(NO)
                return
    print(YES)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)
   
