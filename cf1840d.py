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
    cache = set(nums)
    nums = list(cache)
    nums.sort()
    n = len(nums)
    if n <= 3:
        print(0)
        return
    
    def check2(mid):
        t1 = nums[0] + mid
        pos1 = bisect(nums, t1)
        if pos1 >= n - 1:
            return True
        t2 = nums[pos1] + mid
        pos2 = bisect(nums, t2)
        if pos2 >= n - 1:
            return True

        t3 = nums[pos2] + mid
        pos3 = bisect(nums, t3)
        if pos3 >= n:
            return True
        
        return False
    
    def check(mid):
        t1 = nums[0] + mid
        t2 = -1
        t3 = -1
        for i in range(n):
            if nums[i] > t1 and t2 == -1:
                t2 = nums[i] + mid
            elif t2 != - 1 and nums[i] > t2 and t3 == -1:
                t3 = nums[i] + mid
            elif t3 != -1 and nums[i] > t3:
                return False

        return True
    l = 0 
    r = (nums[-1] - nums[0])//3 + 3
    while l <= r:
        mid = l + (r - l)//2
        # ck = check(mid)
        ck = check2(mid)
        # print(mid, ck)
        if ck:
            r = mid - 1
        else:
            l = mid + 1
    

    print((l + 1)//2)
    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
