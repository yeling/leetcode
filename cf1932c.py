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


def solve(n, m, nums, s):
    # print(n, m, nums, s)
    ans = []
    pos = []
    l = 0
    r = n - 1
    for i in range(n):
        if s[i] == 'L':
            pos.append(l)
            l += 1
        else:
            pos.append(r)
            r -= 1
    temp = 1
    for i in range(n-1, -1, -1):
        temp = (temp * nums[pos[i]])%m
        ans.append(temp)
    print(*reversed(ans))

    

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    nums = li()
    s = input()
    solve(n, m, nums, s)

   
