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
    pre = [0] * n
    suf = [0] * n
    pre[0] = nums[0]
    for i in range(1,n):
        pre[i] = max(nums[i], pre[i - 1] + 1)
    suf[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        suf[i] = max(nums[i], suf[i + 1] + 1)
    # print(pre, suf)
    ans = INF
    for i in range(n):
        curr = max(suf[i], pre[i])
        if i > 0:
            curr = max(suf[i], n - 1 - i + pre[i - 1] + 1)
        if i < n - 1:
            curr = max(curr, pre[i], i + suf[i + 1] + 1)
        ans = min(curr, ans)
    print(ans)
    
    return 


n = int(input())
nums = li()
solve(n, nums)

   
