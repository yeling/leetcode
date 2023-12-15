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
    arr = n.split('0')
    ans = ''
    for v in arr:
        # print(v)
        s = 0
        temp = int(v)
        while temp > 0:
            s += temp%10
            temp //= 10
        # print('sum ',s)
        ans += chr(s + 96)
    print(ans)

    return 

# print(chr(97))
caseNum = int(input())
for i in range(0, caseNum):
    n = input()
    main(n)
