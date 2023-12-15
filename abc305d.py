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


def solve(n, nums, q, qs):
    pre = [0] * (n + 1)
    for i in range(n):
        if i%2 == 0 and i > 0:
            pre[i + 1] = pre[i] + nums[i] - nums[i-1]
        else:
            pre[i + 1] = pre[i]
    ans = 0
    # print(pre)
    # print(nums)
    for l,r in qs:
        lpos = bisect_left(nums, l)
        rpos = bisect_left(nums, r)
        # print(lpos, rpos)
        ans = 0
        if lpos%2 == 1:
            ans += 0
        else:
            ans += nums[lpos] - l
        # print('ll',l, lpos, ans)
        
        if rpos%2 == 0:
            ans += r - nums[rpos - 1]
        else:
            ans += 0
        rpos -= 1
        ans += pre[rpos + 1] - pre[lpos + 1]
        print(ans)
            


    



n = int(input())
nums = li()
q = int(input())
qs = []
for _ in range(q):
    qs.append(li())

solve(n, nums, q, qs)

