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


def main(n, a, b, c):
    ans = 0
    for i in range(n):
        temp = set([a[i],b[i],c[i]])
        cnt = len(temp)
        if cnt == 3:
            ans += 2
        elif cnt == 2:
            ans += 1
        elif cnt == 1:
            ans += 0

    print(ans)


n = int(input())
a = input()
b = input()
c = input()

main(n, a, b, c)
