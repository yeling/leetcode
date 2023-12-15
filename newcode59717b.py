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

def solve(n, nums):
    ans = 0
    curr = defaultdict(int)
    for v in nums:
        next = defaultdict(int)
        for k in curr:
            next[k & v] += curr[k]
        next[v] += 1
        ans += next[0]
        curr = next
        # print(curr)
    print(ans)

    return 


n = int(input())
nums = lint()
solve(n, nums)


   
