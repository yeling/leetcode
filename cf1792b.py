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

def main2(nums):
    a1,a2,a3,a4 = nums
    ans = 0
    if a2 > a3:
        a2,a3 = a3,a2
    if a1 > 0:
        ans += a1
        ans += a2
        ans += min(a3, a1 + a2)
        if a3 > 0:
            ans += min(a4,a2%(2 * a1))
        else:
            ans += min(a4, a1 + 1)
    else:
        if a4 > 0:
            ans = 1

    print(ans)
    return 

def main(nums):
    a1,a2,a3,a4 = nums
    ans = a1
    A,B = a1, a1
    if a2 > a3:
        a2,a3 = a3,a2
    while a2 > 0 and A > 0 and B > 0:
        A += B
        B = 0
        a2 
    

    print(ans)
    return 
# nums = [2, 5, 10, 6]
# main(nums)
caseNum = int(input())
for i in range(0, caseNum):
    main(li())
   
