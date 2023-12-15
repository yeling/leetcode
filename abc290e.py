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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(n, nums):
    ans = 0
    dp1 = defaultdict(defaultdict(int))
    dp2 = defaultdict(defaultdict(int))
    
    print(n)


n = 5
nums = [5, 2, 1, 2, 2]
main(n, nums)

# n = int(input())
# nums = li()
# main(n, nums)
