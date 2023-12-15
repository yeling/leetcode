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

arr = [3,1,4,1,5,9]
preArr = [0,3,4,8,9,14,23]
def solve(p, q):
    # print(p, q)
    # print(ord('A'))
    print(abs(preArr[ord(p) - 65] - preArr[ord(q) - 65]))


p, q = input().split()
solve(p, q)

