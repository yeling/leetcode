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

def main(n, x, nums):
    for seq in permutations(range(1,n+1)):
        # print(seq)
        big = 0
        for i in range(n):
            if seq[i] - nums[i] >= x:
                big += 1
            if big >= n//2 + 1:
                break
        if big >= n//2 + 1:
            print(*seq)

    return 

   
n,x = li()
nums = li()
main(n, x, nums)