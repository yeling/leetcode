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


def main(n, s):
    cnt = 0
    for v in s:
        if v == '|':
            cnt += 1
        if v == '*':
            if cnt == 1:
                print('in')
            else:
                print('out')
            return 

   



n = int(input())
s = input()
main(n, s)
