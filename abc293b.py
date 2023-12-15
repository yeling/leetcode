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
    state = [False] * (n + 1)
    for i,v in enumerate(nums):
        if state[i + 1] == False:
            state[v] = True
        # print(state)

    ans = []
    for i,v in enumerate(state):
        if v == False and i != 0:
            ans.append(i)
    print(len(ans))
    print(*ans)
     

# n = 5
# nums = [3, 1, 4, 5, 4]
# main(n, nums)

n = int(input())
nums = li()
main(n, nums)