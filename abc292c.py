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



def main(n):
    cnt = [2] * (n + 1)
    cnt[1] = 1
    for i in range(2,n):
        for j in range(i,n):
            if i * j > n:
                break
            if i == j:
                cnt[i*j] += 1
            else: 
                cnt[i*j] += 2
    ans = 0
    # print(cnt)
    for i in range(1, n//2 + 1):
        if i*2 != n:
            ans += 2 * cnt[i] * cnt[n - i]
        else:
            ans += cnt[i] * cnt[n - i]
    print(ans)

# main(19876)

n = int(input())
main(n)

