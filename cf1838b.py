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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

input = lambda: sys.stdin.readline().rstrip()
mi = lambda :map(int,input().split())
li = lambda :list(mi())

#2和 头尾较大的交换
def solve1(n, nums):
    one = nums.index(1)
    two = nums.index(2)
    # print(nums)
    if one == 0:
        print(two + 1, n)
    elif one == n:
        print(1, two + 1)
    elif two == 0:
        print(one + 1, n)
    elif two == n:
        print(1, one + 1)
    else:
        i = two + 1
        j = 0
        if nums[0] > nums[-1]:
            j = 1
        else:
            j = n
        print(i, j)
    # print(one, ' t ', two)
    return 

#1，2中间插入最大值
def solve(n, nums):
    one = nums.index(1)
    two = nums.index(2)
    last = nums.index(n)
    # print(nums)
    if last < one and last < two:
        print(last + 1, min(one,two) + 1)
    elif last > one and last > two:
        print(last + 1, max(one,two) + 1)
    else:
        print(one + 1, one+1)

    # print(one, ' t ', two)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)


   
