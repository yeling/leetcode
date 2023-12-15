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
    n = len(s)
    ans = -1
    l,r = 0,0
    while r < n:
        if s[l] == 'o':
            r = l 
            while r + 1 < n and s[r + 1] == 'o':
                r += 1

            if (l - 1 >= 0 and s[l - 1] == '-') or (r + 1 < n and s[r + 1] == '-'):
                temp = r - l + 1
                ans = max(ans, temp)
                # print(l,r, ans)
            l = r + 1
            r = l

        else:
            l += 1
            r = l
    print(ans)


n = int(input())
s = input()
main(n, s)