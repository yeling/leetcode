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
    for i in range(1,n):
        l = 0
        while l + i < n and s[l + i] != s[l]:
            l += 1
        print(l)

n = int(input())
s = input()
main(n, s)

