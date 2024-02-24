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

def solve(n, x, y, nums):
    cache = defaultdict(list)
    for i,v in enumerate(nums):
        de = v % y
        cache[de ^ INF].append(v)
    ans = 0

    for k in cache:
        temp = cache[k]
        xcache = defaultdict(int)
        # print(k^INF, temp)
        for v in temp:
            ans += xcache[((x - v%x)%x)^INF]
            xcache[(v%x)^INF] += 1


    
    print(ans)
    return 

def check(n, x, y, nums):
    ans = 0
    for i in range(n):
        for j in range(i + 1,n):
            if (nums[i] + nums[j])%x == 0 and (nums[i] - nums[j])%y == 0:
                ans += 1
    print(ans)

caseNum = int(input())
for i in range(0, caseNum):
    n,x,y = li()
    nums = li()
    solve(n, x, y, nums)
    # check(n, x, y, nums)

   
