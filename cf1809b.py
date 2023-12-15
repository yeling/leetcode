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
    left = 0
    right = n
    target = n
    while left <= right:
        mid = left + (right - left)//2
        temp = 0
        if mid%2 == 0:
            curr = mid//2
            temp = 1 + 4 * curr * (curr + 1)
        else:
            curr = (mid - 1)//2
            temp = 4 + 4 * curr * (curr + 2)

        if target <= temp:
            right = mid - 1
        elif target > temp:
            left = mid + 1

    print(left)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
   
