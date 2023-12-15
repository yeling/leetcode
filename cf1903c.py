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
    ans = 0
    suf = [0] * (n + 1)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + nums[i]
    
    for i in range(n-1, -1, -1):
        suf[i] = suf[i + 1] + nums[i]
    # print(suf)
    k = 1
    i = 0
    while i < n:
        j = i + 1
        while j < n and suf[j] < 0:
            j += 1
        ans += k * (pre[j] - pre[i])
        k += 1
        i = j
    print(ans)






    return 

def check(n, nums):
    ans = 0
    for i,v in enumerate(nums):
        ans += (i + 1) * v
    print(ans)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)
    # check(n, nums)

   
