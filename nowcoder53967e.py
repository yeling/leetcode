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


def main(n, m, k, nums):
    # magic , begin, end
    # [ )
    ans = [[0,0,0] for _ in range(n + 1)]
    for i,(op,x) in enumerate(nums):
        if op == 1:
            if ans[x][1] != 0:
                ans[x][0] += min(ans[x][2], i) - ans[x][1]
            ans[x][1] = i
            ans[x][2] = i + k
        elif op == 2:
            if ans[x][1] != 0:
                ans[x][0] += min(ans[x][2], i) - ans[x][1]
                ans[x][1] = 0
                ans[x][2] = 0
        elif op == 3:
            if ans[x][1] == 0:
                print(i + ans[x][0])
            else:
                print(i + ans[x][0] + min(ans[x][2], i) - ans[x][1])

n,m,k = li()
nums = []
for _ in range(m):
    nums.append(li())
main(n, m, k, nums)


