# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(n, nums):
    for i in range(0,n+1):
        currlie = 0
        for v in nums:
            if v > i:
                currlie += 1
        if currlie == i:
            print(currlie)
            return 
    print(-1)
    return 

# main(2, [1,2])
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
