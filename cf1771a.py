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

def main(n:int, nums:list):
    b = max(nums)
    s = min(nums)
    ans = 0
    bn = nums.count(b) 
    sn = nums.count(s)
    if b != s:
        ans = bn * sn * 2
    else:
        ans = bn * (bn - 1)
    print(ans)


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n,nums)
   
