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
    s = n
    t = 1
    for i,v in enumerate(nums):
        if v == t:
            t += 1
    
    ans = (n - t + 1 + k - 1)//k
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    nums = li()
    main(n, k, nums)
   
   
