# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve2(n, nums):
    #合并单调减，合并单调增
    ans = n
    l = 0
    #合并单调增
    for i in range(1,n):
        if nums[i] >= nums[i-1]:
            continue
        else:
            print(l, i)
            if i - l > 2:
                ans -= i - l - 2
            l = i
    if n - l > 2:
        ans -= n - l - 2
    #合并单调减
    l = 0
    for i in range(1,n):
        if nums[i] <= nums[i-1]:
            continue
        else:
            print(l, i)
            if i - l > 2:
                ans -= i - l - 2
            l = i
    if n - l > 2:
        ans -= n - l - 2

    print(ans)

    return 


def solve(n, nums):
    #合并单调减，合并单调增
    ans = n
    l = 0
    if nums.count(nums[0]) == n:
        print(1)
        return
    diff = []
    #合并单调增
    for i in range(1,n):
        if nums[i] >= nums[i-1]:
            continue
        else:
            # print(l, i)
            if i - l > 2:
                diff.append([l,i-1])
                ans -= i - l - 2
            l = i
    if n - l > 2:
        diff.append([l,n-1])
        ans -= n - l - 2
    #合并单调减
    l = 0
    for i in range(1,n):
        if nums[i] <= nums[i-1]:
            continue
        else:
            # print(l, i)
            if i - l > 2:
                diff.append([l,i-1])
                ans -= i - l - 2
            l = i
    if n - l > 2:
        diff.append([l,n-1])
        ans -= n - l - 2
    print(ans, diff)
    vis = [False]*n
    for v in diff:
        for i in range(v[0]+1,v[1]):
            vis[i] = True
    print(vis.count(False) )
    return 
# 7
# 5 4 2 1 0 0 4
solve(7, [5,4, 2, 1, 0, 0,4])
# caseNum = int(input())
# for i in range(0, caseNum):
#     n = int(input())
#     nums = li()
#     solve(n, nums)
   
