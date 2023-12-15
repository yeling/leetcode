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
    #0 无毒， 1 有毒
    curr = [0,0]
    for i in range(n):
        next = curr[:]
        if nums[i][0] == 0:
            next[0] = max(next[0], curr[1] + nums[i][1], curr[0] + nums[i][1])
        elif nums[i][0] == 1:
            next[1] = max(next[1], curr[0] + nums[i][1])
        curr = next
    print(max(curr))


    return


n = int(input())
nums = []
for i in range(0, n):
    nums.append(li())

solve(n, nums)

    

