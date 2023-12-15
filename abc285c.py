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
    ans = 0
    p = 1
    n = len(s)
    for i in range(n - 1, -1, -1):
        ans += (ord(s[i]) - 65 + 1)*p
        p *= 26
    print(ans)
    return 

# main('BRUTMHYHIIZP')
s = input()
main(s)

