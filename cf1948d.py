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

def solve2(s):
    ans = 0
    n = len(s)
    # print(s)
    for i in range(n - 1):
        for j in range(1,(n - i)//2 + 1):
            flag = True
            for k in range(j):
                # print(i,j,k, i+j+k)
                if s[i + k] == s[i + j + k] or s[i + k] == "?" or  s[i + j + k] == "?":
                    continue
                else:
                    flag = False
                    break
            if flag:
                ans = max(ans, j)
    print(ans * 2)
    return 

def solve(s):
    ans = 0
    n = len(s)
    dp = [[0]*(n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i,n):
            if s[i] == s[j] or s[i] == "?" or s[j] == "?":
                dp[i + 1][j + 1] = dp[i][j] + 1
            if dp[i + 1][j + 1] > 0 and i + 1 == j - dp[i+1][j+1] + 1:
                ans = max(ans, dp[i+1][j+1])
    # for d in dp:
    #     print(d)

    print(ans * 2)
    return 


caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    solve(s)

   
