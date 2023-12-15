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

def main(n, s):
    cache = defaultdict(list)
    for v in s:
        cache[len(v)].append(v)
    # print(cache)
    for k in cache:
        if len(cache[k]) != 2 or len(cache[k][0]) != len(cache[k][1]):
            print('No')
            return 
        for i in range(len(cache[k][0])):
            if cache[k][0][i] != cache[k][1][-i-1]:
                print('No')
                return 
    print('Yes')
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = (input()).split(' ')
    main(n, s)
   
