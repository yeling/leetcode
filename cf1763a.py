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
    cache = [[0,0] for _ in range(11)]
    # i, (-1,-1)
    for v in nums:
        bs = bin(v)[2:]
        # print(bs)
        for i in range(len(bs) - 1, -1, -1):
            cache[len(bs) - 1 - i ][int(bs[i])] += 1
        for i in range(len(bs), 11):
            cache[i][0] += 1

    maxs = ''
    mins = ''
    for v in cache:
        if v[0] > 0:
            mins = '0' + mins
        elif v[1] > 0:
            mins = '1' + mins
        if v[1] > 0:
            maxs = '1' + maxs
        elif v[0] > 1:
            maxs = '0' + maxs
    
    # print(maxs, mins)
    ans = int(maxs, base=2) - int(mins, base=2)
    print(ans)

    
    return 

# n = 5
# nums = [1, 2, 3, 4, 5]
# main(n,nums)


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
