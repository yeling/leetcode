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

# Wrong answer on pretest 3

def solve(n, k, d, a, v):
    ans = 0
    temp = 0
    for i in range(n):
        if a[i] == i + 1:
            temp += 1
    ans = max(ans, temp + (d - 1)//2)
    # 这里是2n的原因，可能k里面都是1，每次都操作1，所以N是不行的
    # 2n所有数字都走一圈了，不可能更大了
    for i in range(min(2*n,d - 1)):
        pos = v[i%k]
        temp = 0
        end = min(n, pos)
        for j in range(end):
            a[j] += 1
        for j in range(n):
            if a[j] == j + 1:
                temp += 1
        ans = max(ans, temp + (d - (i + 1) - 1)//2)
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k,d = li()
    a = li()
    v = li()
    solve(n, k, d, a, v)

   
