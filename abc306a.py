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
mi = lambda :map(int,input().split())
li = lambda :list(mi())


def solve(n, s):
    # print(n)
    ans = []
    for v in s:
        ans.append(v)
        ans.append(v)
    print(''.join(ans))



n = int(input())
s = input()
solve(n, s)

