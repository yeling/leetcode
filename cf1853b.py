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

def solve(n, k):
    # ax + by = n
    # [1,0], [0,1],开始
    cache = [[1,0],[0,1]]
    while cache[-1][0] <= n or cache[-1][0] <= n:
        temp = [cache[-1][0] + cache[-2][0], cache[-1][1] + cache[-2][1]]
        cache.append(temp)
    ans = 0
    if len(cache) < k:
        print(0)
        return
    curr = cache[k - 1]
    a = 0
    while a * curr[0] <= n:
        if (n - a * curr[0])%curr[1] == 0:
            b = (n - a * curr[0])//curr[1]
            if a <= b:
                ans += 1
            else:
                break
        a += 1
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n, k = li()
    solve(n, k)

   
