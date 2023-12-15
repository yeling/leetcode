# auther yeling
from typing import List
import math
from collections import *

n, q  = [int(v) for v in (input()).split(' ')]
all = []
for i in range(q):
    all.append([int(v) for v in (input()).split(' ')])

# print(n, q)
# print(all)

# curr = [set() for i in range(n+1)]
res = ''

curr = defaultdict(defaultdict)
for v in all:
    curr[v[1]][v[2]] = 0
    curr[v[2]][v[1]] = 0

for v in all:
    if v[0] == 1:
        curr[v[1]][v[2]] = 1
    elif v[0] == 2 :
        curr[v[1]][v[2]] = 0
    elif v[0] == 3:
        if curr[v[1]][v[2]] == 1 and curr[v[2]][v[1]] == 1:
            res += 'Yes\n'
        else:
            res += 'No\n'
print(res)
