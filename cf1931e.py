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

def solve(n, m, nums):
    bc = 0
    cache = [0] * (10)
    for v in nums:
        bc += len(str(v))
        temp = 0
        tv = v
        while tv%10 == 0:
            temp += 1
            tv //= 10
        cache[temp] += 1
    d = 0
    # print(cache)
    for i in range(9,0,-1):
        if cache[i] > 0:
            cache[i] -= d
            bc -= i * ((cache[i] + 1)//2)
            d = cache[i]%2
        
    # print(bc)
    if bc >= m + 1:
        print('Sasha')
    else:
        print('Anna')
    # print(bc)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    nums = li()
    solve(n, m, nums)

   
