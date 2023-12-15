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
    ans = [0] * n
    if n%2 == 0:
        for i in range(n):
            if i%2 == 0:
                ans[i] = 1
            else:
                ans[i] = -1
    else:
        s = 1
        ans[0] = 1 - (n - 1)//2
        ans[1] = 1 - ans[0]
        for i in range(2,n):
            ans[i] = ans[i - 2]
    if ans[0] == 0:
        print('NO')
    else:
        print('YES')
        print(*ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
