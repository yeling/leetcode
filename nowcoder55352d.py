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


def main(n):
    a = []
    b = []
    arr = [v for v in n]
    arr.sort(reverse=True)
    i = 0
    while i < len(arr):
        a.append(arr[i])
        i += 1
        if i < len(arr):
            b.append(arr[i])
            i += 1
    # print(arr)
    print(''.join(a))
    if b.count('0') == len(b):
        print(0)
    else:
        print(''.join(b))

s = input()
main(s)
