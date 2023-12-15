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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(n, nums):
    if len(nums) == 0:
        print(0,0)
        return 
    if len(nums) == 1:
        print(2**nums[0], 2**nums[0])
        return 
    nums.sort(reverse = True)
    # nums.sort()
    l = 0
    r = 2 ** nums[0]
    for i in range(1,n):
        w = 2 ** nums[i]
        l = (r + w) // w * w
        r = l + w
        print(w, l, r)
    print(r)


n = int(input())
nums = li()
main(n, nums)