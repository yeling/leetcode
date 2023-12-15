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


def main(all,k):
    all.sort()
    for i in range(k):
        print(all[i])


caseNum,k = li()
all = []
for i in range(0, caseNum):
    all.append(input())
main(all[:k], k)


