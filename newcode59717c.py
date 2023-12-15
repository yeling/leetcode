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

def solve(n, a, b):
    cache = defaultdict(int)
    for i in range(n):
        cache[b[i]] = i
    # print(cache)
    temp = [0] * n
    for i,v in enumerate(a):
        temp[i] = cache[v]
    curr = temp[0]
    ans = 0
    # print(temp)
    for i in range(1,n):
        if curr < temp[i]:
            curr = temp[i]
            continue
        else:
            curr = temp[i]
            ans += 1

    print(ans)
        

    return 


n = int(input())
a = lint()
b = lint()
solve(n, a, b)
   
