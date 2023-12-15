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
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())

def solve2(n, nums):
    curr = 0
    ans = 0
    # print(nums)
    for v in nums:
        curr ^= v
        ans = max(ans, curr)
    print(ans)
    return 

def solve3(n, nums):
    ans = 0
    # print(nums)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] ^ nums[i]
        ans = max(ans, nums[i], pre[i + 1])

    for i in range(n):
        ans = max(ans, pre[i] ^ pre[n])
    print(ans)
    return 

#TLE 优化速度
def solve4(n, nums):
    ans = 0
    # print(nums)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] ^ nums[i]
        ans = max(ans, nums[i], pre[i + 1])

    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, pre[j + 1] ^ pre[i])
    print(ans)
    return 

#TLE 优化速度
def solve(n, nums):
    ans = 0
    # print(nums)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] ^ nums[i]
        ans = max(ans, nums[i], pre[i + 1])
    cache = set()
    for i in range(n):
        for v in cache:
            ans = max(ans, v ^ pre[i + 1])
        cache.add(pre[i + 1])
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = lint()
    # solve4(n, nums)
    solve(n, nums)

   
