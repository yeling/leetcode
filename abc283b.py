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


def main(n, nums, q, queries):
    for v  in queries:
        if v[0] == 1:
            nums[v[1] - 1] = v[2]
        elif v[0] == 2:
            print(nums[v[1] - 1])

n = int(input())
nums = li()
q = int(input())
queries = []
for i in range(q):
    queries.append(li())
main(n, nums, q, queries)


