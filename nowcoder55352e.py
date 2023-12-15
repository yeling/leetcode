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


def main(s, t):
    # print(s, t)
    if len(s) - len(t) == 1:
        cnt = 0
        j = 0
        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                j += 1
            else:
                cnt += 1
        if cnt > 1:
            print('NO')
        else:
            print('YES')

    elif len(t) - len(s) == 1:
        cnt = 0
        j = 0
        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                j += 1
            else:
                cnt += 1
        if cnt > 1:
            print('NO')
        else:
            print('YES')

    elif len(s) == len(t):
        cnt = 0
        j = 0
        for i in range(len(t)):
            if s[i] != t[i]:
                cnt += 1
        if cnt > 1:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')

s = input()
t = input()
main(s, t)
