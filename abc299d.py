# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string
from sys import *


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(n):
    cache = [-1]*(n + 1)
    cache[1] = 0
    cache[n] = 1
    if n == 2:
        print('?' ,1)
        stdout.flush()
        temp = int(input())
        print('!', 1)
        return

    for i in range(2, n):
        print('?' ,i)
        stdout.flush()
        temp = int(input())
        cache[i] = temp
        if cache[i - 1] != -1 and cache[i] != cache[i - 1]:
            print('!', i-1)
            stdout.flush()
            return
        if cache[i + 1] != -1 and cache[i + 1] != cache[i]:
            print('!', i)
            stdout.flush()
            return
    return




n = int(input())
main(n)

