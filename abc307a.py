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
input = lambda: sys.stdin.readline().rstrip()
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())


def solve(n, nums):
    ans = []
    for i in range(n):
        s = 0
        for j in range(7*i, 7*(i+1)):
            s += nums[j]
        ans.append(s)

    print(*ans)
    return


n = int(input())
nums = lint()
solve(n, nums)
