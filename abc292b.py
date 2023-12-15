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


def main(n, q, nums):
    cnt = defaultdict(int)
    plays = set([i + 1 for i in range(n)])
    # print(plays)
    for type, value in nums:
        if type == 1:
            cnt[value] += 1
            if cnt[value] >= 2:
                plays.remove(value)
            # print('No')
        elif type == 2:
            plays.remove(value)
            # print('No')
        elif type == 3:
            if value in plays:
                print('No')
            else:
                print('Yes')


    # print(n)


n,q = li()
nums = []
for i in range(0, q):
    nums.append(li())
main(n, q, nums)

