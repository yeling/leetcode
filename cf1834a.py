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
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve(n, nums):
    # print(nums)
    s = 0
    m = 1
    for i in range(n):
        s += nums[i]
        m *= nums[i]
    if s >= 0:
        if m == 1:
            print(0)
        elif m == -1:
            print(1)
    else:
        ans = (-s + 1)//2
        if m == 1:
            if ans%2 == 0:
                print(ans)
            else:
                print(ans + 1)
        else:
            if ans%2 == 0:
                print(ans + 1)
            else:
                print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
