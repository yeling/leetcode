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

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(x, y, m):
    ans = 0
    a = 0
    b = 0
    while a * x <= m:
        b = 0
        while a * x + b * y <= m:
            ans = max(ans, a * x + b * y)
            b += 1
        a += 1
    print(ans)
    return 

x, y, m = li()
main(x, y, m)
   
