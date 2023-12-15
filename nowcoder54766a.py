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

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(n, d1, d2):
    dp = [0] * (n + 5)
    dp[1] = 1
    for i in range(1,n+1):
        begin = i - d2 + 1
        end = i - d1
        begin = max(0, begin)
        for j in range(begin, end + 1):
            dp[i] += dp[j]
            dp[i] %= MOD
    ans = 0
    for i in range(d2):
        ans += dp[n-i]
        ans %= MOD
    print(ans)

    return 


n,d1,d2 = li()
main(n, d1, d2)
