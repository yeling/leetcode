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

#TLE
def solve2(n, k, nums):
    stack = []
    for i,v in enumerate(nums):
        heappush(stack, [-v,i + 1])
    ans = []
    while len(stack) > 0:
        temp = heappop(stack)
        temp[0] += k
        if temp[0] >= 0:
            ans.append(temp[1])
        else:
            heappush(stack, temp)
    print(*ans)
    return 

def solve(n, k, nums):
    cache = []
    for i,v in enumerate(nums):
        if v%k == 0:
            cache.append((-k, i + 1))
        else:
            cache.append((-v%k, i + 1))
    cache.sort()
    ans = [v[1] for v in cache]
    print(*ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    nums = li()
    # solve2(n, k, nums)
    solve(n, k, nums)
   
