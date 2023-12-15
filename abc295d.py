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
    cache = defaultdict(int)
    temp = [0] * 10
    cache[tuple(temp)]+= 1
    for v in s:
        temp[int(v)] += 1
        temp[int(v)] %= 2
        key = tuple(temp)
        ans += cache[key]
        cache[key]+= 1
        # print(key, ans)
    print(ans)
    return 


s = input()
main(s)

