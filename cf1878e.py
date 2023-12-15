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

ans = []
def solve2(n, nums, q, grid):
    for l,k in grid:
        curr = nums[l - 1]
        r = l - 1
        while curr >= k and r < n:
            r += 1
            if r < n:
                curr &= nums[r]
        if r < l:
            ans.append(-1)
        else:
            ans.append(r)
    
    return 
#倍增，区间值
#3 -1 -1 3 2
def solve3(n, nums, q, grid):
    cache = [[0] * 31 for _ in range(n)]
    for i in range(n):
        cache[i][0] = nums[i]

    for j in range(1,31):
        dis = 2 ** (j - 1)
        for i in range(n):
            if i + dis < n:
                cache[i][j] = cache[i][j - 1] & cache[i + dis][j - 1]
    # for v in cache:
    #     print(v) 
    ans = []
    for l, k in grid:
        pos = l - 1
        value = cache[pos][0]
        cnt = 1
        if value < k:
            ans.append(-1)
        else:
            while cnt > 0 and pos < n:
                while (value & cache[pos][cnt]) >= k:
                    cnt += 1
                cnt -= 1
                value &= cache[pos][cnt]
                pos = min(pos + 2 ** cnt - 1, n - 1)
            ans.append(pos + 1)
    print(*ans)
    return 

#倍增，区间值
#3 -1 -1 3 2
def solve(n, nums, q, grid):
    cache = [[0] * 31 for _ in range(n)]
    for i in range(n):
        cache[i][0] = nums[i]

    for j in range(1,31):
        dis = 2 ** (j - 1)
        for i in range(n):
            if i + dis < n:
                cache[i][j] = cache[i][j - 1] & cache[i + dis][j - 1]
    ans = []
    for l, k in grid:
        pos = l - 1
        value = cache[pos][0]
        cnt = 1
        if value < k:
            ans.append(-1)
        else:
            while cnt > 0 and pos < n:
                while (value & cache[pos][cnt]) >= k:
                    value &= cache[pos][cnt]
                    pos = min(pos + 2 ** cnt - 1, n - 1)
                    cnt += 1
                cnt -= 1 
            ans.append(pos + 1)
    print(*ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    q = int(input())
    grid = []
    for _ in range(q):
        grid.append(li())
    solve(n, nums, q, grid)

print(*ans)
   
