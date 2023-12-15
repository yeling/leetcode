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

MOD = 998244353

def main(n, nums):
    ans = 0
    for i in range(n//3):
        temp = nums[3*i : 3*i + 3]
        mi = min(temp)
        if temp.count(mi) >= 2:
            ans *= 3
        else:
            ans *= 2
        ans += sum() - min(nums[3*i : 3*i + 3])
    print(ans)
    return 


n = int(input())
nums = li()
main(n, nums)
