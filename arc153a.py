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


def main(n):
    ans = [0] * 9
    ans[0] = ans[1] = 1
    pos = 1
    n = n - 1
    while n > 0:
        if pos == 1:
            ans[8 - 1] = n%10
        elif pos == 2:
            ans[7 - 1] = ans[9 - 1] = n%10
        elif pos == 3:
            ans[5 - 1] = ans[6 - 1] = n%10
        elif pos == 4:
            ans[4 - 1] = n%10
        elif pos == 5:
            ans[3 - 1] = n%10
        elif pos == 6:
            ans[2 - 1] = 1 + n%10
            ans[1 - 1] = 1 + n%10
        pos += 1
        n = n // 10
    ps = ''
    for v in ans:
        ps += str(v)
    print(ps)

# main(2023)
caseNum = int(input())
main(caseNum)

