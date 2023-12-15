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

def solve(a, b, c):
    s = a + b + c
    mi = min(a, b, c)
    for i in range(3,7):
        av = s // i
        if s % i == 0 and  a % av == 0 and b % av == 0 and c % av == 0:
            print(YES)
            return
        
    print(NO)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    a,b,c = li()
    solve(a, b, c)

   
