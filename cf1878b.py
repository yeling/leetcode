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

def solve(n):
    ans = [1 + 2 * i for i in range(n)]
    print(*ans)
    # check(ans)
    return 

def check(nums):
    n = len(nums)
    for i in range(2,n):
        if (nums[i - 1] + nums[i - 2])%(3 * nums[i]) == 0:
            print(NO)
            return
    print(YES)

# for i in range(3,100):
#     solve(i)


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    solve(n)
   
