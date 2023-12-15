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
    if n%2 == 1:
        print('Yes')
        return
    # print(nums)
    a = nums[0]
    for i in range(1,n,2):
        b = nums[i]
        # print(a, b)
        if i + 1 == n:
            if a <= b:
                print('Yes')
            else:
                print('No')
        else:
            c = nums[i + 1]
            if a > b:
                c += abs(a - b)
                a = c
            else:
                c -= b - a
                a = c
                
    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
