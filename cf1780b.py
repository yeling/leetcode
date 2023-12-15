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

def isPrime(n):
    if(n == 1):
        return False
    m = int(sqrt(n))
    for i in range(2,m + 1):
        if n%i == 0:
            return False
    return True

    
def main(n, nums):
    s = sum(nums)
    ans = 1
    pre = 0
    for i in range(0, n - 1):
        pre += nums[i]
        ans = max(ans, gcd(pre, s - pre))
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)