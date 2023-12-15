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
    ans = 0
    n = len(s)
    i = 0
    while i < n:
        if s[i] == '0':
            j = i + 1
            while j < n and s[j] == '0' :
                j += 1
            zero = j - 1 - i + 1
            ans += (zero + 1)//2
            i = j
        else:
            ans += 1
            i += 1
    print(ans)



s = input()
main(s)

