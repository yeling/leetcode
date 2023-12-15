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


def main(nums):
    nums.sort()
    ans = 0
    a = nums[1] - nums[0]
    b = nums[2] - nums[0]
    if a%2 != 0:
        print(-1)
        return 
    if a == b:
        if a%3 != 0:
            print(-1) 
        else:
            print(a//3)
        return 
    ans += a//2
    b = b - a//2 * 4
    if b%6 != 0:
        print(-1)
        return 
    ans += b//3
    print(ans)



main([0,9,27])
# caseNum = int(input())
# for i in range(0, caseNum):
#     main(li())

