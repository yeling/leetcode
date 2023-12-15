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
    ans = max(nums)
    for i in range(1,n):
        curr = nums[i]
        cnt = 0
        for j in range(i-1, -1, -1):
            if nums[j] <= curr and cnt <= k:
                cnt += curr - nums[j] + 1
                curr = curr + 1
                if cnt <= k:
                    ans = max(ans, curr)
            else:
                break 
    print(ans)
    return 


caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    nums = li()
    solve(n, k, nums)

   
