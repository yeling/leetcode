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

def main(s):
    cnt = defaultdict(int)
    for v in s:
        cnt[v] += 1
    # print('len ' , len(cnt))
    if len(cnt) == 4:
        print(4)
    elif len(cnt) == 1:
        print(-1)
    elif len(cnt) == 2 and cnt[list(cnt.keys())[0]] == 2:
        print(4)
    elif len(cnt) == 3:
        print(4)
    else:
        print(6)
    # print( cnt)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    main(s)
   
