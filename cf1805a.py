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
    curr = 0
    for v in nums:
        curr = curr ^ v
    # print('temp', curr)
    if n%2 == 1:
        print(curr^0)
    else:
        if curr == 0:
            print(0)
        else:
            print(-1)
    # print(curr)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
