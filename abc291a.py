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


def main(s):
    # print(s)
    for i, v in enumerate(s):
        if v >= 'A' and v <= 'Z':
            print(i + 1)
            return



# s = 'aBc'
# main(s)

s = input()
main(s)

