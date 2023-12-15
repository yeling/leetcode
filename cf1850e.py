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

def solve(n, c, nums):
    s = 0
    for v in nums:
        s += v
        c -= v * v
    # print(c, s)
    a = 4 * s
    b = 4 * n
    # print(a, b, c)
    # 4sw + 4nw*w = c
    # aw + b*w*w = c
    left = 1
    right = int(sqrt(c)) + 1
    while left <= right:
        mid = left + (right - left)//2
        temp = a * mid + b * mid * mid
        if c < temp:
            right = mid - 1
        elif c > temp:
            left = mid + 1
        elif c == temp:
            print(mid)
            return

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,c = li()
    nums = li()
    solve(n, c, nums)
   
