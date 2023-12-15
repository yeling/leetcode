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

def solve(n, k, q, nums):
    #bfs (index, value)
    # 计算连续 <= q的数量
    pre = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        if nums[i] <= q:
            pre[i] = pre[i + 1] + 1
    cnt = 0
    for i in range(n):
        if pre[i] >= k:
            cnt += pre[i] - k + 1
    print(cnt)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k,q = li()
    nums = li()
    solve(n, k, q, nums)

   
