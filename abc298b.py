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


def main(n, a, b):
    nextA = [[-1]*n for _ in range(n)]
    for i in range(n):
        nextA[i] = a[i][:]
    print(nextA)
    for i in range(1,(n+1)//2):
        for j in range(1,(n+1)//2 + 1):
            print([i,j], [n+1-j,i])
            nextA[i - 1][j - 1], nextA[n + 1 - j - 1][i - 1] = nextA[n + 1 - j - 1][i - 1],nextA[i - 1][j - 1]
            
    print(nextA)



n = int(input())
a = []
b = []
for _ in range(n):
    a.append(li())

for _ in range(n):
    b.append(li())

main(n, a, b)

