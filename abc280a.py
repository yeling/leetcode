# auther yeling
from typing import List
from bisect import *
from collections import *


def main(m, n, grid):
    c = 0
    for v in grid:
        c += v.count('#')
    print(c)


m,n = [int(v) for v in (input()).split(' ')]
nums = []
for t in range(m):
    nums.append(input())
main(m,n, nums)

