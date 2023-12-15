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

def isPrime(n):
    if(n == 1):
        return False
    m = int(sqrt(n))
    for i in range(2,m + 1):
        if n%i == 0:
            return False
    return True

def solve(s):
    for i in range(3, 2**10):
        temp = ''
        for j in range(9):
            if i & (1 << j) != 0:
                temp += s[j]
        if len(temp) >= 2 and isPrime(int(temp)):
            print(temp)
            return
    print(-1)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = input()
    solve(n)

   
