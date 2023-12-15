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

def solve(n, m, d, nums):
    pre = [0] * (m + 2)
    pre[0] = 1
    nums = [1] + nums

    for i in range(1, len(nums)):
        pre[i] = pre[i - 1] + (nums[i] - nums[i - 1] - 1)//d + 1
    pre[-1] = pre[-2] + (n - nums[-1])//d
    
    nums.append(n)
    # print(nums, pre)
    ans = INF
    cnt = 0
    for i in range(1, len(nums) - 1):
        if i == len(nums) - 2:
            temp = pre[i - 1] + (nums[i + 1] - nums[i - 1])//d
        else:
            temp = pre[i - 1] + (nums[i + 1] - nums[i - 1] - 1)//d + 1 + pre[-1] - pre[i + 1]

        if temp < ans:
            ans = temp
            cnt = 1
        elif temp == ans:
            cnt += 1
        # print(i, temp, ans)
        
    print(ans, cnt)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m,d = li()
    nums = li()
    solve(n, m, d, nums)

   
