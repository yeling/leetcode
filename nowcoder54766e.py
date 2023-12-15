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

def main(n, t, nums):
    if t > n:
        print(0)
        return
    l = max(nums)
    r = 10 ** 6
    while l <= r:
        mid = l + (r - l)//2
        curr = 0
        temp = 0
        for v in nums:
            if temp + v > mid:
                curr += 1
                temp = v
            else:
                temp += v
        if temp > 0:
            curr += 1
        
        if curr <= t:
            r = mid - 1
        elif curr > t:
            l = mid + 1
        # print(mid, l, r, curr)

    print(l)
    return 

n,t = li()
nums = li()
main(n, t, nums)
   
