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

def getAllFactor(num):
    ans = defaultdict(int)
    i = 2
    while i * i < num:
        if num % i == 0:
            
            while num % i == 0:
                num //= i
                ans[i] += 1
        i += 1
    if num != 1:
        ans[num] += 1
    return ans


def solve(a, b):
    ans = ( 1 + b) * b // 2
    p = getAllFactor(a)
    c = 1
    for k in p:
        c *= (p[k] + 1)
    print(c, p)
    ans = (1 + (b - 1)) * (b - 1)//2 * c + 1 
    ans %= MOD
    print(ans%MOD)
    return

def check(a, b):
    s = a ** b
    v = 2
    ans = 0
    while v <= s:
        t = v
        while s%v == 0 and t % a == 0:
            t //= a
            ans += 1
            print(v, t, ans)
        v += 1
        # print(v, ans)
    print(ans)
    return


a,b = li()
check(a, b)
solve(a, b)
