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

def solve(n, nums, q, grid):
    pre = [0] * (n + 1)
    for i,v in enumerate(nums):
        pre[i + 1] = v + pre[i]
    ans = []
    def check(l, u, p):
        return pre[p + 1] - pre[l] - u

    for s,u in grid:
        left = s - 1
        right = n - 1
        target = 0
        while left <= right:
            mid = left + (right - left)//2
            t = check(s - 1, u + 1, mid)
            if target < t:
                right = mid - 1
            elif target >= t:
                left = mid + 1
        if left == n:
            left = n - 1
        
        t = pre[left] - pre[s - 1]

        
        if nums[left] >= 2 * t + 1 and left > s:
            left -= 1

        print(nums[left], t, left)
        
        # curr = pre[left + 1] - pre[s]
            
        ans.append(left + 1)
    print(ans)



    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    q = int(input())
    grid = []
    for _ in range(q):
        grid.append(li())
    solve(n, nums, q, grid)

   
