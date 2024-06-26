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


n = int(input())
nums = li()
q = int(input())


def solve():
    # print(n)
    cache = defaultdict(int)
    for i,v in enumerate(nums):
        cache[v] = i + 1
    for i in range(q):
        a,b = li()
        if cache[a] < cache[b]:
            print(a)
        else:
            print(b)
        # print(min(cache[a], cache[b]))

    return

solve()


