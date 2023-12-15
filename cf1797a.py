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

def main(n, m, nums):
    x1, y1, x2, y2 = nums
    curr = 4
    if x1 == 1 or x1 == n:
        curr -= 1
    if y1 == 1 or y1 == m:
        curr -= 1
    ans = curr
    curr = 4
    if x2 == 1 or x2 == n:
        curr -= 1
    if y2 == 1 or y2 == m:
        curr -= 1
    ans = min(ans, curr)
    print(ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    nums = li()
    main(n, m, nums)
   
