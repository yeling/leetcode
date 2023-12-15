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

def solve2(n, nums):
    cache = defaultdict(int)
    for v in nums:
        cache[v] += 1
    for k in cache:
        if cache[k] > n//2:
            print(NO)
            return
    print(YES)
    return 

def solve(n, nums):
    diff = 0
    if n == 1:
        print(NO)
        return
    for v in nums:
        if v == 1:
            diff += 1
        else:
            diff -= (v - 1)
    if diff <= 0:
        print(YES)
    else:
        print(NO)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    # solve2(n, nums)
    solve(n, nums)
    

   
