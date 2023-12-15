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

def main(n, nums):
    one = 0
    ans = 0
    for v in nums:
        if v > 1:
            ans += 1
        else:
            one += 1
    ans += (one + 1)//2
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
