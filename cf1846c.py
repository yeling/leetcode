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
input = sys.stdin.buffer.readline
input = sys.stdin.readline
# print = sys.stdout.write

# input = lambda: sys.stdin.readline().rstrip()
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())

#TLE
def solve(n, m, h, nums):
    #[i,[point, penalty]]
    # print(nums)
    cache = []
    for i in range(n):
        nums[i].sort()
        point,s, penalty = 0,0,0
        for v in nums[i]:
            if s + v <= h:
                point += 1
                s += v
                penalty += s
            else:
                break
        cache.append([i,[point, penalty]])
    cache.sort(key = lambda x:(-x[1][0], x[1][1]))
    # print(cache)
    for i in range(n):
        if cache[i][0] == 0:
            print(i + 1)
            break
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m,h = lint()
    nums = []
    for _ in range(n):
        nums.append(lint())
    solve(n, m, h, nums)


   
