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


def main(n, k, nums):
    cnt = defaultdict(int)
    for v in nums:
        cnt[v] +=1
    keys = list(cnt.keys())
    keys.sort()
    ans = 0
    size = min(k, len(keys))
    for i in range(size):
        if keys[i] == ans:
            ans += 1
        else:
            break

    print(ans)


n,k = li()
nums = li()
main(n, k, nums)
