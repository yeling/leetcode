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

def solve(n, a, b, c):
    # print(n)
    for i in range(n):
        if a[i] == b[i] and a[i] != c[i]:
            print(YES)
            return
        elif a[i] != b[i] and a[i] != c[i] and b[i] != c[i]:
            print(YES)
            return
    print(NO)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = input()
    b = input()
    c = input()
    solve(n, a, b, c)

   
