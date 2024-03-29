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
    ans = [0] * n
    # print(n)
    for i in range(n-2):
        diff = nums[i] - ans[i]
        if diff >= 0:
            ans[i] += diff
            ans[i + 1] += diff * 2
            ans[i + 2] += diff
        else:
            print(NO)
            return
        # print(i, ans)
    if ans[-2] == nums[-2] and ans[-1] == nums[-1]:
        print(YES)
    else:
        print(NO)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
