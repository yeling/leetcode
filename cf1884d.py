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
    cache = defaultdict(int)
    for v in nums:
        cache[v] += 1
    ks = list(cache.keys())
    ks.sort()
    ma = ks[-1]
    cnt = defaultdict(int)
    for k in ks:
        i = 2
        while i * k <= ma:
            if cache[i * k] != 0:
                cnt[i * k] += cache[k]
            i += 1
    pre = cache[ks[0]]
    ans = 0
    print(ks, cache, cnt)
    for i in range(1, len(ks)):
        ans += cache[ks[i]] * (pre - cnt[ks[i]])
        pre += cache[ks[i]]
        print(ks[i], ans)
    print(ans)
    return 

def solve3(n, nums):
    cache = defaultdict(int)
    for v in nums:
        cache[v] += 1
    ks = list(cache.keys())
    ks.sort()
    ma = ks[-1]
    cnt = defaultdict(int)
    for k in ks:
        i = 2
        curr = cache[k]
        while i * k <= ma:
            if cache[i * k] != 0 and cnt[i * k] == 0:
                cnt[i * k] += curr
                curr += cache[ i * k]
            i += 1
    pre = cache[ks[0]]
    ans = 0
    print(ks, cache, cnt)
    for i in range(1, len(ks)):
        ans += cache[ks[i]] * (pre - cnt[ks[i]])
        pre += cache[ks[i]]
        # print(ks[i], ans)
    print(ans)
    return 

def check(n, nums):
    ans = 0
    res = defaultdict(int)
    for i in range(n):
        for j in range(i+1, n):
            flag = False
            for k in range(n):
                if nums[i] % nums[k] == 0 and nums[j] % nums[k] == 0:
                    flag = True
                    break
            if flag == False:
                ans += 1
                res[(nums[i], nums[j])] += 1
    # print(ans, res)
    print(ans)
    return 

def solve(n, nums):
    cache = defaultdict(int)
    for v in nums:
        cache[v] += 1
    ks = list(cache.keys())
    ks.sort()
    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)
    check(n, nums)
   
