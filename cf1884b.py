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
input = sys.stdin.buffer.readline
input = sys.stdin.readline
# print = sys.stdout.write

input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve2(n, s):
    curr = 0
    s = [int(v) for v in s]
    ans = [-1] * (n)
    # print(s)
    for i in range(1,n+1):
        if s[n - i] == 1:
            j = i + 1
            flag = False
            while j <= n:
                if s[n - j] == 0:
                    s[n - j] = 1
                    s[n - i] = 0
                    curr += 1
                    flag = True
                    break
                elif s[n - j] == 1:
                    curr += 1
                j += 1
            
            if flag:
                ans[i - 1] = curr
            else:
                break
        elif s[n - i] == 0:
            ans[i - 1] = curr
        # print(i, s, ans)
    print(*ans)
    return 


def solve(n, s):
    curr = 0
    s = [int(v) for v in s]
    ans = [-1] * (n)
    # print(s)
    l = n - 1
    
    for i in range(1,n+1):
        l = min(l, n - i)
        if s[n - i] == 1:
            while l > 0 and s[l] == 1:
                l -= 1
            if l == -1 or s[l] == 1:
                break
            s[l] = 1
            curr += n - i - l
            ans[i - 1] = curr
        elif s[n - i] == 0:
            ans[i - 1] = curr
        # print(i, s, ans)
    print(*ans)
    return 


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    solve(n, s)

   
