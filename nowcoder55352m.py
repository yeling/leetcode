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


def main(n, nums):
    cache = defaultdict(int)
    ans = 0
    for i,v in enumerate(nums):
        if cache[v] == 0:
            ans += i
        else:
            ans += i - cache[v]
        cache[v] += 1
    print(ans)


n = int(input())
nums = li()
main(n, nums)
