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


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

# input = lambda: sys.stdin.readline().rstrip()
input = lambda: sys.stdin.readline().rstrip()
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())


def solve(n, s):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            temp = s[i] + s[j]
            l = 0
            r = len(temp) - 1
            flag = True
            while l < r:
                if temp[l] == temp[r]:
                    l += 1
                    r -= 1
                else:
                    flag = False
                    break
            if flag == True:
                print(YES)
                return
    print(NO)
    return



n = int(input())
s = []
for _ in range(n):
    s.append(input())
solve(n, s)
