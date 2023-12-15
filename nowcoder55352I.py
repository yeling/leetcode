# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(n, x, nums):
    l,r = 0,0
    ans = INF

    curr = nums[l]
    while l < n:
        if curr >= x or r == n - 1:
            if curr >= x:
                ans = min(ans, r - l + 1)
            curr //= nums[l]
            l += 1
        elif r < n - 1:
            r += 1
            curr *= nums[r]
    if ans == INF:
        print(-1)
    else:
        print(ans)


# n = 5
# x = 9
# nums = [2, 3, 1, 3, 3]
# main(n, x, nums)

n,x = li()
nums = li()
main(n, x, nums)


