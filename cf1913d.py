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
MOD = 998244353
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

def solve(n, nums):

    return 

def check(n, nums):
    cache = set()
    for i in range(n):
        for j in range(i + 1,n):
            temp = nums[i:j+1]
            ans = nums[0:i] + [min(temp)] + nums[j+1:]
            # print(ans)
            cache.add(tuple(ans))
            cache = cache.union(check(len(ans), ans))
    # print(cache)
    return cache


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)
    ret = check(n, nums)
    print(ret, len(ret) + 1)

   
