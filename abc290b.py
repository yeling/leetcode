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


def main(n, k, s):
    cnt = 0
    ans = ''
    for v in s:
        if v == 'o' and cnt < k:
            ans += 'o'
            cnt += 1
        else:
            ans += 'x'
    print(ans)


n,k = li()
s = input()
main(n , k , s)

