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

def solve(n, nums):
    cache = [[0,0] for _ in range(n)]
    l = 0
    for i in range(n):
        l = max(l, nums[i] + i * 100)
        cache[i][1] = l
    r = (n - 1) * 100
    for i in range(n - 1, -1, -1):
        r = min(r, i * 100 - nums[i])
        cache[i][0] = r
    ans = 0
    for i in range(1, n):
        if cache[i][0] > cache[i - 1][1]:
            ans += cache[i][0] - cache[i - 1][1]
    print(ans)
    return 


n = int(input())
nums = li()
solve(n, nums)

   
