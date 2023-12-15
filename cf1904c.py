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

def solve(n, k, nums):
    if k >= 3:
        print(0)
        return
    elif k == 1:
        nums.sort()
        ans = min(nums[0], nums[1] - nums[0])
        for i in range(1,n):
            ans = min(ans, nums[i] - nums[i - 1])
        print(ans)
    elif k == 2:
        nums.sort()
        ans = min(nums[0], nums[1] - nums[0])
        for i in range(1,n):
            ans = min(ans, nums[i] - nums[i - 1])
        for i in range(n):
            for j in range(i + 1, n):
                curr = abs(nums[j] - nums[i])
                pos = bisect_left(nums, curr)
                ans = min(ans, abs(curr - nums[pos]))
                if pos > 0:
                    ans = min(ans, abs(curr - nums[pos - 1]))
        print(ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    nums = li()
    solve(n, k, nums)

   
