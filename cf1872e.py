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

def solve(n, nums, s, q, qs):
    pre = [0]*(n + 2)
    zero = 0
    one = 0
    for i,v in enumerate(nums):
        pre[i + 1] = pre[i]^v
        if s[i] == '1':
            one ^= v
        elif s[i] == '0':
            zero ^= v
    pre[n + 1] = pre[n]
    ans = []
    for v in qs:
        if v[0] == 2:
            if v[1] == 0:
                ans.append(zero)
            elif v[1] == 1:
                ans.append(one)
        elif v[0] == 1:
            l = v[1]
            r = v[2]
            zero ^= (pre[r] ^ pre[l-1])
            one ^= (pre[r] ^ pre[l-1])
    print(*ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    s = input()
    q = int(input())
    qs = []
    for _ in range(q):
        qs.append(li())
    solve(n, nums, s, q, qs)


   
