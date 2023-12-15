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
    allPair = sorted(enumerate(nums), key=lambda x:x[1])
    # print(allPair)
    ans = []
    curr = allPair[0][1]
    for i,v in allPair:
        if v % curr == 0:
            curr = v
            continue
        elif v > curr:
            curr = (v + curr - 1)//curr * curr
            ans.append((i + 1,curr - v))
        elif v < curr:
            ans.append((i + 1,curr - v))

    print(len(ans))
    for v in ans:
        print(*v)
    return 

# n = 3
# nums = [31 ,5,  17]
# main(n, nums)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n,nums)
   
