# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 998244353

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def quickPowMode(a, n, p):
    ans = 1
    while(n > 0):
        if n & 1 == 1:
            ans = ans * a % p
        a = a * a % p
        n = n >> 1
    return ans % p

def main(n, s):
    #(0的次数，1的次数)
    c = [0,0]
    ans = 0
    for i in range(n):
        c[int(s[i])] += 1
        k = i + 1
        if k%2 == 1:
            a = int(s[k//2])
            ans += quickPowMode(2, k - 1 - (k - c[a]), MOD)%MOD
        else:
            # a = 0
            # if c[0] > c[1]:
            #     a = 1
            # ans += quickPowMode(2, k - 1 - (k - c[a]), MOD)%MOD
            ans += quickPowMode(2, k - 1, MOD)%MOD

    print(ans) 

# n = 9
# s = '101101111'
# n = 2
# s = '11'
# main(n, s)

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n,s)
