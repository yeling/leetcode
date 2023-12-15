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
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())

def solve(n, nums):
    nums.sort()
    l = 0
    r = n - 1
    ans = 0
    while l <= r:
        ans += nums[r] - nums[l]
        l += 1
        r -= 1
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = lint()
    solve(n, nums)

   
