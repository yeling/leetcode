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
    if nums[0] != n:
        print(NO)
        return
    last = nums[0]
    left = nums[-1]
    l = 1
    r = n - 1
    while l < n:
        left -= 1
        if left > 0:
            dst = last
        elif left == 0:
            k = r - 1
            while k >= 0:
                if nums[k] - nums[r] > 0:
                    left = nums[k] - nums[r]
                    last -= r - k
                    r = k
                    dst = last
                    break
                k -= 1
            if k == -1:
                print(NO)
                return
        if nums[l] == dst:
            l += 1
            continue
        else:
            print(NO)
            return
        
    print(YES)
    return 


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)


   
