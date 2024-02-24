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

def solve2(n, nums):
    ans = 0
    cache = defaultdict(int)
    for v in nums:
        cache[v] += 1
    ks = list(cache.keys())
    ks.sort(reverse = True)
    left = n
    for k in ks:
        left = left - cache[k]
        ans += (cache[k] * (cache[k] - 1))//2 * left
        ans += (cache[k] * (cache[k] - 1) * (cache[k] - 2))//6
    print(ans)
    return 

def solve3(n, nums):
    ans = 0
    cache = [0] * (3 * (10**5) + 1)
    for v in nums:
        cache[v] += 1
    left = n
    for k in range(len(cache) - 1, -1, -1):
        if cache[k] > 0:
            left = left - cache[k]
            ans += (cache[k] * (cache[k] - 1))//2 * left
            ans += (cache[k] * (cache[k] - 1) * (cache[k] - 2))//6
    print(ans)
    return 

def solve(n, nums):
    ans = 0
    i = 0
    left = n
    nums.sort(reverse = True)
    while i < n:
        temp = 0
        j = i
        while j < n and nums[j] == nums[i]:
            temp += 1
            j += 1
        left = left - temp
        ans += (temp * (temp - 1))//2 * left
        ans += (temp * (temp - 1) * (temp - 2))//6
        i = j
        
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
