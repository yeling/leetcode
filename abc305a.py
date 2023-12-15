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


def solve(n):
    ans = 0
    if n%5 < 5 - n%5:
        ans = n//5
    else:
        ans = n//5 + 1

    print(ans*5)



n = int(input())
solve(n)
