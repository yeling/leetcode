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
    s = sum(nums)
    if s%2 == 0:
        print(0)
        return
    ans = INF
    for v in nums:
        temp = 0
        #even to odd
        if v%2 == 0:
            while v % 2 == 0 and v > 0:
                v = v//2
                temp += 1
        else:
        #odd to even
            while v % 2 == 1 and v > 0:
                v = v//2
                temp += 1
        ans = min(ans, temp)
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n,nums)
   
