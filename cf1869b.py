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

def solve(n, k, a, b, nums):
    mina = INF
    minb = INF
    for i in range(k):
        mina = min(mina, abs(nums[a - 1][0] - nums[i][0]) + abs(nums[a - 1][1] - nums[i][1]))
        minb = min(minb, abs(nums[b - 1][0] - nums[i][0]) + abs(nums[b - 1][1] - nums[i][1]))
    
    dis = abs(nums[a - 1][0] - nums[b - 1][0]) + abs(nums[a - 1][1] - nums[b - 1][1])
    print(min(dis, mina + minb))
    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k,a,b = li()
    nums = []
    for _ in range(n):
        nums.append(li())
    solve(n, k, a, b, nums)

   
