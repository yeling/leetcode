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
    # (cnt,v)
    ans = n
    cache = defaultdict(int)
    # (cnt, v, cnt, s)
    cache2 = defaultdict(int)
    for i in range(n):
        v = nums[i]
        temp = str(v)
        tn = len(temp)
        curr = []
        s = 0
        for i in range(tn):
            s += int(temp[i])
            curr.append((i + 1, s))
        for j in range(1,tn + 1):
            if (tn + j)%2 == 0:
                pt = (j, s - 2 * curr[(tn + j)//2 - j - 1][1])
                ans += cache[pt]
                st = (j, 2 * curr[(len(temp) + j)//2 - 1][1] - s)
                ans += cache[st]
                # print(v, (tn, s), pt, st, ans)
        # for v in cache2:
        #     if cache2[v] != 0:
        #         print(v, cache2[v])
        
        for j in range(tn+1, 6):
            if (tn + j)%2 != 0:
                continue   
            for k in range(1,j+1):
                # print(j)
                for v in range(1,46):
                    pt = (k, v, j, 2 * v - s)
                    # print(pt,st)
                    ans += cache2[pt]
                    st = (k, v, j, 2 * v + s)
                    ans += cache2[st]
                    # print(pt,st)
        for v in curr:
            cache2[(v[0],v[1], tn, s)] += 1
        #借位
        cache[(tn, s)] += 1

        # print(curr, cache)
    print(ans)
    return 

def solve(n, nums):
    # (cnt,v)
    ans = n
    cache = defaultdict(int)
    # (cnt, v, cnt, s)
    cache2 = defaultdict(int)
    for i in range(n):
        v = nums[i]
        temp = str(v)
        tn = len(temp)
        curr = []
        s = 0
        for i in range(tn):
            s += int(temp[i])
            curr.append((i + 1, s))
        for j in range(1,tn + 1):
            if (tn + j)%2 == 0:
                pt = (j, s - 2 * curr[(tn + j)//2 - j - 1][1])
                ans += cache[pt]
                st = (j, 2 * curr[(len(temp) + j)//2 - 1][1] - s)
                ans += cache[st]
                # print(v, (tn, s), pt, st, ans)
        # for v in cache2:
        #     if cache2[v] != 0:
        #         print(v, cache2[v])
        
        for j in range(tn+1, 6):
            if (tn + j)%2 != 0:
                continue   
            for k in range(1,j+1):
                # print(j)
                for v in range(1,46):
                    pt = (k, v, j, 2 * v - s)
                    # print(pt,st)
                    ans += cache2[pt]
                    st = (k, v, j, 2 * v + s)
                    ans += cache2[st]
                    # print(pt,st)
        for v in curr:
            cache2[(v[0],v[1], tn, s)] += 1
        #借位
        cache[(tn, s)] += 1

        # print(curr, cache)
    print(ans)
    return 

def check(n, nums):
    ans = 0
    for i in range(n):
        for j in range(n):
            temp = str(nums[i]) + str(nums[j])
            if len(temp)%2 == 0:
                cnt = len(temp)
                half = 0
                stemp = 0
                for k,v in enumerate(temp):
                    stemp += int(v)
                    if k < cnt//2:
                        half += int(v)
                if half * 2 == stemp:
                    ans += 1
                    print(nums[i], nums[j], ans)
    print(ans)
    return

n = int(input())
nums = li()
check(n, nums)
solve(n, nums)

   
