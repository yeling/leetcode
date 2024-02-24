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
    dp = [0] * n
    # print(s)
    ans = 0
    for i in range(1,n):
        if s[i] == '.':
            dp[i] = max(dp[i], dp[i - 1])
            if i - 2 >= 0:
                dp[i] = max(dp[i], dp[i - 2])
        elif s[i] == '@':
            dp[i] = max(dp[i], dp[i - 1] + 1)
            if i - 2 >= 0:
                dp[i] = max(dp[i], dp[i - 2] + 1)
        ans = max(ans, dp[i])
        if s[i - 1] == '*' and s[i] == '*':
            break

    print(ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    solve(n, s)

   
