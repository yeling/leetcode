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
    cache = set()
    ans = 0
    for v in nums:
        if v in cache:
            ans += 1
            cache.remove(v)
        else:
            cache.add(v)

    print(ans)


n = int(input())
nums = li()
main(n, nums)


