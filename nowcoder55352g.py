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


def main(n, t, nums):

    global ans
    ans = 0
    def dfs(index, score, sum):
        # print(index, score, sum)
        global ans
        if index == n or sum > t:
            return
        #not choose
        dfs(index + 1, score, sum)
        #choose
        if sum + nums[index][1] <= t:
            ans = max(ans, score + nums[index][0])
            dfs(index + 1, score + nums[index][0], sum + nums[index][1])

    dfs(0, 0, 0)
    print(ans)


n,t = li()
nums = []
for i in range(0, n):
    nums.append(li())

main(n, t, nums)

