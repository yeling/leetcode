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

def solve(n, nums):
    ans = []
    cnt = 0
    n = len(nums)
    if n == 1:
        print(1)
        return 
    ans.append(1)
    pre = nums[0]
    for i in range(1,n):
        if (cnt == 0 and nums[i] >= pre) or (cnt == 1 and nums[i] >= pre and nums[i] <= nums[0]):
            pre = nums[i]
            ans.append(1)
            continue
        else:
            if cnt == 0:
                if nums[i] <= nums[0]:
                    pre = nums[i]
                    cnt = 1
                    ans.append(1)
                else:
                    ans.append(0)
            else:
                ans.append(0)
    print(''.join([str(v) for v in ans]))

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
