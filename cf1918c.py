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

def solve2(a, b, r):
    ans = INF
    for i in range(r+1):
        ans = min(ans, abs((a^i) - (b^i)))
    print(ans)
    return 

def solve(a, b, r):
    ans = 0
    a1 = max(a,b)
    b1 = min(a,b)
    pos = 0
    flag = False
    while a1 > 1:
        if ((a1 & 1) == 1 and (b1 & 1) == 0):
            ans |= (1 << pos)
        a1 = a1 >> 1
        if b1 > 0:
            b1 = b1 >> 1
        pos += 1
    if len(bin(ans)) < len(bin(r)):
        print(abs((a ^ ans) - (b ^ ans)))
    else:
        ta = len(bin(ans)[2:])

    print(bin(a)[2:], bin(b)[2:])
    print(abs((a ^ ans) - (b ^ ans)), ans)
    return 

# solve(9,6,10)
# solve2(9,6,10)

caseNum = int(input())
for i in range(0, caseNum):
    a,b,r = li()
    solve(a, b, r)
    solve2(a, b, r)

   
