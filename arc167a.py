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
from os import path

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

# for I/O for local system
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    # sys.stdout = open("output.txt","w")

# For fast I/O
# input = sys.stdin.buffer.readline
# input = sys.stdin.readline
# print = sys.stdout.write

input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())



def solve(n, m, nums):
    ans = [0] * m
    nums.sort(reverse = True)
    i = 0
    while i < n:
        while i < m:
            ans[i] += nums[i]
            i += 1
        if i < n:
            ans[-1 - (i - m)] += nums[i]
        i += 1
    # print(ans)
    ret = sum(v * v for v in ans)
    print(ret)
    return

n,m = li()
nums = li()
solve(n, m, nums)

