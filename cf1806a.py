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

def main(nums):
    a,b,c,d = nums
    y = d - b
    x = c - a
    if y < 0 or y < x:
        print(-1)
        return
    print(y + y - x)
    

    # print(a,b,c,d)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    main(li())

   
