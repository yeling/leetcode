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



def solve(n, m, s, t):
    pre = set()
    suf = set()
    for i in range(0,m):
        for j in range(i + 1, m):
            pre.add(t[i:j])
    
    for i in range(1,m):
        for j in range(i + 1, m + 1):
            print(i,j, t[i:j])
            suf.add(t[i:j])
    

    print(pre, suf)
    check = []
    for i in range(n-m + 1):
        if s[i:i+m] == t:
            check.append(i)
    print(check)
    last = 0
    for v in check:
        print(v)

    return

n,m = li()
s = input()
t = input()
solve(n, m, s, t)
