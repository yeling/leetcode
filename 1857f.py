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

#TLE 47
def solve(n, nums, q, qs):
    nums.sort()
    cache = defaultdict(int)
    for v in nums:
        cache[v^MOD] += 1
    ans = [0] * q
    for i,(x,y) in enumerate(qs):
        if x * x < 4 * y:
            continue
        a = int(x + sqrt(x * x - 4 * y))//2
        b = int(x - sqrt(x * x - 4 * y))//2
        # print(x,y,a,b)
        if a + b == x and a * b == y:
            if a == b:
                ans[i] = cache[a^MOD] * (cache[a^MOD] - 1)//2
            else:
                ans[i] = cache[a^MOD] * cache[b^MOD]
        
    print(*ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    q = int(input())
    qs = []
    for _ in range(q):
        qs.append(li())
    solve(n, nums, q, qs)

cnt = 37
ans = [[] for _ in range(cnt)]
for i in range(100):
    print(i, i%cnt, (i ^ MOD)%cnt)
    ans[i%cnt].append((i ^ MOD)%cnt)
print(ans)