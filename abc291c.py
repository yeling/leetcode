# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(n, s):
    cache = set()
    begin = (0,0)
    cache.add(begin)
    for v in s:
        next = None
        if v == 'R':
            next = (begin[0] + 1, begin[1])
        elif v == 'L':
            next = (begin[0] - 1, begin[1])
        elif v == 'U':
            next = (begin[0], begin[1] + 1)
        elif v == 'D':
            next = (begin[0], begin[1] - 1)
        if next in cache:
            # print(next)
            print('Yes')
            return 
        cache.add(next)
        begin = next
    
    print('No')
    return 

n = int(input())
s = input()
main(n, s)

