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

def solve(n, nums):
    mi = INF
    ma = -INF
    miPos = -1
    maPos = -1
    ans = []
    for i, v in enumerate(nums):
        if v > ma:
            ma = v
            maPos = i
        if v < mi:
            mi = v
            miPos = i

    if mi < 0 and ma > 0:
        if -mi >= ma:
            for i,v in enumerate(nums):
                if v > 0:
                    nums[i] += mi
                    ans.append([i + 1,miPos + 1])
            ma = mi
        elif -mi < ma:
            for i,v in enumerate(nums):
                if v < 0:
                    nums[i] += ma
                    ans.append([i + 1,maPos + 1])
            mi = ma

    # > 0 pre
    if mi >= 0:
        curr = nums[0]
        for i in range(1,n):
            if nums[i] < curr:
                curr += nums[i]
                ans.append([i + 1,i])
            else:
                curr = nums[i]
    elif ma <= 0:
        curr = nums[-1]
        for i in range(2,n + 1):
            if nums[-i] > curr:
                curr += nums[-i]
                ans.append([n - i + 1, n - i + 2])
            else:
                curr = nums[-i]

    print(len(ans))
    for v in ans:
        print(*v)




    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
