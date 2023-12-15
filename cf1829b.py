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
    s = 0
    ans = 0
    for i in range(n):
        if nums[i] == 0:
            ans = max(ans, i - s + 1)
        else:
            s = i + 1
    print(ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
