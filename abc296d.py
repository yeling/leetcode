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

#TLE
def main(n, m):
    ma = n * n
    if m > ma:
        print(-1)
        return
    if m <= n:
        print(m)
        return 
    ans = m
    while ans <= ma:
        temp = min(int(sqrt(ans)), n)
        flag = False
        while temp >= 1:
            if ans%temp == 0:
                if ans//temp <= n and temp <= n:
                    flag = True
                break
            if ans//temp > n:
                break
            temp -= 1
        if flag:
            print(ans)
            return 
        ans += 1
    print(-1)


n, m = li()
main(n, m)

