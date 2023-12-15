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

# mi = lambda: map(int, sys.stdin.buffer.readline().split())
mi = lambda :map(int,input().split())
li = lambda :list(mi())


def solve(n):
    if n <= 10**3 - 1:
        print(n)
    elif n <= 10 ** 4 - 1:
        print(n//10 * 10)
    elif n <= 10 ** 5 - 1:
        print(n//100 * 100)
    elif n <= 10 ** 6 - 1:
        print(n//1000 * 1000)
    elif n <= 10 ** 7 - 1:
        print(n//10000 * 10000)
    elif n <= 10 ** 8 - 1:
        print(n//100000 * 100000)
    elif n <= 10 ** 9 - 1:
        print(n//1000000 * 1000000)
    



n = int(input())
solve(n)

