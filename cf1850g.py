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
    # 4根线
    # (1,y-x) (-1,x + y),(2,x),(3,y)
    cache = defaultdict(int)
    ans = 0
    for x,y in nums:
        ans += cache[(2,x)] * 2
        cache[(2,x)] += 1
        
        ans += cache[(3,y)] * 2
        cache[(3,y)] += 1
        
        ans += cache[(1, y - x)] * 2
        cache[(1, y - x)] += 1

        ans += cache[(-1, y + x)] * 2
        cache[(-1, y + x)] += 1

    print(ans)
    return 

#TLE 14
def solve(n, nums):
    # 4根线
    cachex = defaultdict(int)
    cachey = defaultdict(int)
    # (1,b) (-1,b)
    cacheXY = defaultdict(int)
    ans = 0
    for x,y in nums:
        cachex[x] += 1
        cachey[y] += 1
        cacheXY[(1, y - x)] += 1
        cacheXY[(-1, y + x)] += 1

    for v in cachex:
        ans += cachex[v] * ( cachex[v] - 1)
    for v in cachey:
        ans += cachey[v] * ( cachey[v] - 1)
    for v in cacheXY:
        ans += cacheXY[v] * ( cacheXY[v] - 1)
    
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(li())
    solve2(n, nums)
   
