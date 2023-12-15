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



def solve(n, s):
    cache = [defaultdict(int) for _ in range(26)]
    l = 0
    while l < n:
        r = l
        while r < n and s[l] == s[r]:
            r += 1
            cache[ord(s[l]) - ord('a')][r - l] += 1
        l = r
    ans = 0
    for i in range(26):
        ans += len(cache[i].keys())
    print(ans)
    return


n = int(input())
s = input()
solve(n, s)

