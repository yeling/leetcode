# auther yeling
from typing import List
from collections import *

n = int(input())
nums = [int(v) for v in (input()).split(' ')]
q = int(input())
all = []
for i in range(q):
    all.append([int(v) for v in (input()).split(' ')])

res = []
add = -1
cache = defaultdict(int)
for qnums in all:
    if qnums[0] == 1:
        add = qnums[1]
        cache.clear()
    elif qnums[0] == 2:
        if qnums[1] - 1 in cache:
            cache[qnums[1] - 1] += qnums[2]
        elif add != -1:
            cache[qnums[1] - 1] = add + qnums[2]
        else:
            cache[qnums[1] - 1] = nums[qnums[1] - 1] + qnums[2]
    elif qnums[0] == 3:
        if qnums[1] - 1 in cache:
            res.append(cache[qnums[1] - 1])
        elif add != -1:
            res.append(add)
        else:
            res.append(nums[qnums[1] - 1])

print('\n'.join([str(v) for v in res]))
