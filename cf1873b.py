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
    mul = 1
    zero = 0
    for v in nums:
        mul *= v
        if v == 0:
            zero += 1

    if mul == 0:
        if zero > 1:
            print(0)
        else:
            ans = 1
            for v in nums:
                if v != 0:
                    ans *= v
            print(ans)
    else:
        ans = 0
        for v in nums:
            ans = max(ans, mul//v * (v + 1))
        print(ans)
        
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
