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

def solve2(n, s):
    diff = 0
    l = 0
    r = n - 1
    while l <= r:
        if s[l] != s[r]:
            diff += 1
        l += 1
        r -= 1
    same = n//2 - diff
    ans = [0] * (n + 1)
    for i in range(n+1):
        temp = i
        if temp >= diff:
            if n%2 == 0 and temp%2 == 1:
                continue
            temp -= diff
            if n%2 == 0 and temp%2 == 0 and temp <= 2 * same:
                ans[i] = 1
            elif n%2 == 1 and temp <= 2 * same + 1:
                ans[i] = 1
    print(''.join([str(v) for v in ans]))

    return 

def solve(n, s):
    diff = 0
    l = 0
    r = n - 1
    while l <= r:
        if s[l] != s[r]:
            diff += 1
        l += 1
        r -= 1
    same = n//2 - diff
    ans = [0] * (n + 1)
    for i in range(n+1):
        temp = i
        if temp >= diff:
            temp -= diff
            if n%2 == 0 and temp%2 == 1:
                continue            
            if n%2 == 0 and temp%2 == 0 and temp <= 2 * same:
                ans[i] = 1
            elif n%2 == 1 and temp <= 2 * same + 1:
                ans[i] = 1
    print(''.join([str(v) for v in ans]))

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    solve(n, s)

   
