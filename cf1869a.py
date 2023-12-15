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

def check(now):
    print('check', now)
    curr = 0
    for v in now:
        curr ^= v
    next = [curr] * len(now)
    print(next)
    curr = 0
    for v in next:
        curr ^= v
    next = [curr] * len(now)
    print(next)
    return

def solve(n, nums):
    if n%2 == 0:
        print(2)
        print(1,n)
        print(1,n)
        # check(nums)
    else:
        print(4)
        print(1,2)
        print(1,2)
        # check(nums[0:2])
        # check([0] + nums[2:])
        print(2,n)
        print(2,n)


    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
