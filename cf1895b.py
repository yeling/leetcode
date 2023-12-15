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
    nums.sort()
    ans = 0
    ps = [(nums[0], nums[-1])]
    # print(nums)
    for i in range(1,n):
        p1 = (nums[i - 1], nums[2 * n - 1 - (i - 1)])
        p2 = (nums[i], nums[2 * n - 1 - i])
        # print(p1, p2)
        # ps.append(p1)
        ps.append(p2)
        ans += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    print(ans)
    for p in ps:
        print(*p)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
