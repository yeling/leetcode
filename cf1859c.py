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

def solve2(n):
    ans = 0
    ma = sum(i*i for i in range(1,n+1))
    # print('ma', ma)
    for i in range(1,n):
        if i == n - 1:
            ans += i * n
        else:
            ans += i * i
    print(ans)

    return 

def solve3(n):
    org = list(range(1,n+1))   
    nums = org[0:(n+1)//2] + org[n:(n+1)//2 - 1:-1]
    print(nums)

    temp = 0
    ma = 0
    for v,i in zip(nums, range(1,n+1)):
        temp += v * i
        ma = max(ma, v * i)
    ans = temp - ma
    print(ans)

    return 

def solve(n):
    org = list(range(1,n+1))   
    ans = 0
    for i in range(0,n):
        if i == 0:
            nums = org[::-1]
        else:
            nums = org[0:i] + org[n:i - 1:-1]
        # print(nums)
        temp = 0
        ma = 0
        for v,i in zip(nums, range(1,n+1)):
            temp += v * i
            ma = max(ma, v * i)
        ans = max(ans,temp - ma)
    print(ans)

    return 

def check(n):
    nums = list(range(1,n+1))
    ans = 0
    for p in permutations(nums):
        temp = 0
        ma = 0
        for v,i in zip(p, range(1,n+1)):
            temp += v * i
            ma = max(ma, v * i)
        curr = temp - ma
        if curr >= ans:
            ans = curr
            print(curr, p)
    return

for i in range(2,9):
# i = 2
    check(i)
    solve(i)

# caseNum = int(input())
# for i in range(0, caseNum):
#     n = int(input())
#     solve(n)

   
