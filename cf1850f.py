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
input = sys.stdin.buffer.readline
input = sys.stdin.readline
# print = sys.stdout.write

input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def getAllFactor(num):
    ans = [1]
    i = 2
    while i * i <= num:
        if num % i == 0:
            ans.append(i)
            if num//i != i:
                ans.append(num//i)
        i += 1
    ans.append(num)
    return ans

#TLE
def solve3(n, nums):
    cache = [0]*(n + 1)
    kind = defaultdict(int)
    for v in nums:
        if v <= n:
            kind[v] += 1
    for k in kind:
        j = 1
        while j * k <= n:
            cache[j * k] += kind[k]
            j += 1
    ans = max(cache)
    print(ans)
    return 
#TLE
def solve2(n, nums):
    kind = defaultdict(int)
    for v in nums:
        if v <= n:
            kind[v] += 1
    ans = kind[1]
    for i in range(2,n+1):
        temp = getAllFactor(i)
        # print(temp)
        ans = max(ans, sum([kind[v] for v in temp]))

    print(ans)
    return 


#TLE
def solve(n, nums):
    cache = [0]*(n + 2)
    kind = [0]*(n + 2)
    for v in nums:
        if v <= n:
            kind[v] += 1
    for k in range(1,n + 1):
        j = k
        while j <= n:
            cache[j] += kind[k]
            j += k
    ans = max(cache)
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
