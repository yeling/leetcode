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
    # print(n, nums)
    re = [0,INF]
    for i in range(1, n):
        a = nums[i - 1]
        b = nums[i]
        if a < b:
            re[1] = min(re[1], (a + b)//2)
        elif a > b:
            re[0] = max(re[0], (a + b + 1)//2)
        if re[0] > re[1]:
            print(-1)
            return
    print(re[0])

    return 

# n = 6
# nums = [10, 5, 4, 3, 2, 1]
# main(n,nums)


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
