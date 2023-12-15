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
    ans = ''
    for v in s:
        ans += chr(ord(v) - 32)
    print(ans)

# print(ord('a') - ord('A'))
# main('abccc')
s = input()
main(s)
