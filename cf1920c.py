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
def solve2(n, nums):
    ans = 1
    for i in range(1,n):
        if n%i == 0:
            curr = abs(nums[i] - nums[0])
            for k in range(i):
                for j in range(i + k,n,i):
                    curr = gcd(curr, abs(nums[j] - nums[j - i]))
                    if curr == 1:
                        break
                if curr == 1:
                    break
            if curr != 1:
                ans += 1

    print(ans)
    return 

def solve(n, nums):
    ans = 1
    cache = defaultdict(int)
    for i in range(1,n):
        if n%i == 0:
            cache[i] = 0

    for i in range(1,n):
        if n%i == 0 and cache[i] == 0:
            curr = abs(nums[i] - nums[0])
            for k in range(i):
                for j in range(i + k,n,i):
                    curr = gcd(curr, abs(nums[j] - nums[j - i]))
                    if curr == 1:
                        break
                if curr == 1:
                    break
            if curr != 1:
                if i == 1:
                    ans += 1
                else:
                    t = 1
                    while n%(t * i) == 0 and t * i != n:
                        cache[t*i] = 1
                        ans += 1
                        # print("tt",t * i, i, ans)
                        t += 1
    print(ans)
    return 


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)
    # solve(n, nums)

   
