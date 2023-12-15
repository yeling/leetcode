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


# input = lambda: sys.stdin.readline().rstrip()
input = lambda: sys.stdin.readline().rstrip()
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())


def solve(n, nums):
    stack = []
    for a,b in nums:
        heappush(stack, (a,b))
    ans = 0
    while len(stack) > 0:
        curr = heappop(stack)
        print(curr)

    print(n)
    return



n = int(input())
nums = []
for _ in range(n):
    nums.append(lint())
solve(n, nums)
