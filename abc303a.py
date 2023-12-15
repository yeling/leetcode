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

mi = lambda: map(int, sys.stdin.buffer.readline().split())
li = lambda :list(mi())


def solve(n, s, t):
    for i in range(n):
        if s[i] == t[i]:
            continue
        elif s[i] == '1' and t[i] == 'l':
            continue
        elif s[i] == 'l' and t[i] == '1':
            continue
        elif s[i] == '0' and t[i] == 'o':
            continue
        elif s[i] == 'o' and t[i] == '0':
            continue
        else:
            print(NO)
            return 
    print(YES)
    return



n = int(input())
s = input()
t = input()
solve(n, s, t)

