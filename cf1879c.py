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
MOD = 998244353
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

def solve2(s):
    i = 0
    n = len(s)
    op = 0
    ans = 1
    while i < n:
        j = i + 1
        while j < n and s[j] == s[j - 1]:
            j += 1
        if j > i + 1:
            op += j - i - 1
            for k in range(2, j - i + 1):
                ans *= k
                ans %= MOD
        i = j
    print(op, ans)

    return 

def solve(s):
    i = 0
    n = len(s)
    op = 0
    ans = 1
    while i < n:
        j = i + 1
        while j < n and s[j] == s[j - 1]:
            j += 1
        if j > i + 1:
            op += j - i - 1
        i = j
    
    for k in range(2, op + 2):
        ans *= k
        ans %= MOD

    print(op, ans)

    return 

def solve3(arr) -> None:
    # arr = list(input())
    if arr[-1] == '0':
        arr += "1"
    else:
        arr += "0"
    # arr += str(not int(arr[-1]))
    k = 0
    cnt = 0
    ans = 1
    sm = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            k += 1
        else:
            if not k:
                continue
            cnt += 1
            ans *= k + 1
            # ans %= mod
            sm += k
            k = 0
    print(sm, (ans * sm))

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    solve(s)
    # solve3(s)

   
