# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from sys import *

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(n, nums):
    l = 0
    r = n - 1
    pre = [0] * (n + 1)
    for i,v in enumerate(nums):
        pre[i + 1] = pre[i] + v
    while l <= r:
        mid = l + (r - l)//2
        k = r - mid + 1
        temp = nums[mid:r+1]
        print('?',k, *range(mid+1,r+2))
        stdout.flush()
        test = int(input())
        if test == pre[r+1] - pre[mid]:
            r = mid - 1
        else:
            l = mid + 1
    print('!', l)
    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
