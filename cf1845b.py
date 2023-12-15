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
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())

def solve(a, b, c):
    ans = 1
    if b[0] > a[0] and c[0] > a[0]:
        ans += min(b[0],c[0]) - a[0]
    elif b[0] < a[0] and c[0] < a[0]:
        ans += a[0] - max(b[0],c[0])
    
    if b[1] > a[1] and c[1] > a[1]:
        ans += min(b[1],c[1]) - a[1]
    elif b[1] < a[1] and c[1] < a[1]:
        ans += a[1] - max(b[1],c[1])
    
    print(ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    a = lint()
    b = lint()
    c = lint()
    solve(a, b, c)

   
