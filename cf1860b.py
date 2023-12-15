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

def solve2(m, k, a, b):
    need = m%k + max(0,(m//k - b)) * k
    # print('need', need, m, k, a, b)
    if need <= a:
        print(0)
    else:
        ans = 0
        if a >= m%k:
            ans = (m - m%k)//k - b
            if b != 0:
                ans -= (a - m%k)//k
        else:
            ans = (m - m%k)//k - b + (m%k - a)
        print(ans)
        
    return 

def solve(m, k, a, b):
    ans = 0
    if a >= m%k:
        ans = (m - m%k)//k - b - (a - m%k)//k
    else:
        ans = max(0,(m - m%k)//k - b) + (m%k - a)
    if ans < 0:
        ans = 0
    print(ans)
        
    return 
caseNum = int(input())
for i in range(0, caseNum):
    m,k,a,b = li()
    solve(m, k, a, b)

   
