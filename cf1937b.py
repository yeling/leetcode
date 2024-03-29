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

def solve(n, s1, s2):
    # print(n, s1, s2)
    s = [[] for _ in range(2)]
    s[0] = [v for v in s1]
    s[1] = [v for v in s2]
    ans = [s[0][0]]
    cnt = 1

    for i in range(1,n):
        if s[0][i] == s[1][i - 1]:
            ans += s[0][i]
            cnt += 1
        elif s[0][i] == '1' and s[1][i - 1] == '0':
            ans += s[1][i - 1:]
            break
        elif s[0][i] == '0' and s[1][i - 1] == '1':
            ans += s[0][i]
            cnt = 1
        if i == n - 1:
            ans += s[1][i]
            
        # if s[0][i] == '1' and s[1][i] == '0':
        #     s += s[1][i:]
        #     break
    ret = ""
    for v in ans:
        ret += v
    print(ret)
    print(cnt)
        

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s1 = input()
    s2 = input()
    solve(n, s1, s2)

   
