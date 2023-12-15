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

def solve(n, k, s):
    cache = [0] * 26
    for v in s:
        cache[ord(v) - ord('a')] += 1
    # print(cache)
    single = 0
    for v in cache:
        single += v%2
    # print(single)
    if k < single - 1:
        print(NO)
    elif k <= n:
        print(YES)
    else:
        print(NO)
    

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    s = input()
    solve(n, k, s)
   
