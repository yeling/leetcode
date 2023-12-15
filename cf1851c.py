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
    if k == 1:
        print(YES)
        return
    n = len(nums)
    pre = [0]*(n + 1)
    after = [0]*(n + 2)
    for i in range(n):
        pre[i + 1] = pre[i]
        if nums[i] == nums[0]:
            pre[i + 1] += 1 

    for i in range(n-1, -1, -1):
        after[i + 1] = after[i + 2]
        if nums[i] == nums[-1]:
            after[i + 1] += 1 

    if nums[0] == nums[-1]:
        if pre[n] >= k:
            print(YES)
        else:
            print(NO)
        return
    
    for i in range(1,n):
        # 可以直接跳到整除的地方
        if pre[i] >= k and after[i + 1] >= k:
            print(YES)
            return
    print(NO)


    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    nums = li()
    solve(n, k, nums)

   
