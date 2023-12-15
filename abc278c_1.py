# auther yeling
from typing import List
import math

n, q  = [int(v) for v in (input()).split(' ')]
all = []
for i in range(q):
    all.append([int(v) for v in (input()).split(' ')])

# print(n, q)
# print(all)

curr = [set() for i in range(n+1)]
res = ''
for v in all:
    if v[0] == 1:
        curr[v[1]].add(v[2])
    elif v[0] == 2 and v[2] in curr[v[1]]:
        curr[v[1]].remove(v[2])
    elif v[0] == 3:
        if v[2] in curr[v[1]] and v[1] in curr[v[2]]:
            res += 'Yes\n'
        else:
            res += 'No\n'
print(res)






