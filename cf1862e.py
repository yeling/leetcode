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

def solve2(n, m, d, nums):
    cache = []
    for i,v in enumerate(nums):
        cache.append((v - (i + 1) * d, i))
    cache.sort(reverse=True)
    # pre = []
    # for i in range(n):
    #     if len(pre) < m and cache[i][0] > 0:
    #         pre.append(cache[i])
    pre = cache[0:m]
    print(cache, pre)
    pre.sort(key=lambda x:x[1])
    print(pre)
    ans = 0
    #对pre数组进行二分，出现负数，左移动， 正数 右移动

    print(ans)

    return 

def solve(n, m, d, nums):
    cache = []
    for i,v in enumerate(nums):
        cache.append((v - (i + 1) * d, i))
    cache.sort(reverse=True)
    # pre = []
    # for i in range(n):
    #     if len(pre) < m and cache[i][0] > 0:
    #         pre.append(cache[i])
    pre = cache[0:m]
    print(cache, pre)
    pre.sort(key=lambda x:x[1])
    print(pre)
    ans = 0
    #对pre数组进行二分，出现负数，左移动， 正数 右移动
    
    print(ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m,d = li()
    nums = li()
    solve(n, m, d, nums)

   
