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

def main(n):
    if n <= 9:
        print(n)
        return
    ans = 9 
    while n >= 10:
        n = n//10
        if n >= 10:
            ans += 9
        else:
            ans += n

    print(ans)

# main(13)
# main(42)
# main(1100)

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
