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

input = lambda: sys.stdin.readline().rstrip()
mi = lambda :map(int,input().split())
li = lambda :list(mi())


def solve(n, nums):
    cache = []
    for a,b in nums:
        cache.append((a,b))
    cache.sort(key = lambda x: (x[0], -x[1]))
    ans = cnt = pre = 0
    # print(cache)
    for a,b in cache:
        if a == pre:
            cnt += 1
        else:
            cnt = 1
        pre = a
        if a >= cnt:
            ans += b
    print(ans)
    
    return

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(li())
    solve(n, nums)
