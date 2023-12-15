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

def solve2(n, k, nums):
    if nums[0] != 1:
        print(1)
        return
    diff = []
    for i in range(1,n):
        diff += list(range(nums[i-1] + 1, nums[i]))
    print(diff)
    if len(diff) >= k:
        print(diff[k - 1])
    else:
        if len(diff) > 0:
            print(diff[-1] + (k - len(diff))*n)
        else:
            print(n + (k - len(diff))*n)

    return 

def solve(n, k, nums):
    if nums[0] != 1:
        print(1)
        return
    diff = []
    for i in range(1,n):
        diff += list(range(nums[i-1] + 1, nums[i]))
    print(diff)
    if len(diff) >= k:
        print(diff[k - 1])
    else:
        if len(diff) > 0:
            print(diff[-1] + (k - len(diff))*n)
        else:
            print(n + (k - len(diff))*n)

    return 

def check(n, k, nums):
    cache = list(range(1,nums[-1]+1))
    cnt = nums[-1]
    for _ in range(k+5):
        print(cache)
        next = []
        l = 0
        r = 0
        for j in range(cnt):
            if j == nums[l] - 1:
                l += 1
                cache.append(cache[-1] + 1)
            else:
                next.append(cache[j])
        cache = next + cache[cnt:]
       
        

    return

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    nums = li()
    check(n, k, nums)
    solve(n, k, nums)
    

   
