# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(n, s):
    # o - x 
    a = 0
    b = 0
    for v in s:
        if v == 'o':
            a += 1
        elif v == 'x':
            b += 1
    if a > 0 and b == 0:
        print(YES)
    else:
        print(NO)
    



n = int(input())
s = input()
main(n , s)
