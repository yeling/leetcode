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
    # print(n, nums)
    if nums[0] != 0:
        print(0)
        sys.stdout.flush()
        y = int(input())
        return
    else:
        r = 0
        for i in range(1,n):
            if nums[i] == nums[i - 1] + 1:
                r = i
                continue
            else:
                break
        cache = set(nums)
        print(r + 1)
        cache.add(r + 1)
        r += 1
        sys.stdout.flush()

        while True:
            y = int(input())
            if y >= 0:
                print(y)
                sys.stdout.flush()
            else:
                break
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
