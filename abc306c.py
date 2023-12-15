# auther yeling
import sys
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from heapq import *
import string


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

# input = lambda: sys.stdin.readline().rstrip()
mi = lambda :map(int,input().split())
li = lambda :list(mi())


def solve(n, nums):
    cnt = [0] * (n + 1)
    ans = []
    for v in nums:
        cnt[v] += 1
        if cnt[v] == 2:
            ans.append(v)
    print(*ans)
    return



n = int(input())
nums = li()
solve(n, nums)
