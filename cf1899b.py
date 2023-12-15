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
    pre = [0] * (n + 1)
    for i,v in enumerate(nums):
        pre[i + 1] = pre[i] + v
    ans = 0
    for i in range(1,int(sqrt(n)) + 1):
        if n%i != 0:
            continue
        mi = INF
        ma = 0
        for j in range(0, n, i):
            mi = min(mi, pre[j + i] - pre[j])
            ma = max(ma, pre[j + i] - pre[j])
        ans = max(ans, ma - mi)
        # print(i, ans)
        mi = INF
        ma = 0
        step = n//i
        for j in range(0, n, step):
            mi = min(mi, pre[j + step] - pre[j])
            ma = max(ma, pre[j + step] - pre[j])
        ans = max(ans, ma - mi)

        # print(i, ans)
    print(ans)


    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)
   
