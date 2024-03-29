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


def quickPowMode(a, n, p):
    ans = 1
    while(n > 0):
        if n & 1 == 1:
            ans = ans * a % p
        a = a * a % p
        n = n >> 1
    return ans % p


def solve(n, k, nums):
    l = 0
    r = 0
    pre = [0]*(n + 1)
    for i,v in enumerate(nums):
        pre[i + 1] = pre[i] + v

    maxSeq = 0
    maxAfter = pre[-1]
    for i in range(n-1, -1, -1):
        maxAfter = max(maxAfter, pre[i + 1])
        if maxAfter - pre[i] > 0:
            maxSeq = max(maxSeq, maxAfter - pre[i])
        # print(i, maxAfter, maxSeq)
    maxSeq = (maxSeq + MOD)%MOD
    # print(nums, pre, maxSeq)
    ans = pre[-1] + (maxSeq * (quickPowMode(2, k, MOD) + MOD - 1))%MOD
    ans = (ans + MOD)%MOD
    print(ans )
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    nums = li()
    solve(n, k, nums)


   
