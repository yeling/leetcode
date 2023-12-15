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

def main(m, nums):
    cache = set()
    ans = []
    for i in range(m):
        curr = nums[-1-i]
        flag = False
        for v in curr:
            if v not in cache:
                if flag == False:
                    ans.append(v)
                flag = True
                cache.add(v)
                
        if flag == False:
            print(-1)
            return 
    ans.reverse()
    print(*ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    m = int(input())
    nums = []
    for _ in range(m):
        n = int(input())
        nums.append(li())
    main(m, nums)
   
