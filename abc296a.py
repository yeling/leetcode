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
    pre = s[0]
    for i in range(1,n):
        if pre == s[i]:
            print('No')
            return
        else:
            pre = s[i]
    print('Yes')


n = int(input())
s = input()
main(n, s)   

