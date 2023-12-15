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
    d = 2 * n
    print(bin(n))
    i = 1
    size = len(bin(n)) - 2
    #a,b
    cache = []
    for i in range(size):
        curr = n & (1 << i)
        if curr == 0:
            #0,0 1,1

        else:
            #0,1 1,0

        print(curr)
    

    return 

main(13)
# caseNum = int(input())
# for i in range(0, caseNum):
#     n = int(input())
#     main(n)
