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
    ans = []
    for v in nums:
        if v%2 == 0:
            ans.append(v)
    print(*ans)


n = int(input())
nums = li()
main(n, nums)
