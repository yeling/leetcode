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
    n = len(s)
    ans = [0] * n
    for i in range(0,n,2):
        ans[i] = s[i+1]
        ans[i + 1] = s[i]
    print(''.join(ans))


# main('abcd')

s = input()
main(s)

