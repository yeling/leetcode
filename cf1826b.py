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
    if n == 1:
        print(0)
        return
    diff = []
    l = 0
    r = n - 1
    while l < r:
        diff.append(abs(nums[r] - nums[l]))
        l += 1
        r -= 1
    ans = diff[0]
    # print(diff)
    for i in range(1,len(diff)):
        ans = gcd(ans, diff[i])
    print(ans)
    return 

# main(3, [1, 1, 1])
# print(gcd(0,100))

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
